
'''
1. The list can have the same items multiple times, but
only a single member or item will remain in the set only once.

2. Elements of the set can not be accessed with an index number.

'''

# we can not use {} to create Null set
a={}
print(type(a)) # its a dictionary

# syntex

a=set()
print(type(a))
a={'apple'}
print(a)
print(type(a))

print()

# {} it's hold different type of item

a={'apple','banana',1,3,2.55}
print(a)
print(type(a))

print()

# set function hold only one item

a=set('hafizur rahman')
print(a)
print(type(a))

print()

# add () function use to adding 'only one item '

a.add('01838') # use to add only one item
print(a)
print(type(a))

print()

# update () function use to adding multiple item
b={'hafizur','rahman'}
b.update({'01838','bd','email'})
print(b)
b.remove('hafizur')
print(b)
b.discard('rahman') # it's beter than remove function
print(b)
b.pop()
print(b)
b.clear() # dellet all item
print(b)
print()

# union ()

A={1,2,3,4}
B={5,2,6,3}
C=A.union(B) # use union () function
print(C)
print()

# intersection ()

D=A.intersection(B) # use to find out same value
print(D)
print()

# difference ()

E=A.difference(B)
print(E)
print()
