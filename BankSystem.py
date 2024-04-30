class BankAccount:

    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance

    def Deposite(self,amount):
        if amount>0:
            self.balance+=amount
            print("DEPOSITE SUCCESSFULL!!!!")
        else:
            print("DEPOSITE UNSUCCESSFULL!!!!!")


    def Withdraw(self,ammount):
        if 0<ammount<self.balance:
            self.balance -= ammount
            print("WITHDRAW SUCCESSFULL!!!!")
        else:
            print("AMMOUNT INSUFFICIENT!!!!!")

    def bankFees(self):
        fee=self.balance*0.05
        self.balance-=fee
        print("Bank fees applied - $" + str(round(fee)))
    def Display(self):
        print("Account Number:", self.accountNumber)
        print("Account Name:", self.name)
        print("Account Balance:", "$" + str(round(self.balance)))


bank = BankAccount(232403,"Ranjit Sharma",50000)
bank.Deposite(5000)
bank.Display()
print("--------------------------")
bank.Withdraw(4000)
bank.Display()
print("--------------------------")
bank.bankFees()
bank.Display()

