class bank:
    
    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount

    def log_transaction(self, transaction_string):
        with open("transactionss.txt", "a") as file:
            file.write(f"{transaction_string} with a new balance of {self.balance}\n")

    def withdrawal(self,amount):
        try:
            amount= float(amount)
        except ValueError:
            amount = 0    
        if amount:
            self.balance = self.balance - amount
            self.log_transaction(f"withdrew {amount}")

    def deposit(self,amount):
        try:
            amount= float(amount)
        except ValueError:
            amount= 0
        if amount:
            self.balance = self.balance + amount
            self.log_transaction(f"deposited {amount}")

account = bank(50)      
while True:
    try:
        action = input("What kind of  action do you want to take?")
    except KeyboardInterrupt:
        print("\nleaving the online banking app\n")
        break
    if action in ["withdrawal", "deposit"]:
        if action == "withdrawal":
            amount = int(input("What is the amount you want to withdraw?"))
            if amount<= account.balance:
                account.withdrawal(amount)
            else:
                print("insufficient balance for this transaction")
    
        else:
            amount =input("How much do you want to deposit?")
            account.deposit(amount)

        print("your balance is $", account.balance)    
    else:
        print("that is a not a valid action. try again.")