run_mysql:
	docker compose up -d

run_django:
	python manage.py runserver

create_migration:
	python manage.py makemigrations

apply_migration:
	python manage.py migrate

down:
	docker compose down