def partition(array, p, r):
    x = array[r]
    i = p-1
    for j in range(p,  r-1):
        if array[j] <= x:
            i = i+1
            z = array[i]
            array[i] = array[j]
            array[j] = z
    y = array[i+1]
    array[i+1] = array[r]
    array[r] = y
    a = i+1
    return a

def Quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        Quick_sort(array, p, q-1)
        Quick_sort(array, q+1, r)
array_test = [3, 2,7,5,4]
p = 0
r = len(array_test)-1
Quick_sort(array_test, p, r)
print(array_test)