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

import pytest
from app import *


"""
Test GET request on index with no form data
Condition: HTTP 200 response, static page data in response
"""
def test_index_blank():
    with app.test_client() as client:
        response = client.get("/")

        assert response.status_code == 200
        assert b"CIRADA Visualizer" in response.data
        assert b"CIRADA FIRST Data Visualizer" in response.data


"""
Test POST request on index with coordinate form data
Condition: HTTP 200 response, image in response
"""
@pytest.mark.skip
def test_index_coords_default_radius():
    with app.test_client() as client:
        test_input = {'ra': '338.12', 'dec': '11.53', 'radius': ''}
        response = client.post("/", data=test_input)

        assert response.status_code == 200
        # TODO assert test_image in response.data
        # assert b"img" in response.data?


"""
Test POST request on index with coordinate and radius form data
Condition: HTTP 200 response, image in response
"""
@pytest.mark.skip
def test_index_coords_custom_radius():
    with app.test_client() as client:
        test_input = {'ra': '338.12', 'dec': '11.53', 'radius': '1'}
        response = client.post("/", data=test_input)

        assert response.status_code == 200
        # TODO assert test_image in response.data
        # assert b"img" in response.data?
        