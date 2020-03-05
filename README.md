# RealEstate API
![badge](https://img.shields.io/badge/version-1.0.0-green.svg)

> An simple API to create, update, delete or list estates using Django Rest Framework

## Requirements
- Install [Git](https://git-scm.com/downloads)
- Install [Docker](https://www.docker.com/get-started)
- Install [DockerCompose](https://docs.docker.com/compose/install/)
- Install [Postman](https://www.postman.com/downloads/)

## Install
### Get repository:
``` bash
$ git clone git@github.com:JoValo/realEstate.git
$ cd realEstate
```
## Run with docker
### Build and up Dockerfile
``` bash
$ docker-compose build
$ docker-compose up
```

### Examples of interaction with docker
``` $bash
$ docker exec -it realestate_api_1 python manage.py makemigrations
$ docker exec -it realestate_api_1 python manage.py migrate
```

## Postman