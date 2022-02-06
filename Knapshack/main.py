doller = list(map(int, str(input()).split()))
weight = list(map(int, str(input()).split()))
bag = int(input())
unit = []
price = 0
for i in range(0, len(weight)):
    x = doller[i] / weight[i]
    unit.append(x)
for i in range(0, len(unit)-1):
    max = i
    for j in range(i+1, len(unit)):
        if unit[j] > unit[max]:
            max = j
    if max != i:
        x = unit[i]
        y = doller[i]
        z = weight[i]
        unit[i] = unit[max]
        unit[max] = x
        weight[i] = weight[max]
        weight[max] = z
        doller[i] = doller[max]
        doller[max] = y
print(unit)
print(doller)
print(weight)
while bag > 0:
    max = 0
    for j in range(0, len(unit)):
        if unit[j] > unit[max]:
            max = j
    if weight[max] <= bag:
        bag -= weight[max]
        price += doller[max]
        print(f"X{max+1} = {weight[max]} kg")

    else:
        remain = bag*(unit[max])
        price += remain
        print(f"X{max+1} = {bag} kg")
        bag = 0
    unit[max] = 0
print(f"Max price = {price}")
