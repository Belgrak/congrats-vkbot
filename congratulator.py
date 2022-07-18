import time
from urllib import request
import json
from vk_api import *
from datetime import datetime

URL = "https://www.davno.ru/cards/bd.html"  # url of website with greeting images


def get_congratulation_image():
    url = request.urlopen(URL)
    return url.read()


def congratulate_by_id(destination_id):
    # image = get_congratulation_image()
    vk.messages.send(peer_id=destination_id, random_id=0, message="Поздравляю! С днем рождения)")
    # here could be chosen other int for random_id


with open("configs_and_settings.json", "r") as f:
    file_data = f.read()
    json_data = json.loads(file_data)
    login = json_data['login']
    password = json_data['password']
    token = json_data['token']
    app_id = json_data['app_id']

api = VkApi(login, password, token, app_id=app_id)
api.auth()
vk = api.get_api()

while True:
    currentDate = datetime.now().strftime("%-d.%-m")

    friendsList = vk.friends.get(fields="bdate")['items']
    toCongratulateList = [i for i in friendsList if "bdate" in i.keys() if currentDate in i['bdate']]
    for i in toCongratulateList:
        congratulate_by_id(i['id'])
    time.sleep(24*60*60)  # sleeping for one day
