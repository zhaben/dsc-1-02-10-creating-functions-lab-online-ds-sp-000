# importing testing framwork
import pytest
# library used to check working virtual environment
import importlib

# importing objects from the jupyter notebook here
import ipynb.fs.full.index
from ipynb.fs.full.index import * # variable names go here

# tests to ensure correct environment is loaded
def test_conda_environment_activated():
    assert importlib.util.find_spec("obscure"), "It looks like you didn't 'conda activate learn-env' - try that then run the test again!"

def test_number_of_destinations_func():
    assert 'number_of_destinations' in ipynb.fs.full.index.__dict__, "The function number_of_destinations is not yet defined"
    travel_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
    assert number_of_destinations() == len(travel_destinations), "The number_of_destinations function should return the length of the travel_destinations list"

def test_next_up_func():
    assert 'next_up' in ipynb.fs.full.index.__dict__, "The function next_up is not yet defined"
    travel_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
    assert next_up() == 'argentina', "The next_up function should return the next string in the list of travel_destinations"

def test_favorite_destination_func():
    assert 'favorite_destination' in ipynb.fs.full.index.__dict__, "The function favorite_destination is not yet defined"
    assert favorite_destination() == 'madagascar', "The favorite_destination function should return the string madagascar"

def test_add_favorite_destination_func():
    assert 'add_favorite_destination' in ipynb.fs.full.index.__dict__, "The function add_favorite_destination is not yet defined"
    travel_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
    assert add_favorite_destination() == 'madagascar', "The add_favorite_destination function should return the string madagascar"
    assert travel_destinations == ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia', 'madagascar'], "the add_favorite_destination function should mutate the list travel_destinations and add the string madagascar to the end of the list"

def test_capitalize_countries_func():
    assert 'capitalize_countries' in ipynb.fs.full.index.__dict__, "The function capitalize_countries is not yet defined"
    travel_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
    assert sorted(capitalize_countries()) == sorted(['Argentina', 'Mexico', 'Italy', 'Finland', 'Canada', 'Croatia']), "The capitalize_countries function should return a list with the same countries as strings, but each string should be capitalized"
