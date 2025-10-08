# NO chatgpt involved.

class BankAccount:
    bank_name = "Mandiri"
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} doing deposit right now with {amount}.")
        print(f"Amount added by {amount}.")
        print(f"Transaction succeed.")
        print(f"Balance is now: {self.balance}.")
    def withdraw(self, amount):
        print(f"{self.owner} doing withdrawals right now with {amount}.")
        try:
            if amount > self.balance or self.balance == 0:
                raise ValueError("Insufficient fund.")
            else:
                self.balance -= amount
                print("Transaction succeed.")
        except ValueError as e:
            print(f"Error: {e}")
    def show_balance(self):
        print(f"Total balance is: {self.balance}.")
    
accAsep = BankAccount("Asep", 9500)
accAgus = BankAccount("Agus", 3500)

# intro
print(f"\n{"Banking System":-^30}> {BankAccount.bank_name:-^11}")
print()

# show account
print("Asep account:")
print("\t", end='');accAsep.show_balance()
print("Agus account:")
print("\t", end='');accAgus.show_balance()
print()

# Agus tries to withdraw 10000 amount INVALID INPUT
accAgus.withdraw(10000)
accAgus.show_balance()
print()

# Agus tries to deposit 2500 amount VALID INPUT
accAgus.deposit(2500)
print()

# Asep tries to withdraw 12000 amount INVALID INPUT
accAsep.withdraw(12000)
print()

# Asep tries to deposit 4000 amount VALID INPUT
accAsep.deposit(4000)
print()

# show Asep and Agus final balance
print("Asep final account balance:")
print("\t", end='');accAsep.show_balance()
print("Agus final account balance:")
print("\t", end='');accAgus.show_balance()
print(f"{"End":-^40}")
print()