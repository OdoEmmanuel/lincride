# Ride Hailing Dynamic Pricing API

This is a Django-based API for calculating dynamic pricing for a ride-hailing app.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/OdoEmmanuel/lincride.git
   cd lincride


python -m venv env

source env/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

http://127.0.0.1:8000/api/calculate-fare/?distance=10&traffic_level=high&demand_level=peak

python manage.py test pricing