# Step 1: Input number of items
n = int(input("Enter number of items in inventory: "))

# Step 2: Create empty list to store item names
inventory = []

# Step 3: Get item names from user
for i in range(n):
    item = input("Enter item name: ")
    inventory.append(item)

# Step 4: Bubble Sort using simple loop
for i in range(n):
    for j in range(n - 1 - i):
        if inventory[j] > inventory[j + 1]:
            # Swap items
            temp = inventory[j]
            inventory[j] = inventory[j + 1]
            inventory[j + 1] = temp

# Step 5: Print sorted list
print("\n✅ Sorted Inventory List (Restocked Order):")
for item in inventory:
    print(item)
