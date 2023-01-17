import os
import shutil
import sys
import webbrowser
import zipfile
from time import sleep

import requests
from PIL import Image

from env_paths import DOWNLOAD_PATH, OUTPUT_PATH

try:

    class C:
        b = "\033[94m"
        y = "\033[93m"
        g = "\033[92m"
        e = "\033[0m"

    try:
        comic_url = sys.argv[1].strip()

        if not comic_url.startswith("https://comick.app/comic/"):
            raise requests.exceptions.InvalidURL

        r = requests.get(comic_url, timeout=5)
        if not r:
            raise requests.exceptions.ConnectionError
    except IndexError:
        print(C.y + "No URL was passed!" + C.e)
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        print(
            C.y
            + "It was not possible to connect to the API!\nVerify your connection or the URL!"
            + C.e
        )
        sys.exit(1)
    except requests.exceptions.InvalidURL:
        print(C.y + "Invalid URL!" + C.e)
        sys.exit(1)

    def get_api_url(url: str) -> str:
        comic_code = url.split("/")[-1].split("-")[0]
        return f"https://api.comick.app/chapter/{comic_code}/download"

    def get_folder_name(url: str) -> str:
        comic_name = url.split("/")[-2]
        comic_chapter = url.split("/")[-1].split("-")[-2]
        return f"{comic_name}-{comic_chapter}"

    folder_name = get_folder_name(comic_url)
    api_url = get_api_url(comic_url)

    print(C.b + "\nConnecting to the API...\n" + C.e)
    webbrowser.open(api_url)
    sleep(10)

    print("\n")
    while not os.path.exists(f"{DOWNLOAD_PATH}{folder_name}.zip"):
        print(C.y + "Waiting the download to finish...\r", end="")
        sleep(1)

    print(C.g + "\n\nDownload Completed!" + C.e)

    with zipfile.ZipFile(f"{DOWNLOAD_PATH}{folder_name}.zip", "r") as zip_ref:
        print(C.b + "\nUnzipping images..." + C.e)
        if not os.path.exists(DOWNLOAD_PATH + folder_name):
            os.mkdir(DOWNLOAD_PATH + folder_name)
        zip_ref.extractall(DOWNLOAD_PATH + folder_name)

    print(C.b + "\nBuilding PDF file..." + C.e)

    os.chdir(DOWNLOAD_PATH + folder_name)

    images = os.listdir(".")
    images.sort(key=lambda x: int(x.split(".")[0]))
    cover = Image.open(images[0]).convert("RGB")
    image_list = [Image.open(image).convert("RGB") for image in images[1:]]

    try:
        file_name = sys.argv[2]
    except IndexError:
        file_name = folder_name

    cover.save(f"{OUTPUT_PATH}{file_name}.pdf", save_all=True, append_images=image_list)

except KeyboardInterrupt:
    print(C.y + "\nInterruption Detected! Program Closed!" + C.e)
else:
    print(C.g + "\nConvertion Completed! The PDF is stored at: " + C.e + OUTPUT_PATH)
finally:
    try:
        shutil.rmtree(DOWNLOAD_PATH + folder_name, ignore_errors=True)
        os.remove(f"{DOWNLOAD_PATH}{folder_name}.zip")
        print(C.g + "\nTemporary files cleaned!" + C.e)
    except (NameError, KeyboardInterrupt, FileNotFoundError):
        pass
    else:
        print(C.g + "\nAll Done!\n" + C.e)
