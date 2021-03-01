#Define the Fibonacci sequence
def fib(number):
    
    a,b=0,1
    n=0
    lst=[]
    while n <number:
        
        lst.append(b)
        a,b=b,a+b
        n=n+1
    print(lst)

x=eval(input("What number do you want to get:"))
fib(x)
