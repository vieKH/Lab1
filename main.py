from bs4 import BeautifulSoup
import requests
import os
import logging
HEADERS = {"User-Agent": "Mozilla/5.0 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
           "Accept-Language": "en-US, ru-RU", "Accept-Encoding": "grip, deflate", "Connection": "keep-alive", "one": "true"}
directory = os.getcwd()


def create_file(folder):
    """ Эта фукнция для создании папки
        chdir (change directory) Первый я сделал каталог венрнулся в главный папки
        mkdir (make directory) Создать новую папку (folder)
        Если есть ошибка, она будет появиться на вывод (logging.info)
        :param folder: имена папки """
    try:
        os.chdir(directory)
        os.mkdir(folder)
        os.chdir(f"{directory}\\\\{folder}")
    except OSError as err:
        logging.info(f'При создании файл {folder} есть ошибки \n {err}')


def image_download(folder, obj, url, counter):
    """Эта функция для скачать фото
    Из библиотеки request получить код содержать фото
    Из библиотеки BS4 поменять код в lxml, поиск адресс фото и скачать их
    :param folder: имена папки
    :param obj: объект который вы хотите найти
    :param url: адресс страница ( В задаче https://yandex.ru/images/search?...)
    :param counter: количество фота хотите скачать ( в задаче 1000 фото)
    :return: не возращается значения , для закончить программу когда хватит 1000 фото"""
    create_file(folder)

    page = 0
    while counter > 0:
        print(f"Сейчас мы на странице {page}, ещё {counter} нужно скачать><")
        url = f"{url}?p={page}&text={obj}"
        r = requests.get(url, HEADERS)
        soup = BeautifulSoup(r.text, "lxml")
        images = soup.findAll("img", class_="serp-item__thumb justifier__thumb")
        for image in images:
            if counter == 0:
                return
            image_url = f"https:{image.get('src')}"
            filename = f"{counter:04d}.jpg"
            picture = requests.get(image_url, HEADERS)
            with open(filename, 'wb') as f:
                f.write(picture.content)
            counter -= 1
        page += 1


if __name__ == "__main__":
    image_download('dog', 'dog', "https://yandex.ru/images/search", 1000)
    image_download('cat', 'cat', "https://yandex.ru/images/search", 1000)
