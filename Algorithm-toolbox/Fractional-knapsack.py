'''
Maximum value of Loot Problem
'''
import sys
def get_opt_value(capacity,values,weights):
    value = 0
    value_per_weight = []
    length = len(weights) #Memory Optimisable
    for i in range(length):
        x = values[i]/weights[i] #Memory Optimisable
        value_per_weight.append(x)
    while(capacity!=0):
        chooseIndex = value_per_weight.index(max(value_per_weight))
        putWeight = weights[chooseIndex]
        if(putWeight>capacity):
            excess = putWeight - capacity
            putWeight = putWeight - excess
            value = putWeight*value_per_weight[chooseIndex]
            return value
        else:
            capacity = capacity - putWeight
            value = value + (putWeight*value_per_weight[chooseIndex])
            del value_per_weight[chooseIndex]
            del weights[chooseIndex]
            del values[chooseIndex]
    return value
        
if __name__ == "__main__":
    
    data = list(map(int,input().split()))
    
    for line in range(data[0]):
        userData = list(map(int,input().split()))
        data = data + userData
        
    print("Data",data)
    n,capacity = data[0:2]
    values = data[2:(2*n)+2:2] #last element in range not considered
    weights = data[3:(2*n)+3:2]
    print("values",values)
    print("weights",weights)
    opt_value = get_opt_value(capacity,values,weights)
    print("{:.4f}".format(opt_value))
