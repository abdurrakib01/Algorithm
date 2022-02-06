x = int(input())
array = list(map(int, str(input()).split()))
change = int(input())
x = len(array)-1
while x >= 0:
    while array[x] <= change:
        change = change-array[x]
        print(array[x])
        if change == 0:
            break
    x = x-1
