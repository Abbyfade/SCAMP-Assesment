#function to display fibonacci sequence
def fibonacci(x):
    #the first and second value of the sequence
    n1, n2 = 0, 1
    count = 0
    #check if the value supplied is valid
    if x < 0:
        print("Incorrect input")
    elif x == 0:
        return n1
    elif x == 1:
        return n1
    else:
        #create an empty list
        sequence = []
        while count < x+1:
            sequence.append(n1)
            #update the values
            fib = n1 + n2
            n1 = n2
            n2 = fib
            count += 1
        return sequence


range_of_values = int(input("Enter number to display the fibonacci sequence: "))
print("Fibonacci sequence of {x} is: {y}".format(x = str(range_of_values), y = fibonacci(range_of_values)))
