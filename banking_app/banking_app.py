# Banking APP 
# Class called bank 
# Methods Withdrawal and Deposit
# Write the transaction to a python file 
# While true: 
# input 
# classes 
# open()
# method 
# properties


class Bank:
    
    def  __init__(self):
        self.balance = 0
        self.options = ['withdrawal' , 'deposit']
        
   
    def get_transaction(self):
            print(f"This is your current balance ${self.balance}")
            user = input("Would you like to Withdrawal or Deposit money in your bank account? ")
            user = user.lower()   
            try:            
                if user not in self.options:
                    raise ValueError("Invalid option type. Please enter withdrawal or deposit")         
                return user
            except ValueError as error:
                return self.get_transaction()
    
    
    def deposit(self):
        try:
            amount = float(input("Enter deposit amount: "))
            self.balance += amount
            print(f"Depositing ${amount}. The new balance in your account is $ {self.balance}")
        except ValueError:
            print("That is an invalid option")
        
        
    def withdrawal(self):
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount < 0:
                print("Withdrawal cannot be negative. ")
                return
            elif self.balance < amount: 
                print(f"You do not have enough funds ${self.balance}")
            else:    
                self.balance -= amount
                print(f"Withdrawing ${amount}. The new balance of your account is $ {self.balance}")
        except ValueError:
            print("That is not a valid option")
                

transaction = Bank()

while True:
    
    transaction_type = transaction.get_transaction()
    # print(f"You chose: {transaction_type}")

    if transaction_type == "deposit":
        transaction.deposit()
    if transaction_type == "withdrawal":
        transaction.withdrawal()
    another_transaction = input("Do you want to perform another transaction? yes or no? ").lower()
    
    if another_transaction == "no":
        break
    
    
print(f"Your final account balance is ${transaction.balance}")
    

    

    
    
    