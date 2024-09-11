# Задача "Список пользователей в шаблоне":
# Подготовка:
# Используйте код из предыдущей задачи.
# Скачайте заготовленные шаблоны для их дополнения.
# Шаблоны оставьте в папке templates у себя в проекте.
# Создайте объект Jinja2Templates, указав в качестве папки шаблонов - templates.
# Измените и дополните ранее описанные CRUD запросы:
# Напишите новый запрос по маршруту '/':
# Функция по этому запросу должна принимать аргумент request и возвращать TemplateResponse.
# TemplateResponse должен подключать ранее заготовленный шаблон 'users.html',
#   а также передавать в него request и список users.
#   Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
# Измените get запрос по маршруту '/users' на '/users/{user_id}':
# Функция по этому запросу теперь принимает аргумент request и user_id.
# Вместо возврата объекта модели User, теперь возвращается объект TemplateResponse.
# TemplateResponse должен подключать ранее заготовленный шаблон 'users.html',
#   а также передавать в него request и одного из пользователей - user.
#   Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
# Создайте несколько пользователей при помощи post запроса со следующими данными:
# username - UrbanUser, age - 24
# username - UrbanTest, age - 22
# username - Capybara, age - 60
# В шаблоне 'users.html' заготовлены все необходимые теги и обработка условий,
#   вам остаётся только дополнить закомментированные строки вашим Jinja 2 кодом
#   (использование полей id, username и age объектов модели User)
#   1. По маршруту '/' должен отображаться шаблон 'users.html' со списком все ранее созданных объектов
#   2. Здесь каждая из записей является ссылкой на описание объекта,
#   информация о котором отображается по маршруту '/users/{user_id}'

# Решение:
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/users/{user_id}")
async def get_user(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
    new_id = 1 if not users else users[-1].id + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")
