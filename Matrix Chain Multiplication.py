def Minimum(i,j,min_matrix,d):
   
   for i in 
   pass




def MinMult(n,d,p):
   # ------------------------------------------------
   # min_matrix save and found the number of minimum sup
   # build min_matrix
   min_matrix=[]
   x=[0 for i in range (0,n)]
   for i in range(0,n):
      min_matrix.append(x)
   
   
   # -------------------------------------------------
   i=0
   for t in range (1,n-1):
         if (i+1)==t:
            min_matrix[i][t]= (min_matrix[i][t-1]+ min_matrix[i+1][t])+(d[i]*d[t-1]*d[t])
            
         else:   
            min_matrix[i][t]=Minimum(i,t,min_matrix,d)
   






















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



# =======================================================================================
# build d array:
# d[0] d[1] ... d[n+1]    # n=the number of matrixes

# d=[len(A),len(B),len(C),len(D),len(D[0])]
d=[len(Matrixes[0]),len(Matrixes[1]),len(Matrixes[2]),len(Matrixes[3]),len(Matrixes[3][0])]

# =======================================================================================
# p matrix show us how sup matrixes    # The p matrix is filled by the function (MinMult)
# build p matrix:  

P_matrix=[]
x=[0 for i in range (0,len(Matrixes))]
for i in range(0,len(Matrixes)):
   P_matrix.append(x)

# =======================================================================================

MinMult(len(Matrixes),d,P_matrix)