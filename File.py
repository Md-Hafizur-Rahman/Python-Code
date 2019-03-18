
# file :

'''

We will use the open () function to open Python file.
it have three parameter.
1.file name
2.Access mode
3.Buffering

2.access mode:
-> r,rb,r+,w,wb,w+,a,ab,a+,ab+

'''

# syntex and how to work.

my_file=open('test.txt','r') # open file
conent=my_file.read() # it use to read file
print(conent)
my_file.close() # it use to close file

print()

my_file=open('test.txt','w+')
my_file.write('I am a CSE student of Daffodil Interrnational University') # it use to wright file
print(my_file.read())
my_file.close()
print()

my_file=open('test.txt','r')
print(my_file.read(6))
print(my_file.read()) # it use to read file
print(my_file.tell()) # it find position of  totall index number
my_file.seek(0,0) # it point first index number
print(my_file.read())
my_file.close() # to close file

print()

# with statment in file. it's best to use.not need to define close() method

with open('test.txt','r') as my_file :
    print(my_file.read())
