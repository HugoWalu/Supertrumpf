from queue import Queue
from cards import *

def status_top_card(deck = my_deck):
    if deck.size() == 0:
        return None
    else:
        return deck.peek().check()