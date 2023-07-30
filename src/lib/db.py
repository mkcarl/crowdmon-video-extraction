import psycopg2
import os
import dotenv

dotenv.load_dotenv()

connection_string = f"dbname={os.environ['POSTGRES_DB']} user={os.environ['POSTGRES_USER']} password={os.environ['POSTGRES_PASSWORD']} host={os.environ['POSTGRES_HOST']} port={os.environ['POSTGRES_PORT']}"
conn = psycopg2.connect(connection_string)


def write_image(video_name: str, image_name: str, url: str):
    """
    :param image_name: individual frame name
    :param video_name: source video name
    :param url: cloudinary url of the image
    :return:
    """
    print(f"Writing {video_name}/{image_name} to database")
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO image(image_name, video_name, source, url) values (%s, %s,'YouTube', %s)",
                (image_name, video_name, url)
            )
    print(f"Successfully wrote {video_name}/{image_name} to database")
