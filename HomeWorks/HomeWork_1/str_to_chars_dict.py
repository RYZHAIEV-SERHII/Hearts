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


# Tests
import unittest


class TestStringToSymbolsDict(unittest.TestCase):
    def test_empty_string(self):
        result = string_to_symbols_dict('')
        assert result == {}

    def test_single_letter(self):
        result = string_to_symbols_dict('a')
        assert result == {'a': 100.0}

    def test_word_with_repeated_letters(self):
        result = string_to_symbols_dict('hello')
        expected = {'h': 20.0, 'e': 20.0, 'l': 40.0, 'o': 20.0}
        assert result == expected

    def test_mixed_case(self):
        result = string_to_symbols_dict('AbCDabcD')
        expected = {'a': 25.0, 'b': 25.0, 'c': 25.0, 'd': 25.0}
        assert result == expected

    def test_sentence_with_whitespace(self):
        result = string_to_symbols_dict('The quick brown fox jumps over the lazy dog.')
        expected = {'t': 4.55, 'h': 4.55, 'e': 6.82, ' ': 18.18, 'q': 2.27, 'u': 4.55, 'i': 2.27, 'c': 2.27, 'k': 2.27,
                    'b': 2.27, 'r': 4.55, 'o': 9.09, 'w': 2.27, 'n': 2.27, 'f': 2.27, 'x': 2.27, 'j': 2.27, 'm': 2.27,
                    'p': 2.27, 's': 2.27, 'v': 2.27, 'l': 2.27, 'a': 2.27, 'z': 2.27, 'y': 2.27, 'd': 2.27, 'g': 2.27,
                    '.': 2.27}
        assert result == expected


if __name__ == "__main__":
    # text = input("Please enter your text!\n")
    # print(string_to_symbols_dict(text))

    unittest.main(verbosity=2)
