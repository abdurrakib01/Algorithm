def knapsack(v, w, c):
    n = len(v)
    m = {}
    for i in range(c+1):
        m[(0, i)] = 0
    for i in range(1, n+1):
        for j in range(0, c+1):
            if w[i-1] <= j:
                v1 = m[(i-1, j)]
                v2 = v[i-1] + m[(i-1, j-w[i-1])]
                m[(i, j)] = max(v1, v2)
            else:
                m[(i, j)] = m[(i-1, j)]
    y =  m[(n, c)]
    print(y)
    x = c
    for i in range(n, 0, -1):
        if y <= 0:
            break
        if y == m[(i - 1, x)]:
            continue
        else:
            print(w[i - 1])
            y = y - v[i - 1]
            x = x - w[i - 1]
value = [12, 10, 20, 15]
weight = [2, 1, 3, 2]
c = 5
x = knapsack(value, weight, c)