class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


calculator = Calculator(10, 2)
print(calculator.sum())
print(calculator.subtraction())
print(calculator.multiplication())
print(calculator.division())
