# 804. Unique Morse Code Words


class Solution:
    def __init__(self):
        self.morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                           "....", "..", ".---", "-.-", ".-..", "--", "-.",
                           "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                           "...-", ".--", "-..-", "-.--", "--.."]
        self.alphabets = "abcdefghijklmnopqrstuvwxyz"
        self.alpha_morse = dict(zip(self.alphabets, self.morse_code))

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_set = []
        for word in words:
            s = ""
            for ch in word:
                s += self.alpha_morse[ch]
            word_set.append(s)

        return len(list(set(word_set)))


""" https://leetcode.com/problems/unique-morse-code-words/discuss/120675/\
    Easy-and-Concise-Solution-C++JavaPython

def uniqueMorseRepresentations(self, words):
    d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
         "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
         "..-", "...-", ".--", "-..-", "-.--", "--.."]
    return len({''.join(d[ord(i) - ord('a')] for i in w) for w in words})
"""

# 771. Jewels and Stones, 98.33%
# https://leetcode.com/problems/jewels-and-stones/description/


def numJewelsInStones(self, J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    count = 0
    for jewel in J:
        for stone in S:
            if jewel == stone:
                count += 1

    return count


""" https://leetcode.com/problems/jewels-and-stones/discuss/113553/\
    Easy-and-Concise-Solution-using-hash-set-C++JavaPython
def numJewelsInStones(self, J, S):
        setJ = set(J)
        return sum(s in setJ for s in S)
"""

# 806. Number of Lines To Write String
# https://leetcode.com/problems/number-of-lines-to-write-string/


def numberOfLines(self, widths, S):
    """
    :type widths: List[int]
    :type S: str
    :rtype: List[int]
    """
    lines = 1
    line_width = 0

    for ch in S:
        index = ord(ch) - ord('a')
        if line_width + widths[index] <= 100:
            line_width += widths[index]
        else:
            lines += 1
            line_width = widths[index]

    return [lines, line_width]


""" https://leetcode.com/problems/number-of-lines-to-write-string/discuss/\
    120666/Easy-Solution-6-lines-C++JavaPython
def numberOfcurs(self, widths, S):
    res, cur = 1, 0
    for i in S:
        width = widths[ord(i) - ord('a')]
        res += 1 if cur + width > 100 else 0
        cur = width if cur + width > 100 else cur + width
    return [res, cur]
"""
