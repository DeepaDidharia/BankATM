class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print("Your balance is :-")
        print("Knuts = 100")
        print("Sickles = 200")
        print("Galleon = 300")

    def withdrawl1(self,knuts):
        new_amount = 100 - knuts
        print("You have withdrawn amount "+str(knuts) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl2(self,sickles):
        new_amount = 200 - sickles
        print("You have withdrawn amount "+str(sickles) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl3(self,galleon):
        new_amount = 300 - galleon
        print("You have withdrawn amount "+str(galleon) + ". Your remaining balance is "+ str(new_amount))       

        def deposite1(self,knuts):
        new_amount = 100 - knuts
        print("You have deposited amount "+str(knuts) + ". Your remaining balance is "+ str(new_amount))

    def deposite2(self,sickles):
        new_amount = 200 + sickles
        print("You have deposited amount "+str(sickles) + ". Your remaining balance is "+ str(new_amount))

    def deposite3(self,galleon):
        new_amount = 300 + galleon
        print("You have deposited amount "+str(galleon) + ". Your remaining balance is "+ str(new_amount))        


def main():
    print("Welcome to the ABXYcZ bank! ")
    Account = input("Please enter your acount number: ")
    Card_number = input("Insert your key number:- ")
    pin_number  = input("Enter your pin number:- ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl   3.Deposite")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("Choose the activity number")
        print("1. Add Knuts")
        print("2. Add Sickles")
        print("3. Add Galleon")
        choose = int(input("Enter your activity number here:"))
        if (choose == 1):
           knuts = int(input("Enter the amount:- "))
           new_user.withdrawl1(knuts)
        if (choose == 2):
           sickles = int(input("Enter the amount:- "))
           new_user.withdrawl2(sickles)    
        if (choose == 3):
           galleon = int(input("Enter the amount:- "))
           new_user.withdrawl3(galleon)
    elif (activity == 3):
        print("Choose the activity number")
        print("1. Add Knuts")
        print("2. Add Sickles")
        print("3. Add Galleon")
        choose = int(input("Enter your activity number here:"))
        if (choose == 1):
           knuts = int(input("Enter the amount:- "))
           new_user.deposite1(knuts)
        if (choose == 2):
           sickles = int(input("Enter the amount:- "))
           new_user.deposite2(sickles)    
        if (choose == 3):
           galleon = int(input("Enter the amount:- "))
           new_user.deposite3(galleon)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()