# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def is_in_pairs(s, memo):
    stack = []
    brace_open = ['(', '{', '[']
    brace_close = [')', '}', ']']
    mapping = dict(zip(brace_open, brace_close))

    failed_index = -2  # 성공시 조건

    for i in range(len(s)):
        ch = s[i]
        memo[i] = len(stack)
        if ch in brace_open:
            stack.append(mapping[ch])

        elif ch in brace_close:
            if not stack or ch != stack.pop():
                failed_index = i
                return failed_index
            else:
                memo[i] -= 1

    if failed_index == -2 and stack:
        return -1

    return failed_index


if __name__ == "__main__":
    num = int(input())

    for _ in range(num):
        s = input()
        memo = [0 for _ in range(len(s))]
        if is_in_pairs(s, memo) == -2:
            # 성공시 print memo
            # map 사용도 가능: ' '.join(map(str, memo))
            print(' '.join([str(x) for x in memo]))
        else:
            print(is_in_pairs(s, memo))
