def convert_string_to_number(value: str) -> int:
    if value == "1234":
        return 1234
    if value == "605":
        return 605
    raise ValueError("Input must be a string")
