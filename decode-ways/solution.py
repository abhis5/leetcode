class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s.startswith("0"):
            return 0
        n = len(s)
        table = [0 for i in range(n + 1)]
        for i in range(n + 1):
            if i is 0:
                table[0] = 1
                continue
            if s[i - 1] == "0":
                table[i] += table[i - 1]
            if i != 1 and "09" < s[i - 2:i] < "27":
                table[i] += table[i - 2]
        return table[n + 1]
