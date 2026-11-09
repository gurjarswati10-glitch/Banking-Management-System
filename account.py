from abc import ABC,abstractmethod
from transaction import transaction
from exceptions import InvalidAmountError, InsufficientBalanceError
class BankAccount(ABC):
    account_count = 0

    def __init__(self,acc_holder_name,acc_number,balance):

        BankAccount.account_count += 1

        self.acc_holder_name=acc_holder_name
        self.acc_number=acc_number
        self.__balance=balance
        self.transactions=[]
    @classmethod
    def total_accounts(cls):
        return cls.account_count



    def deposit(self,amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero")
        self.__balance += amount

        txn = transaction("deposit",amount)
        self.transactions.append(txn)
        print(f"Deposited {amount}. New balance is {self.__balance}")


    def withdraw(self,amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero")
        if amount > self.__balance:
            raise InsufficientBalanceError("Insufficient funds")
        else:
            self.__balance -= amount

            txn = transaction("withdrawal",amount)
            self.transactions.append(txn)
            print(f"Withdrew {amount}. New balance is {self.__balance}")

    def get_balance(self):
        return self.__balance
    def get_account_details(self):
        return (
        f"account holder name: {self. acc_holder_name}\n"
        f"account number: {self.acc_number}\n"
        f"balance: {self.__balance}"
        )


    def show_transaction_history(self):
        print("Transaction History:")

        if not self.transactions:
            print("no transaction yet")
        else:
            for txn in self.transactions:
                print(txn)
    @abstractmethod
    def calculate_interest(self):
        pass