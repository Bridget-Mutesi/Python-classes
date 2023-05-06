class Student:
    school = 'Akirachix'
    def __init__(self,age,nationality,first_name,last_name,country): 
       
        self.age = age
        self.nationality = nationality
        self.first_name = first_name
        self.last_name = last_name
        self.country = country

    
    def show_full_name(self):
        return f"Hello my name is {self.first_name} {self.last_name}"

    
    def year_of_birth(self):
         year = 2023-self.age
         return f" Hello {self.first_name} {self.last_name} you are born in {year}"
    def show_initials(self):
        return f"{self.first_name[0]} {self.last_name[0]}"
# 
    


# 'class methods are used to add behavior to classes and
# they operate in the class attribute
# we use normal functions

