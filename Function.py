
# how to use parameter into a function & return type

def add(a,b):
    c=a+b
    return c
a,b=5,10
d=a+b
print (d)

print ()

# use "function_parameter" into a function & return type

def beautiful(text):
    return text + '!!!'

def make_line(function , word):
    return 'hellow '+function(word)

print (make_line(beautiful,'word '))
print()


#অ্যানোনিমাস (anonymous) ফাংশন : work with expretion and return type

def solution (function,arg1,arg2):
    return function(arg1,arg2)

print(solution(lambda a,b: a+b,10,20))

print()

# use "function_parameter" into a function  and return type

def solution (function,arg1,arg2):
    return function(arg1,arg2)

def expretion (c,d):
    return c+d
print(solution(expretion,20,30))
print ()

# use maltiply parameter in a function as a tpule and return type

def parameter (*star):

    temp=0
    print(type(star))
    for i in star:
        temp=temp+i
    return temp

print (parameter(2,3,4,5,6))

print()

#use maltiply parameter in a function as a dictionary and return type

def parameter(**star):
    temp=0
    print(type(star))
    for i in star:
        temp=temp+star[i]
    return temp

print(parameter(a=1,b=2,c=5))

