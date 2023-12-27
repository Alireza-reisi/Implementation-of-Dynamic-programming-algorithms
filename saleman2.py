class Saleman():
    def __init__(self,Matrix):
        self.List=[]
        self.Matrix=Matrix
        self.K=[0 for i in range (len(Matrix))]
       
    def g(self,Node,Set):
        
        for i in range(len(self.List)):
            if (self.List[i][0]==Node and self.List[i][1]==Set):
                return self.List[i][2]
        
        if len(Set)==0:
            Row=[Node,Set,self.Matrix[Node-1][0]]     #self.Matrix[Node][0] means the cost of going to Node 1 By Current Node
            self.List.append(Row)
            return self.Matrix[Node-1][0]
        
        else:
            min=float('inf')
            for k in Set:
                if k==Node:
                    Set=Set-{k}
                else:
                    cost = self.Matrix[Node-1][k-1] + self.g(k,Set-{k})
                    if cost<min:
                        min=cost
                        
                        
            # self.K[(len(self.Matrix)-len(Set))]=k        
            Row=[Node,Set,min]
            self.List.append(Row)
            return min
        
        




# test1:
# s={2,3,4}
# c=[
#     [0,2,9,float("inf")],
#     [float("inf"),0,6,4],
#     [float("inf"),7,0,8],
#     [6,3,float("inf"),0]
# ]


# test2: ----------- Algoritm class "Hamid"
# s={2,3,4,5}
# c=[[0,14,4,10,20],
# [14,0,7,8,7],
# [4,5,0,7,16],
# [11,7,9,0,2],
# [18,7,17,4,0]]


# test3: ----------------- Abdul bari
s={2,3,4}
c=[
    [0,10,15,20],
    [5,0,9,10],
    [6,13,0,12],
    [8,8,9,0]
] 

s_man=Saleman(c)
min=s_man.g(1,s)
print(min)
print(s_man.K)
for i in range(len(s_man.List)):
    print(s_man.List[i])