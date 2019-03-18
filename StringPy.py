c=2**3
d=2*3
e='hafuz'
f=e*3
print("c is : {0} and  d is : {1}".format(c,d))
print("c is : %i and  d is : %i"%(c,d))
print("c is :",c,"and  d is :",d)
print()

print("hello world!\tI am hafiz.")
print()

print("hello world!\nI am hafiz.")
print()

print("hello world!\\I am hafiz.")
print()

print("\"hello world!\"\"I am hafiz.\"")
print()

print("'hello world!''I am hafiz.'")
print()

print(r"hello\'s world!\n i am hafiz.") # use r to avoid extarnal oparetion
print(f)

# acses string

word=' pythonist'

print('j'+word[1:])
print(word[:3])
print(word[-1]) # -1 means last character.
print(word[2:5])
print(word[-2:]) # characters from the second-last (included) to the end
print()

# adding string

m='hafizur rahman a '
print(m+word)
print()

# join () function including ( '.' .join() )

print('->'.join((m,word)))
print()

# capitalize() function

print(m.capitalize())
print()

# upper() function

print(m.upper())
print()

# lower() function and casefold() function and they work same

print(m.lower())
print(m.casefold())
print()

# swapcase() function and it convert upper to lower or lower to upper

print(m.swapcase())
print()

# count any word

n='I am a CSE student of Daffodil International University.!!'

print(n.count('I'))
print(n.count('s',40)) # after index number 30 , counting 'i'
print(n.count('s',5,10)) # count 's'  -> 5 index to 10 index
print()

# replace() function replace another item
print(n.replace('!','')) # delete ! item and replace by blank
print(n.replace('s','g')) # replace 's' to the charectar of 'g'
print()

# find () function to use finding index number

print(n.find('C')) # find it index number
print()

# split() function use to separate each word

print(n.split(' '))
print()