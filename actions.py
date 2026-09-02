from queue import Queue
from cards import Card, unshuffled_deck
import random

my_deck = Queue()
opponent_deck = Queue()
middle_pile = Queue()

def prep_decks(unshuffled_deck):
    random.shuffle(unshuffled_deck)
    for i in range(0,len(unshuffled_deck)):
        if i % 2 == 0:
            my_deck.push(unshuffled_deck[i])
        else:
            opponent_deck.push(unshuffled_deck[i])

def status_top_card(deck = my_deck):
    if deck.size() == 0:
        return None
    else:
        return deck.peek().check()


def check_deck_size(d1 = my_deck, d2 = opponent_deck)-> None:
    return f"My deck size: {d1.size()}\nOppenent deck size:{d2.size()}"

def compare_stats(d1 = my_deck, d2 = opponent_deck, pile = middle_pile)-> str:
    if d1.size() == 0 or d2.size() == 0:
        return "Tie"
    x = input("Enter a stat: ").strip().lower()

    stat_map = {
        "pow": "pow",
        "power": "pow",
        "know": "know",
        "knowledge": "know",
        "agi": "agi",
        "agility": "agi",
        "wis": "wis",
        "wisdom": "wis",
        "stam": "stam",
        "stamina": "stam",
        "xfac": "xfac",
        "xfactor": "xfac",
    }   

    a = d1.pop()
    b = d2.pop()
    attr = stat_map.get(x)
    if attr is None:
        print("Invalid stat")
        compare_stats()
    else:
        astat = getattr(a, attr)
        bstat = getattr(b,attr)

    if (astat == bstat):
        print(f"My {a.name} with {x} {astat} tied against your {b.name} with {x} {bstat}")
        pile.push(a)
        pile.push(b)
        return "Tie"
    elif (astat > bstat):
        print(f"My {a.name} with {x} {astat} wins against your {b.name} with {x} {bstat}")
        d1.push(a)
        d1.push(b)
        if pile.size() != 0:
            for i in range(0,pile.size()):
                tmp = pile.pop()
                d1.push(tmp)
        return "Win"
    else:
        print(f"My {a.name} with {x} {astat} loses against your {b.name} with {x} {bstat}")
        d2.push(b)
        d2.push(a)
        if pile.size() != 0:
            for i in range(0,pile.size()):
                tmp = pile.pop()
                d2.push(tmp)
        return "Lose"


def highest_stat(card: Card):
    stat_names = ["pow", "know", "agi", "wis", "stam", "xfac"]
    return max(stat_names, key=lambda stat: getattr(card, stat))

def opponent_turn(d1 = my_deck, d2= opponent_deck):
    if d1.size() == 0 or d2.size() == 0:
        return "A Deck is empty"
    a = d1.pop()
    b = d2.pop()
    hstat = highest_stat(b)

    astat = getattr(a, hstat)
    bstat = getattr(b, hstat)

    if (astat == bstat):
        print(f"My {a.name} with {hstat} {astat} tied against your {b.name} with {hstat} {bstat}")
        middle_pile.push(a)
        middle_pile.push(b)
        return "Tie"
    elif (astat > bstat):
        print(f"My {a.name} with {hstat} {astat} wins against your {b.name} with {hstat} {bstat}")
        d1.push(a)
        d1.push(b)
        if middle_pile.size() != 0:
            for i in range(0,middle_pile.size()):
                tmp = middle_pile.pop()
                d1.push(tmp)
        return "Win"
    else:
        print(f"My {a.name} with {hstat} {astat} loses against your {b.name} with {hstat} {bstat}")
        d2.push(b)
        d2.push(a)
        if middle_pile.size() != 0:
            for i in range(0,middle_pile.size()):
                tmp = middle_pile.pop()
                d2.push(tmp)
        return "Lose"


def switch(result, turn)->str:
    if result == "Win":
        return "Win"
    elif result == "Lose":
        return "Lose"
    else:
        if turn == "Lose":
            return "Win"
        else:
            return "Lose"   

def main():
   pass

main()