import re


def validate_has_numbers(value: str) -> ValueError:
    if not bool(re.search(r"\d", value)):
        raise ValueError("Input string must contain a number")


def convert_string_to_number(value: str) -> int:
    if not isinstance(value, str):
        raise ValueError("Input must be a string")
    validate_has_numbers(value)
    return int(value)
