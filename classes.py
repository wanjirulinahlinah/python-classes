

# Add these attributes and behaviours to the class Account

# Add attributes deposits and withdrawals in the init method which 
# are empty lists by default and another attribute loan_balance which is zero 
# by default.

class Account:
    def __init__(self):
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
        
# Add a method check_balance which returns the account’s balance


def check_balance(self):
    balance = sum(transaction['amount'] for transaction in self.deposit) - sum (transaction['amount'] for transaction in self.withdrawals)
    return balance


# Update the deposit method to append each withdrawal transaction to the deposits 
# list. Each transaction should be in form of a dictionary like this  
# {
#    "amount": amount,
#    "narration": “deposit”
# }

def deposit(self,amount):
    transaction = {
        "amount": amount,
        "narration": "deposit"
            }
    self.deposits.append(transaction)


#  Update the withdrawal method to append each withdrawal transaction to the 
#  withdrawals list. Each transaction should be in form of a dictionary like like 
#  this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }

def withdrawal(self,amount):
    transaction = {
        "amount":amount,
        "narration":"withdrawal"
    }
    self.withdrawals.append(transaction)
    

 

# Add a new method  print_statement which combines both deposits and withdrawals 
# into one list and, using a for loop, prints each transaction in a new line like 
# this
# deposit - 1000
# withdrawal - 500


def print_statement(self):
    transaction = self.deposit + self.withdrawals
    for transaction in transaction:
        print(f"{transaction['narration']} - {transaction['amount']}")

    
    
# Add a borrow_loan method which allows a customer to borrow if they meet these
# conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount

def borrow_loan(self,amount):
    if self.loan_balance ==  0 and amount > 100 and len(self.deposit) >=10 and amount <= sum(transaction['amount'] for transaction in self.deposits) / 3:
      self.loan_balance = amount
      print("Loan approved!")  
    else:
        print("Loan request denied!")

             



# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance

def repay_loan(self,amount):
    if self.loan_balance > 0:
        if amount > self.loan_balance:
            overpayment = amount - self.loan_balance
            self.deposit(overpayment)
            self.loan_balance = 0
        else:
            self.withdrawal(amount)
            self.loan_balance -= amount
            print("Loan repayment successful!")
    else:
            print("No outstanding loan.")
  
#   Add a transfer method which accepts two attributes (amount and 
# instance of another account). If the amount is less than the current
# instances balance, the method transfers the requested amount from the c
# urrent account to the passed account. The transfer is accomplished by
# reducing the current account balance and depositing the requested amount 
# to the passed account.
def transfer(self,amount,recipient_account):
    if amount <= self.check_balance():
        print("Transfer successful!")
    else:
        print("Insufficient balance for transfer")
        
        

