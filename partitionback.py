def partitions(reste, max_val, part):
    if reste == 0:
        print(part)
        return

    for i in range(min(max_val, reste), 0, -1):
        part.append(i)
        partitions(reste - i, i, part)
        part.pop()      # backtracking

n = 4
partitions(n, n, [])