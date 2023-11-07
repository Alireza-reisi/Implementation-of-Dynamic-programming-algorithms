def choose (n,k):
    Matrix=[[1 for i in range(n)] for x in range (k)]
    for i in range (0,k):
        for j in range (0,min(i,n)):
            if j==i or j==0:
                Matrix[i][j]=1
            else:
                Matrix[i][j]=Matrix[i-1][j-1]+Matrix[i-1][j]
    # ------------------------------
    # for knowing what save in Matrix, uncomment following line:
    
    # for i in range(len(Matrix)): 
    #     print(Matrix[i],end="\n")
    # ------------------------------    
    return Matrix[i][j]


# ================================================================
# getting input's:

k=int(input("Enter total number:"))
n=int(input("Enter the number of choices: "))


anser=choose(n,k)
print(anser)