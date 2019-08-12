# toyota_store


docker run --name sqlalchemy-orm-psql -e POSTGRES_PASSWORD=pass -e POSTGRES_USER=usr -e POSTGRES_DB=sqlalchemy -p 5432:5432 -d postgres


# Migrations
set FLASK_APP=src\main.py

flask db migrate -m "comment"
flask db upgrade