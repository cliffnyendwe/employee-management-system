# Employee System Management

By Cliff Nyendwe, 17/03/2019

### Django admin username

Use the username below to get into my admin
* cliff

### Django admin password

This is my password
* 12344

# Description

This awesome application is meant to keep employers records and also to manage the employers. This will be possible as it requires the employees to give out all their details including the employees unique number.


# Contacts
To find me, use: cliffnyendwe2018@gmail.com
0710755176

# Code Example

Kindly to access code clone the repository.

# Motivation

To keep track of employees.

# Language used

Django - web framework used
HTML
CSS
postgresql
bootstrap4

# pip3 install -r requirements

The following libraries are required
Django==1.11
django-bootstrap4==0.0.7
django-mathfilters==0.4.0
psycopg2==2.7.7
pytz==2018.9


# Installation Requirements

* Clone this repo: git clone https://github.com/cliffnyendwe/employee-management-system.git

* The repo comes in a zipped or compressed format. Extract to your prefered location and open it.

* open your terminal and navigate to award then create a virtual environment.For detailed guide refer here

* To run the app, you'll have to run the following commands in your terminal

* pip install -r requirements.txt
* On your terminal,Create database employ using the command below.

### CREATE DATABASE employ;

* Migrate the database using the command below

* python3.6 manage.py migrate
* Then serve the app, so that the app will be available on localhost:8000, to do this run the command below
* python manage.py runserver
* Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

# Creating a virtual environment

* sudo apt-get install python3.6-venv
* python3.6 -m venv virtual
* source virtual/bin/activate

# Known Bugs & Missing Features

This are features that i didnt manage to accomplish but soon i will include them.

* The CSV upload
* The modal


# License
The project is under license by MIT

# Prerequisites
You will need the following things properly installed on your computer.

* visual studio
* git
* github


# How to deploy to heroku

* Sgn up to heroku account if you dont have an account.
* Then install the Heroku Toolbelt. It is a command line tool to manage your Heroku apps.
* After installing the Heroku Toolbelt, open a terminal and login to your account:

* $ heroku login
* Enter your Heroku credentials.
* Email: gmail.com
* Password (typing will be hidden):
* Authentication successful.

# Add the following:

* Add a Procfile in the project root;
* Add requirements.txt file with all the requirements in the project root;
* Add Gunicorn to requirements.txt;
* A runtime.txt to specify the correct Python version in the project root;
* Configure whitenoise to serve static files.

* Add this to Procfile : web: gunicorn your_project_name.wsgi --log-file -

* Configure static related parameter in settings.py
* Pip install whitenise
* pip freeze > requirements.txt
* pip install python-decouple
* pip install dj-database-url
* Edit settings.py to enable decouple to use the .env configurations.
* Create heroku app eg: heroku create app_name
* Add postgress addon : heroku addons:create heroku-postgresql:hobby-dev
* Add all your configurations in .env file directly to heroku by running the this command: heroku config:set $(cat .env | sed '/^$/d; /#[[:print:]]*$/d')
* git push heroku master
* Run migration with this command : heroku run python manage.py migrate
*  Push your local db to postgres with this command : heroku pg:push mylocaldb DATABASE_URI --app heroku app_name

