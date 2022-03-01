from collections import defaultdict


class Solution:
    def countPairs(self, N, X, numbers):
        hasMap = defaultdict(int)
        X = str(X)
        for ele in numbers:
            ele = str(ele)
            if X.startswith(ele) or X.endswith(ele):
                hasMap[ele] += 1
        ans = 0
        for ele in list(hasMap):
            if X == 2*ele:
                ans += (hasMap[ele])*(hasMap[ele]-1)
            elif X.endswith(ele):
                ans += (hasMap[ele])*hasMap[X[:-len(ele)]]
        return ans
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        numbers = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countPairs(N, X, numbers)
        print(ans)


# } Driver Code Ends