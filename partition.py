def parition(pArr, x, y):
    a, val, sub, xDiff = -1, 0, 0, 0
    b, count, yDiff = 1, 1, 1

    while True:
        a += 1
        aflg, bflg = 0, 0
        if a == 4:
            a = -1
            continue

        count = len(pArr) - sub - 1
        if count < 0:
            break

        if a < 2:
            val += pArr[count]
            aflg = 1
        
        if b % 2 == 0:
            sub += y[yDiff]
            yDiff += 1
            bflg = 1

        if aflg == 0:
            val -= pArr[count]

        if bflg == 0:
            sub += x[xDiff]
            xDiff += 1
        
        b += 1

    return val

def main():
    p = [1, 1]
    x = [1, 2]
    y = [1, 3]

    n = int(input("enter n: "))

    while len(p) <= n:
        try:
            val = parition(p, x, y)
        except:
            x[len(x):-2] = [x[-1]+1]
            y[len(y):-2] = [y[-1]+2]
            val = parition(p, x, y)

        val = parition(p, x, y)
        p[len(p):-2] = [val]

        # p.append(val)

    print("p(" + str(n) + ") = " + str(p[n]))

if __name__ == "__main__":
    main()
