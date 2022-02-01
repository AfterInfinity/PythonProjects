class Animal:
    name="Animal"
    print("I am a Animal Class !")
    numlegs=4
    horn=True
    run="Runs"
    Eats="Grass"
    Eat=["Grass","Meat"]
    def getmyname(self):
        print("My Name is : ",self.name)
    
class Dog(Animal):
    name="Doggy"
    print("I am a Dog Class !")
    Eats="NoGrass"
    eat=["Meat","Rice"]
    horn=False
    def getmyname(self):
        print("My Name is : ",self.name)  
    def getmyname(self,new_name):
        print("My Name is : ",self.name,"And New name is",new_name)
  
        
'''
animal=Animal
print(animal.Eat)
print(animal.horn)
mya=animal
print(mya.Eat)
dog=Dog()
print(dog.Eat)
print(dog.horn)
'''        
dog=Animal()
puppy=Dog()


dog.getmyname()
puppy.getmyname()
puppy.getmyname('Rolo')