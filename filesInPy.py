firstFile = open(
    "firstFile.txt", "w"
)  # open is built in method to create files, it takes two parameters, 1st is fileName, 2nd is mode of file(read,write,readandwrite,append) - NOTEE - whenever we call the open() with write as 2nd parameter, it always deletes the content from the targeted file and insert fresh datas/ rewrite everything to the file => if file is available, if not => then it will create a new file
firstFile.write(
    "My First File, will do more, Hustle..."
)  # write is a method to write a file, important thing the write() method only takes arguments of string
firstFile.close()  # then we need to close the file
print(type(firstFile))
# firstFile is an file-object - in py terms we denoted as filehandler

with open("secondFile.txt", "w") as secondFile:
    secondFile.write("Something Messy!!!")

# with the use of (with) keyword, we have exact behaviour of what we done before, but this time we dont need to close the file, it will done under the hood

# to append a file
with open("firstFile.txt", "a") as firstFile:  # this firstFile act as a filehandler
    firstFile.write("\n This is my Second Line. Prepare for the Revenge...")

with open("secondFile.txt", "a") as secondFile:  # this secondFile act as a filehandler
    secondFile.write("\n This is my Second Line. Lets clean the messs!!!")

with open("iterateFile.txt", "w") as iterateFile:
    for i in range(1, 11):
        iterateFile.write("Line: %d \n" % i)

with open("iterateFile.txt", "a") as iterateAppend:
    for i in range(11, 21):
        iterateAppend.write("Line: %d \n" % i)

# mode - w - to write a file
# mode - w+ - to write a file, and read a file
# mode - r - to read a file
# under mode - r- we have read, readline, readlines are built-in-methods we have...
# read - read the entire data from a file, it accepts parameters also if we pass read(3), it will read only three characters from the targeted file,
# readline - read the entire line of a targeted file
# readlines - read the entire data of a file and return as a List format, after we may able to play with list's methods
# mode - r+ - to read a file, and write a file
# mode - a - to append a file

with open("iterateFile.txt", "r") as readIterateFile:
    # print(
    #     readIterateFile.read()
    # )  # while reading a file we need print to get the desired result
    # print(readIterateFile.read(5))
    # print(readIterateFile.readline())
    print(readIterateFile.readlines())
    print(len(readIterateFile.readlines()))
    print(type(readIterateFile.readlines()))

# read datas from iterateFile and to write those datas to newIterateFile

with open("iterateFile.txt", "r") as iterateFile:
    with open("newIterateFile.txt", "w") as newIterateFile:
        newIterateFile.write(iterateFile.read())
