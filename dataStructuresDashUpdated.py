#Data Structures Dash
#Zackary Audis, Bella Mantini, Dymetrius
#CESC 315 Project
#Ver. 1.0
#Resources:

import random
import re
from collections import deque 

user = {
    "username": "",
    "balance": 0.00,
    "best_run": 0.00,
    "best_card": {"value": 0.00},
    "collection": [],
    "run_history": []
}

userRuns = []
DRAW_COUNT_WEIGHTS = [1, 2, 3]
DRAW_COUNT_PROBS = [0.950, 0.045, 0.005]

packs = [
    {
        "PackName": "Bubble Sort",
        "Cost": 1.00,
        "CardValueRange": (0.25, 30.00),
        "PotentialRarities": ["Common", "Uncommon", "Rare", "Super Rare"],
        "cardIndexRange": (1, 250),
        "Odds": {"Common": 0.965225, "Uncommon": 0.033567, "Rare": 0.001167, "Super Rare": 0.000041}
    },
    {
        "PackName": "Selection Sort",
        "Cost": 5.00,
        "CardValueRange": (1.50, 75.00),
        "PotentialRarities": ["Common", "Uncommon", "Rare", "Super Rare", "Mega Rare"],
        "cardIndexRange": (251, 500),
        "Odds": {"Common": 0.843986, "Uncommon": 0.131740, "Rare": 0.020564, "Super Rare": 0.003210, "Mega Rare": 0.000501}
    },
    {
        "PackName": "Insertion Sort",
        "Cost": 25.00,
        "CardValueRange": (10.00, 600.00),
        "PotentialRarities": ["Uncommon", "Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical"],
        "cardIndexRange": (501, 750),
        "Odds": {"Uncommon": 0.950236, "Rare": 0.047288, "Super Rare": 0.002353, "Mega Rare": 0.000117, "Legendary": 0.000006, "Mythical": 0.0000003}
    },
    {
        "PackName": "Quick Sort",
        "Cost": 50.00,
        "CardValueRange": (20.00, 1500.00),
        "PotentialRarities": ["Uncommon", "Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical"],
        "cardIndexRange": (751, 1000),
        "Odds": {"Uncommon": 0.797951, "Rare": 0.161268, "Super Rare": 0.032593, "Mega Rare": 0.006587, "Legendary": 0.001331, "Mythical": 0.000269}
    },
    {
        "PackName": "Merge Sort",
        "Cost": 100.00,
        "CardValueRange": (40.00, 4000.00),
        "PotentialRarities": ["Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical", "Divine"],
        "cardIndexRange": (1001, 1250),
        "Odds": {"Rare": 0.910210, "Super Rare": 0.081728, "Mega Rare": 0.007338, "Legendary": 0.000659, "Mythical": 0.000059, "Divine": 0.000005}
    },
    {
        "PackName": "Heap Sort",
        "Cost": 500.00,
        "CardValueRange": (90.00, 10000.00),
        "PotentialRarities": ["Rare", "Super Rare", "Mega Rare", "Legendary", "Mythical", "Divine"],
        "cardIndexRange": (1251, 1500),
        "Odds": {"Rare": 0.593986, "Super Rare": 0.242813, "Mega Rare": 0.099259, "Legendary": 0.040576, "Mythical": 0.016587, "Divine": 0.006780}
    },
    {
        "PackName": "King Sort",
        "Cost": 1000.00,
        "CardValueRange": (250.00, 50000.00),
        "PotentialRarities": ["Super Rare", "Mega Rare", "Legendary", "Mythical", "Divine", "Transcendent"],
        "cardIndexRange": (1501, 1750),
       "Odds": {"Super Rare": 0.720668, "Mega Rare": 0.201554, "Legendary": 0.056370, "Mythical": 0.015765, "Divine": 0.004409, "Transcendent": 0.001233}
    },
    {
        "PackName": "God Sort",
        "Cost": 2500.00,
        "CardValueRange": (850.00, 100000.00),
        "PotentialRarities": ["Mega Rare", "Legendary", "Mythical", "Divine", "Transcendent"],
        "cardIndexRange": (1751, 2000),
        "Odds": {"Mega Rare": 0.769806, "Legendary": 0.177592, "Mythical": 0.040970, "Divine": 0.009452, "Transcendent": 0.002180}
    }
]


def printMenu():
    print("\n" + "=" * 50)
    print("        WELCOME TO DATA STRUCTURE DASH")
    print("=" * 50)
    print(f"  Player: {user['username']} | Balance: ${user['balance']:,.2f}")
    print("-" * 50)
    print("  [s] Start a New Run")
    print("  [c] View Card Collection")
    print("  [h] View Run History & High Scores")
    print("  [q] Quit Game")
    print("=" * 50)


def openPackShop():
    purchasedPacks = []
    
    while user["balance"] >= packs[0]["Cost"]:
        print(f"\nCurrent Balance: ${user['balance']:,.2f}")
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
        print("[q] Exit shop & Open Purchased Packs")
        print("-------------------------------------------")
        
        choice = input("Enter your choice (1-8 or q): ").strip().lower()
        
        if choice == "q":
            print("Exiting shop...")
            break
        elif choice.isdigit() and 1 <= int(choice) <= 8:
            selected_pack = packs[int(choice) - 1]
            if user["balance"] >= selected_pack["Cost"]:
                user["balance"] -= selected_pack["Cost"]
                purchasedPacks.append(selected_pack)
                print(f"Bought {selected_pack['PackName']} Pack! Remaining: ${user['balance']:,.2f}")
            else:
                print(f"Insufficient funds! {selected_pack['PackName']} costs ${selected_pack['Cost']:,.2f}, but you only have ${user['balance']:,.2f}.")
        else:
            print("Invalid choice! Enter 1-8 or 'q'.")

    if user["balance"] < packs[0]["Cost"] and user["balance"] > 0:
        print(f"\nRemaining balance (${user['balance']:,.2f}) is less than $1.00 (cheapest pack). Closing shop!")
        
    return purchasedPacks
    
def startRun():
    print("\n" + "=" * 50)
    print("                --- START RUN ---")
    print("=" * 50)
    
    current_bal = user["balance"]
    added_deposit = 0.0

    if current_bal >= packs[0]["Cost"]:
        print(f"You have an existing balance of ${current_bal:,.2f}.")
        while True:
            choice = input("Use current balance [u], deposit more funds [d], or cancel run [q]? ").strip().lower()
            if choice == "u":
                break
            elif choice == "d":
                added_deposit = getValidDeposit()
                if added_deposit == 0:  
                    return
                break
            elif choice == "q":
                print("Canceling run...")
                return
            else:
                print("Invalid choice! Enter 'u', 'd', or 'q'.")
    else:
        if current_bal > 0:
            print(f"Your balance (${current_bal:,.2f}) is less than $1.00. You must add funds to start a run.")
        added_deposit = getValidDeposit()
        if added_deposit == 0:
            return

    purchasedPacks = openPackShop()

    if not purchasedPacks:
        print("No packs purchased. Exiting run.")
        return

    while True:
        print("\nChoose how you want to open your packs:")
        print("[1] Highest Cost to Lowest Cost")
        print("[2] Lowest Cost to Highest Cost")
        sort_choice = input("Select (1 or 2): ").strip()
        
        if sort_choice == "1":
            purchasedPacks.sort(key=lambda x: x["Cost"], reverse=True)
            break
        elif sort_choice == "2":
            purchasedPacks.sort(key=lambda x: x["Cost"])
            break
        else:
            print("Invalid selection! Please type 1 or 2.")

    pack_queue = deque(purchasedPacks)
    print(f"\n{len(pack_queue)} pack(s) loaded into the opening queue!")
    runOpeningPhase(pack_queue, added_deposit if added_deposit > 0 else current_bal)


def getValidDeposit():
    while True:
        try:
            dep_input = input("Enter deposit amount (must end in 0 or 5, up to $5000) or 'q' to cancel: $").strip()
            if dep_input.lower() == 'q':
                print("Canceling deposit...")
                return 0.0
            val = float(dep_input)
            if val > 0 and val <= 5000 and val % 5 == 0:
                user["balance"] += val
                print(f"Added ${val:,.2f}! Total starting balance: ${user['balance']:,.2f}")
                return val
            else:
                print("Error: Deposit must be positive, up to $5000, and end in 0 or 5.")
        except ValueError:
            print("Invalid number entry. Please enter a valid numerical dollar amount.")
            
def historyMenu():
    print("\n" + "=" * 50)
    print("        --- PLAYER STATS & RUN HISTORY ---")
    print("=" * 50)
    print(f"  Username:        {user['username']}")
    print(f"  Current Balance: ${user['balance']:,.2f}")
    print(f"  Best Run Profit: ${user['best_run']:,.2f}")
    
    best_card_display = user["best_card"].get("display", "None")
    print(f"  Best Card:       {best_card_display}")
    print("-" * 50)

    print("\n  Past Runs Log:")
    if not user["run_history"]:
        print("  No completed runs yet.")
    else:
        for idx, run in enumerate(user["run_history"], 1):
            print(f"  Run #{idx:02d} | Deposit: ${run['deposit']:,.2f} | Earned: ${run['earned']:,.2f} | Net: ${run['net']:,.2f}")
            
    print("=" * 50)
    input("\nPress Enter to return to main menu...")


def setNewHighScore(userScore):
    if userScore > user["best_run"]:
        user["best_run"] = userScore


def setBestCard(card):
    if card["value"] > user["best_card"].get("value", 0.00):
        user["best_card"] = card

def openCollection():
    print("\n" + "=" * 50)
    print("           --- YOUR CARD COLLECTION ---")
    print("=" * 50)
    
    if not user["collection"]:
        print("\n  Your collection is currently empty!")
        print("  Start a run ('s') and keep cards to build your collection.\n")
        print("=" * 50)
        input("\nPress Enter to return to main menu...")
        return

    print(f"\n  Total Cards Owned: {len(user['collection'])}")
    
    while True:
        userSortChoice = input("Sort by value ([h or 2] High-to-Low | [l or 1] Low-to-High | Enter to skip): ").strip().lower()
        
        if userSortChoice in ("h", "2"):
            user["collection"].sort(key=lambda x: x["value"], reverse=True)
            break
        elif userSortChoice in ("l", "1"):
            user["collection"].sort(key=lambda x: x["value"])
            break
        elif userSortChoice == "":
            print("Skipping sort...")
            break
        else:
            print("Invalid.")

    print("\n" + "-" * 50)
    for idx, card in enumerate(user["collection"], 1):
        print(f"  {idx:02d}. {card['display']}")
    print("-" * 50 + "\n")
    
    input("Press Enter to return to main menu...")


def selectionMenu(userSelection):
    if userSelection.lower() == "s":
        startRun()
    elif userSelection.lower() == "c":
        openCollection()
    elif userSelection.lower() == "h":
        historyMenu()


def readCards(filename="cards.txt"):
    catalog = []
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            card_id_str, bracket_data = line.split(" ", 1)
            parts = bracket_data.strip("[]").split("][")
            
            if len(parts) == 4:
                rarity, card_type, name, value_str = parts
                base_value = float(value_str.replace("$", "").replace(",", ""))

                catalog.append({
                    "id": int(card_id_str),
                    "rarity": rarity,
                    "type": card_type,
                    "name": name,
                    "base_value": base_value,
                    "value": base_value  
                })
    return catalog
CARD_CATALOG = readCards()

def generateCardFromPack(pack):
    rarities = list(pack["Odds"].keys())
    probs = list(pack["Odds"].values())
    chosen_rarity = random.choices(rarities, weights=probs, k=1)[0]
    
    matching_cards = [c for c in CARD_CATALOG if c["rarity"] == chosen_rarity]
    if not matching_cards:
        matching_cards = CARD_CATALOG
        
    base_card = random.choice(matching_cards)
    
    base_cents = int(round(base_card["base_value"] * 100))
    min_cents = int(round(0.85 * base_cents))
    max_cents = int(round(1.15 * base_cents))
    final_cents = random.randint(min_cents, max_cents)
    final_val = final_cents / 100.0
    
    return {
        "id": base_card["id"],
        "rarity": base_card["rarity"],
        "type": base_card["type"],
        "name": base_card["name"],
        "value": final_val,
        "display": f"#{base_card['id']} [{base_card['rarity']}][{base_card['type']}][{base_card['name']}][${final_val:.2f}]"
    }
def runOpeningPhase(pack_queue, userDeposit):
    run_earned = 0.0
    print("\n--- OPENING PACKS ---")

    while pack_queue:
        current_pack = pack_queue.popleft()
        
        cards_count = random.choices(DRAW_COUNT_WEIGHTS, weights=DRAW_COUNT_PROBS, k=1)[0]
        
        print(f"\nOpening [{current_pack['PackName']} Pack] (Yielded {cards_count} card(s)):")
        for _ in range(cards_count):
            card = generateCardFromPack(current_pack)
            print(f"PULLED: {card['display']}")
            
            setBestCard(card)

            while True:
                action = input("Press [k] to keep in collection or [s] to sell for cash: ").strip().lower()
                if action == "k":
                    user["collection"].append(card)
                    print("Added to collection!")
                    break
                elif action == "s":
                    user["balance"] += card["value"]
                    run_earned += card["value"]
                    print(f"Sold card for ${card['value']:,.2f}!")
                    break
                else:
                    print("Invalid selection. Please enter k or s")
                          
    net_profit = run_earned - userDeposit
    user["run_history"].append({"deposit": userDeposit, "earned": run_earned, "net": net_profit})
    setNewHighScore(net_profit)
    
    print(f"\nRun Finished! Total Deposit: ${userDeposit:,.2f} | Net Profit: ${net_profit:,.2f}")

def main():
    user["username"] = input("Enter your username: ").strip()
    
    while True:
        printMenu()
        choice = input("Enter selection (s/c/h or q to quit): ").strip().lower()
        
        if choice == "q":
            print("\nThanks for playing Data Structure Dash!")
            break
        elif choice in ("s", "c", "h"):
            selectionMenu(choice)
        else:
            print("Invalid selection. Please enter s, c, h, or q.\n")

if __name__ == "__main__":
    main()

