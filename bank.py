class Account:
    bank = 'ABSA'
    def __init__(self,account_name, account_number, branch):
        self.account_name = account_name
        self.account_number = account_number
        self.branch = branch
    def describe_account(self):
        return f"The {self.account_number} is owned by {self.name}"
    def deposit(self):
        return f"This {self.number} deposited 200ksh at {self.branch}"
    def withdraw(self):
        return f"{self.account_name} withdrew 100ksh"

