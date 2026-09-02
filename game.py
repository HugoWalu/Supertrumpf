from queue import Queue
from cards import Card, unshuffled_deck
from actions import *



def supertrumpf(d1 = my_deck, d2 = opponent_deck):
    prep_decks(unshuffled_deck)
    turn = "Win"
    SP_uses = 1
    while (d1.size() != 0 and d2.size() != 0):
        while turn == "Lose":
            result = opponent_turn()
            turn = switch(result,turn)
            break
        x = input("Check Decksize, Compare Stats, Check Topcard, Check_Opponent_Card ").strip().lower()

        action_map = {
            "size": "size",
            "decksize": "size",
            "check decksize": "size",
            "stats": "stats",
            "stat": "stats",
            "compare stats": "stats",
            "card": "card",
            "check card": "card",
            "check topcard": "card",
            "topcard": "card",
            "opponent": "opponent",
            "opponent card": "opponent",
            "check opponent card": "opponent"
        }
        action = action_map.get(x)
        if action == None:
            print("Invalid Action")
        elif action == "size":
            print(check_deck_size())
        elif action == "card":
            print(status_top_card())
        elif action == "opponent":
            check_opp_topcard(SP_uses)
            SP_uses -= 1
        else:
            result = compare_stats()
            turn = switch(result,turn)
    if d1.size() == 0:
        print("You lose!")
        return
    else:
        print("You win!")
        return

