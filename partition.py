def inisialiseP():
    try:
        with open("p.txt", "a+") as f:
            data = f.read()
            if len(data) > 0:
                return list(map(int, data.replace("\n", " ").split()))
            else:
                f.write("1\n1")
                return [1, 1]
    except:
        with open("p.txt", "w") as f:
            f.write("1\n1")
        return [1, 1]

def parition(pArr, x, y):
    _x, _y, tempArr = x, y, pArr
    a = temp = sub = xDiff = 0
    b = count = yDiff = 1

    while count > 0:
        if a == 4:
            a = -1
        else:
            count = (len(tempArr)-1) - sub
            if count >= 0:
                if a < 2:
                    temp += tempArr[count]
                else:
                    temp = temp - tempArr[count]

                if b % 2 == 0:
                    sub += _y[yDiff]
                    yDiff += 1
                else:
                    sub += _x[xDiff]
                    xDiff += 1
                b += 1
        a += 1

    return temp

def main():
    p = inisialiseP()
    counter = 0

    n = int(input("enter n: "))

    if n+1 > len(p):
        x, y = [i for i in range(1, 11)], [i for i in range(1, 22, 2)]

        while len(p) < n+1:
            if counter % 10 == 0:
                x.append(x[-1]+1)
                y.append(y[-1]+2)

            val = parition(p, x, y)
            with open("p.txt", "a") as f:
                f.write("\n"+str(val))
            p.append(val)

    print("p(" + str(n) + ") = " + str(p[n]))

main()
