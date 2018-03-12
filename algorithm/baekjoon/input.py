import unittest

input_list = []
while True:
    input = input()
    if input:
        input_list.append(input)
    else:
        break

for line in input_list:
    print(line)


class UnitTest(unittest.TestCase)
