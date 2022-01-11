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

from http.client import METHOD_NOT_ALLOWED
from flask import Flask, render_template, request, abort
from backend import *

app = Flask(__name__)

"""
Main page for the website

On initial load: GET request that will serve a form page
On form submission: POST request that will reserve the form page with FIRST data to display

Params: None
Return: render_template
"""
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        # Load data and get the target point specified by the user from the HTML form
        data = read_first_data()
        user_input = request.form.to_dict()

        # Send a list of items near the target point to the webpage
        items = get_items_by_radius(data, user_input)
        image = generate_image(items)
        return render_template("index.html", items=items)
    else:
        abort(405)


if __name__ == "__main__":
    app.run(debug=True)