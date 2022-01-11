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

from astropy import units as u
from astropy.io import fits
from astropy.coordinates import SkyCoord
from astropy.table import Table
from astropy.utils.data import get_pkg_data_filename

import matplotlib.pyplot as plt

"""
Takes binary data as a FITS file and returns the decoded data

Params: filename:str    FITS filename (default data/FIRST_data.fit)
        index:int       HDUList index that contains the binary table (default 1)
Return: data
"""
def read_first_data(filename="data/FIRST_data.fit", index=1):
    hdu_list = fits.open(filename)
    binary_table = hdu_list[index]

    return binary_table.data


"""
*DO NOT USE - BETTER WAY IS TO CONVERT ALL COORDINATE USER INPUT TO DECIMAL DEGREES*

Takes a list of data (formatted with RA = data[n, 1] and Dec = data[n, 2])
and makes a new identical list with an added SkyCoord object appended to each item
that represents it's coordinates. This allows for easy unit conversion using the
astropy methods in the SkyCoord object.

Params: raw_data:list:tuple         FITS data to add SkyCoord objects to
Return: processed_data:list:tuple   Data with SkyCoord objects appended to every line 
"""
def process_coordinates(raw_data):
    processed_data = []
    for item in raw_data:
        # Headers: Name, RA, Dec, Integrated flux density, SDSS classification
        ra = item[1] * u.degree
        dec = item[2] * u.degree

        # Appends SkyCoord to end of tuple
        item = (*item, SkyCoord(ra=ra, dec=dec))
        processed_data.append(item)

    return processed_data


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

    # Sort by RA: https://stackoverflow.com/a/3121985
    # data = sorted(data, key = lambda item: float(item[1]))
    # print("-------- DATA", data[0])
    # print("-------- DATA", data[1])
    # print("-------- DATA", data[2])

    ra = float(user_input['ra']) * u.degree
    dec = float(user_input['dec']) * u.degree
    radius = float(user_input['radius']) if user_input['radius'] else default
    
    target_coord = SkyCoord(ra=ra, dec=dec)
    result = next(item for item in enumerate(data) if calculate_distance(item[1], target_coord) < radius)

    print("RESULTS\n", list(result))
    return list(result)


"""
"""
def generate_image(data):
    hdu = fits.PrimaryHDU(data)
    hdu.writeto("data/result.fits")

    image_file = get_pkg_data_filename("data/result.fits")
    image_data = fits.getdata(image_file, ext=0)
    
    plt.figure()
    plt.imsave("result.png", image_data)