# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

moeum = ['a', 'e', 'i', 'o', 'u']


def check_rule_one(word):
    for i in range(len(word)-1):
        if word[i] in moeum:
            if word[i+1] in moeum:
                return True
            else:
                i += i
    return False


def check_rule_two(word):
    for i in range(len(word)-2):
        if word[i] not in moeum:
            if word[i+1] not in moeum and word[i+2] not in moeum:
                return True
            else:
                i += i
    return False


data = input().split()

rule_one = 0
rule_two = 0
for word in data:
    if check_rule_one(word):
        rule_one += 1
    if check_rule_two(word):
        rule_two += 1

print(rule_one)
print(rule_two)
