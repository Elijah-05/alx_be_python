class InvalidAmountError(Exception):
    """Raised when an invalid amount is used for deposit or withdrawal."""
    pass

class InsufficientFundsError(Exception):
    """Raised when a withdrawal amount exceeds the available balance."""
    pass

class BankAccount:
    def __init__(self, initial_balance = 0):
        # check if the initially passed value is a number
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Initial balance must be a number.")
        
        # check the initial balance must be positive
        if initial_balance < 0:
            raise InvalidAmountError("Initial balance cannot be negative.")
        
        self.__account_balance = initial_balance
        pass

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if amount > 0:
                self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if(self.__account_balance >= amount):
            return True
        return False
        # self.__account_balance -+ amount

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")
