ItemLibrary = [{"p3":100,"p5":120,"p7":200}, # Processors
    {"16 GB":75,"32 GB":150},                # RAM
    {"1 TB":50,"2 TB": 100},                 # Storage
    {"19 Inch":65,"23 Inch":120},            # Screen
    {"Mini Tower":40,"Midi Tower":70},       # Case
    {"2 Ports":10,"4 Ports":20}              # USB Ports
]
UserSelection = ["p5","16 GB","2 TB","19 Inch","Midi Tower","4 Ports"]

print("Total Cost:\n[COMPONENT]{}[COST]".format("-"*11))
finalcost = 0
for i in enumerate(ItemLibrary):
    cost = i[1][UserSelection[i[0]]] # Looks complex, but it just accesses the tuple and stuff
    print(UserSelection[i[0]]," "*(20-len(UserSelection[i[0]])),f" ${cost}")
    finalcost+=cost
print(" "*8,f"GRAND TOTAL:  ${finalcost}")