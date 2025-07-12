def bubble_sort(numbers):
    n = len(numbers)

    print("Original List:", numbers)

    for i in range(n):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                # Swap using a temporary variable
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    print("Sorted List:", numbers)

# Example list
my_list = [45, 20, 60, 10, 30]

# Call the function
bubble_sort(my_list)
