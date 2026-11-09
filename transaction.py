class transaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount


    def __str__(self):
        return f"Transaction ID: {self.transaction_id},  Amount: {self.amount}"