from account import BankAccount
class CurrentAccount(BankAccount):
    def __init__(self,acc_holder_name,acc_number,balance,minimum_balance):
        super().__init__(acc_holder_name,acc_number,balance)
        self.minimum_balance = minimum_balance
    def calculate_interest(self):
        print("Current accounts do not earn interest.")

    def withdraw(self,amount):
        if self.get_balance() - amount < self.minimum_balance:
            print("Withdrawal denied. Balance would fall below minimum.")
        else:
            super().withdraw(amount)
            print("withdrawal successful")

