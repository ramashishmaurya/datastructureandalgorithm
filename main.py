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

