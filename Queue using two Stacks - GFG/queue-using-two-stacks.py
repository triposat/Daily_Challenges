#User function Template for python3

#Function to push an element in queue by using 2 stacks.
def Push(x,s1,s2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    #code here
    s1.append(x)

#Function to pop an element from queue by using 2 stacks.
def Pop(s1,s2):
    
    '''
    stack1: list
    stack2: list
    '''
    if not s1:
        return -1
    for _ in range(len(s1)):
        s2.append(s1.pop())
    k=s2.pop()
    if s2:
        for _ in range(len(s2)):
            s1.append(s2.pop())
    return k
    #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry=int(input())
        qtyp_qry=list(map(int, input().strip().split()))
        
        i=0
        stack1=[]
        stack2=[]
        while i <len(qtyp_qry):
            #print(i)
            if qtyp_qry[i]==1:
                Push(qtyp_qry[i+1],stack1,stack2)
                #print(i)
                i+=2
            else:
                print(Pop(stack1,stack2),end=' ')
                i+=1
                
        print()
# } Driver Code Ends