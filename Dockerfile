FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/test_docker

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/test_docker

EXPOSE 5000
CMD ["python", "manage.py", "migrage"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
