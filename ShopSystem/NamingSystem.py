from string import ascii_uppercase as upper
upper = [a for a in upper]

def Convert_Numb_To_Ref(Numb):
    Letter_2 = upper[Numb//9999]
    Counter = 0
    if Letter_2=="F":
        Counter += 1
    Letter_1 = upper[Counter]
    print(f"#{Letter_1}{Letter_2}")
while True:
    a = int(input("Input: "))
    Convert_Numb_To_Ref(a)