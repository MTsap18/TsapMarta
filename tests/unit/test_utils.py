
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
from utils.helpers import format_string, add_numbers

def test_format_string():
    assert format_string("hello") == "Hello"
    assert format_string("world") == "World"

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

