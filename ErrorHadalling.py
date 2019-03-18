
# Error Handalling

# try......except :


try :
    with open('test.txt','r') as my_file:

        print(my_file.read())

except:
    print('file doesn\'t exist')
print('made by hafizur rahman')

print()

# To handle a specific exception, you want to enter the code except for the name of the exception by its name.
# Again, if you want to get rid of the thrown message by expressing the message, it will be displayed to the user.

try :
    with open('test.txt', 'r') as my_file :
        print(my_file.read())

except FileNotFoundError :
        print('file doesn\'t exist')
print('made by hafizur rahman')

try :
    my_list = []
    print(my_list[0])

except IndexError as e:  #  print spech of IndexError .
    print(e)
print()

# In fact for a try block, as much as possible except the block can be written.
# However, the name of the exception will be mentioned in each except the block.

try:
    my_file=open('test.txt','r')
    content=my_file.read()
    print(content)
    i=int (content.split())
except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): ({1})".format(errno, strerror))

except ValueError:
    print("No valid integer in line.")

except:
    print("Unexpected error!")
print()

# If we wanted, we could have settled all the errors in a except block.

try:
    my_file = open('test.txt')
    content = my_file.read()
    i = int(content.strip())

except (IOError, ValueError):
    pass

# try … except … else

try:
    a=10
    b=5
    c=a+b
    print(c)
except ValueError as e :
    print(e)
except NameError as f:
    print(f)
else:
    print('there are no Error')
print()

# Whether any exceptions are rayed or not, finally the block code is executed exactly.
# That's why it is called a clean-up action.

try:
    with open('test.txt', 'r') as my_file:
        content = my_file.read()
        print(content)
except FileNotFoundError:
    print('The file does not exist.')
finally:
    print('To be exceptional or not it work properlly.')


# raise exception
'''

1.Python has many built-in exceptions. If we want, we can raise them.
2.To use Execution Route is to use the statement. After raise,
the name of the built-in exception is to be passed along with the error message strings inside the bracket.

3.In addition to built-in exception, Python user-defined extensions can be used.

'''

try:
    raise NameError('Hey! It is a custom error message.') # raise ErrorName
except NameError as e:
    print(e)