class Item:
    def __init__(self, title: str, year: int):
        if not title:
            raise ValueError("The title must not be empty")
        if not isinstance(title, str):
            raise TypeError("The title needs to be a string")
        self.title = title
        if not isinstance(year, int):
            raise TypeError("The year needs to be an int")
        if year < 0:
            raise ValueError("The year must be a positive value")
        self.year = year

    def describe(self) -> str:
        return f"{self.title} ({self.year})"

    def __repr__(self):
        return f"{type(self).__name__}({self.title!r}, {self.year})"


class Book(Item):
    def __init__(self, title: str, year: int, author: str):
        super().__init__(title, year)
        self.author = author

    def describe(self):
        return super().describe() + f" by {self.author}"


class Movie(Item):
    def __init__(self, title: str, year: int, minutes: int):
        if not minutes > 0:
            raise ValueError("Minutes must be greater than 0")
        super().__init__(title, year)
        self.minutes = minutes

    def describe(self):
        return super().describe() + f", {self.minutes} min"


def group_by_decade(items: list[Item]) -> dict[int, list[str]]:
    titles_by_decade: dict[int, list[str]] = {}
    for item in items:
        decade = calculate_decade(item.year)
        if decade not in titles_by_decade:
            titles_by_decade[decade] = [item.title]
        else:
            titles_by_decade[decade].append(item.title)
    return titles_by_decade


def calculate_decade(year: int) -> int:
    years_to_remove = year % 10
    return year - years_to_remove


def main():
    book_one = Book("Cyberpunk", 2077, "V")
    book_two = Book("Book of life", 1, "Life")
    movie_one = Movie("Encanto", 2018, 300)
    movie_two = Movie("Iron Man", 2012, 200)
    items: list[Item] = [book_one, book_two, movie_one, movie_two]
    for item in items:
        print(item.describe())
    results = group_by_decade(items)
    print(results)


if __name__ == "__main__":
    main()
