class OnlineLibrary:
    """ Online library class is specified for storing information about books, their authors
    and many other information"""

    books = {}


class Book:
    def __init__(self, name, description, language, authors, genres, year, isbn):
        """
Book instance has the following information about it:
        :param name: Name of the book
        :param description: Description of the book
        :param language: Language in which the book is published
        :param authors: List of authors
        :param genres: List of genres
        :param year: Year in which the book was published
        :param isbn: (International Standard Book Number) Book identifier
        """
        self.name = name
        self.description = description
        self.language = language
        self.authors = authors
        self.genres = genres
        self.year = year
        self.isbn = isbn


class Genre:
    def __init__(self, genre, description):
        """
Genre instance has the following information about it:
        :param genre: Name of the genre in which the book is writen
        :param description: Description of genre
        """
        self.genre = genre
        self.description = description


class Author:
    def __init__(self, first_name, last_name, year):
        """
Author instance has the following information about it:
        :param first_name: First name of the author
        :param last_name: Last name of the author
        :param year: Year of birth of the author
        """
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year
