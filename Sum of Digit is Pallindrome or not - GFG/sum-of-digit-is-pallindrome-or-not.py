#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self,N):
        N = str(N)
        sum = 0
        for i in (N):
            sum += int(i) 
        sum = str(sum)
        
        return 1 if sum[::-1] == sum else 0 
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends