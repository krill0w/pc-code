array = [9, 2, 8, 4, 7, 1, 5, 6]
checks = 0
swaps = 0

for i in range(1, len(array)):
    checks += 1
    x = array[i]
    j = i - 1

    # Compare x with each element on the left of it until an element smaller than it is found
    # For descending order, change x<array[j] to x>array[j].
    while j >= 0 and x < array[j]:
        checks += 1
        array[j + 1] = array[j]
        swaps += 1
        j = j - 1

    # Place x at after the element just smaller than it.
    array[j + 1] = x
    swaps += 1

print(array)
print(checks)
print(swaps)