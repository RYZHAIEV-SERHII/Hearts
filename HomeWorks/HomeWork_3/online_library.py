class OnlineLibrary:
    """Online library class is specified for storing information about books, their authors
    and many other information"""

    books = {}


class Author:
    def __init__(self, first_name: str, last_name: str, year_of_birth: int):
        """
        Author instance has the following information about it:
                :param first_name: First title of the author
                :param last_name: Last title of the author
                :param year_of_birth: Year of birth of the author
        """
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.year_of_birth})"

    def __repr__(self) -> str:
        return f"Author('{self.first_name}', '{self.last_name}', {self.year_of_birth})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Author):
            return False
        return (
            self.first_name == other.first_name
            and self.last_name == other.last_name
            and self.year_of_birth == other.year_of_birth
        )


class Genre:
    def __init__(self, name: str, description: str):
        """
        Genre instance has the following information about it:
                :param name: Name of the title in which the book is writen
                :param description: Description of title
        """
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return f"{self.name} - {self.description}"

    def __repr__(self) -> str:
        return f"Genre('{self.name}', '{self.description}')"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Genre):
            return False
        return self.name == other.name and self.description == other.description


class Book:
    def __init__(
        self,
        title: str,
        language: str,
        year_of_publication: int,
        *authors,
        description: str = "",
        isbn: str = "",
        genres: list[Genre] = None,
    ):
        """
        Book instance has the following information about it:
                :param title: Name of the book (mandatory)
                :param language: Language in which the book is published (mandatory)
                :param year_of_publication: Year in which the book was published (mandatory)
                :param authors: List of authors (positionals arguments)
                :param description: Description of the book (optional, default="")
                :param isbn: (International Standard Book Number) Book identifier (optional, default="")
                :param genres: List of genres
        """
        self.title = title
        self.language = language
        self.year_of_publication = year_of_publication
        self.authors = authors
        self.description = description
        self.isbn = isbn
        self.genres = genres if genres is not None else []

    def __str__(self) -> str:
        authors_str = ", ".join(str(author) for author in self.authors)
        genres_str = ", ".join(str(genre) for genre in self.genres)
        return (
            f"{self.title} ({authors_str}) - {self.year_of_publication}, {genres_str}"
        )

    def __repr__(self) -> str:
        return (
            f"Book('{self.title}', '{self.description}', '{self.language}', {self.authors}, "
            f"{self.genres}, {self.year_of_publication}, '{self.isbn}')"
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.authors == other.authors

    def age(self):
        from datetime import datetime

        present = datetime.now()
        return present.year - self.year_of_publication
