# File name: shopSystem.py
# Aim: Create a basic computer shop system that estimates the cost of items and does some other cool stuff, I guess.
import csv
import time
from BuySys import BuySystemV1

def StockRefresh():
    """Refreshes the stock levels of all items available. No arguments."""
    with open("shopStock.csv",newline='') as Stock:
        Stock_List = list(csv.reader(Stock))
        Stock.close
        for item in Stock_List:
            try:
                while True:
                    item.remove('')
            except ValueError:
                continue
    # Converting List into a Dict
    StockLibrary = []
    for Component in Stock_List:
        TempDict = {}
        for item in Component:
            split = item.split(" : ")
            TempDict[split[0]] = int(split[1])
        StockLibrary.append(TempDict)
    return StockLibrary

StockLibrary = StockRefresh() # This is run to make sure any functions or modules always have an inital Stock level to go off of.

def StockUpdate(list,SaveOnly=False):
    """Updates the stock of items. Requires a list of items to update to subtract from each component by 1. It also saves back to the main file. """
    if list: # Checks to see if list has items. [] = false, while [1,2] = true!
        if not SaveOnly:
            for component in StockLibrary:
                for item in list:
                    if component.get(item):
                        component.update({item:component.get(item)-1})
                    
        # Saving to CSV file.           
        with open("shopStock.csv","w+",newline='') as document:
            Writer = csv.writer(document,delimiter=',')
            for part in StockLibrary:
                listAp = []
                for key in part.keys():
                    line = "{} : {}".format(key,part[key])
                    listAp.append(line)
                Writer.writerow(listAp)
            document.close()
    else:
        print("[STOCK MODULE ERROR] No items listed to update!")

# StockUpdate([{'p3': 4, 'p5': 8, 'p7': 4}, {'16GB': 10, '32GB': 7}, {'1TB': 9, '2TB': 12}, {'16 Inch': 6, '23 Inch': 9}, {'Mini': 17, 'Midi': 12}, {'2P': 23, '4P': 18}],SaveOnly=True)

# This library is the pricing list for all items
ItemLibrary = [{"p3-3410i":100,"p5-3420i":120,"p7-3430i":200}, # Processors
    {"16 GB":75,"32 GB":150},                # RAM
    {"1 TB":50,"2 TB": 100},                 # Storage
    {"19 Inch":65,"23 Inch":120},            # Screen
    {"Mini Tower":40,"Midi Tower":70},       # Case
    {"2 Ports":10,"4 Ports":20}              # USB Ports
]

def shopUI():
    """Its the shop UI, duh. It ain't pretty, but it does the job!"""
    #Stock = StockRefresh()
    print("[COMPUTER SHOP]\nWelcome To My Computer Store! Please select one of the options below:\n1 - Buying a PC\n2 - Current Stock\n3 - Admin Console")
    def BuyPC(): # Buying PC
        final_cost,User_Components = BuySystemV1(StockRefresh())
        print(final_cost,User_Components)
        
    def ShowStock():# Show current stock
        ComponentType = ["Processor","RAM Size","Storage","Screen Size","Case Size","USB Ports"]
        for i in range(len(ComponentType)-1):
            print("\n"+ComponentType[i])
            for Name,Amount in zip(StockRefresh()[i].keys(),StockRefresh()[i].values()):
                print(f"{Name}: {Amount} in storage.")

    def AdminPanel(): # Admin panel: Add stock, check recent orders and so on
        if input("\nAccess Denied! Please Enter Password: ") == "ComputerMan69": 
            def AddStock():
                pass
            def Recent_Orders():
                with open("Orders.csv",newline="") as file:
                    Orders = csv.reader(file)
                    print(Orders)

            Internal_Switch = {1:AddStock,2:Recent_Orders}
            print("Access Authorised! Current Admin Commands:\n1 - Add Stock\n2 - Recent Orders\n")
            while True:
                try:
                    userSelection = int(input("Make your pick: "))
                    Internal_Switch[userSelection]()
                    break
                except (KeyError,ValueError):
                    print("That is not a category, pick again!\n")

    Switch_Case = {1:BuyPC,2:ShowStock,3:AdminPanel}
    while True:
        try:
            userSelection = int(input("Make your pick: "))
            Switch_Case[int(userSelection)]()
            break
        except (KeyError,ValueError):
            print("That is not a category, pick again!\n")
while True:
    shopUI()