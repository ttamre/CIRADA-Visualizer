#!/usr/bin/env python3

"""
CIRADA Interview Project
Copyright (C) 2021 Tem Tamre

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


from flask import Flask, render_template, request
from backend import read_first_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = read_first_data()
    user_input = request.form.to_dict()
    # items = get_items(data, user_input)
    return render_template("index.html", items=user_input)


app.run(debug=True)