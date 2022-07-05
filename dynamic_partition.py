import partition as pt
    
def initializePXY(path, hint):
    try:
        with open(path, "rb+") as f:
            data = (f.read()).decode('utf-8').split()
            if len(data) < 2:
                f.write(str(hint).encode('utf-8'))
                return list(map(int, hint.split()))
            return list(map(int, data))
    except FileNotFoundError:
        with open(path, "wb") as f:
            f.write(str(hint).encode('utf-8'))
        return list(map(int, hint.split()))

def main():
    n = int(input("enter n: "))

    p = initializePXY("p.bin", "1 1 ")
    x = initializePXY("x.bin", "1 2 ")
    y = initializePXY("y.bin", "1 3 ")

    while len(p) <= n:
        try:
            val = pt.parition(p, x, y)
        except IndexError:
            x[len(x):-2] = [x[-1]+1]
            y[len(y):-2] = [y[-1]+2]
            with open("x.bin", "ab") as f1, open("y.bin", "ab") as f2:
                tmp = str(x[-1]) + " "
                f1.write(tmp.encode('utf-8'))
                tmp = str(y[-1]) + " "
                f2.write(tmp.encode('utf-8'))
            val = pt.parition(p, x, y)

        with open("p.bin", "ab") as f:
            tmp = str(val) + " "
            f.write(tmp.encode('utf-8'))
        p[len(p):-2] = [val]

    print(f"p({n}) = {p[n]}")
    print(f"\nmax: {len(p)-1}")

main()
