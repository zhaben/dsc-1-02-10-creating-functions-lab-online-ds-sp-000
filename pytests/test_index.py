# importing testing framwork
import pytest
# library used to check working virtual environment
import importlib

# importing objects from the jupyter notebook here
from ipynb.fs.full.index import # variable names go here

# tests to ensure correct environment is loaded
def test_conda_environment_activated():
    assert importlib.util.find_spec("obscure"), "It looks like you didn't 'conda activate learn-env' - try that then run the test again!"

def test_number_of_destinations_func():
    assert number_of_destinations() == len(travel_destinations)

def test_next_up_func():
    assert next_up() == 'argentina'

def test_favorite_destination_func_return():
    assert favorite_destination() == 'madagascar'

def test_capitalize_countries_func():
    assert sorted(capitalize_countries()) == sorted(['Argentina', 'Mexico', 'Italy', 'Finland', 'Canada', 'Croatia', 'Japan'])
