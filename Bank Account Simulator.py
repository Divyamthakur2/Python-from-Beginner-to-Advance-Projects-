# Goal: Simulate deposits and withdrawals using globals

balance = 1000      # global
account_holder = "Divyam Thakur"   # global

def deposit(amount):
    global balance
    balance = balance + amount
    print(f"Deposited £{amount}. New balance: £{balance}")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance = balance - amount
        print(f"Withdrew £{amount}. New balance: £{balance}")

def show_account():
    print(f"Account: {account_holder} | Balance: £{balance}")

# Test it
show_account()
deposit(500)
withdraw(200)
withdraw(2000)
show_account()