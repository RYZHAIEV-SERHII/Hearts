import unittest

from online_library import OnlineLibrary, Author, Genre, Book


class TestOnlineLibrary(unittest.TestCase):
    def test_add_book(self):
        library = OnlineLibrary()
        author = Author("John", "Doe", 1980)
        genre = Genre(
            "Fiction", "Books that tell stories created from the author's imagination."
        )
        book = Book(
            "Sample Book",
            "A sample book description",
            "English",
            [author],
            [genre],
            2022,
            "978-3-16-148410-0",
        )

        library.books[book.title] = book

        self.assertEqual(library.books, {"Sample Book": book})

    def test_add_duplicate_book(self):
        library = OnlineLibrary()
        author = Author("John", "Doe", 1980)
        genre = Genre(
            "Fiction", "Books that tell stories created from the author's imagination."
        )
        book1 = Book(
            "Sample Book",
            "A sample book description",
            "English",
            [author],
            [genre],
            2022,
            "978-3-16-148410-0",
        )
        book2 = Book(
            "Sample Book",
            "Another description",
            "English",
            [author],
            [genre],
            2022,
            "978-3-16-148410-0",
        )

        library.books[book1.title] = book1
        library.books[book2.title] = book2

        self.assertEqual(len(library.books), 1)
        self.assertEqual(library.books["Sample Book"], book1)


class TestAuthor(unittest.TestCase):
    def test_author_str_representation(self):
        author = Author("John", "Doe", 1980)
        expected_str = "John Doe (1980)"
        self.assertEqual(str(author), expected_str)

    def test_author_repr_representation(self):
        author = Author("John", "Doe", 1980)
        expected_repr = "Author('John', 'Doe', 1980)"
        self.assertEqual(repr(author), expected_repr)

    def test_author_equality(self):
        author1 = Author("John", "Doe", 1980)
        author2 = Author("John", "Doe", 1980)
        author3 = Author("Jane", "Doe", 1980)

        self.assertEqual(author1, author2)
        self.assertNotEqual(author1, author3)


class TestGenre(unittest.TestCase):
    def test_genre_str_representation(self):
        genre = Genre(
            "Fiction", "Books that tell stories created from the author's imagination."
        )
        expected_str = (
            "Fiction - Books that tell stories created from the author's imagination."
        )
        self.assertEqual(str(genre), expected_str)

    def test_genre_repr_representation(self):
        genre = Genre(
            "Fiction", "Books that tell stories created from the author's imagination."
        )
        expected_repr = "Genre('Fiction', 'Books that tell stories created from the author's imagination.')"
        self.assertMultiLineEqual(repr(genre), expected_repr)

    def test_genre_equality(self):
        genre1 = Genre(
            "Fiction", "Books that tell stories created from the author's imagination."
        )
        genre2 = Genre(
            "Fiction", "Books that tell stories created from the author's imagination."
        )
        genre3 = Genre("Non-Fiction", "Books based on real events.")

        self.assertEqual(genre1, genre2)
        self.assertNotEqual(genre1, genre3)


class TestBook(unittest.TestCase):
    def test_book_str_representation(self):
        author = Author("John", "Doe", 1980)
        genre = Genre(
            "Fiction", "Books that tell stories created from the author's imagination."
        )
        book = Book(
            "Sample Book",
            "A sample book description",
            "English",
            [author],
            [genre],
            2022,
            "978-3-16-148410-0",
        )
        expected_str = (
            "Sample Book (John Doe (1980)) - 2022, Fiction - Books that tell stories created from the "
            "author's imagination."
        )
        self.assertEqual(str(book), expected_str)

    def test_book_repr_representation(self):
        author = Author("John", "Doe", 1980)
        genre = Genre(
            "Fiction", "Books that tell stories created from the author's imagination."
        )
        book = Book(
            "Sample Book",
            "A sample book description",
            "English",
            [author],
            [genre],
            2022,
            "978-3-16-148410-0",
        )
        expected_repr = (
            "Book('Sample Book', 'A sample book description', 'English', [Author('John', 'Doe', 1980)], "
            "[Genre('Fiction', 'Books that tell stories created from the author's imagination.')], "
            "2022, '978-3-16-148410-0')"
        )
        self.assertMultiLineEqual(repr(book), expected_repr)

    def test_book_equality(self):
        author1 = Author("John", "Doe", 1980)
        author2 = Author("John", "Doe", 1980)
        genre1 = Genre(
            "Fiction", "Books that tell stories created from the author's imagination."
        )
        genre2 = Genre(
            "Fiction", "Books that tell stories created from the author's imagination."
        )
        book1 = Book(
            "Sample Book",
            "A sample book description",
            "English",
            [author1],
            [genre1],
            2022,
            "978-3-16-148410-0",
        )
        book2 = Book(
            "Sample Book",
            "Another description",
            "English",
            [author2],
            [genre2],
            2022,
            "978-3-16-148410-0",
        )
        book3 = Book(
            "Different Book",
            "A different book description",
            "English",
            [author1],
            [genre1],
            2022,
            "978-3-16-148410-1",
        )

        self.assertEqual(book1, book2)
        self.assertNotEqual(book1, book3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
