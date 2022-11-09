#User function Template for python3

class Solution:
    def oppositeFaceOfDice(self, N):
        k = []
        
        for i in range (1, 7): #1000
            k.append(i)
        i = 0
        j = len(k)-1
        
        while i<=j:
            if k[i] == N:
                return k[j]
            elif k[j] == N:
                return k[i]
            i += 1
            j -= 1
                
            
            

                
        
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