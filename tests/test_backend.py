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
    test_data = read_first_data(test_file)

    assert any(test_data)
    assert type(test_data) is FITS_rec


"""
Tests get_items_by_radius()'s ability to find nearby items
Condition: test_result is not null, nearby item is returned
"""
def test_get_items_by_radius():
    test_item_1 = ('test_item_1', 338, 11, 1.12, '')
    test_item_2 = ('test_item_2', 330, 10, 5.73, '')
    test_item_3 = ('test_item_3', 300, 15, 24.0, '')
        
    test_data = [test_item_1, test_item_2, test_item_3]
    test_input = {'ra': '338.12', 'dec': '11.53'}
    test_result = get_items_by_radius(test_data, test_input)

    assert any(test_result)
    assert test_item_1 in test_result

"""
Tests get_items_by_radius()'s ability to find nearby items with user-specified radius
Condition: test_result is not null, nearby item is returned
"""
def test_get_items_by_radius():
    test_item_1 = ('test_item_1', 338, 11, 1.12, '')
    test_item_2 = ('test_item_2', 330, 10, 5.73, '')
    test_item_3 = ('test_item_3', 300, 15, 24.0, '')
        
    test_data = [test_item_1, test_item_2, test_item_3]
    test_input = {'ra': '338.12', 'dec': '11.53', 'radius': '10'}
    test_result = get_items_by_radius(test_data, test_input)

    assert any(test_result)
    assert test_item_1 in test_result
    assert test_item_2 in test_result
