def check_pal(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


def r(n):
    # n은 int, 숫자 뒤집기
    return int(str(n)[::-1])


def f(n):
    return n + r(n)


if __name__ == "__main__":
    num = int(input())
    # 일단 1번은 무조건 진행
    num = f(num)

    for i in range(1, 4):
        if check_pal(num):
            #  팰린드롬 넘버이면 탈출
            break

        elif num >= 10000 or i == 3:
            # 탈출 조건
            num = -1
            break

        else:
            num = f(num)

print(num)
