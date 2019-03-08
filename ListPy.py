
m=[1,2,3,4,5,6,7,8]
n=[9,11,12,13]
z=[m+n]
y=[m,n]
print(m)
print(m[:]) # printed all value
print(m[0]) # print first number
print(m[-1])# print last number
print(m[-3:])# print last three to end
print(m[3:])# print 3 to end
print(m+n+[10])
m[7]=8**2
print(m[:])
m.append(3**2)
print(m)
l=['a','b','c','d','e','f']
print(l)
l[3:5]=['D','E'] # replace some values.
print(l)
l[3:5]=[] # now remove them.
print(l)
l[:]=[] #all dlete
print(l)
print(len(l)) # counting length number.
print(m+n) # including in one braket.
print(z)   # including with two braket.
print(y)   # including with two braket.and they are separet.
print(y[0][1]) # calculate row and colum.
print(z[0][6]) # calculate row and colum.