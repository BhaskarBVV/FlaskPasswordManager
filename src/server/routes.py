"""Routes for the application"""

from controllers.Password import Password
from controllers.User import User

ROUTES = [[Password, "/password"], [User, "/user"]]
