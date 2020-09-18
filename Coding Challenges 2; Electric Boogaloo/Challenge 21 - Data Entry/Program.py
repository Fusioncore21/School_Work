# Get Module(s)
import csv

with open("Data_Store.csv","r") as Data: # Getting Stored Data
    Data = list(csv.reader(Data))

CurrentUsers = list()
for Position in range(1,len(Data)):
    CurrentUser = []
    for Header,Value in enumerate(Data[Position]):
        print(f"{Data[0][Header]}: {Value}")
        CurrentUser.append(Value)
    print("\n")
    CurrentUsers.append(CurrentUser)

class Users:
    def __init__(self,ID,Name,Proficiency,PMember,Time):
        self.ID = ID
        self.Name = Name
        self.Proficiency = Proficiency
        self.PMember = PMember
        self.Time = Time
    def Print_Info(self):
        print(f"User ID: {self.ID}\nName: {self.Name}\nProficency level: {self.Proficiency}\nPayed Membership:{self.PMember}/nTime at club:{self.Time}")

for User in CurrentUsers:
    User = Users(User[0],User[1],User[2],User[3],User[4])

print(CurrentUsers)