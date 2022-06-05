def initializePXY(path, hint):
    try:
        with open(path, "r+") as f:
            data = f.read().split()
            if len(data) < 2:
                f.write(hint)
                return map(int, hint.split())
            return list(map(int, data))
    except FileNotFoundError:
        with open("y.txt", "w") as f:
            f.write(hint)
        return map(int, hint.split())


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
    p = initializePXY("p.txt", "1 1")
    x = initializePXY("x.txt", "1 2")
    y = initializePXY("y.txt", "1 3")

    n = int(input("enter n: "))

    while len(p) <= n:
        try:
            val = parition(p, x, y)
        except:
            x[len(x):-2] = [x[-1]+1]
            y[len(y):-2] = [y[-1]+2]
            with open("x.txt", "w") as f:
                f.write(" ".join(map(str, x)))
            with open("y.txt", "w") as f:
                f.write(" ".join(map(str, y)))
            val = parition(p, x, y)

        with open("p.txt", "a") as f:
            f.write(" " + str(val) + " ")
        p[len(p):-2] = [val]

    print("p(" + str(n) + ") = " + str(p[n]))

main()
