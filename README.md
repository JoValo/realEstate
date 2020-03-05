# RealEstate API
![badge](https://img.shields.io/badge/version-1.0.0-green.svg)

> An simple API to create, update, delete or list estates using Django Rest Framework: [truehome.api.io](http://elb-th-apps-895706480.us-east-1.elb.amazonaws.com/api/real_estate/)

## Test with Postam
- [Check API](https://documenter.getpostman.com/view/2049177/SzRw2BGT)

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

### Create CoordinatesValidation lambda
The instructions are in `lambdas/analysis/README.md`

## Run with docker
### Set your AWS Credentials in docker-compose.yml
``` yml
AWS_DEFAULT_REGION: us-east-1
AWS_ACCESS_KEY_ID: AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```
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
