
# how to ude recursive function : Syntex

def factorial (num):
    if num==0:       # end case
        return  1
    else:
        return num*factorial(num-1)      # exicutive recurtion function
num=int(5)
print (factorial(num))

print()

