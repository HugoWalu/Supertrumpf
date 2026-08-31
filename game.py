from queue import Queue
from cards import *
from actions import *


def supertrumpf(d1 = my_deck, d2 = opponent_deck):
    prep_decks(unshuffled_deck)
    while (d1.size() != 0 and d2.size() != 0):
        x = input("Check Decksize, Compare Stats, Check Topcard").strip().lower()

        action_map = {
            "size": "size",
            "decksize": "size",
            "check decksize": "size",
            "stats": "stats",
            "compare stats": "stats",
            "card": "card",
            "check card": "card",
            "check topcard": "card",
            "topcard": "card"
        }
        action = action_map.get(x)
        if action == None:
            print("Invalid Action")
        elif action == "size":
            print(check_deck_size())
        elif action == "card":
            print(status_top_card())
        else:
            compare_stats()
    if d1.size == 0:
        print("You lose!")
        return
    else:
        print("You win!")
        return

def main():
    supertrumpf()

main()