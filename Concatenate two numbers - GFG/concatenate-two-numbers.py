from collections import defaultdict
class Solution:
    def countPairs(self, N, x, num): 
        mape=defaultdict(int)
        x=str(x)
        for ele in num:
            ele=str(ele)
            if x.startswith(ele) or x.endswith(ele):
                mape[ele]+=1
        # print(mape)
        ans=0
        for ele in list(mape):
            if x==2*ele:
                ans+=(mape[ele])*(mape[ele]-1)
            elif x.endswith(ele):
                ans+=(mape[ele])*mape[x[:-len(ele)]]
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