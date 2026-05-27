
def pluss(x, y): return x + y
def minus(x, y): return x - y
def mul(x, y): return x * y
def delll(x, y): return x / y

a = float(input("Первое число: "))
b = float(input("Второе число: "))

operation = input("Действие (+, -, *, /): ")

if operation == "+": print(pluss(a, b))
elif operation == "-": print(minus(a, b))
elif operation == "*": print(mul(a, b))
elif operation == "/": print(delll(a, b))
else: print("такой операции нте ")