import base64
import os
import cv2
import requests
import dotenv
import numpy as np

dotenv.load_dotenv()

def upload(video_id: str, image_name: str, image: np.ndarray):
    url = 'https://api.imgbb.com/1/upload'

    _, buffer = cv2.imencode(".jpg", image)
    b64_image = base64.b64encode(buffer).decode("utf-8")
    payload = {
        "key": os.environ.get("IMGBB_API_KEY"),
        "image": b64_image,
        "name": f"crowdmon_{video_id}_{image_name}"
    }
    res = requests.post(url, payload)
    return res.json()["data"]["url"]
