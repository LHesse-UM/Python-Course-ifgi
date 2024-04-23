''' 
Exercise 2
Group 7
Erkam Dogan, Luca Hesse, Tobias Krumrein
'''
from easy_shopping import calculator, shopping              # import calculator and shopping from the easy_shopping package

def main():                                                 # main method to run test cases

    calc = calculator.Calculator()                          # create an instance of calculator class
    
    
    print(calc.addition(7, 5))
    print(calc.subtraction(34, 21))
    print(calc.multiplication(54, 2))
    print(calc.division(144, 2))
    print(calc.division(45, 0))

    shoppingCart = shopping.Shoppingcart()                  # create an instance of shoppingcart class

    shoppingCart.addItem(shopping.Item("Proteinpulver", 3)) # add three items
    shoppingCart.addItem(shopping.Item("Magerquark", 2))
    shoppingCart.addItem(shopping.Item("Kultidöner", 5))
    shoppingCart.displayItems()                             # display the items in the shopping cart
    shoppingCart.removeItem("Kultidöner")                   # remove "Kultidöner"
    shoppingCart.displayItems()                             # display the remaining items in the shopping cart

if __name__ == '__main__':
    main()