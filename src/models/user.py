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

from src.database import db
from datetime import datetime

# This is model of user
class Model(db.Model):
    # Common data
    id = db.Column(db.Integer, primary_key=True)
    
    nickname = db.Column(db.String(255))
    password = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.now())
    modified_at = db.Column(db.DateTime, default=datetime.now())

    # Settings
    always_proxy = db.Column(db.Boolean, default=True)
    autoplay = db.Column(db.Boolean, default=True)

    language = db.Column(db.String(8), default='en-US')
    country = db.Column(db.String(8), default='US')
