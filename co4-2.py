class Bank():
    def __init__(self,acc_no,name,typeof,bal):
        self.acc_no=acc_no
        self.name=name
        self.typeof=typeof
        self.bal=bal
    def deposit(self,amount):
        self.bal=self.bal+amount
        print("Balance Amount : ",self.bal)
    def withdraw(self,amount):
        self.bal=self.bal-amount
        print("Balance Amount : ",self.bal)
acc_no=int(input("Enter the account number"))
name=input("Enter account holder name")
typeof=input("Enter the type of account")
amount=int(input("Enter amount to deposit"))
b=Bank(acc_no,name,typeof,amount)
amount=int(input("Enter the amount to deposit : "))
b.deposit(amount)
amount=int(input("Enter the amount to withdraw : "))
b.withdraw(amount)
