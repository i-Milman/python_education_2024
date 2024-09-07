from fastapi import FastAPI


# python -m uvicorn M16T1:app
app = FastAPI()

@app.get("/")
async def welcome():
	return "Главная страница"

@app.get("/user/admin")
async def user_admin():
	return "Вы вошли как администратор"

@app.get("/user/{id}")
async def user_user(id: str):
	return f"Вы вошли как пользоввткль №{id}"

@app.get("/user")
async def news(username: str, age: str):
	return f"Информация о пользователе: имя - {username}, возраст - {age}"
