""" 1 - Varibles & Memory Management in py """

print('Hi we are gonna rock!')
a = 1000
b = 2000 
c = a + b

id(c) 
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
j = complex(4,5>12)
""" it accepts two argument, 1st is real value, 2nd is imaginary value. Note: if you pass string as a 1st argument then the 2nd argument cant be accepted, it provides this error => TypeError: complex() can't take second arg if first is a string, it accepts int, float, string as well as boolean as an argument """
print(j)
print(type(j))

k = 10 > 1
""" in python we say boolean as bool -> true represents 1, false represents 0 """
print(k)
print(type(k))


""" 3 - Sequences & their types """

""" string """
my_name = 'Messi'
print(my_name)
print(type(my_name))

""" List - ordered, mutable, allow duplicates"""
""" List are arrays in python, but it stores different types of datatypes, any values i.e ['str', bool, 1, 0.5], Note: list can be modified """
my_list = ['Messi', 35, 5.5, "Argentenian", 10]
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
""" Tuples are very similar to List, the only difference is the paranthesis, we use tuple like this ('Messi',35,5.5,'Argentenian',10,'GOAT') , important Note: tuples are immutable while lists are mutable, tuples cant be modified after once created in python """
my_tuple = ('Pedri',21,5.8,'Maestro',8)
print(my_tuple)
print(type(my_tuple))

""" this is indexes of an tuple in python, similar to list """
print(my_tuple[3])
""" Note: tuples are immutable, cant able to modify once after the creation """

""" Range """
""" range is often used as loops, if you want to print some range this to this kind of stuff """
""" syntax of range range(start,stop,step) - it accepts three parameters - 1st and 3rd params are optional, 2nd is mandatory - default value of 1st param is 0, default of 3rd param is 1 """
my_range = range(1,10,3)
print(my_range)
print(type(my_range))

my_test_range = tuple(range(10))
print(my_test_range)

""" if i need to print my_range directly, inthis case its just a range, i need get the value from range - how ? i need to convert this range to list, see below """
my_list_range = list(my_range)
print(my_list_range)
print(type(my_list_range))

""" u can also directly convert range to a list """
my_list_range_dir = list(range(10,25,2))
print(my_list_range_dir)

""" 4 - Sets - unordered, immutable, doesn't allow duplicates """
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

con_set_tup = tuple({1, 5, 10 , 15, 20, 300, 30})
print(con_set_tup)
print(type(con_set_tup))

""" Mapping / Dictionaries - ordered, mutable, doesn't allow duplicates """
""" Dictianaries are similar to objects, in other words u can imagine a real dictonary, key value pairs like Why:why are you late? - this is key value pair - why is term key, then the value and inportant note dictionaries can't allow duplicates """
""" syntax - {10:'Messi',7:'Ronaldo'} """
my_map = {10: 'Messi', 7: 'Ronaldo', 8: 'Iniesta'}
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
short_string = 'messi'
long_string = 'messi is the greatest\
 of all\
 time\
 simply mentioned as\
 GOAT'
print(long_string)

""" backslash - \ is to mentioned that the string is not end, its continued i.e 'messi\'s left foot' -  """

long_string_n = 'messi \n Greatest of all Time \n GOAT'
print(long_string_n)

""" \n - to take a new line """

""" real time example see below """
path = "c:\downlaods\app\nodejs"
print(path)
""" c:\downlaodspp
odejs """
""" i get the above result - coz \n in escape characters is to take a new line thats y we got the result - to prevent this behaviour we use double backslash \\ - this \\ is to convert this to \ which means - \\ = \ """

path_n = 'c:\downloads\app\\nodejs'
print(path_n)
""" now i got the expected one - c:\downloadspp\nodejs """

""" there are some escape characters out there """
# \' , \" , \r , \t , \n , \v , \h

""" 7 - Input & Output Statements """
""" Output Statements """
print(16/4)
num1 = num2 = 100
print(num1*num2,'is the multiplication of x and y')
# the above we got 10000 is the multiplication of x and y - but what we expect is 10000 is the multiplication of 100 and 100 - how we do that in python - need to use format()
print('{0} is the multiplication of {1} and {2}'.format(num1*num2,num1,num2))
""" now wwe got the xpected result - 10000 is the multiplication of 100 and 100 """
""" there are so many formating options out there """
""" format() method accepts - any datatype as a argument """
print('{string1} is simply mentioned as {string2} - {string3}'.format(string1 = 'Messi',string2 = 'Greatest of all Time',string3 = 'GOAT'))

""" Input Statements """
my_first_q = input('Provide your name :')
my_second_q = int(input('provide your age :'))
# the input() function returns a string - we need convert to integer for age - this conversion we called as type casting i.e see above line. type casting - type casting means convert one datatype to another datatype
print('Hi {0}, you age is {1}'.format(my_first_q,my_second_q))

messi_bio = {'name':input('Provide your name: '),'age':int(input('Provide your age: ')),'callsign':input('Provide me your callsign: ')}
print('Hi {0}, your age is {1}, your callsign is {2}'.format(messi_bio['name'],messi_bio['age'],messi_bio['callsign']))

""" 8 Built-in functions & modules need to check in documentation """

""" 9 if...elif...else """
jerseyNum = 10
if jerseyNum == 10:
    print('Lionel\'s')
else:
    print('Somenone\'s')
    
print('the above if...else got closed')

print('the below if...elif...else got started')

colorPat = "White"
if colorPat == "Red":
    print(f'Your preferred color is {colorPat}')
elif colorPat == "White":
    print(f'Your preferred color is {colorPat}')
else:
    print('kindly chose color patterns')

isYourAge = int(input('Provide your age: '))
haveVoterId = input('Do you VoterId say YES or NO: ')
if isYourAge >=18 and isYourAge <=25:
    if haveVoterId == 'yes':
        print('Approved, and Eligible for Voting')
    else:
        print('Hold, Get details to provide VoterId')
elif isYourAge >=25 and isYourAge <=60:
    if haveVoterId == 'yes':
        print('Mid Citizens Eligible Candidate')
    else:
        print('Mid Citizens')
elif isYourAge >= 60:
    if haveVoterId == 'yes':
        print('Super Senior Eligible Citizens')
    else:
        print('Super Senior Citizens')
elif isYourAge <=18:
    print('Your are not eligible for Voting')
else:
    print('Retake assesment')
    
    
""" Loops """

# While 
startP = 10000
while startP < 10010:
    print('loop of --->',startP)
    startP = startP + 1
else:
    print('End')
# in python a else block also possible, whether the condition fails then fall under else block

# in keyword in python - to check some values are available in some variable i.e below
A = {1,2,3,4,5}
print(5 in A)

# For - we can list, tuples, range, dictionary in for loops - any iterable object
for i in A:
    print(i) 
    
forDict = {10:'Messi',8:'Iniesta'}
# if you only want keys from dictionary then,
for x in forDict:
    print(x) # by default the for loops takes only keys from dictionary - also get forDict.keys() method to get the keys from dictionary
    
# if you only want values from dictionary then,
for x in forDict.values():
    print(x)

# if you only want both keys and values from dictionary then,
for x,y in forDict.items():
    print(x ," ",y)
else:
    print('End')