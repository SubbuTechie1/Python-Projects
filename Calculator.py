def add(x,y):
    return x+y
def sub(x,y):
    return (x-y)
def mul(x,y):
    return(x*y)
def div(x,y):
    if y == 0:
        print('Error:Division by Zero')
    return x/y
print("-----Simple Calculator-----")
print("Select the Operator")
print("1.Addition (+)")
print("2.Substaction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")
op = input('Enter your choice (+, -, *, /)')
a = float(input('Enter the first number:'))
b = float(input('Enter the second number:'))
if op == '+':
    result = add(a,b)
if op == '-':
    result = sub(a,b)
if op == '*':
    result = mul(a,b)
if op == '/':
    result = div(a,b)
print('Result:',result)