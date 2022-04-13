dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}


def addToInventory(inventory, addedItems):
    for loot in addedItems:
        inventory.setdefault(loot, 0)
        for k, v in inventory.items():
            if loot == k:
                inventory[loot] = v + 1


def displayInventory(inventory):
    totalItems = 0
    for k, v in inventory.items():
        print(str(v) + '---' + str(k))
        totalItems += v
    print('Total number of items: ' + str(totalItems))


addToInventory(inv, dragonLoot)
displayInventory(inv)