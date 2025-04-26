#n is an integer number
n = int(input ("Enter any number: "))
# modulus (%) in this particular code shows the remainder of a number that has been divided by 2
remainder = n % 2
if(remainder ==0):
    print(n, " is an Even number")
else:
    print(n, " is an Odd number")
    