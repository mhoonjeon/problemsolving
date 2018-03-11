# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

num_of_lines = 2
for i in range(num_of_lines):
    if i == 0:
        total_num = int(input())
    else:
        num_list = [int(x) for x in input().split()]

local_min = {"i": 0, "j": 0, "diff": 1000000000}
for i in range(total_num):
    for j in range(total_num):
        if i != j:
            diff = abs(num_list[i] - num_list[j])
            if local_min["diff"] > diff:
                local_min["i"] = i
                local_min["j"] = j
                local_min["diff"] = diff
            elif local_min["diff"] == diff:
                if num_list[local_min["i"]] + num_list[local_min["j"]] > num_list[i] + num_list[j]:
                    local_min["i"] = i
                    local_min["j"] = j

if num_list[local_min['i']] < num_list[local_min['j']]:
    print(num_list[local_min['i']], num_list[local_min['j']])
else:
    print(num_list[local_min['j']], num_list[local_min['i']])
