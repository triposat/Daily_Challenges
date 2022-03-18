import bisect
class Solution:
    # Instead of bisect_right, we can also use this upper_bound function...
    def upper_bound(self, arr, x):
        low = 0
        high = len(arr)
        while low < high:
            mid = (low+high) >> 1
            if arr[mid] < x:
                low = mid+1
            else:
                high = mid-1
        return low

    def minSteps(self, arr, n, k):
        arr.sort()
        pre = 0
        s = sum(arr)
        prefix = []
        for num in arr:
            if len(prefix) == 0:
                prefix.append(num)
            else:
                prefix.append(num+prefix[-1])
        coins = (1 << 31)
        for i in range(n):
            if i != 0 and arr[i] == arr[i-1]:
                pre += arr[i]
                continue
            index = bisect.bisect_right(arr, arr[i]+k)
            if index > n:
                index = n
            temp = s-(prefix[index-1])
            temp = (temp-((arr[i]+k)*(n-index)))
            coins = min(coins, pre+temp)
            pre += arr[i]
        return coins
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.minSteps(A,N,K))
# } Driver Code Ends