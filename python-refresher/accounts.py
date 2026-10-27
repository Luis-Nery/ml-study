class Account:
    def __init__(self,owner,balance=0):
        if not owner:
            raise ValueError("Missing Owner")
        if balance<0:
            raise ValueError("Negative Balance")
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self,deposit_amount):
        if deposit_amount<=0:
            raise ValueError("Deposit must be greater than 0")
        self._balance+=deposit_amount
        return self._balance

    def withdraw(self,withdraw_amount):
        if withdraw_amount<=0:
            raise ValueError("Withdraw amount can not be negative ")
        if self.balance<withdraw_amount:
            raise ValueError("Not enough funds")
        self._balance-=withdraw_amount
        return self._balance 

    def __repr__(self):
        return f"{type(self).__name__}({self.owner!r}, {self.balance})"

class SavingsAccount(Account):
    def __init__(self,owner,balance=0,rate = 0.02):
        if not 0<=rate<=1:
            raise ValueError("Rate must be between 0 and 1")
        super().__init__(owner,balance)
        self.rate=rate
        self.withdraw_counter = 0

    def withdraw(self, withdraw_amount):
        if self.withdraw_counter>=3:
            raise ValueError("You can only perform up to 3 withdrawals")
        new_balance = super().withdraw(withdraw_amount)
        self.withdraw_counter+=1
        return new_balance
    
    def add_interest(self):
        self._balance+=self._balance*self.rate
        return self._balance
class CheckingAccount(Account):
    def __init__(self,owner,balance=0,overdraft=100):
        if overdraft<0:
            raise ValueError("Overdraft must be a positive value")
        if balance<overdraft*-1:
            raise ValueError("Overdraft exceeded")
        super().__init__(owner,balance)
        self.overdraft = overdraft

    def withdraw(self, withdraw_amount):
        if withdraw_amount<=0:
            raise ValueError("Withdraw amount can not be negative ")
        if self.balance-withdraw_amount<(self.overdraft*-1):
            raise ValueError("Not enough funds")
        self._balance-=withdraw_amount
        return self._balance 

def main():
    account = Account("Luis",100000000)
    savings = SavingsAccount("Luis",20,0.314)
    checkings = CheckingAccount("Luis",100000,50)
    account.deposit(100000000)
    savings.withdraw(12)
    checkings.withdraw(100049)
    print(account)
    print(savings)
    print(checkings)

if __name__ == "__main__":
    main()