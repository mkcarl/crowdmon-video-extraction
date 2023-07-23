import psycopg2
import os
import dotenv

dotenv.load_dotenv()

connection_string = f"dbname={os.environ['POSTGRES_DB']} user={os.environ['POSTGRES_USER']} password={os.environ['POSTGRES_PASSWORD']} host={os.environ['POSTGRES_HOST']} port={os.environ['POSTGRES_PORT']}"
conn = psycopg2.connect(connection_string)


def write_image(name: str, url: str):
    """
    :param name: name of the image
    :param url: cloudinary url of the image
    :return:
    """
    print(f"Writing {name} to database")
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO image(name, source, url) values (%s, 'YouTube', %s)",
                (name, url)
            )
    print(f"Successfully wrote {name} to database")
