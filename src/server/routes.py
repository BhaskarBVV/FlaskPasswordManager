"""Routes for the application"""

from controllers.password import Password
from controllers.user import User
from controllers.login import Login
from controllers.logout import Logout

ROUTES = [[Password, "/password"],
            [User, "/user"], 
            [Login, "/login"],
            [Logout, "/logout"]]
