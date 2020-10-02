#MaxPairwiseProduct
#first line = no. of items
#second line = numbers separated by spaces

import time
start = time.time()

def MaxPairwiseProduct(list):
    big1,big2 = 0,0
    for i in range(0,len(list)):
        if list[i]>big1:
            big1 = list[i]
            n = i
    for i in range(0,len(list)):
         if ((i!=n) and (list[i]>big2)):
             big2 = list[i]
    return (big1*big2)

n = int(input("n: "))
nlist = []

x = input("numbers: ").split()
for i in range(len(x)):
    nlist.append(int(x[i])) 
    


print(nlist)
print(MaxPairwiseProduct(nlist))

end = time.time()
print(f"Runtime of the program is {end - start}")
    
