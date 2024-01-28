FROM python:3.12-alpine

RUN apk update \
    && apk add musl-dev mariadb-connector-c-dev gcc

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]