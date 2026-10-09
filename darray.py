

dic = ["abc" , "cab" , "xyz" , "zxy" , "psr"]


def GroupsAnagramm(nums) :

    result = {}

    for n in nums :   # anagrams has to make sense as followed right okay how i can do as followed right okay how i can make sense as followed roght how i can bebest as planed right how i can do as plannned r=okay 

        key = "".join(sorted(n))   # ------>>>>>>>>>>>.  sorted the values is right okay  acb  ---- abc    sorted values here okay bhai right okay 

        if key not in result :

            result[key] = [ ]

        result[key].append(n)


    return result

abc = GroupsAnagramm(dic)

print(abc )


dic = {
    "name" : "ashsih maurya" , 
    "standard" : "Graduate "
}


for n in dic.items():
    print(n)



dictionary = {
    "marks" : ["marathi" , "hindi" , "Engksih" , "Geography"]
}


print(dictionary)


class car :  


    def start(self) :


        print("this is function is started ")

    def stop(self) :
        print("this is functiopon is used to stop the engine okay ")



abc = car()

abc.start()
abc.stop()




class Studnet : 

    def __init__(self , name , age) :
        self.name = name 
        self.age = age

    def introduction(self) :
        print("my name is " , self.name)


b = Studnet("ashish" , 23)

b.introduction()



class BankAccount : 

    def __init__(self , name ,balance ) :

        self.name = name 
        self.__balance = balance

    def depositbalance(self , amount) : 

        self.balance += amount
    
    def show_balance(self) :

        print(self.__balance)


abc = BankAccount("ashish" , 100)  

abc.show_balance()


#here is mean is that how the internal external  we call from internal only bhai right and you can not call from outside okay bhai right okay 


#as planned right as

class Animal :

    def eat(self):
        print("Animal ate by the mouths ") 


class cat(Animal) :

    def catcolor(self) :
        print("cat is black color")

b = cat()

#Input: s = "anagram", t = "nagaram"


#i neede to calculate is this is this bhai anagram or not bhai okay bhai right here okay here right okay bhak make sense as rigt 

s = "anagramf" , 
t = "nagaram"

def Checkvalidanagram(s, t):

    if len(s) != len(t):
        return False

    sresult = {}
    tresult = {}

    for i in s:
        sresult[i] = sresult.get(i, 0) + 1

    for j in t:
        tresult[j] = tresult.get(j, 0) + 1

    return sresult == tresult


print(Checkvalidanagram(s,t))


nums = [ 1 , 2, 3 , 4 ]

def DuplicatedValues(nums) :  

    sets = set()

    for i in nums :

        if i in sets : 
            return True
        return False
    
        sets.add(i)


abc = DuplicatedValues(nums)
print(abc)




name = "ashismaurya"

def Countvector(name) :

    result = {}

    for i in name :
        if i not in result :
            result[i] = 1 
        else:
            result[i]+=1 
    

    return result

abc = Countvector(name)

print(abc)



strnumber =["xyz" , "yzx" , "abc" , "bca" , "tys" , "tsb"]


def functionanagrams(nums) :

    result = {}

    for i in nums :

        key = "".join(sorted(i)) # sorted the value is righ has make sense as right has to make sense as right okay  

        if key not in result : 

            result[key] = []

        result[key].append(i)  # firts values will not kay bol sakte h bhai like in enter into the list 

    return result


print(functionanagrams(strnumber)) 


#intersection of arrays 

nums = [1 , 2, 2, 1 ]

nums2 = [2 , 2 ]


n = set(nums)
n1 = set(nums2)

result = []

for  i in n :
    for i in n1 :
        result.append(i)

print(result)

#b basic run until this condition is failed okay  
i = 1 

while(i < 5) :

    print(i)

    i+= 1 


from dataclasses import dataclass

@dataclass
class abc :
    def __init__(self , name , surname) :
        self.name = name
        self.surname = surname

    @property
    def get_Data(self):
        return "data is coming"



bc = abc("ashish" , "maurya")
print(bc.get_Data)


