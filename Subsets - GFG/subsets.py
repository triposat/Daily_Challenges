class Solution:
    def subsets(self, A):
        outer = []
        outer.append([])
        for num in A:
            n = len(outer)
            for i in range(n):
                inner = outer[i][:]
                inner.append(num)
                outer.append(inner)
        return sorted(outer)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        A = list(map(int,input().strip().split()))
        
        ob=Solution()
        result =ob.subsets(A)
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j],end=" ")
                
            print()
            
            

# } Driver Code Ends