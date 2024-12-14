from flask import Flask
from routes import ROUTES
from flask_cors import CORS
from flask_restful_swagger_2 import Api

app = Flask(__name__)
CORS(app)
api = Api(
    app,
    api_version="1.0.0",
    title="Password Manager svc",
    description="The service for managing the passwords.",
)

for route in ROUTES:
    api.add_resource(route[0], route[1])

if __name__ == "__main__":
    app.run(debug=True, port=8080)
