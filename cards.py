
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


deck: list[Card] =[
    Card("Wizard",2,10,2,8,3,6),
    Card("Dragon",10,5,4,6,7,2),
    Card("Valstraz",7,2,10,3,6,6),
    Card("Unicord,",5,5,7,10,3,1),
    Card("Sage",1,8,1,10,4,9),
    Card("Ricky",3,7,2,6,3,10)
]
