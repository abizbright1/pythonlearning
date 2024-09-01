class bank:
    bank_name = "Nur bank"
    def __init__(self, name, account_no, initial_balance):
        self.bank_name =name
        self.account_no =account_no
        self.initial_balance=initial_balance

    def debit(self, debit_amount):
        print(f"from the {self.bank_name} in the account number with {self.account_no} with {self.initial_balance}")
        self.initial_balance=self.initial_balance - debit_amount
        print("this is the amount debited:",debit_amount,"\nthis is your current balance:",self.initial_balance)
    def credit(self, credit_amount):
        print(f"from the {self.bank_name} in the account number with {self.account_no} with {self.initial_balance}")
        self.initial_balance=self.initial_balance + credit_amount
        print("this is the amount credited:",credit_amount,"\nthis is your current balance:",self.initial_balance)

s1= bank("nyr", 3624763487, 1000)

s1.debit(100)
s1.credit(200)

