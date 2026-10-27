import random

#function

def calculate_interest(balance,rate):
    interest=balance*rate/100
    return interest

def generate_account_number():
    account_no=random.randint(10000,99999)
    return account_no

def validate_phone(phone):
    if len(phone) == 10 and phone.isdigit():
        return True
    else:
        return False
    
#Class creation starts     

class Customer:
    """THIS CLASS STORE CUSTOMER INFORMATION"""
    bank_name="ABC Bank"
    def __init__(self,customer_id,name,age,phone_no,address):
        self.customer_id=customer_id
        self.name=name
        self.age=age
        self.phone_no=phone_no
        self.address=address
    def display_customer(self):
        print("Customer_id : ",self.customer_id)
        print("Customer_Name : ",self.name)
        print("Customer_age : ",self.age)
        print("Customer phone_no : ",self.phone_no)
        print("Customer address : ",self.address)
    def check_age(self):
        if self.age<18:
            print("Customer is minor")
        elif self.age<60:
            print("Customer is an adult")
        else:
            print("Customer is senior citizen")

class Bank_Account:
    """BASE CLASS FOR BANK ACCOUNTS"""
    bank_name="ABC Bank"

    def __init__(self,account_no,account_holder_name,balance=0):
        self.account_no=account_no
        self.account_holder_name=account_holder_name
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print("Amount deposited successfully.")
            print("New Balance",self.balance)
        else:
            print("Invalid Amount")

    def withdraw(self,amount):
        if amount <=0:
            print("Invalid amount")
        elif amount<=self.balance:
            self.balance=self.balance-amount
            print("Amount withdrawn successfully.")
            print("Remaning balance : ",self.balance)
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print("Current Balance :",self.balance)

    def display_account(self):
        print("------------ACCOUNT DETAILS----------")
        print("Bank name      : ",Bank_Account.bank_name)
        print("Account number : ",self.account_no)
        print("Account holder : ",self.account_holder_name)
        print("Balance        : ",self.balance)

class SavingAccount(Bank_Account):
    """Saving Account inherits from BankAccount"""
    def __init__(self,account_no,account_holder_name,balance,interest_rate):
        super().__init__(account_no,account_holder_name,balance)
        self.interest_rate=interest_rate

    def add_interest(self):
        interest=calculate_interest(self.balance,self.interest_rate)

        self.balance=self.balance+interest

        print("Interest Added:",interest)
        print("New balance   :",self.balance)

        ##method overriding
    def display_account(self):
        print("----------SAVING ACCOUNTS----------")
        print("Bank Name      :",Bank_Account.bank_name)
        print("Account Number :",self.account_no)
        print("Account Holder :",self.account_holder_name)
        print("balance        :",self.balance)
        print("Interest rate  :",self.interest_rate,"%")

class PremiumSavingAccount(SavingAccount):
    """PREMIUM SAVING ACCOUNT"""
    def __init__(
            self,
            account_no,
            account_holder_name,
            balance,
            interest_rate,
            minimum_balance
    ):
        super().__init__(
            account_no,
            account_holder_name,
            balance,
            interest_rate
        )
        self.minimum_balance=minimum_balance

    def check_premium_status(self):

        if self.balance>=self.minimum_balance:
            print("Premium account activated")
        else:
            print("Premium account not acctivated")

    def display_account(self):
        print("-------Premium saving account------")
        print("Bank Name           :",Bank_Account.bank_name)
        print("Account Number      :",self.account_no)
        print("Account Holder name :",self.account_holder_name)
        print("Balance             :",self.balance)
        print("interest rate       :",self.interest_rate)
        print("Minimum balance     :",self.minimum_balance)

class CurrentAccount(Bank_Account):
    """     CURRENT ACCOUNT    """
    def __init__(self,
                 bank_name,
                 account_no,
                 account_holder_name,
                 balance,
                 interest_rate,
                 minimum_balance,
                 overdraft_limit
                 ):
        super().__init__(bank_name,
                         account_no,
                         account_holder_name,
                         balance,
                         interest_rate,
                         minimum_balance
                         )
        self.overdraft_limit=overdraft_limit

    def check_overdraft(self,amount):

        if amount <= 0:
            print("Invalid amount")

        elif amount <= self.balance:
            self.balance=self.balance-amount
            print("Withdrawal successful.")
            print("Remaning balance",self.balance)
        elif amount <= self.balance + self.overdraft_limit:
            extra_amount=amount-self.balance
            self.balance = 0

            print("Withdrwal allowed using overdraft.")
            print("Overdraft used   : ",extra_amount)
            print("Remaning balance : ",self.balance)

        else:
            print("Withdrwal exceeds overdraft limit")

    def display_account(self):
        print("Bank Name           : ",Bank_Account.bank_name)
        print("Account number      : ",self.account_no)
        print("Account holder name : ",self.account_holer_name)
        print("Balance             : ",self.balance)
        print("Interest rate       : ",self.interest_rate)
        print("Minimum balance     : ",self.minimum_balance)
        print("Overdraft limit     : ",self.overdraft_limit)

class Loan:
    """Loan related services"""
    def calculate_loan(self,principal,rate,years):
        interest=principal*rate*years/100
        total_amount=principal+interest

        print("----Loan details-----")
        print("Principal amount : ",principal)
        print("Interest earn    :",interest)
        print("Total amount     : ",total_amount)

        return total_amount

class Insurance:
    """Insurance related services"""
    def calculate_insurance(self,amount,years):
        premium=amount*0.5*years

        print("-----Insurance details----")
        print("Insurance amount : ",amount)
        print("years            : ",years)
        print("Premium          :",premium)

        return premium

class Bank_Services(Loan,Insurance):
    """class demonstrating multiple inheritance"""
    def display_services(self):
        print("Bank provides loann and Insurance services.")


####GLOBAL DICTIONARIES####

customers={}
accounts={}

#Customer functions

def add_customer():
    print("------ADD CUSTOMER------")

    customer_id=int(input("Enter customer ID : "))

    if customer_id in customers :
        print("Customer ID already exists.")
        return
    name=input("Enter name : ")
    age=int(input("Enter age : "))
    phone=input("Enter phone number : ")

    if not validate_phone(phone):
        print("Invalid phone number")
        return

    address = input("Enter address : ")

    if age < 18:
        print("Minor cannot create a bank account")
        return

    customer=customer(
        customer_id,
        name,
        age,
        phone,
        address
    )
    customers[customer_id]=customer
    print("Customer added successfully.")

def display_cutomer():
    customer_id=int(input("Enter customer id : "))

    if customer_id in customers:

        customer=customers[customer_id]

        customer.display_customer()
        customer.check_age()

    else:
        print("Customer not found")

def search_customer():

    customer_id=int(input("Enter customer ID : "))

    if customer_id in customers:
        customers[customer_id].display_customer()

    else:
        print("Customer not found.")

def delete_customer():
    customer_id=int(input("Enter Customer ID : "))

    if customer_id in customers:
        del customers[customer_id]

        print("Customer deleted successfully.")

    else:
        print("Customer not found.")

def display_all_customers():

    if len(customers) == 0:
        print("No customers available.")
        return
    print("-------All customers-------")

    for customer_id, customer in customers.items():

        print("Customer ID :", customer_id)
        print("Name        :", customer.name)
        print("Age         :", customer.age)
        print("Phone       :", customer.phone)
        print("Address     :", customer.address)

    
# ACCOUNT FUNCTION

def create_savings_account():
    print("-------CREATE SAVING ACCOUNT-------")

    customer_id=int(input("Enter Customer ID : "))

    if customer_id not in customers:
        print("Customer does notn exist.")
        return

    customer=customers[customer_id]

    account_number=generate_account_number()

    while account_number in accounts:
        account_number=generate_account_number()

        balance=float(input("Enter Initial balance : "))
        interest_rate=float(input("Enter interest rate  :"))
        account=SavingAccount(
            account_number,
            customer.name,
            balance,
            interest_rate

        )

        accounts[account_number]=account

        print("Saving account created successfully.")
        print("Account number :",account_number)

def create_current_account():

    print("\n---------- CREATE CURRENT ACCOUNT ----------")

    customer_id = int(input("Enter Customer ID : "))

    if customer_id not in customers:
        print("Customer does not exist.")
        return

    customer = customers[customer_id]

    account_number = generate_account_number()

    while account_number in accounts:
        account_number = generate_account_number()

    balance = float(input("Enter Initial Balance : "))

    overdraft_limit = float(input("Enter Overdraft Limit : "))

    account = CurrentAccount(
        account_number,
        customer.name,
        balance,
        overdraft_limit
    )

    accounts[account_number] = account

    print("Current Account created successfully.")
    print("Account Number :", account_number)

def deposit_money():
    account_number = int(input("Enter Account Number : "))

    if account_number in accounts:

        amount = float(input("Enter Deposit Amount : "))

        accounts[account_number].deposit(amount)

    else:
        print("Account not found.")


def withdraw_money():

    account_number = int(input("Enter Account Number : "))

    if account_number in accounts:

        amount = float(input("Enter Withdrawal Amount : "))

        accounts[account_number].withdraw(amount)

    else:
        print("Account not found.")


def check_balance():
    account_number = int(input("Enter Account Number : "))

    if account_number in accounts:

        accounts[account_number].check_balance()

    else:
        print("Account not found.")


def add_interest():

    account_number = int(input("Enter Account Number : "))

    if account_number in accounts:

        account = accounts[account_number]

        if isinstance(account, SavingAccount):
            account.add_interest()
       
        else:
            print("Account not found.")


def check_overdraft():

    account_number = int(input("Enter Account Number : "))

    if account_number in accounts:

        account = accounts[account_number]

        if isinstance(account, CurrentAccount):

            amount = float(input("Enter Withdrawal Amount : "))

            account.check_overdraft(amount)

        else:
            print("Overdraft is available only for current accounts.")

    else:
        print("Account not found.")


## INSURANCE FUNCTION
def insurance_calculation():

    print("\n---------- INSURANCE CALCULATION ----------")

    amount = float(input("Enter Insurance Amount : "))
    years = int(input("Enter Number of Years : "))

    service = Bank_Services()

    service.calculate_insurance(
        amount,
        years
    )

# MAIN MENU
while True:

    print("\n")
    print("==============================================")
    print("          ABC BANK MANAGEMENT SYSTEM")
    print("==============================================")

    print("1. Add Customer")
    print("2. Display Customer")
    print("3. Search Customer")
    print("4. Delete Customer")
    print("5. Create Savings Account")
    print("6. Deposit Money")
    print("7. Withdraw Money")
    print("8. Check Balance")
    print("9. Add Interest")
    print("10. Create Current Account")
    print("11. Check Overdraft")
    print("12. Loan Calculation")
    print("13. Insurance Calculation")
    print("14. Display All Customers")
    print("15. Exit")

    choice = int(input("\nEnter your choice : "))

    if choice == 1:
        add_customer()

    elif choice == 2:
        display_cutomer()

    elif choice == 3:
        search_customer()

    elif choice == 4:
        delete_customer()

    elif choice == 5:
        create_savings_account()

    elif choice == 6:
        deposit_money()

    elif choice == 7:
        withdraw_money()
        
    elif choice == 8:
        check_balance()

    elif choice == 9:
        add_interest()

    elif choice == 10:
        create_current_account()

    elif choice == 11:
        check_overdraft()

    elif choice == 12:
        Loan()

    elif choice == 13:
        insurance_calculation()

    elif choice == 14:
        display_all_customers()

    elif choice == 15:
        print("Thank you for using ABC Bank.")
        break
    else:
        print("Invalid choice.")










    








   
        

        

        