#User function Template for python3

# arr is the array
# n is the number of elements in array
def printAl(arr,n):
    
    for i in range (0, n, 2):
        print (arr[i], end = " ")

        
    # your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        printAl(arr,n)
        print()
# } Driver Code Ends