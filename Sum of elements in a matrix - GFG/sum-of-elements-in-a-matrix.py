#User function Template for python3

class Solution:
    def sumOfMatrix(self,N,M,Grid):
        sum = 0
        for i in range (0,N):
            for j in range (0,M):
                sum += (Grid[i][j])
        return sum
                

            
  #   0,1,2
# 0 [[1,0,1],
# 1 [-8,9,-2]]


            
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(' '))
        Grid = [[0 for i in range(M)] for j in range(N)]
        for i in range(N):
            s=list(map(int,input().strip().split(' ')))
            for j in range(M):
                Grid[i][j]=s[j]
        ob=Solution()
        print(ob.sumOfMatrix(N,M,Grid)) 
# } Driver Code Ends