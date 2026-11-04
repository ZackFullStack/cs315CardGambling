#Data Structures Dash
#Zackary Audis, Bella Mantini, Dymetrius
#CESC 315 Project
#Ver. 1.0
#Resources:

import random
from collections import deque 

user = {
    "username": "",
    "balance": 0.00,
    "best_run": 0.00,
    "best_card": "",
    "collection": [],
    "run_history": []
}


userRuns = [
    
    ]
DRAW_COUNT_WEIGHTS = [1, 2, 3]
DRAW_COUNT_PROBS = [0.950, 0.045, 0.005]




def printMenu () :
    print("Welcome to Data Structure Dash!\n")
    print("---------------------------------\n")
    print("Press 's' to start a run\n")
    print("Press 'c' to view your collection")
    print("Press 'h' to view your run history and stats\n")

def setProbs ():
    packs = [
  packs = [
        {
            "PackName": "Bubble Sort",
            "Cost": 1.00,
            "CardValueRange": (0.25, 30.00),
            "PotentialRarities": ["Common", "Uncommon", "Rare", "Super Rare"]
            "PotentialRarities": ["Common", "Uncommon", "Rare", "Super Rare"],
            "cardIndexRange": (1, 250)
        },
        {
            "PackName": "Selection Sort",
            "Cost": 5.00,
            "CardValueRange": (1.50, 75.00),
            "PotentialRarities": ["Common", "Uncommon", "Rare", "Super Rare", "Mega Rare"]
            "PotentialRarities": ["Common", "Uncommon", "Rare", "Super Rare", "Mega Rare"],
            "cardIndexRange": (251, 500)
        },
        {
            "PackName": "Insertion Sort",
            "Cost": 25.00,
            "CardValueRange": (10.00, 600.00),
            "PotentialRarities": ["Uncommon", "Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical"]
            "PotentialRarities": ["Uncommon", "Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical"],
            "cardIndexRange": (501, 750)
        },
        {
            "PackName": "Quick Sort",
            "Cost": 50.00,
            "CardValueRange": (20.00, 1500.00),
            "PotentialRarities": ["Uncommon", "Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical"]
            "PotentialRarities": ["Uncommon", "Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical"],
            "cardIndexRange": (751, 1000)
        },
        {
            "PackName": "Merge Sort",
            "Cost": 100.00,
            "CardValueRange": (40.00, 4000.00),
            "PotentialRarities": ["Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical", "Divine"]
            "PotentialRarities": ["Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical", "Divine"],
            "cardIndexRange": (1001, 1250)
        },
        {
            "PackName": "Heap Sort",
            "Cost": 500.00,
            "CardValueRange": (90.00, 10000.00),
            "PotentialRarities": ["Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical", "Divine"]
            "PotentialRarities": ["Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical", "Divine"],
            "cardIndexRange": (1251, 1500)
        },
        {
            "PackName": "King Sort",
            "Cost": 1000.00,
            "CardValueRange": (250.00, 50000.00),
            "PotentialRarities": ["Super Rare", "Mega Rare", "Legendary", "Mythical", "Divine", "Transcendent"]
            "PotentialRarities": ["Super Rare", "Mega Rare", "Legendary", "Mythical", "Divine", "Transcendent"],
            "cardIndexRange": (1501, 1750)
        },
        {
            "PackName": "God Sort",
            "Cost": 2500.00,
            "CardValueRange": (850.00, 100000.00),
            "PotentialRarities": ["Mega Rare", "Legendary", "Mythical", "Divine", "Transcendent"]
            "PotentialRarities": ["Mega Rare", "Legendary", "Mythical", "Divine", "Transcendent"],
            "cardIndexRange": (1751, 2000)
        }
    ]
    ] 
    
    for pack in packs:
        








        ]
def openPackShop (userDeposit):
    packsAmount = 0
    purchasedPacks = []
    
    while userDeposit >= packs[0]["Cost"]:
        print(f"\nCurrent Balance: ${userDeposit:.2f}")
        print("Select a pack to buy:")
        print("-------------------------------------------")
        print("[1] Bubble Sort Pack    - $1.00     ($0.25 - $30)")
        print("[2] Selection Sort Pack - $5.00     ($1.50 - $75)")
        print("[3] Insertion Sort Pack - $25.00    ($10 - $600)")
        print("[4] Quick Sort Pack     - $50.00    ($20 - $1,500)")
        print("[5] Merge Sort Pack     - $100.00   ($40 - $4,000)")
        print("[6] Heap Sort Pack      - $500.00   ($90 - $10,000)")
        print("[7] King Sort Pack      - $1,000.00 ($250 - $50,000)")
        print("[8] God Sort Pack       - $2,500.00 ($850 - $100,000)")
        print("[q] Exit shop / Quit Run")
        print("-------------------------------------------")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == "q":
            print("Exiting shop...")
            break
        elif choice.isdigit() and 1 <= int(choice) <= 8:
            selected_pack = packs[int(choice) - 1]
            if userDeposit >= selected_pack["Cost"]:
                userDeposit -= selected_pack["Cost"]
                packsAmount += 1
                purchasedPacks.append(selected_pack)
                print(f"Bought {selected_pack['PackName']} Pack! Remaining: ${userDeposit:,.2f}")
            else:
                print(f"Insufficient funds! {selected_pack['PackName']} costs ${selected_pack['Cost']:,.2f}, but you only have ${userDeposit:,.2f}.")
        else:
            print("Invalid choice! Enter 1-8 or 'q'.")
            
            
def startRun ():
    
    userDeposit = input(int("Run Started! Enter the amount you would like to deposit (the amount must end with a 0 or 5):\n"))
    if userDeposit % 5 == 0:
        user["Balance"] += userDeposit
        print(f"Excellent! You will start this run with ${userDeposit}. It is time to purchase your packs:\n")
        openPackShop(userDeposit)
        
    else:
        print("Error, please enter a whole number amount ending in 5 or 0:\n")
    
def openCollection ():

def historyMenu ():
    print(f"Username: {user["username"]}\n")
    print(f"Current Balance: ${user["balance"],.2f}\n")
    print(f"Best Run: ${user["best_run"],.2f}\n")
    print(f"Best Card: {user["best_card"]}\n"")

def setNewHighScore (userScore):
    if (userScore > user["best_run"]):
        user["best_run"] = userScore
        

def userPackChoice (cardsArr):
    for i in range(1, len(cardsArr):
        if cardsArr[i]["PackName"] == "Bubble Sort":
            setProbs("Bubble-Sort")
        elif cardsArr[i]["PackName"] == "Selection Sort":
            setProbs("Selection-Sort")
        elif cardsArr[i]["PackName"] == "Insertion Sort":
            setProbs("Insertion-Sort")
        elif cardsArr[i]["PackName"] == "Quick Sort":
            setProbs("Quick-Sort")
        elif cardsArr[i]["PackName"] == "Merge Sort":
            setProbs("Merge-Sort")
        elif cardsArr[i]["PackName"] == "Heap Sort":
            setProbs("Heap-Sort")
        elif cardsArr[i]["PackName"] == "King Sort":
            setProbs("King-Sort")
        elif cardsArr[i]["PackName"] == "God Sort":
            setProbs("God-Sort")
        else:
            print("Error Setting Card Odds\n")
            return -1



def openCollection():
    print("Your Current Collection:\n") 
    userSortChoice = input("Press h to sort cards from highest to lowest value, press l to sort from lowest to highest:\n")
    
    if userSortChoice == "h" or "H":
        #Sorted Array High to low
    elif userSortChoice == "l" or "L"
    

def selectionMenu (userSelection):
    if userSelection.lower == "s":
        startRun()
    elif userSelection.lower == "c":
        openCollection()
    elif userSelection.lower == "h":
        historyMenu()



def readCards ():
    with open ('cards.pdf', 'r') as file:
        for file in file:

}
