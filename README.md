# FlaskPasswordManager
This is a backend service for password management for users

# How you can manually run the setup locally:
The backend setup consists of flask API, and MongoDb cluster.
1. Create a local network, under which you mongoDb and password manager clusters can communicate as: 
    docker network create <network-name>
2. Create the lastest image of password manager as:
    docker build -t <Image-name> .
3. Spin up the mongoDb cluster, you can assign the docker volume if you want as:
    docker run -it --name <container-name> --network <network-name> mongo
    Note: mongo is the name of the image.
4. Spin the password manager cluster.
    docker run -it -p 8080:8080 \
        -e HOST=0.0.0.0 \
        -e ENCRYPTION_SECRET_KEY=<KEY_VALUE> \
        -e MONGO_URI=mongodb://mongo-db:27017 \
        --name <container-name> \
        --network <network-name> \
        <image_name>:latest
5. We have now successfully build all the requirements.
6. Make API Call to the password manager. First check the base-url of flask server.
It would be like: "http://127.0.0.1:8080"
7. Now, you will need user. So, add a new user with the following cURL:
curl --location 'http://127.0.0.1:8080/users' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "bhaskar4W1222",
    "first_name": "Bhaskar",
    "last_name": "Varshney",
    "email": "bhaskar.nv7@gmail.com",
    "password": "BhaskarBhaskar1@"
}'
8. Now login:
curl --location 'http://127.0.0.1:8080/auth/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "bhaskar4W1222",
    "password": "BhaskarBhaskar1@"
}'
9. We will use the session-id received in the response of login. Now. you can add a new password as:
curl --location 'http://127.0.0.1:8080/passwords' \
--header 'cookie: session=35020708-1232-412c-94fe-904cd486c54f' \
--header 'Content-Type: application/json' \
--data-raw '{
    "website": "leetcode122.com",
    "username": "SDE3",
    "email":"",
    "password": "Let1Code@Pass"
}'

10. To fetch all user saved passwords:
curl --location 'http://127.0.0.1:8080/passwords' \
--header 'cookie: session=35020708-1232-412c-94fe-904cd486c54f' \
--header 'Content-Type: application/json'

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
3. While spinning up the flask container, in the connection string pass: <container_name>:27017, as:
docker run -it -p 8080:8080 \
-e HOST=0.0.0.0 \
-e ENCRYPTION_SECRET_KEY=<KEY_VALUE> \
-e MONGO_URI=mongodb://mongo-db:27017 \
--name <container-name> \
--network <network-name> \
<image_name>:latest
4. 27017 is the default port at which mongoDb serves the request inside the container.

## USING DOCKER COMPOSE:
use command: docker-compose up
Note: before running docker compose up, don't forget to set the ENCRYPTION_SECRET_KEY in the terminal for that session
use command: set ENCRYPTION_SECRET_KEY=<value>

## CAUTION: 
The Same ENCRYPTION_SECRET_KEY will be used while fetching the passwords from database.
Don't loose it.