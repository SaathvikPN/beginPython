 
a = int(input("Enter number: "))  
n = int(input("Mulitplication table till: "))  
  
# display the Mulitiplication Table
for i in range(1,n+1):
    print("{} X {} = {}".format(a,i,a*i))
print("---End---")
