def find_max(arr):
    maximum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]

    return maximum


# Hardcoded input
arr = [10, 25, 7, 99, 43, 18]

result = find_max(arr)

print("Maximum:", result)