Automation REST API testing project on Python

[![API tests](https://github.com/ivanovajulika/Api_Petstore/actions/workflows/action.yml/badge.svg)](https://github.com/ivanovajulika/Api_Petstore/actions/workflows/action.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
---
#  Swagger Petstore

[Api documentation]👉
[<img src="https://github.com/ivanovajulika/Api_Petstore/raw/main/picture/Swagger.jpg" alt='Swagger' width="200" height="150">](https://petstore.swagger.io/)
[OUR]👉
[<img src="https://logosmarken.com/wp-content/uploads/2021/03/Trello-Logo-650x366.png" alt='Trello' width="115" height="70">](https://trello.com/b/6n6e0r1L/psevdokodapip)

## Table of contents
- [Quick start](#some-start)
- [Pytest INFO](#some-pytest)
- [Allure](#some-allure)

___
## Quick start:<a name="some-stat"></a> [![Docker](https://img.shields.io/badge/docker-website-brightgreen.svg?style=flat-square)](https://docs.docker.com/)

> ***Do not forget to install Docker Desktop***

### **Docker commands for your terminal**
    docker build -t image_name .(for example: docker build -t api_pytest_runner .)
> ***This command create an image based on a dockerfile***

    docker run image_name(for example: docker run --rm api_pytest_runner)
> ***This command creates and runs a container based on an image. 
All tests will be run in a container. The container will be deleted after the end of the tests.***