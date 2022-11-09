#User function Template for python3

class Solution:
    def oppositeFaceOfDice(self, N):
        oxf = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
        
        return oxf[N]
            
        
    	#code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.oppositeFaceOfDice(N)
        print(ans)
# } Driver Code Ends