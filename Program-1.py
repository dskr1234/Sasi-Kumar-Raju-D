
# Basic Calculator

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
a=int(input('Enter a value: '))
b=int(input('Enter b value: '))
operation = input('Enter operation Like Addition,Subtraction,Multiplication,Division: ')
cal = Calculator(a,b)
if operation == 'Addition':
    print(cal.add())
elif operation == 'Subtraction':
    print(cal.sub())
elif operation == 'Multiplication':
    print(cal.mul())
else:
    print(cal.div())
