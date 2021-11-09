"""
Libretify
Copyright (C) 2021 Mikhail "netvork109" Serebryakov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from flask_login import LoginManager
from src.models import AdminUser

# Creating the Login manager
login = LoginManager()

# user_loader needs for admin panel user authentication
@login.user_loader
def user_loader(user_id):
    # Getting a user from the database using model
    return AdminUser.query.get(user_id)