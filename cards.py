
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
        pass
    
    def __lt__(self, other: "Card")-> bool:
        pass
    
    def __gt__(self, other: "Card")-> bool:
        pass
    
    def check(self)-> list[tuple]:
        return [(self.name) ,("Power",self.pow),("Knowledge",self.know),("Agility",self.agi),("Wisdom",self.wis),("Stamina",self.stam),("XFactor",self.xfac)]


        