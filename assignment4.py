#task 4
#otp generating

import random
name="premaram"
pswd="prem1234"

def login():
    n=input("Enter username :")
    p=input("Enter password :")
    if n==name and p==pswd:
        print("Login Successfully!")
    else:
        print("Login failed. Choose an option")
        print("1. Try Again")
        print("2. Generate otp")

        a=input("Enter your choice")

        if a=="1":
            login()
        elif a=="2":
            otp()
        else:
            print("Invalid choice!")

def otp():
    otp=str(random.randint(1000,9999))
    print("Generated Otp :",otp)

    while True:
        o1=input("Enter the otp :")
        if o1==otp:
            print("Username :",name)
            print("Password :",pswd)
            break
        else:
            print("OTP is incorrect.")
            print("if you want to regenerate OTP then press 1")
            print("or if you want to exit then press 2")
            a1=input("Enter your choice :")
            if a1=="1":
                otp=str(random.randint(1000,9999))
                print("Generated OTP :", otp)
            else:
                print("Exiting")
                break
login()