def partitions(reste, maximum, courant):
    if reste == 0:
        print(courant)
        return

    for i in range(min(reste, maximum), 0, -1):
        courant.append(i)
        partitions(reste - i, i, courant)
        courant.pop()

n = 4
partitions(n, n, [])