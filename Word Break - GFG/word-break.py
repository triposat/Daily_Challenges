def wordBreak(line, wordDict):
    wordDict = set(wordDict)
    dp = [0]*len(line)
    for i in range(len(dp)):
        for j in range(i+1):
            w2Check = line[j:i+1]
            if w2Check in wordDict:
                if j == 0:
                    dp[i] += 1
                else:
                    dp[i] += dp[j-1]
    return dp[len(line)-1] > 0
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		res = wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends