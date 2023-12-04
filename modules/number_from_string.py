def convert_string_to_number(value: str) -> int:
    print(type(value))
    if not isinstance(value, str):
        raise ValueError("Input must be a string")
    return int(value)
