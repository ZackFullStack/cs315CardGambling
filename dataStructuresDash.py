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


def startRun ():

def openCollection ():
    
def historyMenu ():
    
def setOdds ():
    
def setNewHighScore ():
    

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

