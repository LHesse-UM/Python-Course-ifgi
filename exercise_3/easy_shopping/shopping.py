class Shoppingcart:

    def __init__(self):
        self.shoppingList = []
    
    def addItem(self, item):
        self.shoppingList.append(item)


    def removeItem(self, name):
        for item in self.shoppingList:
            if item.name == name:
                self.shoppingList.remove(item)

    def displayItems(self):
        print("Es befinden sich folgende Elemente im Einkaufswagen:")
        itemCounter = 0
        for item in self.shoppingList:
            itemCounter = itemCounter + item.quantity
            print(item.name)
        
        if itemCounter == 1:
            print(f"Insgesamt gibt es einen Artikel im Einkaufswagen")
        else:
            print(f"Insgesamt gibt es {itemCounter} Artikel im Einkaufswagen")

class Item:

    def __init__(self, name, quantity):
        self.quantity = quantity
        self.name = name


