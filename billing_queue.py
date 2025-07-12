queue = [
    {"customer": "Amit", "items": 15},
    {"customer": "Neha", "items": 5},
    {"customer": "John", "items": 3},
    {"customer": "Tina", "items": 8}
]

def bubble_sort_by_items(queue):
    n = len(queue)
    for i in range(n):
        for j in range(0, n-i-1):
            if queue[j]['items'] > queue[j+1]['items']:
                queue[j], queue[j+1] = queue[j+1], queue[j]

bubble_sort_by_items(queue)

print("Queue sorted by number of items:")
for c in queue:
    print(c)
