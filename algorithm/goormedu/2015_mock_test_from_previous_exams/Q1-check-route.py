# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def can_traverse(a):
    i = j = 0
    try:
        while i < 8 and j < 8:
            val = a[i][j]

            if i == 7 and j == 7:
                return "YES"

            elif val == 1 or val == 3:
                if a[i][j+1] != 1 and a[i][j+1] != 4:
                    return "NO"
                j += 1

            elif val == 2 or val == 4:
                if a[i+1][j] != 2 and a[i+1][j] != 3:
                        return "NO"
                i += 1

            else:
                return "NO"

    except IndexError:
        return "NO"


if __name__ == '__main__':
    num = int(input())

    for _ in range(num):
        a = []
        for _ in range(8):
            a.append([int(x) for x in input().split()])
        print(can_traverse(a))
