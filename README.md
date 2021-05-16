# AVINA API

## Create and Activate Virtual Environment

```shell
python3 -m venv venv
source venv/bin/activate
```

## Install dependencies

```shell
pip install -r requirements.txt
```

## .env file

The .env file contains the environment variables and values needed to run the application. This can be created from the .env.example file by substituting for the actual environment values.

NOTE: To run website, create a local `.env` file from the `.env.example` file at the application root.

## Database Requirement

A PostgreSQL database is required for this project.

### Run application

```shell
python3 manange.py runserver
```

### **ps: Perform databases migration**

To run application for the first time, perform database migration using the commands below at the root folder

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

### Endpoints

All available endpoints are documented and published [here](https://documenter.getpostman.com/view/11647149/TWDdiDAF)
