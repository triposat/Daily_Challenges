from bisect import insort, bisect_left
def Smallestonleft(arr,  n):
    stack = []
    res = []
    res.append(-1)
    stack.append(arr[0])
    for i in range(1, n):
        insort(stack, arr[i])
        leftInd = bisect_left(stack, arr[i])
        if leftInd:
            res.append(stack[leftInd-1])
        else:
            res.append(-1)
    return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = Smallestonleft(arr, n);
    for each in res:
        print(each,end=' ')
    print()




# } Driver Code Ends