class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        l = s.split(" ")
        res = ""
        for i in reversed(range(len(l))):
            if (l[i] is not ""):
                res += l[i]
                res += " "
        return res[0: len(res) - 1]
