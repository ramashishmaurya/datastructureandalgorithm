# main focused as  anaagrams right


n =["abc" , "bca" , "as" , "sa"] # sorted need to soert this right okay 

def groupsanagram(n):

    result = {}

    for i in n :
        key = "".join(sorted(i))

        if key not in result: 
            result[key] = []  
         
        result[key].append(i)
    
    return result


print(groupsanagram(n))


def sumnumber():
    return 10 


# character print okay 

n = 4 
for i in range(1 , n):
    for j in range(1 , i+1):
        print(j , end=" ")
    print( )

n  =5 
for i in range(n):
    for j in range(i +1):
        print(chr(65 + j) , end=" ")
    print( )
    # char is functio that convert speciafic number to the character valeus right


number = [1, 2, 3, 4]

def function(number):
    return number ** 2

n = list(map(function, number))

abc = [i**2 for i in range(1,9)]

print(abc)


def functiondatacalculation():
    return 10 + 10 



# reverse arrayas probles okay 


number = [1 , 2 , 3, 4, 5 ]

abc = number.copy()

def ReverserNumber(number):

    start = 0 
    end = len(number) - 1 

    while start < end:

        number[start] , number[end]  = number[end] , number[start]

        start+= 1 
        end-=1
    
    return number



print("original number" , abc)

print("reverse values" , ReverserNumber(number))


# print the result in pairs okay 

numbers = [1 , 2  , 3 , 4 , 5]

(1 , 2 ) , (1 , 3 ) , (1 ,4) , (1 ,5)
(2 , 3) , (2,4) ,(2,5) , 
(3,4) , (3,5)

for i in range(len(numbers)-1):
    for n in range(i+1 , len(numbers)): # if u talk about time complexity to solve this problems is O(n^2)

        print((numbers[i] , numbers[n]) ,end=" ")

    print()


# maxmimng values in the given arrays 


numbers = [2 , 4, 5 , 7, 10 , 14 ]

maxvalues = 0  # assing the lowest values and compare to each other bhai are u able to more or not bhai okay 

for i in numbers:

    if i > maxvalues :

        maxvalues = i  

print(maxvalues)

# max subarray sum 

# bruate force method right -------->   having the more time complexcity okay     
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]    # 
def  max_subarray_sum(arr):
    max_sum = float("-inf") 

    for i in range(len(arr)):

        for j in  range(1 , len(arr)):

            current_sum = 0  

            for k in range(i , j) :

                current_sum+= arr[k]  
            max_sum = max(current_sum , max_sum)
    
    return max_sum

print(max_subarray_sum(arr))

# utilizinghere that prefix matterd as much right okay .  
arr = [2, 4, 1, 5, 3]

prefix = [0] * len(arr)

prefix[0] = arr[0]

for i in range(1 , len(arr)) :

    prefix[i] = prefix[i-1]  + arr[i]

    
print(prefix)


# kadans algorith deiscuss here okay bha make sense for  me okay 

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def max_currenr_Sum(arr):

    current_sum = arr[0]

    max_sum = arr[0]

    for i in range( 1, len(arr)) :
        current_sum = max(arr[i] ,current_sum + arr[i] )  

        max_sum = max(max_sum , current_sum)
        
    return max_sum

print(max_currenr_Sum(arr))


