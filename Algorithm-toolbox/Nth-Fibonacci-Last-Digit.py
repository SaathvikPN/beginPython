#Last digit of Nth Fibonacci Number

def Fib_last_digit(n):
    if n<=1:
        return n
    elif (n==2):
        return 1
    else:
        num = 0
        a,b = 1,1
        for i in range(n-2):
            num = a + b
            num = num%10
            
            b = a
            a = num
            
        return num

n = int(input("n: "))

print('''{}th Fibonacci Number last digit is "{}"'''.format(n,Fib_last_digit(n)))
