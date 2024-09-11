run:
	uvicorn main:app --reload
	
review:
	alembic revision --autogenerate -m "Create User model"

upgrade:
	alembic upgrade head

downgrade:
	alembic downgrade base

generate_migrations: upgrade
	alembic revision --autogenerate -m "Create User and Note models"