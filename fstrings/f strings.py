#f strings is a way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and formatted using the __format__ protocol.
from cmath import pi
from datetime import datetime


name = "Alice"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")
print(f"The square of {age} is {age**2}.")
print(f"The value of pi is approximately {pi:.2f}.")
print(f"The current date and time is {datetime.now():%Y-%m-%d %H:%M:%S}.")


#variables can also be used in f strings
var: int = 42
print(f'{var}')

#rounding numbers in f strings
number = 3.141592653589793
percentage = 0.123456789
print(f'{number:.2f}')  # Output: 3.14
print(f'{percentage:.2%}')  # Output: 12.35%

#format big numbers with commas
big_number = 1234567890
print(f'{big_number:,}')  # Output: 1,234,567,890