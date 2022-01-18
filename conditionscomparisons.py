var1=10
var2=23
var3=10
var4=34
if(var1==var2):
    print("Equal")

if(var1==var4):
    print("True")
elif(var4>var1):
    print("Greater")
else:
    print("I am out")

if(var1<=var4):
    print("Less")
    if(var4>=var3):
        print("Greater")
        if(var1==var3):
            print("Equal")

value1=int(input("Please enter a number: "))
if(value1%2==0):
    print("Number Is Even")
else:
    print("Numbe is Odd")


