class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def next_revision(revisions):
            try:
                nxt = revisions.pop()
                if not nxt:
                    nxt = "0"
            except IndexError:
                nxt = "0"
            return nxt

        revisions1 = version1.split(".")
        revisions2 = version2.split(".")
        if len(revisions1) > len(revisions2):
            n = len(revisions1)
        else:
            n = len(revisions2)
        for i in range(n):
            a = int(next_rev(revisions1))
            b = int(next_rev(revisions2))
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0
