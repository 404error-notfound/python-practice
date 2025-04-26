def fact (n):
#n==0 is the base case OR the stopping condition. 
# It ensures that the result n has reached 0 for the function to complete the problem.
    if n ==0:
        return 1
# n*fact(n-1) is the recursive case. 
# It is the repetitive function that breaks down the problem into simpler and solvable problems
    else:
        return n * fact(n-1)
    
n = int(input("Enter any number: "))
#the function fact(n) is being called for it to be executed
factorial = fact (n)
print ("The factorial of", n, "is", factorial)