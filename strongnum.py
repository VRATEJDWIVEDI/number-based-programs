import math
"""strong number is a number which is equal to sum of factorials of its each digits"""
num=int(input("enter any number"))
sumoffactorials=0
orinum=num
while num!=0:
    y=num%10
    sumoffactorials=sumoffactorials+math.factorial(y)
    num=num//10
if orinum==sumoffactorials:
    print("it is a strong number")
else:
    print("it not a strong number")