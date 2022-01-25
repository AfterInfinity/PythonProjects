for i in range(2):
    print("Hello")
    print(i)
for i in range(1,4):
    print("Hi")
    print(i)
for i in range(1,5,2):
    print("Huh")
    print(i)
number=0
for i in range(3):
    number=number+i
    print(number,i)
i=1
while(i<=5):
    print(i)
    i=i+1

num4table=int(input("Enter Number for Table: "))
for i in range(1,11):
    print(num4table,"*",i,"=",num4table*i)