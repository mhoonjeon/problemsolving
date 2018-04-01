# 344. Reverse string

def reverseString(self, s):
    """
    :type s: str
    :rtype: str
    """
    return s[::-1]


""" Classic
def reverseString(self, s):
    r = list(s)
    i, j  = 0, len(r) - 1
    while i < j:
        r[i], r[j] = r[j], r[i]
        i += 1
        j -= 1

    return "".join(r)
"""


# 557. Reverse Words in a String III: 96.96%

def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    wlist = s.split()
    new_s = []
    for w in wlist:
        new_s.append(w[::-1])
    return " ".join(new_s)

""" https://leetcode.com/problems/reverse-words-in-a-string-iii/discuss/101909/1-line-Ruby-Python
    Faster solution
def reverseWords(self, s):
    return ' '.join(s.split()[::-1])[::-1]

    More obvious one-liner
def reverseWords(self, s):
    return ' '.join(x[::-1] for x in s.split())
"""


# 811. Subdomain Visit Count

def subdomainVisits(self, cpdomains):
    """
    :type cpdomains: List[str]
    :rtype: List[str]
    """
    from collections import defaultdict
    m = defaultdict(lambda: 0)
    for cpdomain in cpdomains:
        count, domain = cpdomain.split()
        domain = domain.split('.')
        d_name = []
        for name in domain[::-1]:
            d_name = [name] + d_name
            m['.'.join(d_name)] += int(count)

    ret = []
    for domain, count in m.items():
        ret.append("{} {}".format(count, domain))
    return ret

""" 비슷한데 마지막 줄 list comprehension으로 축약가능
https://leetcode.com/problems/subdomain-visit-count/solution/

def subdomainVisits(self, cpdomains):
    ans = collections.Counter()
    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        frags = domain.split('.')
        for i in xrange(len(frags)):
            ans[".".join(frags[i:])] += count

    return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
"""

# 500. Keyboard Row

def findWords(self, words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    m = {
        'A': 2, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 2,
        'G': 2, 'H': 2, 'I': 1, 'J': 2, 'K': 2, 'L': 2,
        'M': 3, 'N': 3, 'O': 1, 'P': 1, 'Q': 1, 'R': 1,
        'S': 2, 'T': 1, 'U': 1, 'V': 3, 'W': 1, 'X': 3, 'Y': 1, 'Z':3
    }
    import copy
    ret = copy.deepcopy(words)
    for word in words:
        comp = m[word[0].upper()]
        for ch in word:
            if m[ch.upper()] != comp:
                ret.remove(word)
                break
    return ret

""" 가장 빠른 방법
    https://leetcode.com/problems/keyboard-row/discuss/97913/Easy-understand-solution-in-7-lines-for-everyone

def findWords(self, words):
    keyboards = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    ans = []
    for w in words:
        if any(set(w.lower()) <= set(r) for r in keyboards):
            ans.append(w)

    return ans
"""
