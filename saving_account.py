from account import BankAccount
class SavingAccount(BankAccount):
    def __init__(self,acc_holder_name,acc_number,balance,interest_rate):
        super().__init__(acc_holder_name,acc_number,balance)
        self.interest_rate=interest_rate
    def calculate_interest(self):
        interest=self.get_balance()*self.interest_rate/100
        print(f"Interest earned: {interest}")
        return interest
    def withdraw(self,amount):
        if amount > self.get_balance():
            print("insufficient funds")
        else:
            super().withdraw(amount)

