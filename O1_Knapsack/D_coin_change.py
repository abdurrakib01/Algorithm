def coinchange(c, t):
    n = len(c)
    m = {}
    m[(0,0)] = 0
    for i in range(1, t+1):
        m[(0, i)] = 500
    for i in range(1, n+1):
        for j in range(0, t+1):
            if c[i-1] <= j:
                v1 = m[(i - 1, j)]
                v2 = 1 + m[(i, j - c[i-1])]
                m[(i, j)] = min(v1, v2)
            else:
                m[(i, j)] = m[(i - 1, j)]
    y = m[(n, t)]
    print(y)
    x = t
    for i in range(n, 0, -1):
        if y <= 0:
            break
        if y == m[(i - 1, x)]:
            continue
        else:
            print(c[i - 1])
            y = y - c[i - 1]
            x = x - c[i-1]
coin = [2, 5, 8, 12]
t = 16
x = coinchange(coin, t)