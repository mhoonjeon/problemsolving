# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 문제에서 주어진 테스트만 통과한다. 코너케이스들은 실패하는듯
# 실패 이유, stack이 비어있는데 닫힌 괄호가 오는 경우 stack에 더하지 않는다.


def is_in_pairs(s):
    stack = []
    brace_open = ['(', '{', '[']

    for ch in s:
        if ch in brace_open:
            stack.append(ch)

        if stack:
            if ch == ')' and stack[-1] == '(':
                    stack.pop()
            elif ch == ']' and stack[-1] == '[':
                    stack.pop()
            elif ch == '}' and stack[-1] == '{':
                    stack.pop()

    if stack:
        # 스택에 남아있는게 있는 경우에 False
        return False
    return True


if __name__ == "__main__":
    num = int(input())

    for _ in range(num):
        s = input()
        if is_in_pairs(s):
            print("YES")
        else:
            print("NO")
