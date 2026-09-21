from main import sumnumber 


def testdata():
    assert sumnumber() == 10


nums = [3 ,2,3 ,3]

def functiomajorityelement(nums):

    result = {}

    for  i in nums:

        if i not in result:
            result[i] = 1 
        else:
            result[i]+= 1 

    for n in result:
        if result[n] > len(nums) / 2  :
            return n
        

abc = functiomajorityelement(nums)

print(abc) 
 

nrows = 5 
ncols = 4 

for i in range(1 , nrows):
    for space in range(1 , nrows - i ):
        print(" " , end=" ")

    for start in range(i):
        print("*" , end=" ")
    
    print()

nrow =5
for i in range(1 , nrows):
    for space in range(i):
        print(" " , end=" ")
    
    for start in range(nrow- i):
        print("*" , end=" ")
    
    print( ) 


sumvalues = 1 
nums = 6
for i in range(1 , nums):
    for j in range(i):
        print(sumvalues , end=" ")
        sumvalues+=1 
    print()



n = 5

# Upper half
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")

    for j in range(2 * (n - i)):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()

# Lower half
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")

    for j in range(2 * (n - i)):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()



