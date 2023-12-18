# написати функцію якам приймає рядок і повертає словник у якому
# ключами є всі символи, які зустрічаються в цьому рядку, а значення - відповідні
# вірогідності зустріти цей символ в цьому рядку.
# № код повинен бути структурований за допомогою конструкції if name == "__main__":,
# всі аргументи і значення що функція повертає повинні бути типізовані, функція має рядок документації


# за допомогою тернарного оператора релізувати логіку:
# є параметри x та у,
# якщо x < y - друкуємо x + y,
# якщо x == y - друкуємо 0,
# якщо x > y - друкуємо x - y,
# якщо x == 0 та y == 0 друкуємо "game over"


def string_to_symbols_dict(text: str) -> dict:
    """
Function to convert text to dictionary in which keys are symbols and values are chances to meet symbol
in the given text.
    :param text: text to convert into dictionary.
    :return:  dictionary containing symbols and their frequencies in the given text.
    """
    letters = tuple(text.lower())
    result = {letter: letters.count(letter) / len(letters) * 100 for letter in letters}
    return result


def task_1():
    print(" Task 1 ".center(80, "="))
    text = input("Please enter your text!\n")
    string_to_symbols_dict(text)

    # for retrieving result in terminal use print statement as follows
    # print(string_to_dict(text))


def task_2():
    print(" Task 2 ".center(80, "="))
    try:
        x, y = int(input("Enter X: ")), int(input("Enter Y: "))
        print(
            f"game over" if x == 0 and y == 0 else
            f"{x + y}" if x < y else
            f"0" if x == y else
            f"{x - y}"
        )

    # another solution :
    # print("game over" if x == 0 and y == 0 else (x + y if x < y else (0 if x == y else x - y))
    except ValueError:
        print("Parameters should be digits!")
        print("Please enter a number")
        task_2()


if __name__ == "__main__":
    task_1()
    task_2()
