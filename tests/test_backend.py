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

from markupsafe import Markup
from backend import *

"""
Tests read_first_data()'s ability to properly process FIRST data files
Condition: data is not null, data is the right type, data is sorted
"""
def test_read_first_data():
    test_file = "data/FIRST_data.fit"
    test_data = read_first_data(test_file)

    assert any(test_data)
    assert isinstance(test_data, list)

    # Checks various item pairs throughout the list to ensure sorting
    length = len(test_data)
    indexes = [0, 10, 100, length//10, length//5, length//3, length//2, length-2]
    assert all(test_data[i][1] < test_data[i+1][1] for i in indexes)


"""
Tests distance calculation between a FITS record and a target SkyCoord
Condition: distance is a float, calculation is valid
"""
def test_calculate_distance():
    test_threshold = 0.25
    test_item_1 = ('test_item_1', 338.10, 11.5, 1.12, 's')
    test_target = SkyCoord(ra=338.12 * u.degree, dec=11.53 * u.degree)
    distance = calculate_distance(test_item_1, test_target)

    assert isinstance(distance, float)
    assert distance < test_threshold


"""
Tests get_items_by_radius()'s ability to find nearby items
Condition: test_result is not empty, nearby item is returned
"""
def test_get_items_by_default_radius():
    test_item_1 = ('test_item_1', 338.10, 11.4, 1.12, '')
    test_item_2 = ('test_item_2', 338.07, 12.0, 5.73, '')
    test_item_3 = ('test_item_3', 300.10, 13.5, 24.0, '')
        
    test_data = [test_item_1, test_item_2, test_item_3]
    test_input = {'ra': '338.12', 'dec': '11.53', 'radius': ''}
    test_result = get_items_by_radius(test_data, test_input)

    assert any(test_result)
    assert test_item_1 in test_result


"""
Tests get_items_by_radius()'s ability to find nearby items with user-specified radius
Condition: test_result is not empty, nearby item is returned
"""
def test_get_items_by_custom_radius():
    test_item_1 = ('test_item_1', 338.10, 11.4, 1.12, '')
    test_item_2 = ('test_item_2', 338.07, 12.0, 5.73, '')
    test_item_3 = ('test_item_3', 300.10, 13.5, 24.0, '')
        
    test_data = [test_item_1, test_item_2, test_item_3]
    test_input = {'ra': '338.12', 'dec': '11.53', 'radius': '10'}
    test_result = get_items_by_radius(test_data, test_input)

    assert any(test_result)
    assert test_item_1 in test_result
    assert test_item_2 in test_result


"""
Tests formatted results
Condition: test_formatted_results is not empty, each result is a Markup object
"""
def test_format_results():
    test_item_1 = ('test_item_1', 338.10, 11.4, 1.12, '')
    test_item_2 = ('test_item_2', 338.07, 12.0, 5.73, '')
    test_item_3 = ('test_item_3', 300.10, 13.5, 24.0, '')
    test_results = [test_item_1, test_item_2, test_item_3]
    test_formatted_results = format_results(test_results)

    assert any(test_formatted_results)
    assert all(isinstance(item, Markup) for item in test_formatted_results)


"""
Tests image generation
Condition: test_output_file exists as a valid png file
"""
def test_generate_image():
    test_item_1 = ('test_item_1', 338.10, 11.4, 1.12, '')
    test_item_2 = ('test_item_2', 338.07, 12.0, 5.73, '')
    test_item_3 = ('test_item_3', 300.10, 13.5, 24.0, '')
    test_results = [test_item_1, test_item_2, test_item_3]

    test_output_file = "test_results.png"
    test_output_file = generate_image(test_results, output_file=test_output_file)

    assert os.path.exists('static/' + test_output_file)
    assert test_output_file.endswith('.png')
