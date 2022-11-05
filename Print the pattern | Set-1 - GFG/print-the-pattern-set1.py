def printPat(n):
    for i in range(n,0,-1):

        for j in range(n,0,-1):

            print(("{0} ".format(j))*i,end="")

        print("$",end="")

    print()
    
    
    
    
    

    #Code here


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        printPat(n)
# } Driver Code Ends