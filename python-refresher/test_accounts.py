from accounts import Account, SavingsAccount, CheckingAccount
import pytest


def test_new_account_stores_owner_and_balance():
    account = Account("Jane Doe", 1000)
    assert account.owner == "Jane Doe"
    assert account.balance == 1000


def test_deposit_increases_and_returns_balance():
    account = Account("Jane Doe", 1000)
    new_balance = account.deposit(1000)
    assert new_balance == 2000
    assert account.balance == 2000


def test_depositing_negative_amount_raises():
    account = Account("Jane Doe", 1000)
    with pytest.raises(ValueError):
        account.deposit(-1)


def test_depositing_zero_amount_raises():
    account = Account("Jane Doe", 1000)
    with pytest.raises(ValueError):
        account.deposit(0)


def test_withdraw_more_than_balance_raises():
    account = Account("Jane Doe", 1000)
    with pytest.raises(ValueError):
        account.withdraw(2000)
    assert account.balance == 1000


def test_assigning_balance_raises():
    account = Account("Jane Doe", 1000)
    with pytest.raises(AttributeError):
        account.balance = 1000000000


def test_add_interest_returns_new_balance():
    account = SavingsAccount("Jane Doe", 1000, 0.05)
    new_balance = account.add_interest()
    assert new_balance == 1050
    assert account.balance == 1050


def test_fourth_savings_withdrawal_raises():
    account = SavingsAccount("Jane Doe", 1000, 0.05)
    account.withdraw(100)
    account.withdraw(100)
    account.withdraw(100)
    with pytest.raises(ValueError, match="You can only perform up to 3 withdrawals"):
        account.withdraw(200)


def test_checking_can_go_negative_within_overdraft():
    account = CheckingAccount("Jane Doe", 100, 100)
    new_balance = account.withdraw(150)
    assert new_balance == -50
    assert account.balance == -50


def test_checking_cannot_go_past_overdraft():
    account = CheckingAccount("Jane Doe", 100, 100)
    with pytest.raises(ValueError, match="Not enough funds"):
        account.withdraw(201)
    assert account.balance == 100


def test_account_repr_shows_class_name():
    account = Account("Jane Doe", 1000)
    assert repr(account) == "Account('Jane Doe', 1000)"


def test_savings_repr_shows_class_name():
    account = SavingsAccount("Jane Doe", 1000)
    assert repr(account) == "SavingsAccount('Jane Doe', 1000)"


def test_checking_repr_shows_class_name():
    account = CheckingAccount("Jane Doe", 1000)
    assert repr(account) == "CheckingAccount('Jane Doe', 1000)"
