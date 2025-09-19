# bank system
class Account:
    def __init__(self , owner:str, balance = 0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self , amount:float):
        self.balance = amount
        
    def withdraw(self , amount:float):
        if amount >= self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            
        
    def get_balance(self):
        return self.balance
    
    
    


account1 = Account("Johnson" , 1000)
account2 = Account("Walker" , 2000)
    
balance = account1.get_balance()
print(balance)