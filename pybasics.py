""" this three quotation indicates multi-line docstring comments """
# this # indicates single line comments
""" 1 - Varibles & Memory Management in py """

print("Hi we are gonna rock!")
a = 1000
b = 2000
c = a + b

id(c)  # id is a identity of the variable
""" here id() returns a unique id for the variable, which means its returned the memory location of a variable, each variable has a unique memory location unless its has a same value
i.e x = 1000, a = 1000 => here the both variables have a same memory location, python will store them in a  container in a efficient way, whenever the variable changes to different value then only its creates new memory location unless the location remains the same... """
print(c)

d = 3000
e = 2000
f = d + e

id(d)
id(f)
print(f)

""" 2 - Datatypes in py => 1 - pre-defined/built-in datatypes, 2 - user-defined datatypes """
""" we often use built-in datatypes, unless if you jumping to algorithm/data structures then we use user-defined datatypes """
""" now 5 types of datatypes in built-in datatypes,
    1 - None - nothing other but null in other launguages
    2 - Numeric - under we split into four, 1- Int, 2 - Float, 3 - Complex, 4 - Bool
    3 - sequences - under we split into four, 1 - String, 2 - List, 3 - Tuple, 4 - Range
    4 - sets
    5 - mapping which is also known as dictionaries
 """

""" 1 - None """
g = None
""" is equals to null, cpaital N is mandatory one - None """
print(g)

""" 2 - Numerics & their types """

""" int """
h = 50
print(type(h))

""" float """
i = 40.90
print(type(i))

""" complex """
j = complex(4, 5 > 12)
""" it accepts two argument, 1st is real value, 2nd is imaginary value. Note: if you pass string as a 1st argument then the 2nd argument cant be accepted, it provides this error => TypeError: complex() can't take second arg if first is a string, it accepts int, float, string as well as boolean as an argument """
print(j)
print(type(j))

k = 10 > 1
""" in python we say boolean as bool -> true represents 1, false represents 0 """
print(k)
print(type(k))


""" 3 - Sequences & their types """

""" string """
my_name = "Messi"
print(my_name)
print(type(my_name))

""" List - ordered, mutable, allow duplicates"""
""" List are arrays in python, but it stores different types of datatypes, any values i.e ['str', bool, 1, 0.5], Note: list can be modified """
my_list = ["Messi", 35, 5.5, "Argentenian", 10]
print(my_list)
print(type(my_list))

""" this is indexes of an list in python, similar to arrays """
print(my_list[3])

""" we can able to add elements to the existing list """
my_list.append("Greatest of all time - GOAT")
print(my_list)

""" append - add a element at the end of a list """
""" insert - to add element at a specific index - it accepts two parameters - 1st is which index to add, 2nd is the value """
""" extend - to add another list elements in current list - its not only from another list any iterable object like tuples, sets, dictionaries/mapping """

""" Tuples - ordered, immutable, allow duplicates """
""" Tuples are very similar to List, the only difference is the paranthesis, we use tuple like this ('Messi',35,5.5,'Argentenian',10,'GOAT') , important Note: tuples are immutable while lists are mutable, tuples cant be modified after once created in python, usually tuples are faster than Lists """
my_tuple = ("Pedri", 21, 5.8, "Maestro", 8)
print(my_tuple)
print(type(my_tuple))

""" this is indexes of an tuple in python, similar to list """
print(my_tuple[3])
""" Note: tuples are immutable, cant able to modify once after the creation """

""" Range """
""" range is often used as loops, if you want to print some range this to this kind of stuff """
""" syntax of range range(start,stop,step) - it accepts three parameters - 1st and 3rd params are optional, 2nd is mandatory - default value of 1st param is 0, default of 3rd param is 1 """
my_range = range(1, 10, 3)
print(my_range)
print(type(my_range))

my_test_range = tuple(range(10))
print(my_test_range)

""" if i need to print my_range directly, inthis case its just a range, i need get the value from range - how ? i need to convert this range to list, see below """
my_list_range = list(my_range)
print(my_list_range)
print(type(my_list_range))

""" u can also directly convert range to a list """
my_list_range_dir = list(range(10, 25, 2))
print(my_list_range_dir)

""" 4 - Sets - unordered, mutable, doesn't allow duplicates """
""" sets is a unordered collection of elements, syntax {1, 20, 23, 232} """
my_set = {1, 5, 0, 90, 456}
print(my_set)
""" the print show result like this {0, 1, 5, 456, 90}, thats y its called as unordered collection of elements, u cant access the element of a set like this my_set[1] like this, becoz its an unordered collection of elements, if we do we got the error - 'set' object is not subscriptable """
print(type(my_set))
# print(my_set[0])

""" we can able to convert some list or tuple to a set """
list_set = [1, 2, 3, 4, 30, 200]
set_list = set(list_set)
print(set_list)
print(type(set_list))

tuple_set = (1, 2, 5, 90, 200)
set_tuple = set(tuple_set)
print(set_tuple)
print(type(set_tuple))

""" we can also able convert set to a list or tuple """
con_set_li = list({1, 2, 3, 4, 500, 20, 40})
print(con_set_li)
print(type(con_set_li))

con_set_tup = tuple({1, 5, 10, 15, 20, 300, 30})
print(con_set_tup)
print(type(con_set_tup))

""" Mapping / Dictionaries - ordered, mutable, doesn't allow duplicates """
""" Dictianaries are similar to objects, in other words u can imagine a real dictonary, key value pairs like Why:why are you late? - this is key value pair - why is term key, then the value and inportant note dictionaries can't allow duplicates """
""" syntax - {10:'Messi',7:'Ronaldo'} """
my_map = {10: "Messi", 7: "Ronaldo", 8: "Iniesta"}
print(my_map)
print(type(my_map))

""" we can able to access values inside of dictinaries like below, same what we are do in objects, but not with . we use my_map[10] like this """
print(my_map[10])


# syntaxes
# None
# x = 1, y = 0.5, complex(rea,value,imaginaryvalue), bool represents 1 - true, 0 - false
# z = 'messi', [1,2,3,4], (1,2,3,4), range(start,stop,step)
# a = {1,2,3,4}
# able to convert set to a tuple or list and also vice versa, able to convert tuple or list to set

""" 3 - Literals and Identifiers """
m = 90
""" here m is a Identifier, 90 is a Literal - in nnormal terms m is variable we defined, 90 is a value we assigned to that variable and = is a operator assigning literals to identifiers """
""" In Literals we split into three - numeric - (int,float,decimal,octal,hexadecimal,complex), boolean, string """
""" we called it as a integer literal that - 90 """

""" 4 - Reserved words in python, we cant used to Identifiers/Variables - need to check in github - put a image regd that """

""" 5 - Operators in python """
""" General purpose of programming is, we provide data, then the interpreter/system performs a operation, then it will give the results - how we do that """

""" i.e x + y - here x,y are operands and + is an operator, we provide literals to x and y identifiers """
""" Operators and its types 
        1 - Arithmetic (we perform operations) -> + (add), - (sub), * (mul), / (div) - it gives the division of two int literals in float lietal, % (modulus) - give you the remainder of division, // (quotient) - it gives floor value of division(int), ** (exponent) - it gives power root of given number ie. 2 ** 3 - 2 is a value, 3 is power (here is 2cube)
        2 - Assignment (we assign literals to identifiers and perform operations using assignment operators) -> =, +=, -=, *=, /=, %=, //=, **=
        3 - Unary Minus -> - and + before we assign it to a variable it will convert this to negative or positive
        4 - Relational (we compare two identifiers) -> >, <, ==, !=, >=, <=
        5 - Logical -> and, or, not
        6 - Boolean -> True, False

        note : = is used to assign a value
               == is used to compare two values
               === is used to compare two value and also checks whether the two datatypes are same
"""

""" Unary minus """
n = 30
print(-n)
print(n)
o = -20
print(-o)
""" in the end it gives the result of positive literal, which means - into - + thats y we get the positive result, same applicable in vice versa """


""" 6 - Escape Characters """
short_string = "messi"
long_string = "messi is the greatest\
 of all\
 time\
 simply mentioned as\
 GOAT"
print(long_string)

""" backslash - \ is to mentioned that the string is not end, its continued i.e 'messi\'s left foot' -  """

long_string_n = "messi \n Greatest of all Time \n GOAT"
print(long_string_n)

""" \n - to take a new line """

""" real time example see below """
path = "c:\downlaods\app\nodejs"
print(path)
""" c:\downlaodspp
odejs """
""" i get the above result - coz \n in escape characters is to take a new line thats y we got the result - to prevent this behaviour we use double backslash \\ - this \\ is to convert this to \ which means - \\ = \ """

path_n = "c:\downloads\\app\\nodejs"
print(path_n)
""" now i got the expected one - c:\downloadspp\nodejs """

""" there are some escape characters out there """
# \' , \" , \r , \t , \n , \v , \h

""" 7 - Input & Output Statements """
""" Output Statements """
print(16 / 4)
num1 = num2 = 100
print(num1 * num2, "is the multiplication of x and y")
# the above we got 10000 is the multiplication of x and y - but what we expect is 10000 is the multiplication of 100 and 100 - how we do that in python - need to use format()
print("{0} is the multiplication of {1} and {2}".format(num1 * num2, num1, num2))
""" now wwe got the xpected result - 10000 is the multiplication of 100 and 100 """
""" there are so many formating options out there """
""" format() method accepts - any datatype as a argument """
print(
    "{string1} is simply mentioned as {string2} - {string3}".format(
        string1="Messi", string2="Greatest of all Time", string3="GOAT"
    )
)

""" Input Statements """
my_first_q = input("Provide your name :")
my_second_q = int(input("provide your age :"))
# the input() function returns a string - we need convert to integer for age - this conversion we called as type casting i.e see above line. type casting - type casting means convert one datatype to another datatype
print("Hi {0}, you age is {1}".format(my_first_q, my_second_q))

messi_bio = {
    "name": input("Provide your name: "),
    "age": int(input("Provide your age: ")),
    "callsign": input("Provide me your callsign: "),
}
print(
    "Hi {0}, your age is {1}, your callsign is {2}".format(
        messi_bio["name"], messi_bio["age"], messi_bio["callsign"]
    )
)

""" 8 Built-in functions & modules need to check in documentation """

""" 9 if...elif...else """
jerseyNum = 10
if jerseyNum == 10:
    print("Lionel's")
else:
    print("Somenone's")

print("the above if...else got closed")

print("the below if...elif...else got started")

colorPat = "White"
if colorPat == "Red":
    print("Your preferred color is {colorPat}")
elif colorPat == "White":
    print("Your preferred color is {colorPat}")
else:
    print("kindly chose color patterns")

isYourAge = int(input("Provide your age: "))
haveVoterId = input("Do you VoterId say YES or NO: ")
if isYourAge >= 18 and isYourAge <= 25:
    if haveVoterId == "yes":
        print("Approved, and Eligible for Voting")
    else:
        print("Hold, Get details to provide VoterId")
elif isYourAge >= 25 and isYourAge <= 60:
    if haveVoterId == "yes":
        print("Mid Citizens Eligible Candidate")
    else:
        print("Mid Citizens")
elif isYourAge >= 60:
    if haveVoterId == "yes":
        print("Super Senior Eligible Citizens")
    else:
        print("Super Senior Citizens")
elif isYourAge <= 18:
    print("Your are not eligible for Voting")
else:
    print("Retake assesment")


""" Loops """

# While
startP = 10000
while startP < 10010:
    print("loop of --->", startP)
    startP += 1
else:
    print("End")
# in python a else block also possible, whether the condition fails then fall under else block

# in keyword in python - to check some values are available in some variable i.e below
A = {1, 2, 3, 4, 5}
print(5 in A)

# For - we can list, tuples, range, dictionary in for loops - any iterable object
for i in A:
    print(i)

forDict = {10: "Messi", 8: "Iniesta"}
# if you only want keys from dictionary then,
for x in forDict:
    print(
        x
    )  # by default the for loops takes only keys from dictionary - also get forDict.keys() method to get the keys from dictionary

# if you only want values from dictionary then,
for x in forDict.values():
    print(x)

# if you only want both keys and values from dictionary then,
for x, y in forDict.items():
    print(x, " ", y)
else:
    print("End")

""" Continue & Break statements """
B = [0, 1, 2, 3, 4, 5]
for x in B:
    if x == 2:
        break  # if we use break here, it will end the iteration of remaining elements, get out of the loop
    print(x)
print("End")

C = (100, 101, 102, 103, 104, 105)
for y in C:
    if y == 104:
        continue  # if we use continue, it will skip current iteration of element and remaining code, it will directly jump to the next element for iteration
    print(y)
print("End")

""" Strings and its methods """
my_str_l = "messi"
my_str_u = "MESSI"  # case-sensitive
print(id(my_str_l))
print(id(my_str_u))
# returns two different memory location

print(my_str_l.upper())
print(my_str_u.lower())
print(my_str_l[3])
print(
    my_str_u[4]
)  # if we use like, its a indexing of particular string, but what if if i want a substring, see below

subs_s = "Good Evening"  # here we want the good only not evening, how we do that, its done by slicing in python, see below to get the substring
print(
    subs_s[0:4]
)  # it is slicing, which index position to start the search, which index position to end, important note the end index position stopped at which position we given as arguement, means the stop at 4th index position and the 4th index element not included

str_without_strip = "          Hell Yeah                 "
print(str_without_strip)
print(
    str_without_strip.strip()
)  # the strip() method is to remove the whitespace from the beginning and at the end of the string

# lstrip() - while lstrip() removes the whitespaces only ffrom left side of the string
# rstrip() - while rstrip() removes the whitespaces only ffrom right side of the string
# islower() - to check whether the given string is lowercase - even a single character in uppercase its returns false
# isupper() - to check whether the given string is uppercase - even a single character in lowercase its returns false
# replace() - to replace characters as well as sequence of characters, i.e Hello - replace("l","i") - it replaces all the l characters in string and replaces it with i
# split() - to split a string based on some characters, this method always returns a list

print(subs_s.replace("Evening", "Boy"))

sp_str = "hukum-tiger-ka-hukum"
print(sp_str.split("-"))
print(type(sp_str.split("-")))

""" here one additional funny thing """
print(sp_str * 10)  # it will print the string * 10


""" List and its methods """
xList = ["Messi", 10, "GOAT", 10.00]
xList.insert(4, "Ronaldo")
xList.insert(5, "Ronaldo")
print(xList)

xList.remove(
    "Ronaldo"
)  # it will remove the specified element from the list, if the list has 2 Ronaldo then the least index position element got the removed and then the remaining Ronaldo are still available in the List
print(xList)

# if you want to remove the last element of a list you can use pop method
xList.pop()  # we dont need to mention anything, it always removes the last element of a List
print(xList)

# if you don't want to delete the list, just want to clear the List use xList.clear() - to clear the List, after List cleared if you print the list you got the empty list
xList.clear()

# if you want to delete the entire List
del xList  # it delete the entire list and also clear the List in memory location also and not even present in our garbage memory

""" sort() method in List ASC to DESC - sort is only applicable if a List have same datatype, not applicable for mixed datatype List, i.e """
sorListNum = [1, 5, 0, 3, 6, 2, 4]
sorListNum.sort()
print(sorListNum)
sorListAlp = ["a", "c", "d", "b", "e", "g", "f"]
sorListAlp.sort()
print(sorListAlp)

""" reverse() method in List DESC to ASC """
sorListNum.reverse()
print(sorListNum)
sorListAlp.reverse()
print(sorListAlp)

""" append() to add element at the end of the list """
""" len() to return the length of a given List - length means how many elements present in that list, this method mostly available all the datatypes """
""" count() to check whether the given argument is how many times occured in the List and this method also available for Tuples """
print(len(sorListNum))
print(
    sorListNum.count(2)
)  # checks and returns the count, the 2 argument/element is how many times occured in the list

""" Tuples and its methods """
""" count() to check whether the given argument is how many times occured in the Tuple """
""" len() to check the length of the Tuple"""
""" max() to get the max element in a tuple """
""" min() to get the min element in a tuple """
""" del(tuple_name) to delete the tuple """

""" important note: we can't modify tuples, but we can concate tuples (one tuple with another tuple) - see below """
tup1, tup2 = (100, 200), (300, 400)
tup3 = tup1 + tup2
print(tup3)
""" here i assign my tup3 to tup1 is the other way to around to modify tuple """
tup1 = tup3
print(tup1)

""" if sometimes tuple have a single element - to denote/mention its a tuple we should do like that - see below """
test_tup = (
    "Chaos",
)  # comma in that tuple denotes its tuple, if we didn't use that comma its difficult to identity what datatypes that is ?, putting that comma in the end it doesn't affect the code behaviour
test_tupp = ("Chaos",) * 5
print(test_tupp)  # it prints the element of a tuple 5times

""" Dictionaries and its methods """
new_dict = {
    "name": "messi",
    "age": 35,
    "callsign": "god",
    ("spouse", "children1"): ("antonela", "thiagomessi"),
}

print(new_dict[("spouse", "children1")])
(print(new_dict.get("callsign")))  # to access particular value of a dictinary key

n_d = {
    "Barcelona": {
        "gk": "Mats",
        "lb": "balde",
        "cb1": "Araujo",
        "cb2": "kounde",
        "rb": "cancelo",
        "dm": "oriol",
        "rm": "gundo",
        "lm": "dejong",
        "lwf": "ferran",
        "amf": "pedri",
        "cf": "lewa",
    }
}
print(n_d["Barcelona"]["amf"])
print(type(n_d))

n_d["Barcelona"]["skipper"] = "messi"
print(n_d)
print(len(n_d["Barcelona"]))

# pop() is usually to remove element from end of a iterable object
n_d["Barcelona"].pop("dm")
print(n_d)

# clear() to cleaar the dictianry, truncate
# del n_d entirely delete the dictinary from memory location as well as garbage collector, here after not able the acces the n_d dictionary
# keys() - to access ony dictionaries keys()
# values() - to access ony dictionaries values()
# items() - to access ony dictionaries items()
# update() - to  update the values using keys in dictionary
n_d["Barcelona"].update({"skipper": "Lionel Messi"})
print(n_d)

# uppdate ok, then how we overwritten the dictionary see below
n_d["Barcelona"]["amf"] = "PedriGonzalez"
print(n_d)

# Indexing, Negative Indexing, Slicing
qwer = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(qwer[0])  # -> indexing to get the values form a list

# Slicing with positive indexing
print(
    qwer[0:3]
)  # -> slicing to get the values from 0th index position to 3rd index position, which means the 3rd index position not include, we got the result of [0,1,2] - if we use third argument then it willl be step i.e qwer[0:3:1] - the default value of third argument is 1
print(
    qwer[5:]
)  # -> use like this it start the search from 5th index position, till the last index position, the 5th index position will be included
print(
    qwer[:5]
)  # if we use like this, it start the search from 0th index position (default), to the given index position
print(
    qwer[:]
)  # this will get the entire elements from a list, start, end, step all are gonna take defualt arguments, end argument is optional
print(qwer[::2])  # with step
print(qwer[::3])  # with step

# Slicing with Negative Indexing
# take MESSI as eg

""" M  E  S  S  I  I """
"""-6 -5 -4 -3 -2 -1 """
# the above is the negative indexing looks like, its starts invertly from last with -1 as 1st index position, if we want reverse the result see below..
og = "MESSII"
print(
    og[::-1]
)  # it will start the position from -1, and it will reverse the given string
print(
    og[-6:-1:]
)  # this will start the search from -6th index position to the -1st index position
print(og[:-1])
print(og[-6:])

print(og[0])  # positive indexing
print(og[-6])  # negative indexing
# both return the same result

print(og[3::-1])  # will get the result in reverse order


# Functions are to do a specific task whenever is needed, Functions are divided into two 1st one is Built-in-Functions like print(), input(), id() etc, and the 2nd one is User-defined-Functions - custom functions created by us.
# syntax -> def function_name (param1,param2): # inside function block with indendation
def call_now(num1, num2):
    return num1 + num2


print(call_now(1, 2))


# positional arguments
def posA(param1, param2):
    print("1kg of {0} Rs.{1}.00".format(param1, param2))


posA("Tomato", 100)


# keyword arguments
def keyA(item, price):
    veggies = {"vegetable": {item, price}}
    print(veggies["vegetable"])


keyA(item="Beetroot", price=30)


# default argument - in default arguments if we pass arguments then it will take the proivded value, else if we dont pass value it will take the default argument as a value to the particular parameter
def defA(item, price=20):
    print("item", item)
    print("value", price)


defA(item="Carrot", price=25)


# variable length arguments
def varL(
    name, age, *skills
):  # if we use asterick before the parameter, it tells the python interpreter - 'that particular param contains/has/able to accepts multiple values, the multiple value returned from function is tuples - remember its only for last arguments'
    print("name", name)
    print("age", age)
    print("skills", skills)


varL("Messi", 23, "Python", "Javascript", "React", "Redux")


def varL2(
    name, age, **skills
):  # if we use double astericks, then it will accepts mulitple keywords, this ttells the python interpreter that the particular parameter contain multiple keywords - note it will return as a dictionary(key:value pair) not as a tuple
    print("name", name)
    print("age", age)
    print("skills", skills)
    for x, y in skills.items():
        print(x, y)


varL2(
    "Messi",
    23,
    backend="Python",
    frontend="Javascript",
    frontend_library="React",
    frontend_library_package="Redux",
)

# Global Variables & Local Variables
# global variables are accessible anywhere in the file i.e see below...
# this g_v variable can be accessible anywhere during the compilation
g_v = 10


# local variables are accessible only within the specific limit, i.e
def locV():
    global var_t1
    var_t1 = 10
    var_t2 = 20


locV()

# the above var_t1 and var_t2 are local variables only accessible inside the function, if i try to print that variables outside of the function then it will throw a error only undefined variables

# one more thing if you want access var_t1 globally - we need to use a global keyword on that - see above function.

print(g_v)
print(var_t1)
# print(var_t2)  - ameError: name 'var_t2' is not defined. Did you mean: 'var_t1'?


""" OOPS - Object Oriented Programming System """

# Class - Blueprint or structure plan
# Object - A member following same structure of Class
# Encapsulation - to encapsulate data and methods together, and protect them using private, public, protected methods to avoid unneccessary accidents, to protect data from some users
# Abstraction - Only give neccessary details to the user, hiding background operations to the external world
# Inheritance - we can inherit classes from base class, which means we can able to re-use code from base class to intermediate class to derived class
# Polymorphism - poly- many, morphos - forms, Polymorphism is the ability of an object to take on many forms


""" Class - in class we have attributes and methods """
# all attributes will be our variables
# all methods will be our functions/actions - note: whenever we use functions/actions in our class we denoted as methods


class Car:
    def __init__(self, carName, carColor, carMaxspeed):
        self.name = carName
        self.color = carColor
        self.maxspeed = carMaxspeed
        print("hit initialization __init__ method")

    def getCar(self):
        print(
            "The car name is {0} and my car color is {1} with the maxspeed of {2}".format(
                self.name, self.color, self.maxspeed
            )
        )


suzukiDesire = Car("Desire", "Purple", 300)  # this suzukiDesire is a instance of class
print(
    "The car name is {0} and my car color is {1} with the maxspeed of {2}".format(
        suzukiDesire.name, suzukiDesire.color, suzukiDesire.maxspeed
    )
)
suzukiDesire.getCar()

suzukiCiaz = Car("Ciaz", "White", 400)  # this suzukiCiaz is a instance of class
print(
    "The car name is {0} and my car color is {1} with the maxspeed of {2}".format(
        suzukiCiaz.name, suzukiCiaz.color, suzukiCiaz.maxspeed
    )
)
suzukiCiaz.getCar()

""" now let learn about __init__ and self """
# __init__() - init function is called a constructor or initializer and is automatically called when you create a instance of class, its used to initialize the attributes/variables
# whenever i create a instance of class that is object, it will automatically first call the __init__() method from a class which means initialization method. example see below

suzukiAlto = Car("Alto", "Black", 150)
suzukiCelerio = Car("Celerio", "Red", 180)

# self is a variable that refers to current class instance
# whenever we create a instance for the class Car, a separate memory block is allocated on the heap, the memory location by default store in this self variable - here self refers to our instances which means objects memory location
# Constructor - is a special type of function/method which is used to initialize the instance members of the class.
# __init__() is a constructor method

print(id(Car))
print(id(suzukiDesire))
print(id(suzukiCiaz))
print(id(suzukiAlto))
print(id(suzukiCelerio))


class Student:
    def __init__(self, stuRollno, stuName, stuAge, stuGrade, stuGender):
        self.rollno = stuRollno
        self.name = stuName
        self.age = stuAge
        self.grade = stuGrade
        self.gender = stuGender
        self.standard = "12th A"

    def getStuPosition(self):
        print(
            "{0},{1},{2},{3},{4},{5}".format(
                self.rollno,
                self.name,
                self.age,
                self.grade,
                self.gender,
                self.standard,
            )
        )
        students = {
            self.rollno: {
                "Name": self.name,
                "Age": self.age,
                "Grade": self.grade,
                "Gender": self.gender,
                "Standard": self.standard,
            }
        }
        print(students)


studentOne = Student(
    int(input("Student Roll no: ")),
    input("Student Name: "),
    int(input("Student Age: ")),
    input("Student Grade: "),
    input("Student Gender: "),
)
studentOne.getStuPosition()

studentTwo = Student(
    int(input("Student Roll no: ")),
    input("Student Name: "),
    int(input("Student Age: ")),
    input("Student Grade: "),
    input("Student Gender: "),
)
studentTwo.getStuPosition()

# IMPORTANT note: a class have only one constructor function which means one __init__() method, if we use multiple then it will take last __init__() method only, the remaining methods are useless!


# Encapsulation meaning we create restrictions for a particular attribute/methods, which means we prevent data from modify accidently
# in python we dont use private, public, protected keyword instead we use __new_speed - start with double underscore means its a private attribute, then what is private attribute - which means only accessible under the class not accessible by outside of a class, i.e see below


# here we see how to use private attributes in py
class Speed:
    def __init__(self):
        self.speed = 80
        self.__new_speed = 100  # its a private attribute, only accessible inside a class, not able to accessible by outside of a class
        print(self.__new_speed, "I AM A PRIVATE ATTRIBUTE")

    def get_speed(self):
        return self.__new_speed  # here we use getter to get the private attribute

    def set_speed(self, new_speed):
        self.__new_speed = new_speed
        # here we use setters to set new values to the attributes


speed = Speed()
print(speed.speed)
# print(speed.__new_speed) # 'Speed' object has no attribute '__new_speed' - we got this error, here thats why we use getters and setters to get the values
print(speed.get_speed())
speed.set_speed(120)
print(speed.get_speed())

# lets have a look on conventions in py
""" _x = 10 - which means _ single underscore denotes its, partially private, it accessible outside of the class also """
""" __x = 10 - which means __ double underscore denotes its, completely private, it can't be accessible outside of the class """
""" def __private_func() - its a private method, it can't be accessible outside of the class """


# here we see how to use private methods in py
class Test:
    def __init__(self):
        print("hit CONSTRUCTOR")
        self.a = "A"  # its a public attribute
        self._b = "B"  # its partially private attribute
        self.__c = "C"  # its a private attribute

    def public_method(self):  # its a public method
        print("{0},{1},{2}".format(self.a, self._b, self.__c))
        self.__private_method()

    def __private_method(self):
        # its a private method, it only accessible inside of a class
        print("I AM PRIVATE METHOD")


testIt = Test()
testIt.public_method()
# testIt.__private_method() # we got this error - 'Test' object has no attribute '__private_method'.
# then how will access the private method, we use getters


""" POP - Procedural Oriented Programming - which means writing code from scratch for every functions"""
""" OOPS - Object Oriented Programming System - which means we re-use code for every functions and its features"""

""" Inheritance - whenever we require same/similar functionality for a class's attributes/methods to another class we inherit a derived class from a base class with all the base class features means base class's attributes/methods
real example: GrandFather -> Father -> Me -> MySon = your father acquire some attributes/behaviours from your grandparents, then you  acquire some attributes/methods from your parents, then yourson acquire some behaviours from you
in programming terms see below 
GrandFather - BaseClass/SuperClass
Father - DerivedClass/SubClass/ChildClass (Derived From GrandFather)
Me - DerivedClass/SubClass/ChildClass (Derived From Father - means Father is a base class of Me)
MySon - DerivedClass/SubClass/ChildClass (Derived From Me - means Me is a base class of MySon)
"""


class Polygon:
    __width = None
    __height = None

    # here we didn't use __init__(self) method - bcoz we didn't create any instance of a base class Polygon,
    # whenever we use __private attributes, __private methods in a class, then we need to use getter and setters to get the attributes/methods accessible outside of a class

    def set_value(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


class Square(Polygon):
    # here Sqaure a derived/child class is derived from base/super class Polygon, here Square class able to use attributes/methods features of a Polygon class
    def areaOfSquare(self):
        return self.get_width() * self.get_height()


areaOfSq = (
    Square()
)  # here I create a instance which means object for a class, that derived class Square is derived from base class Polygon
areaOfSq.set_value(10, 40)
print(areaOfSq.areaOfSquare())


class Triangle(Polygon):
    def areaOfTriangle(self):
        return (self.get_width() * self.get_height()) * 1 / 2


areaOfTr = Triangle()
areaOfTr.set_value(30, 40)
print(areaOfTr.areaOfTriangle())

""" Module - what is Module -> is just a python file - we able to import and export python files/modules """
