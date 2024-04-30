#Create a class BankAccount with attributes account_number, balance, and interest_rate,
#and methods deposit(), withdraw(), get_balance(), and get_interest_rate(). Create a
#subclass CheckingAccount that inherits from BankAccount and adds the attribute
#overdraft_fee and method apply_overdraft_fee(). Create objects of both the classes and
#demonstrate the use of all the methods.


class BankAccount:

    def __init__(self,account_number,balance,interest_rate):
        self.account_number=account_number
        self.balance=balance
        self.interest_rate=interest_rate

    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            print("DONE!!")
        else:
            print("NOT DONE!!!")


    def withdraw(self,amount):
        if 0<amount<self.balance:
            self.balance -=amount
            print("Done!!")
        else:
            print("Not Done!!")

    def get_balance(self):
        return self.balance

    def get_interest_rate(self):
        return self.interest_rate


class CheckingAccount(BankAccount):

    def __init__(self,account_number,balance,interest_rate,overdraft_fee):
        super().__init__(account_number,balance,interest_rate)
        self.overdraft_fee=overdraft_fee

    def apply_overdraft_fee(self):
        if self.balance < 0:
            self.balance -= self.overdraft_fee

    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance-=amount
        else:
            self.balance-=amount
            self.apply_overdraft_fee()



ban = BankAccount(23456,600000,5.9)
ban.deposite(50000)
ban.withdraw(5000)

balance1=ban.get_balance()
interest1=ban.get_interest_rate()
print(f"Balance is {balance1}")
print(f"Interest is {interest1 *100}")
print("----------------------------------")

check = CheckingAccount(123456,800000,9.8,80)
check.deposite(60000)
check.withdraw(7000)

balance2=check.get_balance()
interest2=check.get_interest_rate()
check2=check.apply_overdraft_fee()
print(f"Balance is {balance2}")
print(f"Interest is {interest2 *100}")
print(f"overdraft fee is {check2}")

