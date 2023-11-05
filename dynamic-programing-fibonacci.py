def Fibonacci(n):
    fib=[1,1]
    for i in range (1,n):
        fib.append(fib[i]+fib[i-1])
    return fib[-1]
    


n=int(input("Enter the desired sentence number: "))
print(Fibonacci(n))
