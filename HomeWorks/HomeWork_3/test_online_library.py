import pytest

from online_library import OnlineLibrary, Author, Genre, Book


@pytest.fixture
def sample_book():
    author = Author("John", "Doe", 1980)
    genre = Genre(
        "Fiction", "Books that tell stories created from the author's imagination."
    )
    return Book(
        "Sample Book",
        "English",
        2022,
        author,
        description="A sample book",
        isbn="978-3-16-148410-0",
        genres=[genre],
    )


def test_add_book(sample_book):
    library = OnlineLibrary()
    book = sample_book
    library.books[book.title] = book
    assert library.books == {"Sample Book": book}


def test_add_duplicate_book(sample_book):
    library = OnlineLibrary()
    book1 = sample_book
    book2 = sample_book
    library.books[book1.title] = book1
    library.books[book2.title] = book2
    assert len(library.books) == 1
    assert library.books["Sample Book"] == book1


def test_author_str_representation():
    author = Author("John", "Doe", 1980)
    expected_str = "John Doe (1980)"
    assert str(author) == expected_str


def test_author_repr_representation():
    author = Author("John", "Doe", 1980)
    expected_repr = "Author('John', 'Doe', 1980)"
    assert repr(author) == expected_repr


def test_author_equality():
    author1 = Author("John", "Doe", 1980)
    author2 = Author("John", "Doe", 1980)
    author3 = Author("Jane", "Doe", 1980)
    assert author1 == author2
    assert author1 != author3


def test_genre_str_representation():
    genre = Genre(
        "Fiction", "Books that tell stories created from the author's imagination."
    )
    expected_str = (
        "Fiction - Books that tell stories created from the author's imagination."
    )
    assert str(genre) == expected_str


def test_genre_repr_representation():
    genre = Genre(
        "Fiction", "Books that tell stories created from the author's imagination."
    )
    expected_repr = "Genre('Fiction', 'Books that tell stories created from the author's imagination.')"
    assert repr(genre) == expected_repr


def test_genre_equality():
    genre1 = Genre(
        "Fiction", "Books that tell stories created from the author's imagination."
    )
    genre2 = Genre(
        "Fiction", "Books that tell stories created from the author's imagination."
    )
    genre3 = Genre("Non-Fiction", "Books based on real events.")
    assert genre1 == genre2
    assert genre1 != genre3


def test_book_str_representation(sample_book):
    expected_str = (
        "Sample Book (John Doe (1980)) - 2022, Fiction - Books that tell stories created from the author's "
        "imagination."
    )
    assert str(sample_book) == expected_str


def test_book_repr_representation(sample_book):
    expected_repr = (
        "Book('Sample Book', 'A sample book', 'English', (Author('John', 'Doe', 1980),), [Genre('Fiction', "
        "'Books that tell stories created from the author's imagination.')], 2022, '978-3-16-148410-0')"
    )
    assert repr(sample_book) == expected_repr


def test_book_equality():
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
        "English",
        2022,
        author1,
        description="A sample book",
        isbn="978-3-16-148410-0",
        genres=[genre1],
    )
    book2 = Book(
        "Sample Book",
        "English",
        2022,
        author2,
        description="A sample book",
        isbn="978-3-16-148410-0",
        genres=[genre2],
    )
    book3 = Book(
        "Different Book",
        "English",
        2022,
        author1,
        description="A different book",
        isbn="978-3-16-148410-1",
        genres=[genre1],
    )
    assert book1 == book2
    assert book1 != book3


def test_book_age(sample_book):
    # Assuming the test is run within the same year the book was published
    assert sample_book.age() == 1
