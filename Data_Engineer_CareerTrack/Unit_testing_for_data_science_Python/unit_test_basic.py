# Import the pytest package
import pytest

# Import the function convert_to_int()
from preprocessing_helpers import convert_to_int

# Complete the unit test name by adding a prefix
def test_on_string_with_one_comma():
  # Complete the assert statement
  assert convert_to_int("2,081") == 2081

# =====================================================

# What is the correct IPython console command to run the tests in this test module?
!pytest test_convert_to_int.py

# =====================================================

def convert_to_int(string_with_comma):
    # Fix this line so that it returns an int, not a str
    return int(string_with_comma.replace(",", ""))

# =====================================================

# Benefits of unit testing

# Time savings, leading to faster development of new features.
# Improved documentation, which will help new colleagues understand the code base better.
# More user trust in the software product.
# Better user experience due to reduced downtime.

# =====================================================

# Unit tests as documentation

In [1]:
!cat test_mystery_function.py

import numpy as np
import pytest

from mystery_function import mystery_function

def test_on_clean_data():
    assert np.array_equal(mystery_function("example_clean_data.txt", num_columns=2), np.array([[2081.0, 314942.0], [1059.0, 186606.0]]))

# It converts data in a data file into a NumPy array.

