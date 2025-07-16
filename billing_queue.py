# Input as a list of tuples: (Customer Name, Item Count)
queue = [
    ("Amit", 15),
    ("Neha", 5),
    ("John", 3),
    ("Tina", 8)
]

# Bubble Sort based on the item count
n = len(queue)
for i in range(n):
    for j in range(0, n - i - 1):
        if queue[j][1] > queue[j + 1][1]:
            queue[j], queue[j + 1] = queue[j + 1], queue[j]

# Display sorted queue
print("Queue sorted by number of items:")
for customer in queue:
    print(f"Customer: {customer[0]}, Items: {customer[1]}")
