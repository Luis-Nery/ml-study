# Python checkpoint: library catalog

Build a small class hierarchy for a library catalog, a function that groups items with a dict and a list, and pytest tests. Blank file: no notes, no docs, no AI. Time box: 1 hour.

This is the step 0 checkpoint. It passes when every box under "Done when" is ticked inside the hour. If it doesn't, note what went wrong at the bottom and retry another day from a new blank file.

When you are done, ask for a review of both files.

## Files

| File | What goes in it |
| --- | --- |
| `library.py` | The three classes, `group_by_decade`, a `main()` with a short demo, and a main guard |
| `test_library.py` | Your pytest tests |

Run from the repo root (`ml-study/`):

```
python python-refresher/checkpoint/library.py
pytest python-refresher/checkpoint -v
```

## `Item` (base class)

### Constructor: `Item(title, year)`

- [x] `title` must be a non-empty string, otherwise raise `ValueError`. (Empty raises `ValueError`; a non-string raises `TypeError`, a deliberate choice.)
- [x] `year` must be an `int`, otherwise raise `ValueError`. (Raises `TypeError` instead, a deliberate choice.)

### `describe()`

- [x] Returns a short string such as `"Dune (1965)"`.

### `__repr__`

- [x] Returns something like `Item('Dune', 1965)`.
- [x] Uses the real class name, so subclasses print their own name without overriding `__repr__`.

## `Book(Item)`

### Constructor: `Book(title, year, author)`

- [x] Calls `super().__init__` so the parent's validation still runs.

### `describe()`

- [x] Overrides the parent and adds the author, e.g. `"Dune (1965) by Frank Herbert"`.
- [x] Reuses the parent's text through `super().describe()` instead of rebuilding it.

## `Movie(Item)`

### Constructor: `Movie(title, year, minutes)`

- [x] `minutes` must be greater than 0, otherwise raise `ValueError`.

### `describe()`

- [x] Overrides the parent and adds the runtime, e.g. `"Alien (1979), 117 min"`.

## `group_by_decade(items)`

A plain function, not a method.

- [x] Takes a list of items (any mix of `Book` and `Movie`).
- [x] Returns a dict that maps each decade to a list of the titles from that decade, e.g. `{1960: ["Dune"], 1970: ["Alien", "Jaws"]}`.
- [x] Titles keep the order they had in the input list.
- [x] An empty list returns an empty dict.

## `main()` and the main guard

- [x] `main()` builds a list with at least two books and two movies, prints each item's `describe()`, then prints the result of `group_by_decade`.
- [x] `main()` only runs with `python library.py`, not when pytest imports the file.

## Tests (at least 3, one behavior per `test_` function)

- [x] `repr()` of a subclass shows the subclass name.
- [x] `group_by_decade` returns the right dict for a small mixed list.
- [x] One invalid input raises `ValueError` (use `pytest.raises`). (Tests a non-string title, which raises `TypeError`.)

## Done when

- [ ] Finished inside 1 hour from a blank file. (Practice run: had AI help. Redo from a new blank file.)
- [x] `pytest -v` passes every test.
- [x] `python library.py` runs the demo.
- [x] Running `pytest` does not run the demo.

## Optional extras (only if time is left)

- [ ] Type hints on every method and on `group_by_decade`.
- [ ] More tests: `describe()` for each class, an empty list, a bad `minutes` value.
- [ ] `__eq__`: two items are equal when they have the same type, title and year.

## What the review will look at

1. Correctness: every checkbox above, including the edge cases.
2. Pythonic style: snake_case, `super()`, f-strings, `type(self).__name__`, no Java-isms.
3. Tests: does each test check one thing, and would it catch a real bug?

