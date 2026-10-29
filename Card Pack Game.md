Data Structure Dash is a card pack gambling game in which a player can do a "run" in which they can purchase either $1, $5, $25, $50, $100, $500 , $1000, or $2500 card packs and receive 1 random card, or a small chance of doubles and a tiny chance of triples. A "run" is defined when a player presses the 'S' key to begin a run, where they can choose to make an initial deposit of $1-$5000. Upon depositing the funds, the player can choose to purchase whichever packs they please, but they must exhaust their entire deposit until they can no longer purchase any packs. The lower the pack cost, the lower the potential payout, and higher packs give a higher potential payout. Once the player has purchased all of their desired packs, they can choose to open packs from highest cost to lowest, or vice versa. Each pack is opened one at a time, and upon receiving the card, the player can choose to collect the card or sell it. Selling a card will add it to their collection, which can be viewed by pressing "C". Once all packs are opened, the user can choose to end the run or buy another set of packs, and this will continue until the player chooses to stop or until they run out of money. Once one of these conditions is met, the run will end and the player's "best run" is defined by the run in which they made the most net profit. A player's current balance will always be displayed.



A breakdown of the card packs:





|Pack Name|Pack Cost|Card Value Range|Potential Rarities|
|-|-|-|-|
|Bubble Sort|$1|$0.25 - $30|Common, Uncommon, Rare, Super Rare|
|Selection Sort|$5|$1.50 - $75|Common, Uncommon, Rare, Super Rare, Mega Rare|
|Insertion Sort|$25|$10 - $600|Uncommon, Rare, Super Rare, Mega Rare, Legendary, Mythical|
|Quick Sort|$50|$20 - $1500|Uncommon, Rare, Super Rare, Mega Rare, Legendary, Mythical|
|Merge Sort|$100|$40 - $4000|Rare, Super Rare, Mega Rare, Legendary, Mythical, Divine|
|Heap Sort |$500|$90 - $10,000|Rare, Super Rare, Mega Rare, Legendary, Mythical, Divine|
|King Sort|$1000|$250 - $50,000|Super Rare, Mega Rare, Legendary, Mythical, Divine, Transcendent |
|God Sort|$2500|$850 - $100,000|Mega Rare, Legendary, Mythical, Divine, Transcendent |





There are 2000 unique cards, though one unique card can be obtained at varying prices.

A card is displayed as follows: \[Rarity]\[Type]\[Name]\[Value]. "Name" refers to a card with the name of someone part of the CPSC 315 Class, and "Type" refers to the variant of the person. For example:



\[Mega Rare]\[Cyber Wizz]\[Heather Marriot]\[$920].



This exact card can range in price +- 15% from the middle value.



The probabilities of drawing each rarity varies depending on the pack, and once a rarity is chosen, a random card from that rarity is chosen, and once the specific card type is chosen, its value can vary +-15% from the base value. 



For example:



A card pack has a 10% chance to drop a rare

If a rare is chosen, a random rare card valued within the min-max range of the pack is chosen.

Once the specific rare is chosen, a randomizer chooses a value within 15% of the base value.





