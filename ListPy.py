
m=[1,2,3,4,5,6,7,8]
n=[9,11,12,13]
c=m+n
z=[m+n]
y=[m,n]
print(m)
print(m[:]) # printed all value
print(m[0]) # print first number
print(m[-1])# print last number
print(m[-3:])# print last three to end
print(m[3:])# print 3 to end
print(m+n+[10]) # adding two list
m[7]=8**2 # replace 7 index to another number
print(m[:])
m.append(3**2) # append use to 'adding' number in the 'last position'
print(m)
m.insert(0,88) # insert use to 'adding' number following 'index' number
print(m)
m.sort() # organaizing to assending order
print(m)
m.remove(m[8]) # remove item following index number
print(m)
m.remove(6)
print(m)
m.pop() # pop use to remove last item
print(m)
m.pop(m[2]) # pop use to remove number following index
print(m)
m.clear() # to remove all item
print(m)
m=[1,1,2,2,2,3,3,5]
m=m+['a','b','c'] # adding another list
print(m)
print(m.count(2)) # to count item number
m.extend([3,4,8,6,77]) # use to add moltiple item
print(m)
m.reverse() # use it to reverse item
print(m)
l=['a','b','c','d','e','f']
print(l)
l[3:5]=['D','E'] # replace some values.
print(l)
del l[0] # delete number following index
print(l)
l[3:5]=[] # now remove them.
print(l)
l[:]=[] #all dlete
print(l)
print(len(l)) # counting length number.
print(c) # including in one braket.
print(z)   # including with two braket.
print(y)   # including with two braket.and they are separet.
print(y[1][1]) # calculate row and colum.
print(z[0][6]) # calculate row and colum.