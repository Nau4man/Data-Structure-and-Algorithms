# Login Implementation using If else


def login(email, password):
    if email == "mulunehrediet@gmail.com" and password == 1234567:
        print("You're Logged In! Welcome")
    else:
        print("Sorry, Incorrect Credentials")


email = input("Enter your Email:")
password = input("Enter your Password:")

login(email, password)
