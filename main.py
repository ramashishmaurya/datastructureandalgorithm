# # main focused as  anaagrams right


# n =["abc" , "bca" , "as" , "sa"] # sorted need to soert this right okay 

# def groupsanagram(n):

#     result = {}

#     for i in n :
#         key = "".join(sorted(i))

#         if key not in result: 
#             result[key] = []  
         
#         result[key].append(i)
    
#     return result


# print(groupsanagram(n))


# def sumnumber():
#     return 10 


# character print okay 

# n = 4 
# for i in range(1 , n):
#     for j in range(1 , i+1):
#         print(j , end=" ")
#     print( )

# n  =5 
# for i in range(n):
#     for j in range(i +1):
#         print(chr(65 + j) , end=" ")
#     print( )
    # char is functio that convert speciafic number to the character valeus right


number = [1, 2, 3, 4]

def function(number):
    return number ** 2

n = list(map(function, number))

abc = [i**2 for i in range(1,9)]

print(abc)


