import os

os.system("clear")

def inisialiseP():
    pArr = []

    f = open("p.txt", "r+")
    data = f.read(100)
    f.seek(0)
    if len(data) > 0:
        for i in f:
            x = i.replace("\n", "")
            pArr.append(int(x))
    else:
        f.write("1\n1")
        pArr = [1, 1]

    f.close()

    return pArr

def parition(pArr, x, y):
    _x = x
    _y = y
    a = temp = sub = xDiff = 0
    b = count = yDiff = 1
    tempArr = pArr

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
        x = [1, 2, 3, 4, 5, 6, 7, 8,9,10]
        y = [1, 3, 5, 7, 9, 11, 13, 15,17,19,21]
        while len(p) < n+1:
            if counter % 10 == 0:
                x.append(x[-1]+1)
                y.append(y[-1]+2)

            val = parition(p, x, y)
            f = open("p.txt", "a")
            f.write("\n"+str(val))
            f.close()
            p.append(val)

    print("p(" + str(n) + ") = " + str(p[n]))

main()
