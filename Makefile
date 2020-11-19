docker:
	@docker-compose down --remove-orphans
	@docker-compose build
	@docker-compose up

django-makemigrations:
	docker-compose run --rm django ./manage.py makemigrations

django-migrate:
	docker-compose run --rm django ./manage.py migrate

django-createsuperuser:
	docker-compose run --rm django ./manage.py createsuperuser

test:
	@docker-compose run --rm django flake8
	@docker-compose run --rm django pytest
