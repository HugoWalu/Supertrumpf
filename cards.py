
class Card():
    def __init__(self, name: str, pow: int,know: int,agi: int,wis: int,stam: int,xfac: int,) -> None:
        self.pow = pow
        self.know = know
        self.agi = agi
        self.wis = wis
        self.stam = stam
        self.xfac = xfac
        self.name = name

    def __eq__(self, other:object)-> bool:
        return self == other
    
    def __lt__(self, other: "Card")-> bool:
        return self < other
    
    def __gt__(self, other: "Card")-> bool:
        return self > other
    
    def check(self)-> list[tuple]:
        return [(self.name) ,("Power",self.pow),("Knowledge",self.know),("Agility",self.agi),("Wisdom",self.wis),("Stamina",self.stam),("XFactor",self.xfac)]


unshuffled_deck: list[Card] =[
    Card("Wizard",2,10,2,8,3,6),
    Card("Dragon",10,5,4,6,7,2),
    Card("Valstraz",7,2,10,3,6,6),
    Card("Unicorn,",5,5,7,10,3,1),
    Card("Sage",1,8,1,10,4,9),
    Card("Ricky",3,7,2,6,3,10),
    Card("Joe",5,5,5,5,5,5),
    Card("Gato",3,7,7,5,6,2),
    Card("Anime Guy",1,7,2,8,3,6),
    Card("Boba",4,7,6,7,2,8),
    Card("Jimmy",2,9,4,9,4,6),
    Card("Hulk",7,3,6,7,7,3),
    Card("Loser",3,2,3,3,3,1),
    Card("Mother",6,6,6,4,6,3),
    Card("Breacher",8,4,5,6,8,3),
    Card("Jackman",6,7,4,8,5,2),
    Card("Mysterio",3,2,9,5,7,8),
    Card("Blanka",7,1,5,3,9,7),
    Card("Jakey",4,8,3,7,6,6),
    Card("Brokey",3,7,5,8,4,6),
    Card("Mr X",2,8,5,6,4,7),
    Card("Blast",6,6,5,7,3,5)
]
