import pytest
from modules import number_from_string


def describe_dummy_kata():
    def should_return_error_when_input_is_not_a_string(capsys):
        """🧪 should return an error when the input is not a string"""
        with pytest.raises(ValueError, match="Input must be a string"):
            number_from_string.convert_string_to_number(8908)
