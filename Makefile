run:
	python manage.py runserver

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

collect-static:
	python manage.py collectstatic

superuser:
	python manage.py createsuperuser