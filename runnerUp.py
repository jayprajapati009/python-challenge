if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrFin = []
    for x in arr:
        if x not in arrFin:
            arrFin.append(x)

    arrFin = sorted(arrFin)

    print(arrFin[len(arrFin)-2])
