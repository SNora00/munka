from zeep import Client
import re
from enum import Enum

class Operators(str, Enum):
    Add = "+"
    Divide = "/" 
    Multiply = "*"
    Subtract =  "-"

def Add(A: int,B: int):
    return (client.service.Add(A,B))

def Divide(A: int,B: int):
    return  (client.service.Divide(A,B))

def Multiply(A: int,B: int):
    return  (client.service.Multiply(A,B))

def Subtract(A: int,B: int):
    return  (client.service.Subtract(A,B))

client = Client('http://www.dneonline.com/calculator.asmx?WSDL')

def Calculate(expression):
    numbers = re.findall(r"[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", expression)
    operators = re.findall(r'[-+*/]', expression)

    while operators:
        num1 = round(float(numbers.pop(0)))
        num2 = round(float(numbers.pop(0)))
        op = operators.pop(0)

        if op == Operators.Add:
            result = Add(num1,num2)
        elif op == Operators.Subtract:
            result = Subtract(num1,num2)
        elif op == Operators.Multiply:
            result = Multiply(num1,num2)
        elif op == Operators.Divide:
            result = Divide(num1,round(num2))
        else:
            raise ValueError(f"Invalid operator: {op}")

        numbers.insert(0, str(result))
        print(numbers)

    return (numbers[0])

expression = "((55+42)*12+3)/3.14"
result = Calculate(expression)

print(f"Result of the expression '{expression}' is: {result}")
