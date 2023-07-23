import base64

import cloudinary
import cloudinary.uploader
import cv2
import numpy as np

cloudinary.config(secure=True)


def upload(video_id: str, image_name: str, image: np.ndarray):
    """
    Uploads an image to cloudinary
    :param image_name:
    :param video_id: id of the Youtube video
    :param image: the image to upload
    :return: the url of the uploaded image
    """
    print(f'Uploading {image_name} to cloudinary')
    _, buffer = cv2.imencode(".jpg", image)

    b64_image = base64.b64encode(buffer).decode("utf-8")
    data_uri = f"data:image/jpeg;base64,{b64_image}"
    url = cloudinary.uploader.upload(data_uri, public_id=f"crowdmon/{video_id}/{image_name}", )["secure_url"]
    print(f'Successfully uploaded {image_name} to cloudinary')

    return url
