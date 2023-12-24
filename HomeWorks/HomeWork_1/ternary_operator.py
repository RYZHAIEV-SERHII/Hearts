# за допомогою тернарного оператора релізувати логіку:
# є параметри x та у,
# якщо x < y - друкуємо x + y,
# якщо x == y - друкуємо 0,
# якщо x > y - друкуємо x - y,
# якщо x == 0 та y == 0 друкуємо "game over"


def ternary_operation(x: [int | float], y: [int | float]) -> [int | float | str]:
    """
    Function to implement following logic with ternary operator:
    if x < y: return x + y
    if x > y: return x - y
    if x == y: return 0
    if x == 0 and y == 0: return "game over"

        :param x: int or float number to compare
        :param y: int or float number to compare
    """
    try:
        return (
            "game over" if x == 0 == y else x + y if x < y else 0 if x == y else x - y
        )

        # another solution (shorter but not so readable):
        # return "game over" if x == 0 == y else (x + y if x < y else (0 if x == y else x - y))

    except ValueError:
        print("Parameters should be digits!")
        print("Please enter a number")
        ternary_operation(x, y)


# Tests
import unittest


class TestTernaryOperation(unittest.TestCase):
    def test_x_less_than_y(self):
        result = ternary_operation(1, 2)
        assert result == 3

    def test_x_greater_than_y(self):
        result = ternary_operation(3, 2)
        assert result == 1

    def test_x_equals_y(self):
        result = ternary_operation(3, 3)
        assert result == 0

    def test_x_and_y_zero(self):
        result = ternary_operation(0, 0)
        assert result == "game over"


if __name__ == "__main__":
    unittest.main(verbosity=2)
