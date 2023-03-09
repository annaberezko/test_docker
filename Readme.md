### Docker container for Django project + postgres
#### Create .env variables file for dev
```
SECRET_KEY=<your_secret_key>
ALLOWED_HOSTS=*
DEBUG=True

POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_USER=hello_django
POSTGRES_PASSWORD=hello_django
POSTGRES_DB=hello_django_dev
POSTGRES_HOST=db
POSTGRES_PORT=5432

```
#### Create Dockerfile and docker-compose.yml
#### in terminal
```
docker-compose build
docker-compose up
```
For connect with db create migrations and create superuser admin, just in case
```
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py createsuperuser 
```
#### turn off the container
```
docker-compose down
```