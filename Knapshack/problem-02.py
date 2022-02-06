x = int(input())
array = list(map(int, str(input()).split()))
for y in range(1, len(array)):
    x = array[y]
    while (array[y-1] > x) and y > 0:
        z = array[y-1]
        array[y-1] = array[y]
        array[y] = z
        y = y-1
        print(array)
print(array)
