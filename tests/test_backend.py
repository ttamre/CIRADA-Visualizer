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

from backend import *
from astropy.io.fits.fitsrec import FITS_rec


"""
Tests read_first_data()'s ability to properly process FIRST data files
Condition: data is not null, data is the right type
"""
def test_read_first_data():
    test_file = "data/FIRST_data.fit"
    data = read_first_data(test_file)

    assert data is not None
    assert type(data) is FITS_rec


"""
TODO Tests get_items_by_radius()
"""
def get_items_by_radius():
    assert True