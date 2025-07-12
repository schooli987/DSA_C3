from datetime import datetime

groceries = [
    {"name": "Corn", "expiry": "2025-02-01"},
    {"name": "Beans", "expiry": "2024-12-15"},
    {"name": "Peas", "expiry": "2024-10-05"},
    {"name": "Tomato Paste", "expiry": "2025-01-10"}
]

def bubble_sort_by_expiry(items):
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            date_j = datetime.strptime(items[j]['expiry'], "%Y-%m-%d")
            date_next = datetime.strptime(items[j+1]['expiry'], "%Y-%m-%d")
            if date_j > date_next:
                items[j], items[j+1] = items[j+1], items[j]

bubble_sort_by_expiry(groceries)

print("Sorted by Expiry Date (Earliest First):")
for item in groceries:
    print(item)
