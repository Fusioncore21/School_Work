# Get Module(s)
import csv
Data = list(csv.reader(open("Data_Store.csv","r"))) # Get Stored Data

CurrentUsers = list()
for Position in range(1,len(Data)):
    CurrentUser = []
    for Header,Value in enumerate(Data[Position]):
        #print(f"{Data[0][Header]}: {Value}")
        CurrentUser.append(Value)
    #print("\n")
    CurrentUsers.append(CurrentUser)

def Get_Input(Query,Range):
    """Gets a user input, regardless of how fucking stupid they are\nQuery - The question\nRange - How far would you like the range of values to be?"""
    while True:
        try:
            Attempted_Input = int(input(Query))
            if Attempted_Input in range(1,Range+1):
                return Attempted_Input
            else:
                raise ValueError
        except ValueError:
            print("That is not an option!")

def GUI():
    print("Welcome to the Rock Climbing Club! How many I help you today?\n1 - Enter Club\n2 - Join Club\n3 - Admin")
    Get_Input("What is your choice?: ",3)
GUI()