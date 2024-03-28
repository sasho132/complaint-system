import os

from dotenv import load_dotenv
from fastapi.exceptions import HTTPException
from minio import Minio
from minio.error import S3Error

from utils.url_shortener import shorten_url

load_dotenv()


def file_upload(file_name, file_path):
    client = Minio(
        os.getenv("MINIO_HOSTNAME") + ":9000",
        access_key=os.getenv("MINIO_ACCESS_KEY"),
        secret_key=os.getenv("MINIO_SECRET_KEY"),
        secure=False,
    )

    bucket_name = "complaint-system"

    try:
        client.fput_object(
            object_name=file_name, bucket_name=bucket_name, file_path=file_path
        )
        presigned_url = client.get_presigned_url("GET", bucket_name, file_name)
        obj_url = shorten_url(presigned_url)
        return obj_url
    except S3Error as ex:
        raise HTTPException(500, "Minio is not available")
