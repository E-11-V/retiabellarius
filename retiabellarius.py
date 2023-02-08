import requests
import os
import re
import urllib.parse
from tqdm import tqdm

def download_from_web_archive(urls):
    for url in urls:
        archive_url = "https://web.archive.org/web/" + url
        response = requests.get(archive_url)
        if response.status_code == 302:
            location = response.headers["Location"]
            match = re.search(r"https://web.archive.org/web/(\d+)/" + url, location)
            if match:
                archive_url = match.group(0)
                response = requests.get(archive_url)
        content_length = int(response.headers.get("Content-Length", 0))
        filename = urllib.parse.quote(url, safe="")
        with open(filename, "wb") as f:
            for chunk in tqdm(response.iter_content(1024), total=content_length // 1024, unit="KB", desc=filename):
                f.write(chunk)
        print(f"Downloaded content from {url} to {filename}")


urls = [
    -replace this with urls-
]

download_from_web_archive(urls)
