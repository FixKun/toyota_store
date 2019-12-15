# toyota_store user guide

## Starting an app:
1. docker-compose up -d
2. Run `prepare_db.py` script to populate db
3. Run  `main.py` script to run an app

## Endpoints:

POST `/api/tokens/` - request auth token (basic auth required)
GET `/api/cars/` - returns a list of all cars in db
GET `/api/model/{id}`
GET `/api/colour/{id}`
GET `/api/engine/{id}`
GET `/api/gearbox/{id}`
PUT `/api/car/`