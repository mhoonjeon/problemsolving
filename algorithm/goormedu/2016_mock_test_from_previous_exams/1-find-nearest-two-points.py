"""
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
"""

if __name__ == '__main__':
    num = int(input())
    n_list = [int(x) for x in input().split()]

    sorted_list = sorted(n_list)

    # 첫번째 케이스를 미리 temp min값에 넣어두자
    temp_min = sorted_list[1] - sorted_list[0]
    sum = sorted_list[1] + sorted_list[0]
    num1, num2 = sorted_list[0], sorted_list[1]

    for i in range(len(sorted_list) - 1):
        local_min = sorted_list[i+1] - sorted_list[i]
        # 이미 정렬되어 있으므로 두개의 합이 최소가 되는지 비교할 필요가 없다.
        if (sorted_list[i+1] - sorted_list[i] < temp_min):
            temp_min = local_min
            num1, num2 = sorted_list[i], sorted_list[i+1]

    print(num1, num2)
