import pytest
from modules import number_from_string


def describe_dummy_kata():
    def should_return_error_when_input_is_not_a_string():
        """🧪 should return an error when the input is not a string"""
        with pytest.raises(ValueError, match="Input must be a string"):
            number_from_string.convert_string_to_number(8908)

    def should_return_1234():
        """🧪 should print the number 1234 for '1234'"""
        assert number_from_string.convert_string_to_number("1234") == 1234

    def should_return_605():
        """🧪 should print the number 605 for '605'"""
        assert number_from_string.convert_string_to_number("605") == 605

    def should_return_1405():
        """🧪 should print the number 1405 for '1405'"""
        assert number_from_string.convert_string_to_number("1405") == 1405

    def should_return_negative_7():
        """🧪 should print the number -7 for '-7'"""
        assert number_from_string.convert_string_to_number("-7") == -7

    def should_error_if_not_number_in_string():
        """🧪 should throw an error in the string doesn't contain a number"""
        with pytest.raises(ValueError, match="Input string must contain a number"):
            number_from_string.convert_string_to_number("blah")
