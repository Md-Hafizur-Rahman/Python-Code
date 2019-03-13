
# how to use Break , Continue and Pass statement in a code :

# Break statment:

for i in range(1,11):
    if i == 5:
        break
    print(i)

print()

# Continue statment:

for i in range(1,8):
    if i == 5:
        continue
    print(i)

print()

# pass statment:

for i in range(1,8):
    if i == 5:
        pass # no change here. pass statment is a NULL statment .
    print(i)