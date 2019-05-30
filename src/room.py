# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.w_to = None
        self.s_to = None
        self.e_to = None
        self.n_to = None
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def addItems(self, *items):
        self.items.append(items)

    def dropItem(self, itemName):
        for item in self.items:
            if item.name == itemName:
                self.items.remove(item)

    def __str__(self):
        return f"{self.name}\n  {self.description}"

    def getItem(self, itemName):
        items = [item for item in self.items if item.name == itemName]
        return items[0]

    def get_items(self):
        itemNames = [item.name for item in self.items]

        if len(itemNames) == 0:
            print("No items")
        else:
            print(*itemNames)
