# toyota_store user guide

## Starting an app:
1. docker-compose up -d
2. Run `prepare_db.py` script to populate db
3. Run  `main.py` script to run an app

## Endpoints:

GET `/cars/` - returns a list of all cars in db
GET `/model/{id}`
GET `/colour/{id}`
GET `/engine/{id}`
GET `/gearbox/{id}`
PUT `/car/`