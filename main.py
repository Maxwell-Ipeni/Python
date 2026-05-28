#Strings
#/Variable definitions
name = "Maxwell"
age = 30

print("Hello, " + name + "! You are " + str(age) + " years old.")
print("Hello, " + name + "! You are " + str(age) + " years old.")



#numbers/intengers/floats
height = 5.9
weight = 150

print("Your height is " + str(height) + " feet.")
print("Your weight is " + str(weight) + " pounds.")

#Boolean values either true/false
is_student = True
is_employed = False

print("You are a student: " + str(is_student))
print("You are employed: " + str(is_employed))

#Tuples
coordinates = (10, 20)
print("Your coordinates are: " + str(coordinates))

#lists
fruits = ["apple", "banana", "cherry"]
print("Your favorite fruits are: " + str(fruits))

#sets
unique_numbers = {1, 2, 3, 4, 5}
print("Your unique numbers are: " + str(unique_numbers))

#a dictionary
person = {"name": "Maxwell",
"age": 30,"height": 5.9,
"weight": 150,"is_student": True,
"is_employed": False,"coordinates": (10, 20),
"fruits": ["apple", "banana", "cherry"],"unique_numbers": {1, 2, 3, 4, 5}}
print("Your person information is: " + str(person)) 


#convert string to int
age = int("30")
height = float("5.9")
print("Your age is: " + str(age))
print("Your height is: " + str(height))

#type annotations helps with code readability and can be used by tools for type checking. 
# It does not affect the runtime behavior of the code but serves as documentation for developers. 
# Here's how you can use type annotations in Python:
name: str = "Maxwell"  
age: int = 30
height: float = 5.9
is_student: bool = True
coordinates: tuple = (10, 20)
fruits: list = ["apple", "banana", "cherry"]
unique_numbers: set = {1, 2, 3, 4, 5}
person: dict = {"name": "Maxwell", "age": 30, "height": 5.9, "is_student": True, "coordinates": (10, 20), "fruits": ["apple", "banana", "cherry"], "unique_numbers": {1, 2, 3, 4, 5}}
print("Your name is: " + name)
print("Your age is: " + str(age))
print("Your height is: " + str(height))
print("You are a student: " + str(is_student))
print("Your coordinates are: " + str(coordinates))
print("Your favorite fruits are: " + str(fruits))
print("Your unique numbers are: " + str(unique_numbers))
print("Your person information is: " + str(person))



#f strings
name = "Maxwell"
age = 30
print(f"Hello, {name}! You are {age} years old.")   
