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
events = soup.find_all('div', class_='i-react event-card-react i-bem')

# print(*events, sep='\n')
# print()

for i in range(len(events)):
    # Вытаскиваю оттуда JSON
    jtext = str(events[i])
    jtext = jtext[jtext.find('{'):jtext.rfind('}') + 1]

    # Извлекаем нужную информацию с помощью json
    event_data = json.loads(jtext)
    props = event_data['event-card-react']['props']

    # Печатаем информацию
    print("Название:", props['title'])
    try:
        print('Описание:', props['argument'])
    except:
        print('Описание: отсутствует')
    print("Возрастное ограничение:", props['ageLimit'])
    print("Ссылка на изображение:", props['image']['retina']['2x'])
    print("Ссылка на событие:", "https://afisha.yandex.ru" + props['link'])
    print()


