from math import lcm, gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1:
                stack.append(lcm(stack.pop(), stack.pop()))
        return stack