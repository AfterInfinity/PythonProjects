from numpy import isin


def check_odd_even(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

def print_table(tablenum):
    for incriment in range(1,11):
        print(tablenum,"*",incriment,"=",int(tablenum)*incriment)

for num in range(1,10):
    print(check_odd_even(num))

num4table=input("Enter Number to print table of: ")
print_table(num4table)

def seggrgateList(list1):
    if isinstance(list1,list):
        listNum=[]
        liststrint=[]
        for i in list1:
            if isinstance(i,int) or isinstance(i,float):
                listNum.append(i)
            else:
                liststrint.append(i)
        print("Integer List : ",listNum)
        print("String List : ",liststrint)
    else:
        print("Wrong input type, Input should be a list type")



nslist=[1,'shashwat',3,'shriparv',5,'delhi',9,'ghaziabad',34,'Uttar Praesh']
print(nslist)
datatype=23
seggrgateList(datatype)
seggrgateList(nslist)