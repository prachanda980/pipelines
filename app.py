def sum_two_numbers(a, b):
    return a + b
def multiply_two_numbers(a, b):
    return a * b
def subtract_two_numbers(a, b):
    return a - b
def divide_two_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power_two_numbers(a, b):
    return a ** b
def modulus_two_numbers(a, b):
    return a % b




if __name__ == "__main__":
    # Example usage
    print("Sum:", sum_two_numbers(5, 3))
    print("Multiply:", multiply_two_numbers(5, 3))
    print("Subtract:", subtract_two_numbers(5, 3))
    print("Divide:", divide_two_numbers(5, 3))
    print("Power:", power_two_numbers(5, 3))
    print("Modulus:", modulus_two_numbers(5, 3))