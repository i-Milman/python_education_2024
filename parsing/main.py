import datetime
import requests
import json
from bs4 import BeautifulSoup

# Скачивание сайта

# date: datetime.date = datetime.date.today() + datetime.timedelta(days=7)
# print(date)
#
# # говорим веб-серверу, что хотим получить html
# st_accept = "text/html"
# # имитируем подключение через браузер Mozilla на macOS
# st_useragent = "Fancy-Browser/2.0"
# # формируем хеш заголовков
# headers = {
#     "Accept": st_accept,
#     "User-Agent": st_useragent
# }
# # отправляем запрос с заголовками по нужному адресу
# req = requests.get(f"https://afisha.yandex.ru/saint-petersburg/cinema?source=menu&date={date}", headers)
# src = req.text
# with open('afisha.yandex.ru.html', 'wb') as f:
#     f.write(src.encode('utf-8'))

# Анализ

src = str()
with open ('afisha.yandex.ru.html', 'rb') as f:
    src = f.read()

# Создаем объект BeautifulSoup и указываем парсер
soup = BeautifulSoup(src, 'html.parser')
event_card = soup.find_all('div', class_='i-react event-card-react i-bem')

print(*event_card, sep='\n\n')

