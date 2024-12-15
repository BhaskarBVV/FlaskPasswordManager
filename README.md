# FlaskPasswordManager
This is a backend service for password management for users

## HOW TO CREATE CONTAINER
To start the container please pass the required environemnt variables:
1. Host
2. ENCRYPTION_SECRET_KEY
3. MONGO_URI

## HOST 0.0.0.0 is needed because:
Flask's development server binds to the host and handles network interfaces. 
By default, Flask binds to 127.0.0.1 (localhost), which makes the server accessible only from inside the container itself, not from the host machine or external clients.

## SAMPLE COMMAND TO CREATE CONTAINER:
docker run -d -p 8080:8080 \
    -e HOST = 0.0.0.0 \
    -e ENCRYPTION_SECRET_KEY = KEY_VALUE \
    -e MONGO_URI = BASE_URI\
    --name <contianer_name> <image_name>

## CAUTION: 
The Same ENCRYPTION_SECRET_KEY will be used while fetching the passwords from database.
Don't loose it.