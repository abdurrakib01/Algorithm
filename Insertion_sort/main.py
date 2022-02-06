array = [5, 4, 7, 8, 2, 6]
for y in range(1, len(array)):
    key = array[y]
    a = y
    while (array[a-1] > key) and a > 0:
        z = array[a-1]
        array[a] = z
        a = a-1
    array[a] = key
    print(array[a])
print(array)
