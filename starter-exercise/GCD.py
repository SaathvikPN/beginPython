def gcd(a,b):
    smaller = a if a<b else b
    while (smaller>0):
        if((a%smaller==0) and (b%smaller==0)):
            return smaller
        smaller = smaller - 1
    return ("terminated")

m = int(input("1st number "))
n = int(input("2nd number "))
print("GCD of {} and {} is \"{}\"".format(m,n,gcd(m,n)))
    
