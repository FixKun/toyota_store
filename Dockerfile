# Dockerfile

# Pull base image
FROM python:3.7

# Set work directory
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
EXPOSE 80
ENV FLASK_APP /src/main.py

# CMD ./migrations/alembic update head
CMD ["python", "./src/db/prepare_db.py"]
CMD ["python", "./src/main.py"]