def login_required(func):
    def login_wrapper(user, password):
        if user=="quest" and password=="quest123":
            func()
            return True
        else:
            print("Invalid credentials...!")
            exit()
    return login_wrapper



@login_required
def home_page():
    print("Login successful")
    print("Welcome to QIS")



@login_required
def about_page():
    print("About QIS")



@login_required
def profile_page():
    print("profile page")


user = input("Enter the username :- ")
password = input("Enter the password :- ")


login_status = home_page(user, password)

while True:
    if login_status:
        choice = int(input("Enter the option :- 1. About Page 2. Profile Page 3. Log out :- "))

        if choice == 1:
            about_page(user, password)

        elif choice == 2:
            profile_page(user, password)
            print("USERNAME :- ", user)
            print("PASSWORD :- ", password)

        elif choice == 3:
            exit()

        else:
            print("Please enter valid choice...!")
