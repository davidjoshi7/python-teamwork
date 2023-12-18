class GrandFather(object):
    house="Luxerxy House"

    def __init__(self) -> None:
        print("Grandfather")
    
    def get_house(self):
        return self.house
        


class GrandMother:
    def __init__(self) -> None:
        print("GrandMother")
    jewellary="suun wala diamond "
    
    
class Father(GrandFather,GrandMother):

    car="Mercedes"
    
    def get_house(self):
        print(super().get_house())
        return "jhan ramro ghar"
    
class Son(Father):
    console="PS5"

father=Father()

print(father.get_house())
# example of inhertiace
# print(son.console)

# print(isinstance(son,object))