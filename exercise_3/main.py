''' 
Exercise 2
Group 7
Erkam Dogan, Luca Hesse, Tobias Krumrein
'''
from  exercise_3.easy_shopping.calculator import Calculator
from exercise_3.easy_shopping.shopping import Shoppingcart, Item
from easy_shopping import calculator, shopping

def main():

    calc = Calculator()
    
    
    print(calc.addition(7, 5))
    print(calc.subtraction(34, 21))
    print(calc.multiplication(54, 2))
    print(calc.division(144, 2))
    print(calc.division(45, 0))

    shoppingCart = Shoppingcart()

    shoppingCart.addItem(Item("Proteinpulver", 3))
    shoppingCart.addItem(Item("Magerquark", 2))
    shoppingCart.addItem(Item("Kultidöner", 5))
    shoppingCart.displayItems()
    shoppingCart.removeItem("Kultidöner")
    shoppingCart.displayItems()

if __name__ == '__main__':
    main()