def MinMult(key,frequency,n):
    optimal_key=[[0 for i in range(n+1)] for j in range(n+1)]
    optimal_weight=[[0 for i in range(n+1)] for j in range(n+1)]
    for x in range(1,n+1):
        for i in range(0,n-x+1):
            j=i+x
            min=float('inf')
            k=i+1
            weight=0
            for w in range(i,j):
                weight+=frequency[w]
            while k<=j:
                z=optimal_weight[i][k-1]+optimal_weight[k+1][j]+weight # Not complete #logical eror
                if z<min:
                    min=z
                    optimal_key[i][j]=k
                k=k+1
            optimal_weight[i][j]=min
    return optimal_weight,optimal_key




# ========================================================================

# key=[10,20,30,40]
key=[1,2,3,4,5]

# frequency=[4,2,6,3]
frequency=[0.3,0.05,0.08,0.45,0.12]
optimal_weight,optimal_key=MinMult(key,frequency,len(key))

# ========================================================================

for i in range(len(key)):
    print(optimal_key[i]) 

print("=============================")

for i in range(len(key)):
    print(optimal_weight[i]) 

print("=============================")
