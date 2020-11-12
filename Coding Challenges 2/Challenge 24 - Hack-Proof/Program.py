`# See CHALLENGE.md for more information
import Custom_Tools as CT
import random
import time
import csv
import string

User_Data = list(csv.reader(open("Auth_Usrs.csv","r")))
print(len(User_Data))
def UI():
    """My UI's are supreme!"""
    print("Hello. Please make a selection below. Be quick before I get impatient\n- Security Guard\n1 - Login\n2 - Create Secure Login")
    def Login():
        if len(User_Data)<1: print("Huh, seems like there is no one in the system yet. Now SCRAM.")
        else:
            print("You want to come in here?")
            Name = input("Give me your name, now: ")
            Passcode = input("And what about your passcode?: ")
            for index in range(1,len(User_Data)):
                if Name and Passcode in User_Data[index]:
                    print("Hello There. I shall now fetch the data you want.\nFetching...")
                    time.sleep(5)
                    print(open("Secret_Document.txt").read())
                    break
    def Create_Login():
        print("\nHmm, alright then. I'll help you make a login here.")
        User_Name = input("Alright, what do you want your username to be?: ")
        Generated_Password=""
        for _ in range(1,20):
            randint = random.randint(55,99)
            Generated_Password+=chr(randint)

        print(f"As I am a man of security, I'll generate a secure password for you.\nHow does {Generated_Password} sound?\n")
        def Final_Step():
            print("Alright then, I'll finish up your registration...")
            csv.writer(open("Auth_Usrs.csv","a")).writerow([len(User_Data)+1,User_Name,Generated_Password])
            print("Done! Now get outta here!")

        def User_Password():
            print("Oh look at you, all strong and like. You want to write your own password? Here are a few rules.\n[RULES]\n1. Password must be longer than 8 characters.\n2. Password must contain 1 uppercase letter and 1 symbol.\n3. Must not be explicit.")
            while True:
                attempted_password = input("Tell me a password: ")
                if len(attempted_password)<8:
                    print("This is not long enough!")
                else:
                    Symbol = [[symbol for symbol in attempted_password if symbol in string.punctuation],[letter for letter in attempted_password if letter in string.ascii_uppercase]]
                    if len(Symbol[0])>=1 and len(Symbol[1])>=1:
                        print("Password accepted. Hold on while I write this down...\n")
                        break
            csv.writer(open("Auth_Usrs.csv","a")).writerow([len(User_Data)+1,User_Name,attempted_password])
            print("Done! Now scram!")
        ChoiceSwitch = {1:Final_Step,2:User_Password}
        print("1 - Continue with generated password\n2 - Write own password")
        ChoiceSwitch[CT.Get_Int_Inputv2("Tell me your choice: ",2)]()

    Switch_Case = {1:Login,2:Create_Login}
    Switch_Case[CT.Get_Int_Inputv2("Enter Selection: ",2)]()
while __name__ == "__main__":
    UI()