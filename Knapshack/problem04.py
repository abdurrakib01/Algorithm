x = int(input())
array = list(str(input()).split())
for y in range(1, len(array)):
    x = array[y]
    while (array[y-1] > x) and y > 0:
        z = array[y-1]
        array[y-1] = array[y]
        array[y] = z
        y = y-1
print(array)
name = str(input())
f = 0
for i in range(0, len(array)):
    if array[i] == name:
        print("find")
        f = 1
        break
if f == 0:
    print("cant find")
