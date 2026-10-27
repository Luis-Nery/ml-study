# Account task: classes, inheritance, pytest

Build an `Account` base class with `SavingsAccount` and `CheckingAccount` subclasses, plus pytest tests. No AI while coding. Time box: 1.5 hours.

When you are done, ask for a review of both files.

## Files

| File | What goes in it |
| --- | --- |
| `accounts.py` | The three classes, a `main()` with a short demo, and a main guard |
| `test_accounts.py` | Your pytest tests |

Run from the repo root (`ml-study/`):

```
python python-refresher/accounts-task/accounts.py
pytest python-refresher/accounts-task -v
```

## `Account` (base class)

### Constructor: `Account(owner, balance=0)`

- [ ] `owner` must be a non-empty string, otherwise raise `ValueError`. (Empty is rejected, but `Account(123)` is still accepted: add a type check.)
- [x] A negative starting `balance` raises `ValueError`.

### `balance`: read-only property

- [x] Reading `acct.balance` returns the current balance.
- [x] Writing `acct.balance = 500` fails with `AttributeError` (a getter with no setter).
- [x] The balance only changes through `deposit` and `withdraw`.

### `deposit(amount)`

- [x] An amount of 0 or less raises `ValueError`.
- [x] Otherwise add it to the balance and return the new balance.

### `withdraw(amount)`

- [x] An amount of 0 or less raises `ValueError`.
- [x] An amount larger than the balance raises `ValueError` ("Insufficient funds").
- [x] Otherwise subtract it and return the new balance.

### `__repr__`

- [x] Returns something like `Account('Harry', 100)`.
- [x] Uses the real class name, so a savings account prints as `SavingsAccount('Harry', 100)` without you rewriting `__repr__` in the subclass.

## `SavingsAccount(Account)`

### Constructor: `SavingsAccount(owner, balance=0, rate=0.02)`

- [x] Calls `super().__init__` for `owner` and `balance`, so the parent's validation still runs.
- [x] `rate` must be between 0 and 1 (inclusive), otherwise raise `ValueError`.

### `add_interest()`

- [x] Adds `balance * rate` to the balance and returns the new balance.

### Withdrawal limit

- [x] At most 3 withdrawals. The 4th call to `withdraw` raises `ValueError`.
- [x] Override `withdraw`: check and count, then let the parent do the real work with `super().withdraw(amount)`.
- [x] A withdrawal that fails (for example, insufficient funds) should not use up one of the 3.

## `CheckingAccount(Account)`

### Constructor: `CheckingAccount(owner, balance=0, overdraft=100)`

- [x] `overdraft` must be 0 or more, otherwise raise `ValueError`.
- [x] The balance may go negative, down to `-overdraft`.

### `withdraw(amount)`

- [x] Override it. Allowed when `balance - amount >= -overdraft`, otherwise raise `ValueError`.
- [x] An amount of 0 or less still raises `ValueError`.
- [x] You cannot simply call the parent's `withdraw`, because it rejects anything above the balance. Decide how to reuse code anyway; there is more than one good answer.

## `main()` and the main guard

- [x] `main()` creates one of each account, does a few deposits and withdrawals, and prints the accounts.
- [x] `main()` only runs with `python accounts.py`, not when pytest imports the file.

## Tests (at least 8, one behavior per `test_` function)

- [x] A new account stores the owner and the balance.
- [x] `deposit` increases the balance and returns it.
- [x] Depositing 0 or a negative amount raises `ValueError`.
- [x] Withdrawing more than the balance from an `Account` raises `ValueError`.
- [x] Assigning to `balance` raises `AttributeError`.
- [x] `SavingsAccount.add_interest()` gives the right result. Pick exact numbers, like 1000 at 0.05.
- [x] The 4th savings withdrawal raises `ValueError`.
- [x] A checking account can go negative within its overdraft, but not past it.
- [x] `repr()` of each class shows the correct class name.

Use `pytest.raises(SomeError)` for the error cases.

## Done when

- [x] `pytest -v` passes every test.
- [x] `python accounts.py` runs the demo.
- [x] Running `pytest` does not run the demo.

## Optional extras

- [ ] `__eq__`: two accounts are equal when they have the same type, owner and balance.
- [ ] A custom `InsufficientFundsError(ValueError)`, used for every insufficient-funds case.
- [ ] A class variable counting how many accounts have been created.

## What the review will look at

1. Correctness: every checkbox above, including the edge cases.
2. Pythonic style: naming, properties, `super()`, f-strings, no Java-isms like `getBalance()`.
3. Tests: does each test check one thing, and would it catch a real bug?

## Reference

The [Python OOP for Java devs](https://claude.ai/artifact/Udy8pRvTK9dTSpjnKVqTd8) doc. Sections 2, 3, 4, 5, 7 and 10 cover everything here.
