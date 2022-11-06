#User function Template for python3

class Solution:
    def findIndex (self,a, N, key ):
        ans = []
        for i in range (0, N):
            if a[i] == key:
                ans.append(i)
                break
        
        for i in range (N-1, -1, -1):
            if a[i] == key:
                ans.append(i)
                break
        if (len(ans)) == 0:
            return [-1, -1]
        return ans
            
        
        #code here.


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends