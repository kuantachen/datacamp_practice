
from re import X
import pytest
import numpy as np

from models.train import split_into_training_and_testing_sets

# Declare the test class
class TestSplitIntoTrainingAndTestingSets(object):
    # Fill in with the correct mandatory argument
    def test_on_one_row(self):
        test_argument = np.array([[1382.0, 390167.0]])
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
        expected_error_msg = "Argument data_array must have at least 2 rows, it actually has just 1"
        assert exc_info.match(expected_error_msg)

# =====================================================

# In the IPython console, what is the correct command for running all tests contained in the tests folder?
# !pytest

# Assuming that you simply want to answer the binary question "Are all tests passing" without wasting time and resources, what is the correct command to run all tests till the first failure is encountered?
# !pytest -x

# =====================================================

import numpy as np

def split_into_training_and_testing_sets(data_array):
    dim = data_array.ndim
    if dim != 2:
        raise ValueError("Argument data_array must be two dimensional. Got {0} dimensional array instead!".format(dim))
    num_rows = data_array.shape[0]
    if num_rows < 2:
        raise ValueError("Argument data_array must have at least 2 rows, it actually has just {0}".format(num_rows))
    # Fill in with the correct float
    num_training = int(0.75 * data_array.shape[0])
    permuted_indices = np.random.permutation(data_array.shape[0])
    return data_array[permuted_indices[:num_training], :], data_array[permuted_indices[num_training:], :]

# Now let's see if that modification fixed the broken function. 
# The current working directory in the IPython console is the tests folder that contains all tests. 
# The test class TestSplitIntoTrainingAndTestingSets resides in the test module tests/models/test_train.py.
# What is the correct command to run all the tests in this test class using node IDs?
!pytest models/test_train.py::TestSplitIntoTrainingAndTestingSets

# What is the correct command to run only the previously failing test test_on_six_rows() using node IDs?
!pytest models/test_train.py::TestSplitIntoTrainingAndTestingSets::test_on_six_rows

# What is the correct command to run the tests in TestSplitIntoTrainingAndTestingSets using keyword expressions?
!pytest -k "SplitInto"

# =====================================================

# Mark the whole test class as "expected to fail"
# @pytest.mark.xfail
# Add a reason for the expected failure
@pytest.mark.xfail(reason="Using TDD, model_test() has not yet been implemented")
class TestModelTest(object):
    def test_on_linear_data(self):
        test_input = np.array([[1.0, 3.0], [2.0, 5.0], [3.0, 7.0]])
        expected = 1.0
        actual = model_test(test_input, 2.0, 1.0)
        message = "model_test({0}) should return {1}, but it actually returned {2}".format(test_input, expected, actual)
        assert actual == pytest.approx(expected), message
        
    def test_on_one_dimensional_array(self):
        test_input = np.array([1.0, 2.0, 3.0, 4.0])
        with pytest.raises(ValueError) as exc_info:
            model_test(test_input, 1.0, 1.0)

# =====================================================

# Import the sys module
import sys

class TestGetDataAsNumpyArray(object):
    # Mark as skipped if Python version is greater than 2.7
    # Add a reason for skipping the test
    @pytest.mark.skipif(sys.version_info > (2, 7), reason="Works only on Python 2.7 or lower")
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                             ]
                            )
        actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
        assert actual == pytest.approx(expected), message

# What is the command that would only show the reason for expected failures in the test result report?
!pytest -rx
# What is the command that would only show the reason for skipped tests in the test result report?
!pytest -rs
# What is the command that would show the reason for both skipped tests and tests that are expected to fail in the test result report?
!pytest -rsx

# =====================================================
# Continuous Integration Server = CI Server

# Travis CI
# Codecov

