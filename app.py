# n = 5

# # Upper half
# for i in range(1, n + 1):

#     # Print spaces
#     for j in range(n - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1 or i == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# # Lower half
# for i in range(n - 1, 0, -1):

#     # Print spaces
#     for j in range(n - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# n = "Banana"

# def numberoftimewordfetched(n):

#     result = {}

#     for i in n :
#         if i not in result:
#             result[i] = 1 
        
#         result[i]+= 1 

#     for char, number in sorted(result.items(), key=lambda x: x[1]):
#        print(char, ":", number)

# numberoftimewordfetched(n)




# nums = [2, 7, 11, 15]
# target = 9

# def Twosumproblems(nums , target):
#     dic = {}

#     for index  , values  in enumerate(nums):

#         targetsvalues = target  - values

#         if targetsvalues in dic:
#             return[dic[targetsvalues] , index]
        
#         dic[values] = index

# abc = Twosumproblems(nums , target)
# print(abc)


# Linear search 

# numbers = [1 , 2,3,4,5]
# keys  = 4 

# def Linearsearchalgorithm(nums , keys  ):

#     if keys not in nums:
#         return "Keys should be presenr in list"
    
#     for n in nums:
#         if n == keys:
#             return n 

# print(Linearsearchalgorithm(numbers , keys))



# Largets numberes in lit okay 


# numbers = [1 , 3,6,2 , 10]  

# def Largestnumberinlist(numbers):

#     largestnu = 0 

#     for i in numbers:
#         if i > largestnu:
#             largestnu = i 
#     return largestnu
    


# print(Largestnumberinlist(numbers))


# numbers = [2 , 4, 6 , 8, 10 , 12 , 14]
# keys = 8 


# def BinarysearcgAlgorithm(numbers , keys):

#     sorted(numbers)

#     start = 0 
#     end = len(numbers)-1 

#     while(start <= end) :

#         midpoints = (start + end) // 2 

#         if numbers[midpoints] == keys:
#             return [numbers[midpoints] , midpoints ]
        
#         if keys < numbers[midpoints] :
#             end = end - 1 
#         else:
#             start = start + 1 



# print(BinarysearcgAlgorithm(numbers , keys))




# reverse An Arrays 

numbers = [ 2 , 4 ,  5, 6 , 10 ]

abc = numbers.copy()
# arrys = numbers[::-1]


# b = numbers.reverse()

# print(b)

# def ReverseNumbers(numbers):

#     start = 0 

#     end = len(numbers) -1 

#     while start <= end:

#         numbers[start] , numbers[end] = numbers[end] , numbers[start]

#         start+= 1 
#         end-= 1 

#     return numbers



# print(ReverseNumbers(numbers))

# print("original number " , abc  )

