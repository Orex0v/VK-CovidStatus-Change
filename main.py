import requests
from time import sleep


TOKEN = ""
APP_ID = "7362610"
METHOD = "users.setCovidStatus"
FORMAT = "json&v=5.103"
time_sleep = 2  # Задаем интервал


def status_change():
    for status_id in range(1, 18):
        url = f"https://api.vk.com/method/users.setCovidStatus?api_id={APP_ID}" \
              f"&method={METHOD}" \
              f"&format={FORMAT}" \
              f"&status_id={status_id}" \
              f"&access_token={TOKEN}"
        get = requests.post(url)
        data = get.json()
        try:  # Проверяем токен
            if data["response"]:
                print(f"Новый статус с номером: {status_id} успешно поставлен")
        except:
            print("Ошибка токена")
        sleep(time_sleep)


while True:
    status_change()
