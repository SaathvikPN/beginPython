#MaxPairwiseProduct
#first line = no. of items
#second line = numbers separated by spaces

import time
start = time.time()

def MaxPairwiseProduct(list,l):
    big1,big2 = -1,-1
    for i in range(0,l):
        if list[i]>big1:
            big1 = list[i]
            n = i
    for i in range(0,l):
         if ((i!=n) and (list[i]>big2)):
             big2 = list[i]
    return (big1*big2)

n = int(input("n: "))
nlist = []

x = input("numbers: ").split()
l = len(x)
for i in range(l):
    nlist.append(int(x[i])) 
    


print(nlist)
print(MaxPairwiseProduct(nlist,l))

end = time.time()
print(f"Runtime of the program is {end - start}")
    
