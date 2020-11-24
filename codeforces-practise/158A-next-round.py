n,k = map(int, input().split())
s = [int(x) for x in input().split()]
c=0

for i in range(n):
    if s[i]>0 and s[i]>=s[k-1]:
        c+=1
    else:
        break
print(c)
        

