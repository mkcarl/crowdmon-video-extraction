from src.lib.video_processor import extract

if __name__ == '__main__':
    URLS = [
        "https://youtu.be/MnqWQQzXWZE",
        "https://youtu.be/MGZIuKuXI6A",
        "https://youtu.be/uu_x8HW3_eg",
        "https://youtu.be/TkEXIJ8XoMY",

    ]

    for url in URLS:
        extract(url)