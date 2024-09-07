from fastapi import FastAPI, Path
from typing import Annotated


# python -m uvicorn M16T1:app
app = FastAPI()

@app.get("/")
async def welcome():
	return "Главная страница"

@app.get("/user/admin")
async def user_admin():
	return "Вы вошли как администратор"

@app.get("/user/{id}")
async def user_user(id: Annotated[int, Path(
		ge=1, le=100,
		description="Enter User ID",
		example="1"
	)]):
	return f"Вы вошли как пользоввткль №{id}"

@app.get("/user/{username}/{age}")
async def news(username: Annotated[str,  Path(
		min_length=5, max_length=20,
		description="Enter username",
		example="UrbanUser"
	)], age: Annotated[int, Path(
		ge=18, le=120,
		description="Enter age",
		example="24"
	)]):
	return f"Информация о пользователе: имя - {username}, возраст - {age}"
