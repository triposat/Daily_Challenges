def greaterElement(arr,  n):
    arrS = sorted(arr)
    d = {arrS[i]: i for i in range(len(arrS))}
    for i in range(n):
        idx = d[arr[i]]
        if idx+1 == n:
            arr[i] = -10000000
        else:
            arr[i] = arrS[idx+1]
    return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = greaterElement(arr, n);
    ans = ""
    for i in res:
        if(i == -10000000):
            ans += "_ "
        else:
            ans += str(i)+" "
    print(ans)



# } Driver Code Ends