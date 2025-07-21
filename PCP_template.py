# Step 1: Input number of items
n = int(input("Enter number of items in inventory: "))

# Step 2: Create empty list to store item names
inventory = []

# Step 3: Get item names from user
for i in range(n):
    item = input("Enter item name: ")
    inventory.append(item)