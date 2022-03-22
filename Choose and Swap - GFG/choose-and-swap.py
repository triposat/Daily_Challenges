class Solution:
    def chooseandswap(self, arr):
        arr = list(arr)
        s = list(set(arr))
        s.sort()
        for i in range(len(arr)):
            if arr[i] in s:
                s.remove(arr[i])
            if not s:
                break
            ch1 = s[0]
            if ch1 < arr[i]:
                ch2 = arr[i]
                for j in range(len(arr)):
                    if arr[j] == ch1:
                        arr[j] = ch2
                    elif arr[j] == ch2:
                        arr[j] = ch1
                break
        return "".join(arr)

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        A = input()
        ans = ob.chooseandswap(A)
        print(ans)


# } Driver Code Ends