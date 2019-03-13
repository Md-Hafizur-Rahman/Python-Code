
"""
 Comprehension use for itarate with expretion . it's have three part:

 1.output expretion
 2.input sequence
 3.condition (optional)


"""

# list comperihension :

my_list=[i**2 for i in range(10) if i%2==0] # use comprehension .
print(my_list)
print(type(my_list))

print()

# Set comprehention :

my_list=['hafizur','rahman','python','a','b']
new_list={i for i in my_list if len(i)>1} # use comprehension
print(new_list)
print(type(new_list))

print()

# dictionary comprehention :

my_list=['name','country','passion']
my_list1=['hafizur.','bangldesh.','programming.']
new_list={i:j for i,j in zip(my_list,my_list1)} # zip use to itarator with parallal.
print(new_list)

print()
