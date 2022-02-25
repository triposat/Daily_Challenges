from itertools import zip_longest


class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1 = v1.split(".")
        v2 = v2.split(".")
        for x, y in zip_longest(v1, v2, fillvalue="0"):
            if int(x) > int(y):
                return 1
            if int(x) < int(y):
                return -1
        return 0