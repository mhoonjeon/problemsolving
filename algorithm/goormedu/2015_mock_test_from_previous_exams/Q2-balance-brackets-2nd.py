# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def is_in_pairs(s):
    stack = []
    brace_open = ['(', '{', '[']
    brace_close = [')', '}', ']']
    mapping = dict(zip(brace_open, brace_close))

    for ch in s:
        if ch in brace_open:
            stack.append(mapping[ch])

        elif ch in brace_close:
            if not stack or ch != stack.pop():
                return False

    return not stack


if __name__ == "__main__":
    num = int(input())

    for _ in range(num):
        s = input()
        if is_in_pairs(s):
            print("YES")
        else:
            print("NO")
