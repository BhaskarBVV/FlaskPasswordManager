from flask_restful_swagger_2 import Schema


# UserSchema class definition for serialization and validation
class AddUserSchema(Schema):

    properties = {
        "username": {"type": "bhaskar"},
        "first_name": {"type": "string", "example": "first"},
        "second_name": {"type": "string", "example": "second"},
        "password": {"type": "string", "example": "Password@123"},
        "email": {"type": "string", "example": "bhaskar@gmail.com"},
    }

    @staticmethod
    def validate_username(username):
        if not username:
            return "Username is required.", False
        if len(username) < 4:
            return "Username should be at least 4 characters long.", False
        return None, True

    @staticmethod
    def validate_first_name(first_name):
        if not first_name:
            return "First name is required.", False
        if len(first_name) < 2:
            return "First name should be at least 2 characters long.", False
        return None, True

    @staticmethod
    def validate_second_name(second_name):
        if not second_name:
            return "Second name is required.", False
        if len(second_name) < 2:
            return "Second name should be at least 2 characters long.", False
        return None, True

    @staticmethod
    def validate_password(password):
        if not password:
            return "Password is required.", False
        if len(password) < 8:
            return "Password should be at least 8 characters long.", False
        if not any(char.isdigit() for char in password):
            return "Password should contain at least one number.", False
        if not any(char.isalpha() for char in password):
            return "Password should contain at least one letter.", False
        return None, True

    @staticmethod
    def validate_email(email):
        if not email:
            return "Email is required.", False
        if "@" not in email or "." not in email:
            return "Invalid email format.", False
        return None, True

    @staticmethod
    def validate(data):
        errors = {}

        for key, value in AddUserSchema.properties.items():
            if key == "username":
                error, valid = AddUserSchema.validate_username(value)
            elif key == "first_name":
                error, valid = AddUserSchema.validate_first_name(value)
            elif key == "second_name":
                error, valid = AddUserSchema.validate_second_name(value)
            elif key == "password":
                error, valid = AddUserSchema.validate_password(value)
            elif key == "email":
                error, valid = AddUserSchema.validate_email(value)

            if not valid:
                errors[key] = error

        if errors:
            return errors
        return None
