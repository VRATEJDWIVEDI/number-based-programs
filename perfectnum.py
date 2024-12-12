"""perfect number is a number whose sum of factor or 
divisors is equal to the original number EXCLUDING THE NUMBER ITSELF"""
num=int(input("enter any number"))
sumoffactors=0
for i in range(1,num):#Excluding the original number
    if num%i==0:
        sumoffactors=sumoffactors+i
if num==sumoffactors:
    print("its a perfect number")
else:
    print("its not a perfect number")