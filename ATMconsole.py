balance = int(input("Enter the balance amount :- "))
while True:
    print(' ')
    options = int(input("Enter the options :- \n" 
    "1. Check current balance \n" 
    "2. Withdraw \n" 
    "3. Deposit \n" 
    "4. Exit \n"))

    if options == 1:
        print("Your Current Balance :-", balance)

    elif options == 2:
        withdraw_amount = int(input("Enter the amount to withdraw :- "))
        if withdraw_amount < balance:
            balance -= withdraw_amount
            print(f"{withdraw_amount} withdrawn successfully...")
            print(f"Your current balance :- ", balance)
        else:
            print("Insufficient balance...!")

    elif options == 3:
        deposit_amount = int(input("Enter the amount to deposit :- "))
        balance += deposit_amount
        print(f"{deposit_amount} deposited successfully...")
        print(f"Your current balance :- ", balance)

    elif options == 4:
        exit()

    else:
        print("Enter a valid option...!")