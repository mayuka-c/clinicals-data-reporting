# Clinicals Data Reporting App using Django

## Running the app
 
Note: Make sure the Docker is installed

### ***Using docker***

Run mysql container
```bash
docker run --name django-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=clinicalsdb -p 3306:3306 -d mysql
```

Build the app
```bash
docker build -t clinicals_app .
docker run -t --name=clinicals_app --link django-mysql:mysql -p 10111:8000 clinicals_app
docker exec -it clinicals_app python manage.py migrate
```

Run the app
- Open the url `localhost:10111` in the browser

### ***Using docker compose***
```bash
docker-compose up
```

Run the app
- Open the url `localhost:8000` in the browser

