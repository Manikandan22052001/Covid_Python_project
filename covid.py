import random
import mysql.connector

print("--------------------------------------------------\n")
print("*********** COVID-19 MANAGEMENT SYSTEM ***********\n")
print("--------------------------------------------------\n")

def mydb():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "money"
    )
    mycursor = mydb.cursor()
    mycursor.execute("select * from stud")


class covid():
    
    def __init__(self,Name,age,dies):
        self.user_name = Name
        self.age = age
        self.dies = dies
    # covid=covid()

def loging():

    print("1. SIGN UP\n2. SIGN IN")

    user = int(input("\n Enter your choice:"))

    if user == 1:
        print("\n WELCOME TO SIGNUP PAGE\n")
        print("Please Enter your singup details\n")

        user_name = input("Enter your Name:")
        user_phone_number = int(input("\n Enter your phone number: "))
        user_mail = input("\n Enter your Valuale Mail ID:")
        user_password = input("\n Enter your password:")
        

        print(f"{user_name}, your are successfully singup \n")
        print(f"CHECK OUT YOUR INFORMATION,\nYour Name is = {user_name},\n Your phone number= {user_phone_number},\n Your mailID = {user_mail}")

        ask = input("\nDo you want to continue(YES/No):").lower()

        if ask == "yes":
            main_function()
        else:
            print("Thank to come.... ALL THE BEST FOR YOUR HEALTH")
                
    elif user == 2:
        print("\n WELCOME TO SIGNIN PAGE\n")
        print("Please Enter your singin details\n")

        user_name = input("Enter your username/mailid:").upper()
        user_password = input("\nEnter your password:")

        print(f"\n{user_name},You are successfully signin this page.")
        
        ask = input("\nDo you want to continue(YES/No):").lower()

        if ask == "yes":
            main_function()
        else:
            print("Thank to come.... ALL THE BEST FOR YOUR HEALTH")

def hos_detail():

    print("1. Government\n2. private")

    hos_name = int(input("Enter your choice:")) 

    if hos_name == 1:
        
        bed = random.randint(0,6)

        print(f"\n Avialble Bed in government hospital = {bed}")

        ask = input("\nDo you want to continue(YES/No):").lower()

        if ask == "yes":
            main_function()
        else:
            print("Thank to come.... ALL THE BEST FOR YOUR HEALTH")
    
    elif hos_name == 2:
        
        bed = random.randint(0,6)
        print(f"\n private Bed in government hospital = {bed}")

        ask = input("\nDo you want to continue(YES/No):").lower()

        if ask == "yes":
            main_function()
        else:
            print("Thank to come.... ALL THE BEST FOR YOUR HEALTH")

def reservation():

    aviable_bed = [1,2,3,4,5,6]

    res_bed = int ( input("\n How many Bed are want:"))

    if res_bed in aviable_bed:

        print(f"\nyes!...{res_bed} Bed is available")
        booking_bed = input("\n Booking or Not (Yes/No):").lower()
        if  booking_bed == "yes":
            print(f"\nYes....your Bed is booked.")
            ask = input("\nDo you want to continue(YES/No):").lower()

            if ask == "yes":
                main_function()
            else:
                print("Thank to come.... ALL THE BEST FOR YOUR HEALTH")

    else:
        print(f"\n Not avaible your wanted bed in our hospital.")
        ask = input("\nDo you want to continue(YES/No):").lower()
        if ask == "yes":
            main_function()
        else:
            print("Thank to come.... ALL THE BEST FOR YOUR HEALTH")

def main_function():

    print("\n1. LOGIN & SINGUP\n2. HOSPITAL DETAILS\n3. RESERVATION\n4. EXIT")
    user = int(input("Enter your choice:"))
    if user ==1:
        loging()
    elif user ==2:
        hos_detail()
    elif user == 3:
        reservation()
    elif user == 4:
        input(exit)
    else:
        print("\n ******* Please choose your right choice *******")

main_function()




