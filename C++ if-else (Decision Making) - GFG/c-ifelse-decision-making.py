#User function Template for python3
class Solution:
    def compareFive (ob,N):
        
        if N > 5:
            return ("Greater than 5")
        if N < 5:
            return ("Less than 5")
        if N == 5:
            return ("Equal to 5")
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())

        ob = Solution()
        print(ob.compareFive(N))
# } Driver Code Ends