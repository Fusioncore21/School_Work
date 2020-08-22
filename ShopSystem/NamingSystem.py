from string import ascii_uppercase as upper
upper = [a for a in upper]

def Convert_Numb_To_Ref(Order_Number):
    """Takes an Order_Number (int), and converts it into a unique Order_ID"""
    Number = str((Order_Number%9999)+1) # Makes it so it never is bigger than 4 digits
    Number = ("0"*(4-len(str(Number))))+Number # If number < 1000, adds on 0s to the beginning, so 1 -> 0001
    try:
        Letter = upper[Order_Number//9999] # Divides and floors
    except IndexError:
        print("Number too large! Cannot generate Product_ID")
        return False
    return f"#{Letter}{Number}"
while True:
    Product_UD = Convert_Numb_To_Ref(int(input("Number please: ")))
    print(Product_UD)