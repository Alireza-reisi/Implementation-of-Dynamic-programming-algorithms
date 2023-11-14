def Fibonacci(n):
    fib=[None for i in range(0,n+1)]
    fib[0]=0
    fib[1]=1
    for j in range (2,n+1):
        fib[j]=fib[j-1]+fib[j-2]
    
    return fib[n]
    


n=int(input("Enter the desired sentence number: "))
x=Fibonacci(n)
print(x)
