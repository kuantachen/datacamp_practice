
import pytest
from preprocessing_helpers import convert_to_int

def test_on_string_with_one_comma():
    test_argument = "2,081"
    expected = 2081
    actual = convert_to_int(test_argument)
    # Format the string with the actual return value
    message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(actual)
    # Write the assert statement which prints message on failure
    assert actual is expected, message

# =====================================================

import numpy as np
import pytest
from as_numpy import get_data_as_numpy_array

def test_on_clean_file():
  expected = np.array([[2081.0, 314942.0],
                       [1059.0, 186606.0],
  					   [1148.0, 206186.0]
                       ]
                      )
  actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
  message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
  # Complete the assert statement
  assert actual == pytest.approx(expected), message

# =====================================================

def test_on_six_rows():
    example_argument = np.array([[2081.0, 314942.0], [1059.0, 186606.0],
                                 [1148.0, 206186.0], [1506.0, 248419.0],
                                 [1210.0, 214114.0], [1697.0, 277794.0]]
                                )
    # Fill in with training array's expected number of rows
    expected_training_array_num_rows = int(0.75 * 6)    #4
    # Fill in with testing array's expected number of rows
    expected_testing_array_num_rows = 6 - int(0.75 * 6) #2
    actual = split_into_training_and_testing_sets(example_argument)
    # Write the assert statement checking training array's number of rows
    assert actual[0].shape[0] == expected_training_array_num_rows, "The actual number of rows in the training array is not {}".format(expected_training_array_num_rows)
    # Write the assert statement checking testing array's number of rows
    assert actual[1].shape[1] == expected_testing_array_num_rows, "The actual number of rows in the testing array is not {}".format(expected_testing_array_num_rows)

    # Check the definition of test_on_six_rows(). 
    # Did you correctly specify the body? Did you check the number of rows of your training array? 
    # Remember that actual is a tuple of the form (training_array, testing_array). 
    # Therefore, actual[0] is the training array. 
    # The shape attribute of the training array returns a tuple containing the number of rows and columns. 
    # Therefore, actual[0].shape[0] gives the number of rows.
    
# =====================================================

# =====================================================

# =====================================================

# =====================================================

# =====================================================

# =====================================================

# =====================================================

# =====================================================

# =====================================================

# =====================================================

# =====================================================

# =====================================================

# =====================================================

# =====================================================