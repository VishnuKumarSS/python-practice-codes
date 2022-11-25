# Own Code
class Bank:
    def __init__(self):
        self.details = {}
        self.acc_no = int(input("Enter Account Number: "))
        self.acc_name = input("Enter Account Name: ")
        self.password = input("Enter Password: ")
        self.amount = 0
        self.details[self.acc_no] = {
            "name" : self.acc_name,
            "balance" : self.amount
            }

    def deposit(self):
        pw = input("password: ")
        if pw == self.password:
            self.deposit_amount = int(input("Enter Amount to deposit: "))
            self.details[self.acc_no] = {
                "name" : self.acc_name,
                "balance" : self.details[self.acc_no]["balance"]+self.deposit_amount,
            }
            print("\nDetails --- ",self.details[self.acc_no])
    def withdraw(self):
        pw = input("password: ")
        if pw == self.password:
            self.withdraw_amount = int(input("Enter Amount to withdraw: "))
            if self.withdraw_amount < self.details[self.acc_no]["balance"]:
                self.details[self.acc_no] = {
                    "name" : self.acc_name,
                    "balance" : abs(self.details[self.acc_no]["balance"]-self.withdraw_amount),
                }
            elif self.withdraw_amount > self.details[self.acc_no]["balance"]:
                print("Insufficient balance. Can't withdraw :)")
                bank.withdraw()
            print("\nDetails --- ",self.details[self.acc_no])

    def display(self):
        print("\nDetails --- ",self.details[self.acc_no])
        
bank = Bank()
while True:
    action = input("""
Enter 
1 = 'deposit' or
2 = 'withdraw' or
3 = 'display'
4 = 'exit'. """)
    if action == str(1):    
        bank.deposit()
    elif action == str(2):
        bank.withdraw()
    elif action == str(3):
        bank.display()
    elif action == str(4):
        print("\nExited.")
        break
    else:
        print("Enter valid input.")
        continue
