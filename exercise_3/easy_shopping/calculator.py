class Calculator:                           # create class calculator, it has the following functions (all have two arguemnts)


    def addition(self, a, b):               # add b to a
        return a + b
    

    def subtraction(self, a, b):            # subtract b from a
        return a - b


    def multiplication(self, a, b):         # multiply a with b
        return a * b

    
    def division(self, a, b):               # divide a through b when b is not 0
        if b == 0:
            return "Can't divide by zero"
        else:
            return a / b 