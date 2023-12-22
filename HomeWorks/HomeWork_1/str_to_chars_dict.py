# написати функцію якам приймає рядок і повертає словник у якому
# ключами є всі символи, які зустрічаються в цьому рядку, а значення - відповідні
# вірогідності зустріти цей символ в цьому рядку.
# № код повинен бути структурований за допомогою конструкції if name == "__main__":,
# всі аргументи і значення що функція повертає повинні бути типізовані, функція має рядок документації

def string_to_symbols_dict(text: str) -> dict[str: float]:
    """
Function to convert text to dictionary in which keys are symbols and values are chances to meet symbol
in the given text.
    :param text: text to convert into dictionary.
    :return:  dictionary containing symbols and their frequencies in the given text.
    """
    letters = tuple(text.lower())
    result = {letter: round((letters.count(letter) / len(letters) * 100), 2) for letter in letters}
    return result


if __name__ == "__main__":
    text = input("Please enter your text!\n")
    print(string_to_symbols_dict(text))

    # example:
    # text = "Hello World!"
    # print(string_to_symbols_dict(text))
    # result = {'h': 8.33, 'e': 8.33, 'l': 25.0, 'o': 16.67, ' ': 8.33, 'w': 8.33, 'r': 8.33, 'd': 8.33, '!': 8.33}
