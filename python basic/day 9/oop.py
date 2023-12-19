class House: 
    def __init__(self,name,window=1,door=2,color="red",price=100):
        self.price=price
        self.name=name
        self.window=window
        self.color=color
        self.door=door
    
    def __str__(self) -> str:
        return f"{self.name} ko ghar"
    
    def __eq__(self, value) -> bool:
        return self.window==value.window
    
    def __gt__(self,value) -> bool:
        return self.price==value.price
    
    def set_color(self,color):
        self.color=color
        
    def get_color(self):
        return self.color
    
    
ram_ko_ghar=House(name="ram")
print(ram_ko_ghar)
shyam_ko_ghar=House(name="shyam",color="black")


is_name=ram_ko_ghar.__gt__(shyam_ko_ghar)
print(is_name)

# print(ram_ko_ghar.get_color())
# print(shyam_ko_ghar.get_color())
# print(ram_ko_ghar.door)
# print(ram_ko_ghar.window)