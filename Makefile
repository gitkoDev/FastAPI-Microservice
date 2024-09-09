run:
	fastapi dev main.py

review:
	alembic revision --autogenerate -m "Create User model"

upgrade:
	alembic upgrade head