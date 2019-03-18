
# how to use map() function
"""
it's have two argument .
1. function
2. iterator object ( aply function depend iterator object )

"""

my_list =[2,3,4,5,6,7,8]

def squre(x):
    return x * x *x
new_list = (map(squre,my_list))  # use map() function
print(new_list)
print(list(new_list))

print()

# A programe use to map() function to collect user input

print('Enter two input number: ')
a,b =map(int ,input().split())
z= a+b
print(z)

print()

# how to use filter() function :

"""
it's have two argument .
1. function
2. iterator object ( aply function depend iterator object )

work:filter() use to filter if any item return false than filter() function avoid this return result. 

"""

my_list=[1,5,9,4,7,5,6,3,8]

def separation (x):
    if x%2==0:
        return True
    else:
        return False

new_list=(filter(separation,my_list))
print(new_list)
print(list(new_list))