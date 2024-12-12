#automorphic number is anumber whose squares end with the original number 
num=int(input("enter a number "))
sq=num**2 #square of number
str_num=str(num)
str_sq=str(sq) #num convert into string
if str_sq.endswith(str_num):
    print(f"{num} is an automorphic number")
else:
    print(f"{num} is NOT an automorphic number")
