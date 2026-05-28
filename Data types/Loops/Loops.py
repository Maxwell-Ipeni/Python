#types of loops in python like for loop and while loop
#for loop is used for finite looping and while loop is used for infinite looping
#for loop used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.


for i in range(1, 6):
    print("This is a for loop iteration: " + str(i))
for i in range(5):
    print("This is a for loop iteration: " + str(i))
 

 #for loop in a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("This is a fruit: " + fruit)  



    #while loop is used to execute a block of code as long as a specified condition is true.
#

i: int = 1
while i <= 5:
    print("This is a while loop iteration: " + str(i))
    i += 1  # Increment the counter to avoid infinite loop

    #elif  and else statement is used to check multiple conditions in a loop. It allows you to specify additional conditions to check if the previous conditions were not met. Here's how you can use elif statements in a loop:

for i in range(1, 11):  #if this does not work
    if i % 2 == 0:
        print(str(i) + " is an even number.")
    elif i % 2 != 0:    #checks for something else if the previous condition is not met
        print(str(i) + " is an odd number.")
    else:   #if none of the above conditions are met, this block will be executed
        print(str(i) + " is neither even nor odd.")


    
        a, b =10, 'five'
        try:
            print(a + b)  # This will raise a TypeError since you cannot add an integer and a string
        except TypeError as e:
            print("Error: " + str(e))  # This will catch the error and print it out