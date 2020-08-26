# Some Things we'll need
#StockLibrary = [{'p3': 4, 'p5': 0, 'p7': 0}, {'16GB': 0, '32GB': 7}, {'1TB': 9, '2TB': 12}, {'16 Inch': 6, '23 Inch': 9}, {'Mini': 17, 'Midi': 12}, {'2P': 23, '4P': 18}]

ItemLibrary = [{"p3-3410i":100,"p5-3420i":120,"p7-3430i":200}, # Processors
    {"16 GB":75,"32 GB":150},                # RAM
    {"1 TB":50,"2 TB": 100},                 # Storage
    {"19 Inch":65,"23 Inch":120},            # Screen
    {"Mini Tower":40,"Midi Tower":70},       # Case
    {"2 Ports":10,"4 Ports":20}              # USB Ports
]
ComponentType = ["Processor","RAM Size","Storage Option","Screen Size","Case Size","USB Port Amount"]

def BuySystemV1(StockLibrary): # This doesn't really work yet but whatever
    """Standard buy screen. Requires a list of stock."""
    print("\nWelcome to the PC building screen!\nLets begin by selecting the component you'd like from the list below:")
    SelectedComponents = []

    for Type in range(6):
        print(f"COMPONENT: {ComponentType[Type]}")
        ItemKeys = ItemLibrary[Type].keys()
        StockKeys = StockLibrary[Type].keys()
        Numb_Items = 1
        Available_Items = []

        for ItemKey,StockKey in zip(ItemKeys,StockKeys):
            Availability = "" 
            if not StockLibrary[Type][StockKey]:
                Availability = "[NOT IN STOCK]"
                Available_Items.append(None)
            else:
                Available_Items.append(ItemLibrary[Type][ItemKey])
            print(f"{Numb_Items}: {ItemKey} -> ${ItemLibrary[Type][ItemKey]} {Availability}")
            Numb_Items += 1

        while True:
            try:
                ItemSelection = int(input("\nPlease make your selection.\nINPUT: "))
                if (ItemSelection > 0 and ItemSelection <= len(ItemKeys)) and Available_Items[ItemSelection-1] is not None:
                    SelectedComponents.append(([q for q in StockKeys][ItemSelection-1])) # Do something to do with tables [q for q in StockKeys]
                    break
                else:
                    raise ValueError
            except (ValueError,IndexError):
                print("[ERROR] That is not a selection!")
    print(SelectedComponents)

    # Final Pricing and stuff
    print("Total Cost:\n[COMPONENT]{}[COST]".format("-"*11))
    finalcost = 0
    for i in enumerate(ItemLibrary):
        cost = i[1][SelectedComponents[i[0]]] # Looks complex, but it just accesses the tuple and stuff
        print(SelectedComponents[i[0]]," "*(20-len(SelectedComponents[i[0]])),f" ${cost}")
        finalcost+=cost
    finalcost *= 1.2 # VAT
    visual_Cost = finalcost

    if finalcost.is_integer():
        visual_Cost = str(int(visual_Cost))
        visual_Cost+=".00"
    else:
        visual_Cost = str(visual_Cost)
        visual_Cost+="0"
        
    print(" "*8,f"GRAND TOTAL:  ${visual_Cost} (with 20% VAT)")
    
    return finalcost,SelectedComponents