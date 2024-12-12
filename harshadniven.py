s=0
num=int(input("enter any number"))
while num!=0:#finding sum of digits using while loop
        y=num%10
        s=s+y
        num=num//10
if num%s==0:
    print("the given number is a harshad or niven number")
else:
    print("the given number  is NOT a harshad or niven number")
    
