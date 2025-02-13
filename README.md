# Ride Hailing Dynamic Pricing API

This is a Django-based API for calculating dynamic pricing for a ride-hailing app.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/OdoEmmanuel/lincride.git
   cd lincride

## Create environment folder
python -m venv env

## Activate env
source env/bin/activate

## Install dependencies
pip install -r requirements.txt


## Run migrations to create the table in the database
python manage.py makemigrations
python manage.py migrate


## Start the Django development server:
python manage.py runserver


## Access the API endpoint:
http://127.0.0.1:8000/api/calculate-fare/?distance=10&traffic_level=high&demand_level=peak


## Run test script
python manage.py test pricing


## Update pricing via the Django admin interface:
http://127.0.0.1:8000/admin/


## Create an Admin User
   ## Enter Username, Email Address and Password
python manage.py createsuperuser