from exceptions import AccountNotFoundError
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self,account):
        for  existing_account in self.accounts:
            if account.acc_number == existing_account.acc_number:
                print(f"Account with number {account.acc_number} already exists.")
                return
        self.accounts.append(account)
        print("account added successfully")

    def find_account(self,acc_number):
        for account in self.accounts:
            if account.acc_number == acc_number:
                return account
        raise AccountNotFoundError("account not found")