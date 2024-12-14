from flask_restful_swagger_2 import Schema


class ErrorSchema(Schema):
    type = "object"
    properties = {
        "error": {"type": "string"},
        "status": {"type": "string", "example": "failed"},
    }
