'''
Problem Introduction
You are going to travel to another city that is located 𝑑 miles away from your home city. Your car can travel
at most 𝑚 miles on a full tank and you start with a full tank. Along your way, there are gas stations at
distances stop1
,stop2
, . . . ,stop𝑛 from your home city. What is the minimum number of refills needed?
Problem Description
Input Format. The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line
specifies an integer 𝑛. Finally, the last line contains integers stop1
,stop2
, . . . ,stop𝑛.
Output Format. Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles
on a full tank, and there are gas stations at distances stop1
,stop2
, . . . ,stop𝑛 along the way, output the
minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to
reach the destination, output −1.
Constraints. 1 ≤ 𝑑 ≤ 105
. 1 ≤ 𝑚 ≤ 400. 1 ≤ 𝑛 ≤ 300. 0 < stop1 < stop2 < · · · < stop𝑛 < 𝑑.
Sample 1.
Input:
950
400
4
200 375 550 750
Output:
2
The distance between the cities is 950, the car can travel at most 400 miles on a full tank. It suffices
to make two refills: at points 375 and 750. This is the minimum number of refills as with a single refill
one would only be able to travel at most 800 miles.

'''


def minRefills(distance,tank,stops,refills):
    i=1

    #comparing immediate next stop
    if (tank<(stops[i]-stops[0])):
        print("Oops!. Next-stop is NOT in refill-range")
        return -1

    
    else:
        #Iterating until last stop within or equal to car Range
        while(tank>(stops[i]-stops[0])or(tank==(stops[i]-stops[0]))):
            if (tank==(stops[i]-stops[0])):
                fillTank = stops[i]
                fillIndex = i
                refill = refills + 1
                break
            
            fillTank = stops[i]
            fillIndex = i
            i = i+1  #check if any next stop available
            
            refill = refills + 1 #(currentRefill number) = (alreadyRefilled no.)+1
        print(f"Refilling {refill}th time at {fillTank}") 
        #Preparing list for subproblem similar to original problem
        del stops[0:fillIndex]

        #stops[0] = last_fillIndex
        #If destination within range, this is the Last refill
        if((distance-stops[0])<tank):
            refill = refills + 1
            print(f"{refill} is the last refill because destination in range!")

        #Cannot reach destination. Another refill needed
        else:
            print("going for another refill")
            refill = minRefills(distance,tank,stops,refill)
            
        #return current refill number
        return refill
        

d = int(input()) #distance
m = int(input()) #Car range of dist in Full Tank
n = int(input()) #No. stops (unused in this program)
stops = list(map(int,input().split()))
stops.insert(0,0)
stops.append(d)
print("Checkpoints",stops) #List including starting 0 and destination distance for calculation
print("car Range = ",m)
refills = 0
print("Refills {}".format(minRefills(d,m,stops,refills)))
