num=int(input("enter any number"))
c=0
for i in range(1,num+1):
    if num%i==0:
        c=c+1
if c==2:
    print("it is a prime number")
else:
    print("it is not a prime number")