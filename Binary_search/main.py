x = int(input())
array = list(map(int, str(input()).split()))
key = int(input())
start_point = 0
end_point = len(array)-1
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
