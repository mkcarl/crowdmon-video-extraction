import boto3
import cv2
import dotenv
import os
from io import BytesIO

import numpy as np

dotenv.load_dotenv()

s3 = boto3.client(
    's3',
    endpoint_url=os.environ.get("FILEBASE_URL"),
    aws_access_key_id=os.environ.get("FILEBASE_KEY"),
    aws_secret_access_key=os.environ.get("FILEBASE_SECRET")
)

def upload(video_id: str, image_name: str, image: np.ndarray):
    _, buffer = cv2.imencode(".jpg", image)
    img_data = BytesIO(buffer)

    s3.put_object(Body=img_data, Bucket='crowdmon', Key='test.jpg')
    return 'yes'