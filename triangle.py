import math


def is_valid_triangle(a, b, c) -> bool:
    # if any side is less than or equal to zero, it's not a valid triangle
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # if the sum of any two sides is less than or equal to the third side, it's not a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    return True


def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        if math.isclose(math.pow(a, 2) + math.pow(b, 2), math.pow(c, 2)):
            return "Right Isosceles"
        return "Isosceles"

    if math.isclose(math.pow(a, 2) + math.pow(b, 2), math.pow(c, 2)):
        return "Right Scalene"
    return "Scalene"
