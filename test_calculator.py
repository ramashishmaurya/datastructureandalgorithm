# from main import sumnumber 


# def testdata():
#     assert sumnumber() == 10


# nums = [3 ,2,3 ,3]

# def functiomajorityelement(nums):

#     result = {}

#     for  i in nums:

#         if i not in result:
#             result[i] = 1 
#         else:
#             result[i]+= 1 

#     for n in result:
#         if result[n] > len(nums) / 2  :
#             return n
        

# abc = functiomajorityelement(nums)

# print(abc) 
 

# nrows = 5 
# ncols = 4 

# for i in range(1 , nrows):
#     for space in range(1 , nrows - i ):
#         print(" " , end=" ")

#     for start in range(i):
#         print("*" , end=" ")
    
#     print()

# nrow =5
# for i in range(1 , nrows):
#     for space in range(i):
#         print(" " , end=" ")
    
#     for start in range(nrow- i):
#         print("*" , end=" ")
    
#     print( ) 


# sumvalues = 1 
# nums = 6
# for i in range(1 , nums):
#     for j in range(i):
#         print(sumvalues , end=" ")
#         sumvalues+=1 
#     print()



# n = 5

# # Upper half
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end=" ")

#     for j in range(2 * (n - i)):
#         print(" ", end=" ")

#     for j in range(i):
#         print("*", end=" ")

#     print()

# # Lower half
# for i in range(n - 1, 0, -1):
#     for j in range(i):
#         print("*", end=" ")

#     for j in range(2 * (n - i)):
#         print(" ", end=" ")

#     for j in range(i):
#         print("*", end=" ")

#     print()



# # linear search 
    
# n = [1 ,2 ,3,4 , 5 ]

# keys = 4 

# def functionkeycheckvaleus(n):
#     for i , k  in enumerate(n):
#       if k == keys:
#         return({
#             "indexnumberis" : f"this is index number {i}"
#         })


# abc = functionkeycheckvaleus(n)
# print("here is output = " ,  abc)


# binary search 

# n = [2 , 4, 5 , 8 , 10 ]
# keys = 5 
# start = 0
# end = len(n)-1 



# def binarysearchdata(n, keys):
#     start = 0
#     end = len(n) - 1

#     while start <= end:
#         midpoint = (start + end) // 2

#         if n[midpoint] == keys:
#             return midpoint

#         elif n[midpoint] > keys:
#             end = midpoint - 1

#         else:
#             start = midpoint + 1

#     return -1

# abc = binarysearchdata(n  , keys)
# print(abc)

# from main import functiondatacalculation



# def testdata():
#     assert functiondatacalculation() == 20 

# def adddunctionmatch(variable):

#     if not variable:
#         return f"this number is present okay  {variable}"


# print(adddunctionmatch(12))


