def FindRunnerUP(lst):
    return sorted(set(lst))[-2]


if __name__ == '__main__':

    n = int(input())
    arr = map(int, input().split())
    print(FindRunnerUP(arr))

    """
    Code V 2.0
    n = int(input())
    arr = map(int, input().split())
    arrFin = []
    for x in arr:
        if x not in arrFin:
            arrFin.append(x)

    print(FindRunnerUP(arrFin))
    """

    """ 
    Code V 1.0

    n = int(input())
    arr = map(int, input().split())
    arrFin = []
    for x in arr:
        if x not in arrFin:
            arrFin.append(x)

    arrFin = sorted(arrFin)

    print(arrFin[len(arrFin)-2])
    """
