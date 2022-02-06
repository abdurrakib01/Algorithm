length = 12
pipe_array = [2, 2, 3, 3, 3, 3, 4, 4, 4, 6, 7, 7]
total_l = 0
for i in range(len(pipe_array)):
    total_l += pipe_array[i]
l_bound = total_l/length
if int(l_bound) != l_bound:
    l_bound += 1
print(l_bound)
