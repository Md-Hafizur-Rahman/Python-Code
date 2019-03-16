# topic about dictionary
"""
dictionary denoted {}  sign .it's have three parts.
1.key
2." : " sign
3.value

than use ( , ) comma to separat item.
N.B:1. key unic and value repetable.

"""
# class type of dictionary and syntex

a={}
print(type(a))
a={'name' : 'hafizur rahman','country' :'bangladesh','language': 'bangla'}
print(a)
print()

# we can represent it another way

a=dict()
print(a)
print(type(a))
print()

# we can acsess dictionry to use key into [] :

a={'name' : 'hafizur rahman','country' :'bangladesh','language': 'bangla'}
print(a['name'])
print(a['language'])
print()

# update dictionary
"""

"""

a={'name' : 'hafizur rahman','country' :'bangladesh','language': 'bangla'}
a['name']='md hafizur rahman' # update name value
print(a)
a['hometown']='kurigram' # update new key and value
print(a)
print()

# if we want that adding another item into one item than we use update() function

a={'name' : 'hafizur rahman','country' :'bangladesh','language': 'bangla'}
b={'hometown':'kurigram','favouriteColor':'black-white','name':'mahdi'}
a.update(b) # update use to update another dictinary
print(a)
print()

# delet only one item

del a['name']
print(a)
print()

# remove all item

a.clear()
print(a)
print()

''' dellet all item

del b
print(b) # doesn't print as a any dictionary
print() 

'''

# copy function

D={'name' : 'hafizur','Another_Name' : 'rahman','Programe': 'CSE'}
D.copy()
print(D)
print()

# get () function

print(D.get('name')) # use to find 'keys value'
print()

# if find correct than return 'ture'  otherwise return 'false'

print('name' in D)

# items ()

print(D.items())
print()

# keys ()

print(D.keys()) # to find out all key name
print()

# values ()

print(D.values()) # to find out all value name
print()
