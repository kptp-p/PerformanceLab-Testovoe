
def round_mass(total, n):
    total += ''.join([str(x) for x in range(2, n + 1)]) + '1'
    return total


def pathfinder(n: int, m: int) -> str:
    total = '1'
    current_sym = 0
    path = ''
    step = m - 1

    while True:
        if len(total) <= current_sym + step:
            total = round_mass(total, n)
            continue
        path += total[current_sym]
        if total[current_sym + step] == '1':
            return path
        current_sym += step


print(pathfinder(int(input()), int(input())))
