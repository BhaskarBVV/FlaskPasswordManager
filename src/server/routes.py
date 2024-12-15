"""Routes for the application"""

from controllers.password import Password
from controllers.user import User
from controllers.login import Login
from controllers.logout import Logout
from controllers.health import Health

ROUTES = [[Password, "/password"],
            [User, "/user"], 
            [Login, "/login"],
            [Logout, "/logout"],
            [Health, "/health"]]
