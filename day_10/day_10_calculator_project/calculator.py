
import os
from art import logo

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1,n2):
  return n1 - n2

# Multiply
def multiply(n1,n2):
  return n1 * n2

# Divide
def divide(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
    print(logo)
    
    num1 = float(input("What's the first number?: ").replace(",", "."))

    print()
    for symbol in operations:
      print(symbol)
    print()  
    should_continue = True
  
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: ").replace(",", "."))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
  
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        question = input(f"\nType:\n'C' - to continue calculating with {answer}\n'N' - to start a new calculation\n'E' - to exit\n").lower()
  
        if question == "c":
            num1 = answer
        elif question == 'e':
            should_continue = False
            print("\nGoodbye")
        else:
          should_continue = False
          os.system("clear")
          calculator()

calculator()
