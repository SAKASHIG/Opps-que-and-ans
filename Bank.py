class BankAccount:
    def __init__(self,accountno,balance,interest_rate):
        self.accountno=accountno
        self.balance=balance
        self.interest_rate=interest_rate

    def get_balance(self):
        return self.balance

    def get_interest_rate(self):
        return  self.interest_rate

    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            print("DEPOSITE SUCCESSFULL!!!")
        else:
            print("DEPOSITE UNSUCCESSFULL!!!")


    def withdraw(self,amount):
        if 0<amount<self.balance:
            self.balance-=amount
            print("WITHDRAW SUCCESSFULL!!!!")

        else:
            print("WITHDRAW UNSUCCESSFULL!!!!")


class SavingAccount(BankAccount):

    def __init__(self,mini_balance,accountno,balance,interest_rate):
        super().__init__(accountno,balance,interest_rate)
        self.mini_balance=mini_balance

    def calculate_interest(self):

        if self.balance>=self.mini_balance:
            interest=self.balance*self.mini_balance/100
            return interest
        else:
            print("NOT MINIMUM BALANCE")
            return 0


# Create a BankAccount object
account1 = BankAccount(12345678, 1000, 2.5)

# Deposit and withdraw money from the account
account1.deposite(500)
account1.withdraw(200)

# Get the current balance and interest rate
balance1 = account1.get_balance()
interest_rate1 = account1.get_interest_rate()
print(f"Account 1 balance: {balance1}")
print(f"Account 1 interest rate: {interest_rate1}%")

print("----------------------------------------------------")
# Create a SavingsAccount object
account2 = SavingAccount(98765432, 5000, 1.5, 1000)

# Deposit and withdraw money from the account
account2.deposite(1000)
account2.withdraw(500)

# Get the current balance, interest rate, and calculate interest
balance2 = account2.get_balance()
interest_rate2 = account2.get_interest_rate()
interest2 = account2.calculate_interest()
print(f"Account 2 balance: {balance2}")
print(f"Account 2 interest rate: {interest_rate2}")
print(f"Account 2 interest: {interest2}")


