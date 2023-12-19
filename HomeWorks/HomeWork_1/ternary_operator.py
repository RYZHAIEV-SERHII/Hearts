# за допомогою тернарного оператора релізувати логіку:
# є параметри x та у,
# якщо x < y - друкуємо x + y,
# якщо x == y - друкуємо 0,
# якщо x > y - друкуємо x - y,
# якщо x == 0 та y == 0 друкуємо "game over"

def ternary_operation(x: int, y: int):
    """
Function to implement following logic with ternary operator:
if x < y: print x + y
if x > y: print x - y
if x == y: print 0
if x == 0 and y == 0: print "game over"

    :param x: int number to compare
    :param y: int number to compare
    """
    try:
        print(
            f"game over" if x == 0 == y else
            f"{x + y}" if x < y else
            f"0" if x == y else
            f"{x - y}"
        )

    # another solution (shorter but not so readable):
    # print("game over" if x == 0 == y else (x + y if x < y else (0 if x == y else x - y))

    except ValueError:
        print("Parameters should be digits!")
        print("Please enter a number")
        ternary_operation(x, y)


if __name__ == "__main__":
    ternary_operation(1, 2)  # result = 3
    ternary_operation(3, 2)  # result = 1
    ternary_operation(3, 3)  # result = 0
    ternary_operation(0, 0)  # result = "game over"
