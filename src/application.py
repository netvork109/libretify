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

from flask import Flask

from src.database import db
from src.admin import admin
from src.login import login
from flask_bootstrap import Bootstrap

import json

class Application:
    def __init__(self) -> None:
        self.app = Flask(__name__)
    
    def setup(self) -> None:
        # Setup a configuration from JSON file
        self.app.config.from_file('../configuration.json', json.load)
        self.app.secret_key = self.app.config.get('SECRET_KEY')

        # Adding a libraries to application
        db.init_app(self.app)
        admin.init_app(self.app)
        login.init_app(self.app)
        self.bootstrap = Bootstrap(self.app)

    def run(self) -> None:
        self.app.run()
    