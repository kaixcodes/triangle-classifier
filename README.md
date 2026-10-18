# triangle-classifier

A triangle classifier that contains two functions in triangle.py, is_valid_triangle and classify_triangle.

|           Function           |                         Description                         |               Parameters               | Return Type |
| :--------------------------: | :---------------------------------------------------------: | :------------------------------------: | :---------: |
| `is_valid_triangle(a, b, c)` | Checks if a triangle is valid based on 3 given side lengths | `a: float`<br>`b: float`<br>`c: float` |   `bool`    |
| `classify_triangle(a, b, c)` |   Returns type of triangle based on 3 given side lengths    | `a: float`<br>`b: float`<br>`c: float` |    `str`    |

**_Note:_** _An equilateral triangle can never be a right triangle becuase all three of its angles must always measure 60°, whereas a right triangle requires one angle to measure 90°._

## How to Run Tests

- Ensure pytest is properly installed on your machine
- In terminal, navigate to project directory
- For full test suite run `pytest`
- For a specific test run `pytest test_traingle.py` or `pytest test_acceptance.py`

## Equivalence Classes & Boundaries

Assume `a`, `b`, and `c` are finite real-valued side-length inputs; nonpositive
values are included as invalid cases. The input order does not affect the result,
so each class represents all permutations of its example.

### Equivalence classes

| Class                                                         | Representative input      | Expected result   |
| :------------------------------------------------------------ | :------------------------ | :---------------- |
| At least one side is zero or negative                         | `(0, 2, 2)`; `(-1, 2, 2)` | `Invalid`         |
| Triangle inequality is violated                               | `(1, 2, 4)`               | `Invalid`         |
| Degenerate triangle: one side equals the sum of the other two | `(1, 2, 3)`               | `Invalid`         |
| All three sides are equal                                     | `(4, 4, 4)`               | `Equilateral`     |
| Exactly two sides are equal; not right                        | `(5, 5, 6)`               | `Isosceles`       |
| Exactly two sides are equal; right                            | `(1, 1, sqrt(2))`         | `Right Isosceles` |
| All sides differ; not right                                   | `(4, 5, 6)`               | `Scalene`         |
| All sides differ; right                                       | `(3, 4, 5)`               | `Right Scalene`   |

### Boundary values

| Boundary                                     | Just below / at boundary                  | Just above / inside boundary                                                           | Expected behavior                                                                                                                                                                                 |
| :------------------------------------------- | :---------------------------------------- | :------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Side length must be positive                 | `a = 0`                                   | `a > 0` (for example, `a = 0.1`)                                                       | Zero is `Invalid`; a positive side may be valid if the other conditions hold.                                                                                                                     |
| Triangle inequality for the longest side `c` | `a + b = c`                               | `a + b > c`                                                                            | Equality is `Invalid`; greater-than is required for a valid triangle.                                                                                                                             |
| Equality of all sides                        | `(4, 4, 4)`                               | `(4, 4, 3.9)`                                                                          | All equal is `Equilateral`; changing one side makes it non-equilateral (and this example is `Isosceles`).                                                                                         |
| Equality of exactly two sides                | `(5, 5, 6)`                               | `(5, 5.1, 6)`                                                                          | Equal sides give `Isosceles`; with all sides different, this example is `Scalene`.                                                                                                                |
| Right-triangle condition                     | `a² + b² = c²` (for example, `(3, 4, 5)`) | A nearby valid triple that does not satisfy the condition (for example, `(3, 4, 5.1)`) | The equality is right; the nearby example is not. The implementation uses `math.isclose` when comparing squared lengths, so floating-point values near the equality may also be treated as right. |

## Copilot Review Log

|                     Test                     | Copilot-suggested? | Kept / edited / rejected |                                      Why                                      |
| :------------------------------------------: | :----------------: | :----------------------: | :---------------------------------------------------------------------------: |
|            `test_valid_triangle`             |        yes         |           Kept           |                 Parameters satisfy valid triangle qualifiers                  |
|       `test_rejects_nonpositive_side`        |        yes         |           Kept           |                        Properly tests zero length side                        |
| `test_rejects_triangle_inequality_violation` |        yes         |           Kept           |                         Properly tests degenrate case                         |
|      `test_classifies_invalid_triangle`      |        yes         |          Edited          |                   Added assertion for zero side length case                   |
|    `test_classifies_equilateral_triangle`    |        yes         |           Kept           |                     Properly tests if all sides are equal                     |
|     `test_classifies_isosceles_triangle`     |        yes         |          Edited          |          Added two additional assertions to test if b == c or a == c          |
|  `test_classifies_right_isosceles_triangle`  |        yes         |          Edited          | Added two additional assertions to test if a is hypotenuse or b is hypotenuse |
|      `test_classifies_scalene_triangle`      |        yes         |           Kept           |               Properly tests if all sides are different lengths               |
|   `test_classifies_right_scalene_triangle`   |        yes         |          Edited          | Added two additional assertions to test if a is hypotenuse or b is hypotenuse |

## Acceptance Criteria

- Given I am a customer, when I enter three side lengths, then I will be told the shape and whether it's buildable.
- Given I am a customer, when my shape is not a valid triangle, I will be shown a message instead of the program crashing.
- Given I am a stained-glass maker, when a customer wants a right-angle piece, then I will see it flagged as one so I can add reinforced corners.

## AI-use Disclosure

_Github Copilot:_ Used to draft pytest test suite, I edited multiple test functions to better meet the requirement specifications. Also used to write equivalence classes & boundaries to README.md, then reviewed for accuracy.
