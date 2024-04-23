''' 
Exercise 2
Group 7
Erkam Dogan, Luca Hesse, Tobias Krumrein
'''
from easy_shopping import calculator, shopping              # import calculator and shopping from easy_shopping package

def main():                                                 # main method to run test cases

    calc = calculator.Calculator()                          # make a instanz of calculator class
    
    
    print(calc.addition(7, 5))
    print(calc.subtraction(34, 21))
    print(calc.multiplication(54, 2))
    print(calc.division(144, 2))
    print(calc.division(45, 0))

    shoppingCart = shopping.Shoppingcart()                  # make an instance of shoppingcart class

    shoppingCart.addItem(shopping.Item("Proteinpulver", 3))
    shoppingCart.addItem(shopping.Item("Magerquark", 2))
    shoppingCart.addItem(shopping.Item("Kultidöner", 5))
    shoppingCart.displayItems()
    shoppingCart.removeItem("Kultidöner")
    shoppingCart.displayItems()

if __name__ == '__main__':
    main()