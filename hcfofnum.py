num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
while num2!=0:
    num1,num2=num2,num1%num2
print(f"hcf of {num1} and {num2}:==",num1)