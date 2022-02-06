x = int(input())
array = list(map(int, str(input()).split()))
for i in range(0, len(array)-1):
    mn = i
    for j in range(i+1, len(array)):
        if array[j] < array[mn]:
            mn = j
    if mn != i:
        x = array[i]
        array[i] = array[mn]
        array[mn] = x
print(array)