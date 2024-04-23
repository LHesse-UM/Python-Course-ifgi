class Shoppingcart:

    def __init__(self):
        self.shoppingList = []
    
    def addItem(self, item):
        self.shoppingList.append(item)
        print(f"added {item.name} to shopping cart")


    def removeItem(self, name):
        for item in self.shoppingList:
            if item.name == name:
                self.shoppingList.remove(item)
                print(f"removed {name} from shopping cart")

    def displayItems(self):
        print("The following items are in the shopping cart:")
        itemCounter = 0
        for item in self.shoppingList:
            itemCounter = itemCounter + item.quantity
            print(f"{item.quantity} x {item.name}")
        
        if itemCounter == 1:
            print(f"There is one item in the shopping cart")
        else:
            print(f"There is a total of {itemCounter} items in the shopping cart")

class Item:

    def __init__(self, name, quantity):
        self.quantity = quantity
        self.name = name


