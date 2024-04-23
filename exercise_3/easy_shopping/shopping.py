class Shoppingcart:                     # create class shopping cart


    def __init__(self):                 # it is initialized with an empty list shoppingcart
        self.shoppingcart = []
    

    def addItem(self, item):            # add an item to the list shoppingcart
        self.shoppingcart.append(item)
        print(f"added {item.name} to shopping cart")



    def removeItem(self, name):         # remove an item from list shoppingcart only if a item.name is in the list
        for item in self.shoppingcart:

            if item.name == name:
                self.shoppingcart.remove(item)

                print(f"removed {name} from shopping cart")


    def displayItems(self):             # displays every item with it's quantity

        print("The following items are in the shopping cart:")

        itemCounter = 0
        for item in self.shoppingcart:

            itemCounter = itemCounter + item.quantity

            print(f"{item.quantity} x {item.name}")
        

        if itemCounter == 1:            # additionally the total quantity of items in the shoppingcart is printed

            print(f"There is one item in the shopping cart")
        else:

            print(f"There is a total of {itemCounter} items in the shopping cart")


class Item:                             # create class Item 


    def __init__(self, name, quantity=1): # every item is initialized with a name and a quantity, the default quantity is 1

        self.quantity = quantity

        self.name = name



