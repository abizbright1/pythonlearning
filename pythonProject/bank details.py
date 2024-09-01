account_no= input("account number:")
account_balance = int(input("account balance"))

def credit(amount):


    global account_balance
    account_balance=account_balance+amount
    print(f"{amount} was credited and your new balance is: {account_balance}")



def debit(amount):


    global account_balance
    account_balance=account_balance-amount
    print(f"{amount} was debited and your new balance is: {account_balance}")

credit(20)
debit(20)


