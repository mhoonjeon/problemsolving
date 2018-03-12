# 20개의 테스트중 약 6개는 통과못함


def check_pal(n):
    # 팔린드롬인지 아닌지 확인
    if str(n) == str(n)[::-1]:
        return True
    return False


def r(n):
    # n은 int
    return int(str(n)[::-1])


def f(n):
    return n + r(n)


if __name__ == "__main__":
    num = int(input())
    ret = -1

    temp = num
    for _ in range(3):
        temp = f(temp)
        if check_pal(temp) and temp < 10000:
            ret = temp
            break

print(ret)
