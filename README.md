# toyota_store user guide

## Starting an app:
1. docker-compose up -d
2. Run `prepare_db.py` script to populate db
3. Run  `main.py` script to run an app

## Endpoints:

POST `/api/tokens/` - request auth token (basic auth required)

GET `/api/cars/` - returns a list of all cars in db

GET `/api/model/{id}` - returns a car model or a list of all models if no id was provided
 
GET `/api/colour/{id}` - returns a car colour or a list of all colours if no id was provided

GET `/api/engine/{id}` - returns a car engine or a list of all engines if no id was provided

GET `/api/gearbox/{id}` - returns a car gearbox or a list of all gearboxes if no id was provided

PUT `/api/car/` - add a new car into DB. Token auth required. Request body example:

{
	"model": 1,
	"colour": 1,
	"gearbox": 1,
	"engine_capacity": 1
}
