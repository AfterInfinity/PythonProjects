#from classobj_1 import Animal,Dog
from classesandobjs.classcollection import Mammal
'''
animal=Animal()
print(animal.Eat)
animal.getmyname("PomPom")
'''

mm=Mammal();
mm.getproperties()
mm.addtommlist("Whale",0,False,"['Blue','Black']")
mm.addtommlist("Human",2,False,"['Black','White','Brown']")
mm.pringmmlist()
mm.mmlist.pop()
mm.pringmmlist()