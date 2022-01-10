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
import csv


"""
Takes headers as a CSV file and returns the headers as a list

Params: filename:str    header filename (default data/FIRST_data_columns.txt)
Return: headers:list    headers
"""
def read_headers(filename="data/FIRST_data_columns.txt"):
    with open(filename) as f:
        reader = csv.reader(f)
        headers = list(reader)

    formatted_headers = []
    for item in headers[1:]:
        name, formt, units, explanation = item
        formatted_headers.append(f"{name} ({formt.strip()};{units}): {explanation}")

    return '\n'.join(formatted_headers) + '\n'


"""
Takes binary data as a FITS file and returns the decoded data

Params: filename:str    FITS filename (default data/FIRST_data.fit)
        index:int       HDUList index that contains the binary table (default 1)
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

headers = read_headers()
data = read_first_data()