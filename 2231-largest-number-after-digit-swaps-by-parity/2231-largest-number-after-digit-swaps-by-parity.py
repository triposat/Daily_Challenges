class Solution:
    def largestInteger(self, num: int) -> int:
        num = [int(i) for i in str(num)]
        n = len(num)
        even = [i for i in num if i % 2 == 0]
        odd = [i for i in num if i % 2 != 0]
        even.sort()
        odd.sort()
        ans = 0
        for i in range(n):
            if num[i] % 2 == 0:
                ans = ans*10+even.pop()
            else:
                ans = ans*10+odd.pop()
        return ans