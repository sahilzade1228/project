Total = 1000
def Balance():
    print("********************")
    print(f" Your current balnce is ${Total}")
    print("********************")

def Withdrawl():
    global Total
    print("********************")
    amount = float(input("Enter the withdrawal amount: "))
    Total-=amount
    print(f"Your withdrwal amount is ${amount}.Your new balance is ${Total}")
    print("********************")

def Credit():
    global Total
    print("********************")
    amount = float(input("Enter the credit amount: "))
    Total += amount
    print(f"You have credited ${amount}.  Your new balance is ${Total}.")
    print("********************")



def main():
    is_running = True
    while is_running:
        print("********************")
        print("1 . Balance")
        print("2. Withdrawl")
        print("3. Credit")
        print("4. Exit")
        print("********************")
        
        print("********************")
        choice = int(input("entr the number(1-4): "))
        print("********************")

        if choice == 1:
            Balance()
        elif choice==2:
            Withdrawl()
        elif choice==3:
            Credit()
        elif choice ==4:
            is_running = False
        else:
            print("Enter a valid number")
    print("Thank you for visiting")
    print("********************")

if __name__== "__main__":
    main()