##File Pointers / File Data Types
# f = open("helloWorld.txt", "r")
# print(f)
# print(type(f))
#
# f.close()
#
#
##Read and print every line
# f = open("helloWorld.txt", "r")
#
# for line in f:
#    print(line)
#
# f.close()
#
#
#
##Read and print a selection of lines
# f = open("helloWorld.txt", "r")
#
# #skip first three lines
# for i in range(0, 3):
#    f.readline()  #read and ignore the line
#
# #read and print the next five lines
# for i in range(0, 5):
#    line = f.readline()
#    print(line)
#
# f.close()
#
#
##Using the with block to open and close
# with open("helloWorld.txt", "r") as fileIn:
#
#    for line in fileIn:
#        print(line[0:5])
#
#
##no need to call fileIn.close()
#
#
#
#
##Counting lines
# with open("helloWorld.txt", "r") as fileIn:
#     c = fileIn.read().count("\n")
#     print(c)

# Count how many times "hello world" appears in file
# with open("helloWorld.txt") as fileIn:
#
#    counter = 0
#
#    for line in fileIn:
#        counter += line.count("hello world")
#
# print(f'hello world appears {counter} times in the file')
