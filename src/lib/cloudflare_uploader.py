import os
from io import BytesIO

import boto3
import cv2
import dotenv
import numpy as np

dotenv.load_dotenv()
cloudflare_r2_url = os.getenv('CLOUDFLARE_R2_URL')
cloudflare_r2_key_id = os.getenv('CLOUDFLARE_R2_KEY_ID')
cloudflare_r2_secret = os.getenv('CLOUDFLARE_R2_SECRET')
image_url_prefix = os.getenv('IMAGE_URL_PREFIX')

s3 = boto3.client('s3',
    endpoint_url= cloudflare_r2_url,
    aws_access_key_id= cloudflare_r2_key_id,
    aws_secret_access_key= cloudflare_r2_secret
    )


def upload(video_id: str, image_name: str, image: np.ndarray):
    _, buffer = cv2.imencode(".jpg", image)
    img_data = BytesIO(buffer)
    key = f'{video_id}/{image_name}.jpg'

    s3.put_object(Body=img_data, Bucket='crowdmon', Key=key)
    return f"{image_url_prefix}/{key}"