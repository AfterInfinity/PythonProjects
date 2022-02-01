class Mammal:
    mmlist=[]
    name="Human"
    num_of_legs=4
    feather=True
    skilcolor=["Red","Green","Yellow","Pink","Black","White","Orange"]
    def getproperties(self):
        print(self.num_of_legs,self.feather,self.skilcolor)
    def addtommlist(self,nm,nlegs,fethur,skinclr):
        self.mmlist.append([nm,nlegs,fethur,skinclr])
    def pringmmlist(self):
        print(self.mmlist)
        

