class Fruit:
    nutrients = "vitamin c"
    def __init__(self,name,color,test):
        self.name = name
        self.color = color
        self.test = test
    def describe_fruit(self):
        return f"{self.name} which is{self.color} is{self.test}"
    def fruit_price(self):
        return f"The price of {self.name} is 100ksh"
    def cut_fruit(self):
        return f"can you cut that {self.name} into slices"
