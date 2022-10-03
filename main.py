from bs4 import BeautifulSoup
import requests
import os
HEADERS = {"User-Agent": "Mozilla/5.0"}
directory = os.getcwd()


def image_download(folder, obj, url):
    os.chdir(directory)
    os.mkdir(folder)
    os.chdir(directory + '\\' + folder)

    page = 0
    counter = 0
    while counter < 1000:
        print(page)
        url = f"{url}?p={page}&text={obj}"
        r = requests.get(url, HEADERS)
        soup = BeautifulSoup(r.text, "lxml")
        images = soup.findAll("img", class_="serp-item__thumb justifier__thumb")
        for image in images:
            if counter == 1000:
                return None
            image_url = f"https:{image.get('src')}"
            filename = f"{counter:04d}.jpg"
            picture = requests.get(image_url, HEADERS)
            with open(filename, 'wb') as f:
                f.write(picture.content)
            counter += 1
        page += 1


if __name__ == "__main__":
    image_download('dog', 'dog', "https://yandex.ru/images/search")
    image_download('cat', 'cat', "https://yandex.ru/images/search")
