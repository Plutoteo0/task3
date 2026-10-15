import math

def is_valid(s: str):
    return s is not None and s.isdecimal() and s.isascii()

def lcm(x: str | None = None, y: str | None = None):
    if not is_valid(x) or not is_valid(y):
        return "NaN"
    x = int(x)
    y = int(y)
    result = math.lcm(x, y)
    return str(result)