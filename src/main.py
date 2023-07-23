from src.lib.video_processor import extract

if __name__ == '__main__':
    URLS = [
        "https://youtu.be/L5aXPk01G6k",
        "https://youtu.be/MGZIuKuXI6A",
        "https://youtu.be/uu_x8HW3_eg"
    ]

    for url in URLS:
        extract(url)