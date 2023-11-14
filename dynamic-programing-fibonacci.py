def Fibonacci(n):
    fib=[0,1,None]
    if n<2:
        return fib[n]
    else:
        for i in range (2,n+1):
            fib[2]=fib[0]+fib[1]
            fib[0]=fib[1]
            fib[1]=fib[2]
    return fib[2]
    


n=int(input("Enter the desired sentence number: "))
print(Fibonacci(n))
