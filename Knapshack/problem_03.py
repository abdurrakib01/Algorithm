def insertionsort(array):
    for y in range(1, len(array)):
        x = array[y]
        while (array[y - 1] > x) and y > 0:
            z = array[y - 1]
            array[y - 1] = array[y]
            array[y] = z
            y = y - 1
    return array
def binary_search(array, key):
    start_point = 0
    end_point = len(array) - 1
    found = 0
    while start_point <= end_point:
        mid_point = (start_point + end_point) // 2
        if array[mid_point] == key:
            print(f"key placed in {mid_point} position of array")
            found = 1
            break
        elif key > array[mid_point]:
            start_point = mid_point + 1
        else:
            end_point = mid_point - 1
    if found == 0:
        print("can't found key in array")
arr = [5,3,8,2,1]
arr1 =insertionsort(arr)
print(arr1)
key = int(input())
binary_search(arr1, key)
