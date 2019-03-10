def setup(i, j):
    global size
    global chess
    global arr
    global deep
    global count

    x = [ 2, 2, 1, -1, -2, -2, -1,  1]
    y = [-1, 1, 2,  2,  1, -1, -2, -2]

    chess[i][j] = count
    arr.append(count)
    deep += 1

    temp = []
    for k in range(len(x)):
        x0 = i + x[k]
        y0 = j + y[k]
        c = 0
        for l in range(len(x)):
            x1 = x0 + x[l]
            y1 = y0 + y[l]
            if (0 <= x1 < size) and (0 <= y1 < size) and chess[x1][y1] == 0:
                c += 1
        temp.append((c,k))
        temp = sorted(temp)
    if len(arr) == size*size:
        return True
    for k in temp:
        x0 = i + x[k[1]]
        y0 = j + y[k[1]]
        if (0 <= x0 < size) and (0 <= y0 < size) and chess[x0][y0] == 0:
            count += 1
            if(setup(x0, y0)):
                return True

    chess[i][j] = 0
    count -= 1
    arr.pop()
    return False


if __name__ == "__main__":
    arr = []
    deep = 0
    size = 8
    chess = [[0 for _ in range(size)] for _ in range(size)]
    count = 1
    setup(5, 5)

    for i in chess:
        print(i)
    print(deep)