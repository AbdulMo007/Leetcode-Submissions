#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        x = str(n)
        sum = 0
        for i in x:
            sum += (int(i))**3
            
        return "Yes" if sum == n else "No"
            
        
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends