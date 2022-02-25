class Solution:
    def moveRobots (self, s1, s2):
        temp1=s1.replace("#", "")
        temp2=s2.replace("#", "")
        if temp1!=temp2:
            return "No"
        n=len(s1)
        cnt=0
        for i in range(n):
            if s1[i]=='B':
                cnt+=1
            if s2[i]=='B':
                cnt-=1
            if cnt<0:
                return "No"
        cnt=0
        for i in range(n)[::-1]:
            if s1[i]=='A':
                cnt+=1
            if s2[i]=='A':
                cnt-=1
            if cnt<0:
                return "No"
        return "Yes"
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        s1 = input()
        s2 = input()

        ob = Solution()
        print(ob.moveRobots(s1, s2))

# } Driver Code Ends