from queue import Queue
from cards import Card, unshuffled_deck
import random

middle_pile = Queue()
my_deck = Queue()
opponent_deck = Queue()

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

def compare_stats(d1 = my_deck, d2 = opponent_deck, pile = middle_pile):
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
    else:
        astat = getattr(a, attr)
        bstat = getattr(b,attr)

    if (astat == bstat):
        print(f"My {a.name} with {x} {astat} tied against your {b.name} with {x} {bstat}")
        pile.push(a)
        pile.push(b)
    elif (astat > bstat):
        print(f"My {a.name} with {x} {astat} wins against your {b.name} with {x} {bstat}")
        d1.push(a)
        d1.push(b)
        if pile.size() != 0:
            for i in range(0,pile.size()):
                tmp = pile.pop()
                d1.push(tmp)
    else:
        print(f"My {a.name} with {x} {astat} loses against your {b.name} with {x} {bstat}")
        d2.push(b)
        d2.push(a)
        if pile.size() != 0:
            for i in range(0,pile.size()):
                tmp = pile.pop()
                d2.push(tmp)


def main():
   pass

main()