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

import os

from astropy import units as u
from astropy.io import fits
from astropy.coordinates import SkyCoord
from PIL import Image, ImageDraw
from markupsafe import Markup, escape

"""
Takes binary data as a FITS file and returns the decoded data sorted by right ascention

Params: filename:str    FITS filename (default data/FIRST_data.fit)
        index:int       HDUList index that contains the binary table (default 1)
Return: data:list       List of data from the binary table sorted by RA
"""
def read_first_data(filename="data/FIRST_data.fit", index=1):
    hdu_list = fits.open(filename)
    binary_table = hdu_list[index]
    data = binary_table.data
    return sorted(data, key=lambda data: data[1])


"""
Calculates the distance between a FITS item and a target SkyCoord

Params: item:list       First item to calculate distance to
        target:SkyCoord Target SkyCoord to calculate distance from

Return: :float          The distance between the item and the target (in degrees)
"""
def calculate_distance(item, target):
    item_coord = SkyCoord(ra=item[1] * u.degree, dec=item[2] * u.degree)
    return item_coord.separation(target).degree


"""
Gets all items near the user specified point

Params: data:list:tuple     FITS data that contains the items
        user_input:dict     HTTP POST form data that contains RA, Dec, and (optionally) radius
        default:float       Default radius (=0.25)

Return: results:list        List of items near the user specified point
"""
def get_items_by_radius(data, user_input, default=0.25):
    if not any(user_input.values()):
        return None

    ra = float(user_input['ra']) * u.degree
    dec = float(user_input['dec']) * u.degree
    radius = float(user_input['radius']) if user_input.get('radius').isnumeric() else default
    
    target_coord = SkyCoord(ra=ra, dec=dec)
    # result = next(item for item in enumerate(data) if calculate_distance(item[1], target_coord) < radius)
    
    results = []
    for item in data:
        if calculate_distance(item, target_coord) < radius:
            results.append(item)

    return results


"""
Takes a list of FITS records and formatts them into HTML paragraphs

Params: results:list            List of FITS records
Return: formatted_results:list  Formatted list of FITS records as safely escaped strings
"""
def format_results(results):
    formatted_results = []
    for item in results:
        name, ra, dec, flux, spss = item
        spss = {'s': 'Star', 'g': 'Galaxy', '': 'No Classification'}.get(spss)
        item = """<b>{0}:</b> <em>{1}</em><br>{2} mJy ({3} deg, {4} deg)<br><br>
        """.format(escape(name), escape(spss), escape(flux), escape(ra), escape(dec))
        formatted_results.append(Markup(item))
    
    return formatted_results

"""
Generate image file from a FITS data entry

Params: data:list           List of FITS data records
        scale:int           Scale to multiply the image size by (=5)
        png_filename:str    Filename for PNG image output (will be rendered in HTML)
Return: output_file:str     Resulting PNG filename
"""
def generate_image(data, scale=5, output_file="results.png"):
    colours = {'s': (255,223,51,255), 'g': (169,51,255,255), '': (51,255,153,255)}
    image = Image.new('RGBA', (360 * scale, 180 * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    image_data = [(int(item[1]) * scale, (int(item[2]) + 90) * scale, item[4]) for item in data]
    for item in image_data:
        coords = (item[0]-scale, item[1]-scale, item[0]+scale, item[1]+scale)
        draw.ellipse(coords, fill=colours.get(item[2]), outline=(0,0,0,0))
    
    for filename in os.listdir('static/'):
        if filename.endswith(".png"):
            os.remove("static/" + filename)

    image.save('static/' + output_file, 'png', quality=95)
    return output_file