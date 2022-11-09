#User function Template for python3
class Solution:
    def reciprocalString(self, S):
           n=''
           for i in S:
              if ord(i)>=97 and ord(i)<=122:
                value=ord(i)-97    
                temp=122-value
                n+=chr(temp)
              elif ord(i)>=65 and ord(i)<=90:
                 value=ord(i)-65 # = 8
                 temp=90-value
                 n+=chr(temp)
              else:
                   n+=i
           return n
                
                    
                

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        print(ob.reciprocalString(S))
# } Driver Code Ends