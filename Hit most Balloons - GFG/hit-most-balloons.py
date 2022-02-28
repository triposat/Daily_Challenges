class Solution:
    def mostBalloons(self, N, arr):
        res = 1
        for i in range(len(arr)):
            hashMap = {}
            temp = 0
            for j in range(len(arr)):
                x1, y1 = arr[i][0], arr[i][1]
                x2, y2 = arr[j][0], arr[j][1]
                yDif = (y2-y1)
                xDif = (x2-x1)
                if xDif == 0 and yDif == 0:
                    temp += 1
                else:
                    slope = float("inf") if yDif == 0 else xDif/yDif
                    hashMap[slope] = hashMap.get(slope, 0)+1
            res = max(res, max(hashMap.values())+temp)
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input()) 
        arr=[[] for j in range(N)]
        for j in range(2): 
            inp = [int(i) for i in input().split()] 
            for i in range(N): 
                arr[i].append(inp[i])
        ob = Solution()
        print(ob.mostBalloons(N, arr))
        
        T -= 1
# } Driver Code Ends