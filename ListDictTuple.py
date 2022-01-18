'''This is Python Code for understanding List Dictionary and Tuple'''
##print(chr(27)+'[2j')
##print('\033c')
print('\x1bc')
## List
print("\n--------------\n1D List \n----------------\n")
listitems1d=[1,2,3,4,5,6,7,8]
for i in listitems1d:
    print(i)
print("\n--------------\n2D List \n----------------\n")
listitems2d=[[1,2],[3,4],[5,6],[7,8]]
for i,j in listitems2d:
    print(i,j)
    print(i,[i,j])
print("\n--------------\n1D List pop \n----------------\n")
listitems1d.pop()
print(listitems1d)
print("\n--------------\n2D List pop \n----------------\n")
print(listitems2d)
listitems2d.pop()
print(listitems2d)
##Dictionary
print("\n--------------\nDictionary \n----------------\n")
dictionary={
    "Name":"Shashwat",
    "Age":"40",
    "Address":"B2-905, BharatCity, Ghaziabad, Uttar Prades-201102",
    "CompanyExp":
    {"HCL":"1 Year",
     "Cloudwick":"1 Year"
            }
}
print(dictionary)
print(dictionary.keys())
print(dictionary["CompanyExp"]["HCL"])
print(dictionary["CompanyExp"].keys())
##Using Loop
for keys in dictionary:
    print("Key : "+keys)


##Tupple
print("\n--------------\nTupple \n----------------\n")
tupple=("Name","Shashwat")
print(tupple)
print(tupple[0])
tupple1=(
    ("Name","Shashwat"),
    ("Home","BharatCity")
)
print(tupple1)

print("This is test2 branch")

