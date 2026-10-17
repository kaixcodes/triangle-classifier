import pytest
from triangle import is_valid_triangle, classify_triangle


def test_valid_triangle():
    assert is_valid_triangle(3, 4, 5)


def test_rejects_nonpositive_side():
    assert not is_valid_triangle(0, 2, 2)


def test_rejects_triangle_inequality_violation():
    assert not is_valid_triangle(1, 2, 3)


def test_classifies_invalid_triangle():
    assert classify_triangle(0, 2, 2) == "Invalid"
    assert classify_triangle(1, 2, 3) == "Invalid"


def test_classifies_equilateral_triangle():
    assert classify_triangle(4, 4, 4) == "Equilateral"


def test_classifies_isosceles_triangle():
    assert classify_triangle(5, 5, 6) == "Isosceles"
    assert classify_triangle(5, 6, 5) == "Isosceles"
    assert classify_triangle(6, 5, 5) == "Isosceles"


def test_classifies_right_isosceles_triangle():
    assert classify_triangle(1, 1, 2**0.5) == "Right Isosceles"
    assert classify_triangle(1, 2**0.5, 1) == "Right Isosceles"
    assert classify_triangle(2**0.5, 1, 1) == "Right Isosceles"


def test_classifies_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_classifies_right_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(4, 3, 5) == "Right Scalene"
    assert classify_triangle(5, 3, 4) == "Right Scalene"
