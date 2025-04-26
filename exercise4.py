def reverse_string(string1):
#it stores the reversed version of string 1
    reversed_string = ""
#each character in the string is reversed from left to right
    for char in string1:
      reversed_string = char + reversed_string
    return reversed_string

string1 = input("Enter a string value: ")
#the function reverse_string is being called
string2 = reverse_string(string1)
print ("The reversed string value is", string2)