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
        {
            "PackName": "Bubble Sort",
            "Cost": 1.00,
            "CardValueRange": (0.25, 30.00),
            "PotentialRarities": ["Common", "Uncommon", "Rare", "Super Rare"]
        },
        {
            "PackName": "Selection Sort",
            "Cost": 5.00,
            "CardValueRange": (1.50, 75.00),
            "PotentialRarities": ["Common", "Uncommon", "Rare", "Super Rare", "Mega Rare"]
        },
        {
            "PackName": "Insertion Sort",
            "Cost": 25.00,
            "CardValueRange": (10.00, 600.00),
            "PotentialRarities": ["Uncommon", "Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical"]
        },
        {
            "PackName": "Quick Sort",
            "Cost": 50.00,
            "CardValueRange": (20.00, 1500.00),
            "PotentialRarities": ["Uncommon", "Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical"]
        },
        {
            "PackName": "Merge Sort",
            "Cost": 100.00,
            "CardValueRange": (40.00, 4000.00),
            "PotentialRarities": ["Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical", "Divine"]
        },
        {
            "PackName": "Heap Sort",
            "Cost": 500.00,
            "CardValueRange": (90.00, 10000.00),
            "PotentialRarities": ["Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical", "Divine"]
        },
        {
            "PackName": "King Sort",
            "Cost": 1000.00,
            "CardValueRange": (250.00, 50000.00),
            "PotentialRarities": ["Super Rare", "Mega Rare", "Legendary", "Mythical", "Divine", "Transcendent"]
        },
        {
            "PackName": "God Sort",
            "Cost": 2500.00,
            "CardValueRange": (850.00, 100000.00),
            "PotentialRarities": ["Mega Rare", "Legendary", "Mythical", "Divine", "Transcendent"]
        }
    ]
    
        
        
        
        
        
        
        
        ]
def startRun ():

def openCollection ():
    
def historyMenu ():
    
def setNewHighScore ():
    
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
