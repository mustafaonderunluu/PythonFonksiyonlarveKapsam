#Function vss method


my_name= "Onder"
my_name.upper()

my_name_upper= my_name.upper()
my_name_upper

help(my_name.upper)

#Functions 

def hello_python():
    print("Hello Python")
    
    
hello_python()

#input 

def hello_name(name):
    print("hello",name)
    
hello_name("Onder")

def sumex(num1,num2):
    print(num1+num2)
    
sumex(5,6)
#defaultfonks
def hello_surname(surname="Sam"):
    print("hello",surname)
    
hello_surname()

#Return(Çıktı)

def summation(num1,num2,num3):
    print(num1+num2+num3)
    
summation(5, 6, 7)

x = summation(5, 6, 7)
print(x) #none

type(x) #nonetype

def  return_summation(num1,num2,num3):
    return num1+num2+num3

return_summation(5, 4, 5)
x= return_summation(8, 5, 8)
x

def controll_string(s):
    if s[0]== "a":
       print("a")
       
controll_string("Mert")
controll_string("arda")

#args ,kwarg (arguments, keywordarguments)

def args_sum(*args):
    return sum(args)

args_sum(55,48,5,6,8,2,2,88)

def kwargs_examp(**kwargs):
     print(kwargs)
     
kwargs_examp(apple = 100, banana = 150, melon = 200)

def kwargs_examp2(**kwargs):
    if "apple" in kwargs:
        print("Appleeee")
    else:
        print(":(")
        
kwargs_examp2(apple = 100)


    


