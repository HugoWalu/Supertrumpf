import random
from queue import Queue
from cards import *

shuffled_deck = random.shuffle(deck)
my_deck = Queue()
opponent_deck = Queue()

