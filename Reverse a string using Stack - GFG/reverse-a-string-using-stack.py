#{ 
#Driver Code Starts

 # } Driver Code Ends
def reverse(S):
    ans=""
    hey=[]
    for i in S:
        hey.append(i)
    for i in range(len(S)):
        ans+=hey.pop()
    return ans
    #Add code here

#{ 
#Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
#} Driver Code Ends