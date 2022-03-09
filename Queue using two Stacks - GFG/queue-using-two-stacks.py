def Push(x, stack1, stack2):
    stack1.append(x)

def Pop(stack1, stack2):
    if not stack1:
        return -1
    for _ in range(len(stack1)):
        stack2.append(stack1.pop())
    k = stack2.pop()
    if stack2:
        for _ in range(len(stack2)):
            stack1.append(stack2.pop())
    return k


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