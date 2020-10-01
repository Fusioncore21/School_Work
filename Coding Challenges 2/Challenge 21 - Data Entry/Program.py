# Get Module(s)
import csv
from time import sleep
import Custom_Tools as CT # Custom module that I made to store frequently used functions
Data = list(csv.reader(open("Data_Store.csv","r"))) # Get Stored Data

CurrentUsers = list()
for Position in range(1,len(Data)):
    CurrentUser = []
    for Header,Value in enumerate(Data[Position]):
        #print(f"{Data[0][Header]}: {Value}")
        CurrentUser.append(Value)
    #print("\n")
    CurrentUsers.append(CurrentUser)
print(CurrentUsers)

def UI():
    print("Welcome to the Rock Climbing Club! How many I help you today?\n1 - Enter Club\n2 - Join Club\n3 - Admin")
    def enter_club():
        name = input("What is your username?: ")
        for n in range(1,len(Data)):
            if name in Data[n]:
                print(f"Welcome to the club, {name.capitalize()}!")
                break
            else:
                print("Sorry, you're not on our list!\n")
                sleep(2)
                UI()
        print("I am now here")
    def join_club():
        print("I see you would like to join us!\nPlease fill out these questions:")
        Name = input("What is your name?: ")
        Prof = input("How would you rate your proficiency?: ")
        Time = input("How long have you been rock climbing for? (Hours): ")
        csv.writer(open("Data_Store.csv","a+",newline='')).writerow([len(CurrentUsers)+1,Name,Prof,False,Time])
        print("Adding to database...")
        sleep(1)
        print("\nThank you for filling out our form! You need to pay your membership first, which will be asked for when you enter the club! Thank you for joining!")
    def admin_control():
        print("Admin control")
    Switch = {1:enter_club,2:join_club,3:admin_control}
    Switch[CT.Get_Int_Inputv2("What is your choice?: ",3)]()
UI()