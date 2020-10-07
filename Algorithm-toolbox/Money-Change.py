''' Money Change Question
Convert money into min no. of coins [Denominations 1,5,10 only]
'''

def minCoins(n):
    a = n//10
    b = (n - (a*10))//5
    c = n - ((a*10)+(b*5))
    return a+b+c
n = int(input())
print(minCoins(n))
