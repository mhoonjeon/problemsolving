# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

num = int(input())
n_list = sorted([int(x) for x in input().split()])


def find_max(n_list):
    n_list = sorted(n_list, key=lambda integer: str(integer)[0])


min_num = ""
for i in n_list:
    min_num += str(i)

max_num = ""
for i in reversed(n_list):
    max_num += str(i)


print(int(min_num)+int(max_num))
