#Pratical Functions

def divideNumber(number):
    return number / 2

divideNumber(20)


myList=[55,66,88,55,22,33,44]


myResultList= []
for num in myList:
    myResultList.append(divideNumber(num))
print(myResultList)


#Map Class

help(map)

list(map(divideNumber,myList)) #Basit Hal 

def controll_string(string):
    return"Onder" in string
    
controll_string("Onder")

myStringList = ["onder","Onderunlu","MUSTAFA  UNLU"]

list(map(controll_string,myStringList))

#Filter

list(filter(controll_string,myStringList))

#Lambda

multiplyLambda= lambda num : num *3

type(multiplyLambda)

multiplyLambda(20)

result = multiplyLambda(20)
result

numList = [10,20,30,40,50]

list(map(lambda num:num/4,numList))

x= 20 

# Scope

def multiply(number):
    z = 5
    return number*z


multiply(5)


#LEGB L > Local , E > Enclosing, G > Global, B > Bulilt
"Global"
myString = "Onder"  

def myFunction():
    "Enclosing"
    myString = "Onder 2"
    
    def myFunction2():
        "Local"
        myString="Onder 3"
        print(myString)
        
    myFunction2()
        
myString

myFunction()
myString
myFunction()
myString

myVariable = 30  #Globalde Gözükür 

def test1():
    myVariable = 10
    print (myVariable * 2)
    
    def test2():
        print(myVariable * 2)
    
test1()

 

    