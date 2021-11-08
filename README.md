# :point_right: SpotHero API Installation Steps :star_struck: : SpotHero Backend Engineer Challenge :white_check_mark:

## Requirements (Development Tools)

This App was devepled with the following dev tools:
- Python 3.9
- Docker v19.03.12
- docker-compose v1.27.2

## NOTE: Please, clone the repo if you have not. :innocent:

# Serve the App Locally via following ways:
## 1. With using Docker Compose

The SpotHero API will be run locally on your pc soon, needs to navigate to the root directory of the repo and execute the following commands:
### Start serve the app (Spin up and Start development servers)
```
docker-compose up -d --build
```
This command starts build the docker images with the name `spotheroapi_backend` (Python:3.9 image for Django Rest Framework) And also starts development servers: `spotheroapi_backend_1` (SpotHero APIs).

### Stop serve the app (Stop development servers)
```
docker-compose down -v
```
This command stops the docker containers (development servers) `spotheroapi_backend_1` (SpotHero APIs).

NOTE: (__*For start again development servers*__), just need to execution the command:  ```docker-compose up -d``` without create/build the images.


## 2. Without using Docker Compose

1. __Create Python virtual env__: 
To convert Given xlsx input data file to sqlite3 db and install application dependencies, navigate to the root directory of the repo and execute the following command.
```
python3 -m venv python_venv
```
2. __Activate virtual python env__ (python_venv): 
Navigate to the spotheroapi directory of the repo and execute the following command.
```
source python_venv/bin/activate
```
3. __Install requirement python package__: 
Navigate to the spotheroapi directory of the repo and execute the following command.
```
pip install -r requirements.txt
```
4. __Start Back-end Server__: 
Open new terminal, Navigate to the root directory of the repo and execute the following commands. (:warning:.venv should be activated, if not then ref step: 2)
```
python manage.py makemigrations parkprice parkspot
&& python manage.py migrate
&& python manage.py load_intial_data
&& python manage.py runserver 0.0.0.0:5000
```

## API Testing
Run pytest commnad (pyton_venv should be activated and requirements package need to be installed)
```
pytest
```

## Back-end server URLs :star_struck:
The Back-end REST APIs should be available at http://localhost:5000/.
- The Admin Interface should be available at http://localhost:5000/admin/ .  
  - usr:pass -- admin:admin
  - Note: create superuser (need to run onetime only) `echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell`
- The Swagger Docs should be available at http://localhost:5000/swagger/.
- The ReDoc should be available at http://localhost:5000/redoc/.

## :tada: Finally, The SpotHero API Web-App should be available at http://localhost:5000/. :star_struck:


## SpotHero API Web-App (Coding Challenge)
- The application publishes an API with two endpoints that computes a price for an input datetime
range.
- The API must respond to requests on port 5000
- The API must respond using JSON

## Requirements
- [x] Build rates Endpoint (GET, PUT, POST, DELETE)
- [x] Build prices endpoint (GET)
  - e.g: http://localhost:5000/prices/?start=2015-07-01T07:00:00-05:00&end=2015-07-01T12:00:00-05:00
- [x] Load given Intial json data (rates) in db (When application start)
- [x] Python (v3.9) as primary backend programing language
- [x] API endpoints must be documented
- [x] Tests need to be in place
- [x] There must be documentation that one can follow the get the application up and running
- [x] There must be documentation that one can follow the get the application up and running

## Extra Credit :star_struck:
- [x] Build rates Endpoint (POST, DELETE)
- [x] :sunglasses: Include a Swagger Spec
  - The Swagger Docs should be available at http://localhost:5000/swagger/.
  - The ReDoc should be available at http://localhost:5000/redoc/.
- [x] :sunglasses: Include a Dockerfile 
- [ ] :star_struck: Metrics for endpoint(s) captured and available to be queried via an endpoint (e.g. average response
time). Add the metrics you feel would be appropriate to identify the health and performance of your
application
- [x] :cool: Get REST API Response in json/api format.
  - e.g:
    - http://localhost:5000/property/?format=json
    - http://localhost:5000/property/?format=api
   
  
