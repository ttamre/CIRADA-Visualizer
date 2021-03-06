#!/usr/bin/env python3

"""
CIRADA Interview Project
Copyright (C) 2022 Tem Tamre

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

import logging
from backend import *

from flask import Flask, render_template, request, abort
from waitress import serve

app = Flask(__name__)
logging.basicConfig(level=logging.CRITICAL)


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
        logging.info("Reading FITS data...")
        data = read_first_data()
        logging.info(f"Loaded {len(data)} items")

        # Get the user's input from the HTML form
        logging.info("Reading user input...")
        user_input = request.form.to_dict()

        # Send a list of items near the target point to the webpage
        logging.info("Getting items...")
        items = get_items_by_radius(data, user_input)
        formatted_items = format_results(items)
        logging.info(f"Found {str(len(items))} items")

        # Attempt to generate a PNG file from the results
        try:
            logging.info("Generating image...")
            image = generate_image(items)
            logging.info("Generated image!")
        except:
            logging.critical("Couldn't generate image")
            image = None

        return render_template("index.html", items=formatted_items, image=image)
    else:
        abort(405)


if __name__ == "__main__":
    print("""
    CIRADA Interview Project Copyright (C) 2022 Tem Tamre

    This program comes with ABSOLUTELY NO WARRANTY; This is free software,
    and you are welcome to redistribute it under certain conditions;
    Visit https://www.gnu.org/licenses/gpl-3.0.en.html for details.
    """)
    
    serve(app)