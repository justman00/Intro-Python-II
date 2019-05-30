# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def dropItem(self, itemName):
        for item in self.items:
            if item.name == itemName:
                self.items.remove(item)

    # def get_item(self, itemName):
    #     itemNames = [item.name for item in self.items if item.name == itemName]

    #     if len(itemNames) == 0:
    #         print("No such item")
    #     else:
    #         print(f"Here is your {itemName}")

    def get_items(self):
        itemNames = [item.name for item in self.items]

        if len(itemNames) == 0:
            print("No items")
        else:
            print(*itemNames)

    def getItem(self, itemName):
        items = [item for item in self.items if item.name == itemName]
        return items[0]
