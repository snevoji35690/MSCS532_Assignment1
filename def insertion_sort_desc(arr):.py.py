def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements that are less than key
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [5, 2, 4, 6, 1, 3,10]
insertion_sort_desc(arr)
print("Sorted array (descending):", arr)
