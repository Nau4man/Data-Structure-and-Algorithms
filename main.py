class Authentication:

	def __init__(self, name, email, password):
	    self.name = name
	    self.email = email
	    self.password = password

	# Login Implementation using If else

	def login(email, password):
	    if email == "mulunehrediet@gmail.com" and password == 1234567:
	        print("You're Logged In! Welcome")
	    else:
	        print("Sorry, Incorrect Credentials")

	def register(name,email,password):
		print(name)

		# return "Welcome "+name+"\n Please note down your email and Password to login: \n Email: "+email+"\n Password: "+password

	


def main():
	name = input("Enter your Name:")
	email = input("Enter your Email:")
	password = input("Enter your Password:")
	auth = Authentication(name, email, password)
	print(auth.register(name, email,password))
	email = input("Enter your Email:")
	password = input("Enter your Password:")
	auth.login(name, email)
	
if __name__ == '__main__':
	main()
