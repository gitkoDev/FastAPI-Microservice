run:
	docker compose up --build
	
upgrade:
	alembic upgrade head

downgrade:
	alembic downgrade base

generate_migrations:
	alembic revision --autogenerate -m "Create User and Note models"