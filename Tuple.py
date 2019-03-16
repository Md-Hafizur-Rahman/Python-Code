
'''

Tappal can not be modified as per the list.
The item type of the copper item can be anything.
the integers, the floats that could be used happily. we could also use list, tapal or dictionary if we wanted to.

'''

# syntex for tuple

a=() # its a tuple
print(type(a))
print()
a=('hafizur','rahman',2,6,2.55) # different type of data type
print(a)
print(type(a))

print()

# ascces tuple

print(a[0])
print(a[1:3])

print()

# we can add another item

print(a+('new item',))
print()

# count item

print(a.count('rahman'))
print()

# find out index number

print(a.index(2.55))
print()

# find length

print(len(a))

