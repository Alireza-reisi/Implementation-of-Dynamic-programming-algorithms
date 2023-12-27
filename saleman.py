class saleman():
    def __init__(self,c):
        self.c=c
        self.k=[None for i in range(len(c))]
    
    def Run(self,i,s):
        if len(s)==0:
            return self.c[i][0]
        else:    
            min=float('inf')
            for k in s:
                cost=self.c[i][k] + self.Run(k,s-{k})
                if cost<min:
                    min=cost
                    self.k[i]=k
            return min






s={1,2,3,4,5}
# C=[
#     [0,2,9,float("inf")],
#     [float("inf"),0,6,4],
#     [float("inf"),7,0,8],
#     [6,3,float("inf"),0]
# ]

C=[[0,14,4,10,20],
[14,0,7,8,7],
[4,5,0,7,16],
[11,7,9,0,2],
[18,7,17,4,0]]
 
s_man=saleman(C)
min=s_man.Run(1,s)
print(min)
print(s_man.k)