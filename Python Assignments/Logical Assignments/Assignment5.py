stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    total_items = 0
    print ("Inventory:")
    for item in inventory:
        print(str(inventory[item]) + ' ' + item)
        total_items += inventory[item]
    print("Total number of items: " + str(total_items))

if __name__ == '__main__':
    display_inventory(stuff)