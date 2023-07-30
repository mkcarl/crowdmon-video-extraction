import cv2
from yt_dlp import YoutubeDL
from multiprocessing.pool import Pool
import os
import dotenv

from src.lib.cloudflare_uploader import upload
from src.lib.db import write_image

dotenv.load_dotenv()


def _video_to_frames(url, start, end, skipSeconds=1):
    print(f"Initiated extraction of {url} from {start}s to {end}s interval {skipSeconds}s")
    with YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)

    valid_video_formats = list(  # only get the 1080p videos
        filter(lambda x: x.get('format_note') is not None and "360p" in x.get('format_note'), info.get("formats")))

    video = cv2.VideoCapture(valid_video_formats[0]["url"])

    video.set(cv2.CAP_PROP_POS_MSEC, start * 1000)  # skip to starting point

    count = start

    while count < end or count < info["duration"]:  # while we are within the interval
        print(f"[{info['id']}] Extracting at {count}s")
        ret, frame = video.read()
        if not ret:
            print(f"no video feed at {count}s")
            break
        frame_url = upload(info["id"], f"{count}", frame)
        write_image(info['id'], f"{count}.jpg", frame_url)

        # skip to next frame
        count += skipSeconds
        video.set(cv2.CAP_PROP_POS_MSEC, count * 1000)


def extract(url):
    with YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)

    parallel = os.cpu_count()

    length = info.get("duration")
    segment_length = int(length / parallel)
    segments = [(i * segment_length, (i + 1) * segment_length) for i in range(parallel)]

    with Pool(parallel) as pool:
        pool.starmap(_video_to_frames, [(url, start, end, 5) for start, end in segments])

