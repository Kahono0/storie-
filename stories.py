import random
import json
#print("Hello and welcome to user stories.\nPlease login to continue")
print("Welcome to USER STORIES,\n\tPlease login..")


class credentials:
	"""
	This class accepts account_name, username, password.
	It stores them as a dictionary.
	"""
	def __init__(self,account,username,password):
		self.account = account
		self.username = username
		self.password = password
	def save(self):
		f = open("acc.txt","a")
		f.write(self.account+"\n")
		f.write(self.username+"\n")
		f.write(self.password+"\n")
		f.close()

class user:
	"""
	This class holds information on user.
	"""
	def __init__(self,data):
		self.data = data

	def user(self):
		return self.data["user"]

	def password(self):
		return self.data["pass"]

def main():
    """
    This is the main function of the application.
    """
    login("")
    choose("")
def login(a):
	"""
	This is the login function.
	It verifies each user.
	"""
	if a!= "":
	    print(a)
	username = input("Username>>> ")
	password = input("Password>>> ")
	with open("cr.json","r") as f:
		data = f.read()
		data = json.loads(data)
	user_data = user(data)
	if username == user_data.user():
		if password == user_data.password():
			print("Login successful.\n\tWelcome..")
		else:
			print("Incorrect password")
			login("Please try again..")
	else:
		print("Incorrect username")
		login("Please try again..")

def choose(a):
    """
    This function allows the user to choose from the
    available options.
    """
    if a != "":
        print(a)
    x = int(input("What do you want to do:\n\t1.Add an existing account.\n\t2.Create a new account.\n\t3.Delete an account.\n\t4.View your accounts.\n>>> "))
    print(x)
    if x == 1:
        add()
    elif x == 2:
        create()
    elif x == 3:
        delete()
    elif x == 4:
        view()
        choose("")
    else:
        choose("Invalid!")
        
def add():
    acc = input("Enter the name of account. (eg facebook,twitter)\n>>> ")
    username = input("Enter username for the account.\n>>> ")
    password = input("Enter password for the account.\n>>> ")
    crd = credentials(acc,username,password)
    crd.save()
    choose("")
    
def create():
    acc = input("Enter name of account(e.g,facebook,twitter,etc.\n>>> ")
    usr = input("Enter username for account.\n>>> ")
    opt = input("Do you want a generated password?(yes,no)")
    if opt=="yes" or opt == "no":
        if opt == "yes":
            length = int(input("How long do you want your password?"))
            pas = gen(length)
            print("Your password is: ",pas)
        else:
            pas = input("Enter password.\n>>> ")
    else:
        print("Invalid!")
        create()
    
    acc_data = credentials(acc,usr,pas)
    acc_data.save()
    choose("")
def make_arr():
    f = open("acc.txt","r")
    arr = []
    small = []
    x = f.readlines()
    i = 0
    while i<len(x):
        small.append(x[i])
        small.append(x[i+1])
        small.append(x[i+2])
        arr.append(small)
        small = []
        i += 3
    f.close()
    return arr
def view():
    #f = open("acc.txt","r")
    arr = make_arr()
    j = 0
    for a in arr:
        print(j+1,":")
        print("\tAccount:",a[0],"\tUsername:",a[1],"\tPassword:",a[2])
        j += 1
    #choose("")
    
def delete():
    print("Enter number of record you want to delete")
    view()
    no = int(input(">>> "))
    arr = make_arr()
    if no<=len(arr):
        print(arr[0])
        f = open("acc.txt","w")
        arr[no-1] = ""
        arr.remove("")
        for a in arr:
            for i in a:
                file.write(i)
        f.close()


if __name__ == "__main__":
	main()
