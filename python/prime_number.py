import math
num=int(input("enter number :"))
is_prime = True
factor = 1
#for i in range(2,num):
for i in range(2, int(math.sqrt(num))+1):
    if num%i == 0:
        is_prime = False
        factor = i
        break

if is_prime:
    print(num, " is a prime number")
else:
    print(num, " is not a prime number and its factor is " , factor, num//factor)

