class Node:
    def __init__(self, x):
        self.data = x
        self.nxt = None


class Solution:
    def mergeKLists(self, arr, K):
        res = []
        for i in range(K):
            while arr[i]:
                res.append(arr[i].data)
                arr[i] = arr[i].next
        res.sort()
        temp = Node(0)
        out = temp
        for i in range(len(res)):
            hey = Node(res[i])
            out.next = hey
            out = out.next
        return temp.next

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next
    
def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        
        heads=[]
        index=0
        
        for i in range(n):
            size=line[index]
            index+=1
            
            newList = LinkedList()
            
            for _ in range(size):
                newList.add(line[index])
                index+=1
            
            heads.append(newList.head)
        
        merged_list = Solution().mergeKLists(heads,n)
        printList(merged_list)

# } Driver Code Ends