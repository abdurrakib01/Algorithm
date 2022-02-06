def Merge_sort(array):
    if len(array) > 1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]

        Merge_sort(left_array)
        Merge_sort(right_array)
        i = 0
        j = 0
        k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
array_test = [5, 4, 7, 8, 2, 6]
Merge_sort(array_test)
print(array_test)