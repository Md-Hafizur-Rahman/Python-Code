word=['cat','window','defenestrate']
for x in word:
    print(x,len(x))
print ()

for x in word[:]:   # Loop over a slice copy of the entire list.
    if len(x) < 4 :
        word.insert(2,x)
print (word)
print ()

for i in range(10): # print 1 to 10 number.
    print(i+1)
print()

for i in range(0,3): # print 0 to 2 number.
    print(i)
print()

for i in range(0, 100, 30): # print 0 to 100 number with 30 distance.
    print(i)
print()

a=['marry','had','a','little','lamb'] # print element with length number.
for i in range(len(a)):
    print(i+1 ,a[i])
print()

print(range(10)) # print -> range.
i = list(range(3))  # list -> range.
print(i)
print()

for i in range(2, 10):
    for j in range(2, i):
        if i % j != 0:
            print(i,'equals',j,'*',i//j)
            break
    else:
        print(i,'is a prime number.')