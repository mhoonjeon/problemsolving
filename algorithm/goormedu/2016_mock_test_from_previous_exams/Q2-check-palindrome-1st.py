# 최초 답안
# 코드를 보면 말도 안되는 수준 ^^;;


def check_pal(n):
    num = str(n)
    for i in range(len(num)//2):
        if num[i] == num[len(num)-1-i]:
            pass
        else:
            return False
    print(num)
    return True


def reverse(n):
    s = ''
    num = str(n)
    for ch in reversed(num):
        s += ch
    return int(s)


def func(n):
    return int(n) + reverse(n)


n = int(input())
d = []


def main(n):
    for i in range(3):
        if i == 0:
            d.append(n + reverse(n))
            if check_pal(d[i]):
                print(d[i])
                return True
        else:
            d.append(func(d[i-1]))


if not main(n):
    print(-1)
