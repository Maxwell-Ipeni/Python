#Functions make codes more reusable and organized. They allow us to break down complex problems into smaller, manageable pieces. Here's how you can define and use functions in Python:

# Defining a function
def greet(name):
    return "Hello, " + name + "!"   

def add(a: int, b: float) -> float:
    print(f"Adding {a} and {b}...")
    return a + b    

print(greet("Maxwell"))
result = add(5, 3.2)
print("The result of addition is: " + str(result))


def greet(name: str) -> str:
    return f"Hello, {name}!"    

def function_with_no_return() -> None:
    print("This function does not return anything.")

    def func(x: int) -> int:
        return x * 2