from bs4 import BeautifulSoup
import requests
import os
HEADERS = {"User-Agent": "KH"}
directory = os.getcwd()


def image_download(folder, obj):
    os.chdir(directory)
    try:
        os.mkdir(folder)
    except IOError:
        pass
    os.chdir(directory + '\\' + folder)

    page = 0
    counter = 0
    while counter < 1000:
        print(page)
        url = f"https://yandex.ru/images/search?p={page}&text={obj}"
        r = requests.get(url, HEADERS)
        soup = BeautifulSoup(r.text, "lxml")
        image_need = 0
        images = soup.findAll("img", class_="serp-item__thumb justifier__thumb")
        for image in images:
            if counter == 1000:
                return None
            image_url = "https:" + image.get("src")
            filename = str(counter).rjust(4, '0') + ".jpg"
            picture = requests.get(image_url, HEADERS)
            direct = open(filename, 'wb')
            direct.write(picture.content)
            direct.close()
            counter = counter + 1
            image_need = image_need + 1
        page = page + 1


image_download('dog', 'dog')
image_download('cat', 'cat')
