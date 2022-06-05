def parition(pArr, x, y):
    a, temp, sub, xDiff = -1, 0, 0, 0
    b, count, yDiff = 1, 1, 1

    while count > 0:
        a += 1
        aflg, bflg = 0, 0
        if a == 4:
            a = -1
            continue

        count = (len(pArr)-1) - sub
        if count < 0:
            break

        if a < 2:
            temp += pArr[count]
            aflg = 1
        
        if b % 2 == 0:
            sub += y[yDiff]
            yDiff += 1
            bflg = 1

        if aflg == 0:
            temp -= pArr[count]

        if bflg == 0:
            sub += x[xDiff]
            xDiff += 1
        
        b += 1

    return temp

def main():
    p = [1, 1]

    n = int(input("enter n: "))

    counter = 1
    x = [1, 2]
    y = [1, 3]
    while len(p) < n+1:
        if counter % 5 == 0:
            x.append(x[-1]+1)
            y.append(y[-1]+2)

        counter += 1
        val = parition(p, x, y)

        p.append(val)

    print("p(" + str(n) + ") = " + str(p[n]))

main()
