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

## SAMPLE COMMAND TO CREATE CONTAINER SINGLE CONTAINER (+ MongoDb's cloud instance)
docker run -d -p 8080:8080 \
    -e HOST=0.0.0.0 \
    -e ENCRYPTION_SECRET_KEY=<KEY_VALUE> \
    -e MONGO_URI=<BASE_URI>\
    --name <contianer_name> <image_name>

## IF YOU ARE ALSO USING MONGODB'S CONTAINER:
1. Create common network under which both networks can communicate.
2. Spin mongo container: docker run -it --name mongo-db --network <network-name> mongo
2. While spinning up the flask container, in the connection string pass: <container_name>:27017, as:
docker run -it -p 8080:8080 \
-e HOST=0.0.0.0 \
-e ENCRYPTION_SECRET_KEY=<KEY_VALUE> \
-e MONGO_URI=mongodb://mongo-db:27017 \
--name <container-name> \
--network <network-name> \
<image_name>:latest
3. 27017 is the default port at which mongoDb serves the request inside the container.

## USING DOCKER COMPOSE:
use command: docker-compose up
Note: before running docker compose up, don't forget to set the ENCRYPTION_SECRET_KEY in the terminal for that session
use command: set ENCRYPTION_SECRET_KEY=<value>

## CAUTION: 
The Same ENCRYPTION_SECRET_KEY will be used while fetching the passwords from database.
Don't loose it.