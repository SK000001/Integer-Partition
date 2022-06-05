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

    counter, i = 1, 2
    while len(p) <= n:
        if counter % i == 0:
            x[len(x):-2] = [x[-1]+1]
            y[len(y):-2] = [y[-1]+2]
            i += 1

        counter += 1
        val = parition(p, x, y)
        p[len(p):-2] = [val]

        # p.append(val)

    print("p(" + str(n) + ") = " + str(p[n]))

main()
