class Solution:
    def findMaxAverage(self, arr, n, k):
        add = sum(arr[:k])
        curAdd=add
        ans = 0
        for i in range(1, n-k+1):
            add = add-arr[i-1]+arr[i+k-1]
            if curAdd < add:
                add = curAdd
                ans = i
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxAverage(arr, n, k)
        for i in range(ans, ans+k):
            print(arr[i], end=" ")
        print()
        tc -= 1
# } Driver Code Ends