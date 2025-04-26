#int prevents n from being read as a string value
n = int(input("Enter a number, ANY number: "))
factorial = 1
#n is the starting value
#0 is the ending value
#-1 is the stepping value
#0 is excluded from the calculations since it is the range's boundary
for i in range (n, 0, -1):
     factorial = factorial*i
print ("The factorial of", n, "is", factorial)