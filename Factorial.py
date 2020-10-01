#To find the factorial of a number 

print("Enter the number to find its factorial")

numb = int(input())

factorial = 1


if(numb<0):

    print("Factorial of a negative number is not defined")


elif(numb==0):

    print("Factoial of 0 is 1")


else:

    for x in range(1, numb+1):

        factorial = x*factorial

    print("Factorial of given number is", factorial)