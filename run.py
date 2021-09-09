#!/usr/bin/env python3.6

import random
import json


print("welcome to password manager,\n\tplease login..")

class credentials:
    '''
    These class accepts account name,username, password.
    It stores them as a dictionary.

    '''
    def __init__(self,account,username,password,usr):
        self.account = account
        self.username = username
        self.password = password
        self.usr = usr
    
    def save(self):
        f=open(self.usr+".text","a")
        f.write(self.account+ "\n")
        f.write(self.username + "\n")
        f.write(self.password + "\n")
        f.close()

class user:
    '''
    These class holds information about the user

    '''
    def __init__(self,data,usr):
        self.data=data
        self.usr = usr

    def password(self):
        return self.data[self.usr]

def create_acc():
    usr = input("Username>>> ")
    pas = input("password>>> ")
    data = {}
    file = open("locker.json","r")
    data = json.load(file)
    file.close()
    file = open("locker.json","w")
    data[usr] = pas
    json.dump(data,file)
    file.close()
    global usrname
    usrname = usr
    return usr

def login(a):
    '''
    These is the login function that verifies each and every user

    '''
    if a!= "":
        print(a)
    username = input("username>>> ")
    password = input("password>>> ")
    global usrname
    usrname = username
    with open("locker.json","r") as f:
        data = json.load(f)
    user_data = user(data,username)
    if password == user_data.password():
        print("Login successful.\n\tWelcome..")
    else:
        print("Incorrect password")
        login("please try again")

def gen(x):
    chars = "qwrftyuipokjnh768905432werfdxcvbhuijk"
    pas = ""
    for i in range(x):
        pas += chars[random.randint(0,36)]
    return pas


def main():
    '''
    These is the main function of the application

    '''
    choice = input("Select:\n1: create\n2: login")
    if choice == "1":
        create_acc()
        choose("",usrname)
    elif choice == "2":
        login("")
        choose("",usrname)




def choose(a,usr):
    '''
    These function allows the user choose from available option

    '''

    if a!= "":
        print(a)
    x = int(input("What do you want to do:\n\t1. Add an existing account. \n\t2. Create a new account.\n\t3. Delete an account.\n\42.View your accounts.\n>>> "))
    print(x)
    if x == 1:
        add(usr)
    elif x == 2:
        create(usr)
    elif x == 3:
        delete(usr)
    elif x == 4:
        view(usr)
        choose("",usrname)
    else:
        choose("Invalid",usrname)

def add(usr):
    account = input("Enter the name of the account.(ie, Facebook,twitter,email)\n>>")
    username =input("Enter your username.\n>>")
    password = input("Enter your password.\n>>")
    details = credentials(account,username,password,usr)
    details.save()
    choose("",usrname)

def create(usr):
    account = input("Enter the name of the account(ie,facebook,twitter,email.\n>>>)")
    username =input("Enter your username.\n>>>")
    password = input("Do you want to create a password?(yes, no)  ")
    if password == "yes" or password == "no":
        if password =="yes":
            length = int(input("How long do you want your password  "))
            pas = gen(length)
            print("Your password is:",pas)

        else:
            pas = input("Enter password.\n>>>")

    else:
        print("Invalid")
        create()

    account_data = credentials(account,username,pas,usr)
    account_data.save()
    choose("",usrname)

def make_arr(usr):
    f = open(usr+".text", "r")
    arr = []
    small = []
    x = f.readlines()
    i = 0
    while i <len(x):
        small.append(x[i])
        small.append(x[i+1])
        small.append(x[i+2])
        arr.append(small)
        small = []
        i += 3
        f.close()
        return arr

def view(usr):
	
    arr = make_arr(usr)
    j = 0
    if len(arr) == 0:
        print("No entries")
        return
    for a in arr:
        print(j+1,":")
        print("\tAccount:", a[0],"\tUsername:",a[1],"\tPassword:",a[2])
        j+= 1

def delete(usr):
    print("Enter number of the record you want to delete")
    view(usrname)
    no = int(input(">>>"))
    arr = make_arr(usrname)
    if no <= len(arr):
        f = open(usr+".txt","w")
        arr[no-1] = ""
        arr.remove("")
        print(arr)
        for a in arr:
            for i in a:
                f.write(i)
        f.close()
    choose("",usrname)

if __name__ == '__main__':
    main()






    
            








    
