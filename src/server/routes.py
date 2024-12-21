"""Routes for the application"""

from controllers.password import Password
from controllers.user import User
from controllers.login import Login
from controllers.logout import Logout
from controllers.health import Health
from controllers.update_user_password import UpdatePassword

ROUTES = [[Password, "/passwords"],
            [User, "/users"], 
            [Login, "/auth/login"],
            [Logout, "/auth/logout"],
            [Health, "/health"],
            [UpdatePassword, "/update-password"]]
