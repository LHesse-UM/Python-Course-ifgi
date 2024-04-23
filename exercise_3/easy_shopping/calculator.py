class Calculator:


    def addition(self, a, b):
        return a + b
    

    def subtraction(self, a, b):
        return a - b


    def multiplication(self, a, b):
        return a * b

    
    def division(self, a, b):
        if b == 0:
            return "Can't divide by zero"
        else:
            return a / b 