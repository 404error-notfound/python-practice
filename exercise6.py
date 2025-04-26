#This code sums the digits of a number using the MAD Technique
#MAD = Modulus, Addition, Division
n = int(input("Enter number:  "))
sum = 0

while (n>0):
#Modulus calculates the last digit of a number
    last_digit = n % 10
# Addition is used to add the last digit to the sum
    sum = sum + last_digit
#Division is used to remove the last digit from the number
    n = n//10

#the loop is repeated until n becomes 0   
print ("The sum of the digits of the number is", sum)