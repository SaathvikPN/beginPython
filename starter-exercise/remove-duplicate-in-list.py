#Remove duplicate from a list

myList = []
n = int(input("total items: "))
for i in range(n):
    x = input()
    myList.append(x)
print(myList,"\n")

fList = []
for i in myList:
    if i not in fList: #putting only non-repetitive item
        fList.append(i) 
del myList
print("After operation\n",fList)
    
