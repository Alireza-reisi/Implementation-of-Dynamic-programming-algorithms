# min mult
def MinMult(n,d):
   #p matrix show us how sup matrixes    # The p matrix is filled by the function (MinMult)
   # build p matrix:  
   P_matrix=[[0 for i in range(n)] for x in range (n)]
   # min_matrix save and found the number of minimum sup
   # build min_matrix:
   min_matrix=[[0 for i in range(n)] for x in range (n)]
   # -------------------------------------------------
   for x in range(1,n):
      for i in range(1,n-x):
         j=i+x
         min=float('inf')
         k=i
         while k<=j-1:
            z=min_matrix[i][k]+min_matrix[k+1][j]+((d[i-1]*d[k])*d[j])
            if z<min:
               min=z
               P_matrix[i][j]=k
            k=k+1
         min_matrix[i][j]=min
         
   return min_matrix,P_matrix
      
            
# ==================================================================================
# ==================================================================================
# ==================================================================================

Matrixes=[]
# A -> 20*2
A=[[1,2],
   [2,2],
   [3,2],
   [4,2],
   [5,2],
   [6,2],
   [7,2],
   [8,2],
   [9,2],
   [10,2],
   [11,2],
   [12,2],
   [13,2],
   [14,2],
   [15,2],
   [16,2],
   [17,2],
   [18,2],
   [19,2],
   [20,2],]
# B -> 2*15
B=[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
   [2,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]
# C -> 15*12
C=[[1,2,3,4,5,6,7,8,9,10,11,12],
   [2,2,3,4,5,6,7,8,9,10,11,12],
   [3,2,3,4,5,6,7,8,9,10,11,12],
   [4,2,3,4,5,6,7,8,9,10,11,12],
   [5,2,3,4,5,6,7,8,9,10,11,12],
   [6,2,3,4,5,6,7,8,9,10,11,12],
   [7,2,3,4,5,6,7,8,9,10,11,12],
   [8,2,3,4,5,6,7,8,9,10,11,12],
   [9,2,3,4,5,6,7,8,9,10,11,12],
   [10,2,3,4,5,6,7,8,9,10,11,12],
   [11,2,3,4,5,6,7,8,9,10,11,12],
   [12,2,3,4,5,6,7,8,9,10,11,12],
   [13,2,3,4,5,6,7,8,9,10,11,12],
   [14,2,3,4,5,6,7,8,9,10,11,12],
   [15,2,3,4,5,6,7,8,9,10,11,12],]
# D -> 12*5
D=[[1,2,3,4,5],
   [2,2,3,4,5],
   [3,2,3,4,5],
   [4,2,3,4,5],
   [5,2,3,4,5],
   [6,2,3,4,5],
   [7,2,3,4,5],
   [8,2,3,4,5],
   [9,2,3,4,5],
   [10,2,3,4,5],
   [11,2,3,4,5],
   [12,2,3,4,5]]

Matrixes.append(A)
Matrixes.append(B)
Matrixes.append(C)
Matrixes.append(D)
# Matrixes[0]== A // Matrixes[1]== B // Matrixes[2]== C // Matrixes[3]== D
# The Matrixes array is a 3D array



# ------------------------------------------------
# build d array:
# d[0] d[1] ... d[n+1]    # n=the number of matrixes
# d=[len(A),len(B),len(C),len(D),len(D[0])]
d=[len(Matrixes[0]),len(Matrixes[1]),len(Matrixes[2]),len(Matrixes[3]),len(Matrixes[3][0])]

# ------------------------------------------------
n=len(Matrixes)+1

min_matrix,P_matrix=MinMult(n,d)

for i in range (len(min_matrix)):
   print(min_matrix[i],end='\n')

print("-----------------------------------------")

for i in range (len(P_matrix)):
   print(P_matrix[i],end='\n')
   
print("-----------------------------------------")
   
   
