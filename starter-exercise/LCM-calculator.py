#LCM Calculator
def LCM(a,b):
    greater = a if a>b else b
    while True:
        if(greater%a==0) and (greater%b==0):
            return greater
        greater = greater + 1
m = int(input("m="))
n = int(input("n="))

print("LCM of {} and {} is {}".format(m,n,LCM(m,n)))
