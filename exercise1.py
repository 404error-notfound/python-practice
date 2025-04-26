# user inputs how many numbers they want in the list
n =  int(input("List size:"))
#the number of the list size is stored
list = []
sum = 0

for i in range (n):
    num = int(input())
    #for each number the user enters, the number is added to the total sum 
    list.append (num)
    sum = sum + num

print ("The Sum of all elements in the list", list, "is", sum)