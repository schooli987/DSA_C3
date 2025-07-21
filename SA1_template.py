groceries = [
    {"name": "Milk", "freshness": 30},
    {"name": "Yogurt", "freshness": 90},
    {"name": "Cheese", "freshness": 20},
    {"name": "Butter", "freshness": 75},
    {"name": "Cream", "freshness": 10}
]

def bubble_sort_by_freshness(items):
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j]['freshness'] > items[j+1]['freshness']:
                items[j], items[j+1] = items[j+1], items[j]

bubble_sort_by_freshness(groceries)

print("Sorted by Freshness (Low to High):")
for item in groceries:
    print(item)