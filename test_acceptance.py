from triangle import classify_triangle


def test_classify_triangle():
    # Acceptance Criteria 1
    assert classify_triangle(5, 5, 5) == "Equilateral"
    # Acceptance Criteria 2
    assert classify_triangle(0, 2, 2) == "Invalid"
    # Acceptance Criteria 3
    assert classify_triangle(1, 1, 2**0.5) == "Right Isosceles"
