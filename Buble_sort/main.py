array = [5, 4, 7, 8, 2, 6]
x = sorted(array)
for z in range(0, len(array)-1):
    for y in range(0, len(array)-1):
        if array[y] > array[y+1]:
            w = array[y]
            array[y] = array[y+1]
            array[y+1] = w
print(array)