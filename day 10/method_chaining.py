class Pizza:
    
    def dough(self):
        print("dough")
        return self
    
    def sauce(self):
        print("sauce")
        return self
    
    def cheese(self):
        print("cheese")
        return self
        

pizza=Pizza()
pizza.dough().sauce().cheese()
