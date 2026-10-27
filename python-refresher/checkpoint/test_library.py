import pytest
from library import Book, Item, Movie, group_by_decade


def test_repr_subclass_works():
    movie_one = Movie("Encanto", 2018, 300)
    assert repr(movie_one) == "Movie('Encanto', 2018)"


def test_group_by_decade_correct_output():
    book_one = Book("Cyberpunk", 2077, "V")
    book_two = Book("Book of life", 1, "Life")
    movie_one = Movie("Encanto", 2018, 300)
    movie_two = Movie("Iron Man", 2012, 200)
    items: list[Item] = [book_one, book_two, movie_one, movie_two]
    results = group_by_decade(items)
    assert results == {
        2070: ["Cyberpunk"],
        0: ["Book of life"],
        2010: ["Encanto", "Iron Man"],
    }


def test_invalid_title_type_raises():
    with pytest.raises(TypeError):
        Book(32, 2077, "V")
