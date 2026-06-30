class bankaccount:
    def __init__(self, owner,balance):
        self.owner=owner
        self.balance=balance     
    def deposit(self,amount):
        print(f"deposited total amount is:{amount}")
        self.balance=self.balance+amount   
    def withdraw(self,amount):
        if amount > self.balance:
         print("insufficient balnce!")
        else:
            print("withdraw in process...") 
            self.balance=self.balance-amount        
    def __str__(self):
        print(f"account holder:{self.owner}")
        print(f"total balance{self.balance}") 
stall=bankaccount("yash",10000)
stall.deposit(5000)
stall.__str__()    