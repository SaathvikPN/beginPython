#Prime Check
def PrimeCheck(n):
    for i in range(2,(n//2)):
        if n%i==0:
            return ("NOT prime")
    return ("Prime")
            
        

n = int(input("Number: "))
print(n,"is",PrimeCheck(n))
