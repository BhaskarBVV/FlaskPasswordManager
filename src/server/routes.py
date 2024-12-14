"""Routes for the application"""

from controllers.password import Password
from controllers.user import User
from controllers.login import Login

ROUTES = [[Password, "/password"],
            [User, "/user"], 
            [Login, "/login"]]
