
# how to use for loop : Syntex

word=['cat','window','defenestrate']
for x in word:
    print(x,len(x))
print ()

# Loop over a slice copy of the entire list.

for x in word[:]:
    if len(x) < 4 :
        word.insert(2,"hafizur rahman")
print (word)
print ()

# print 1 to 10 number.

for i in range(10):
    print(i+1)
print()

# print 0 to 2 number.

for i in range(0,3):
    print(i)
print()

# print 0 to 100 number addition with 30 number.

for i in range(10, 100, 30):
    print(i)
print()

# print element with length number.

a=['marry','had','a','little','lamb']
for i in range(len(a)):
    print(i+1,a[i])
print()

# print -> range.
# list -> range.

print(range(10))
i = list(range(3))
print(i)
print()

# write a code that a number is a prime

for i in range(2, 10):
    for j in range(2, i):
        if i % j != 0:
            print(i,'equals',j,'*',i//j)
            break
    else:
        print(i,'is a prime number.')


print ()

fruit =['football','cricket','badminton','hoki','kabadi']

for i in fruit:
    print(i)

print ()


# partern: practice

for i in range(4):
    for j in range(i+1):
        print ("# ",end ="")
    print ()
print()

# another partern practics

for i in range(4):
    for j in range(4-i):
        print ("# ",end ="")
    print ()

print()

a = {'name' : 'hafizur', 'nickname' : 'litton', 'email' : 'mdhafizurrahman694@gmail.com', 'phone' : '00011269557'}
print(a)
print(type(a))
for item in a:
    print(a[item])

print()

a = {'name' : 'hafizur', 'nickname' : 'litton', 'email' : 'mdhafizurrahman694@gmail.com', 'phone' : '00011269557'}
print(type(a))
for item in a:
    print(item)


print()

# we also can use "else statment" in a for loop :

for i in range(1,6):
    print(i)

else:
    print("loop is over.")