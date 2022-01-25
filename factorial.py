fact=1
number=int(input("Enter the Number for Factorial: "))
for i in range(1,(number+1)):
    fact=fact*i
print("Factorial of ",number,"Is",fact)

fact=1
i=1
number=int(input("Enter the Number for Factorial: "))
while(i<=number):
    fact=fact*i
    i=i+1
print("Factorial of ",number,"Is",fact)
