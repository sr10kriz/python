""" 1 - Varibles & Memory Management in py """

print('Hi we are gonna rock!')
a = 1000
b = 2000 
c = a + b

id(c) 
""" here id() returns a unique id for the varaible, which means its returned the memory location of a variable, each variable has a unique memory location unless its has a same value
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

""" List """
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

""" Tuples """
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

""" if i need to print my_range directly, inthis case its just a range, i need get the value from range - how ? i need to convert this range to list, see below """
my_list_range = list(my_range)
print(my_list_range)
print(type(my_list_range))

""" u can also directly convert range to a list """
my_list_range_dir = list(range(10,25,2))
print(my_list_range_dir)

""" 4 - Sets """
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

""" Mapping / Dictionaries """
""" Dictianaries are similar to objects, in other words u can imagine a real dictonary, key value pairs like Why:why are you late? - this is key value pair - why is term key, then the value """
""" syntax - {10:'Messi',7:'Ronaldo'} """
my_map = {10: 'Messi', 7: 'Ronaldo', 8: 'Iniesta'}
print(my_map)
print(type(my_map))

""" we can able to access values inside of dictinaries like below, same what we are do in objects """
print(my_map[10])


# syntaxes
# None
# x = 1, y = 0.5, complex(param1,param2), bool represents 1 - true, 0 - false
# z = 'messi', [1,2,3,4], (1,2,3,4), range(start,stop,step)
# a = {1,2,3,4}
# able to convert set to a tuple or list and also vice versa, able to convert tuple or list to set

""" 3 - Literals and Identifiers """
m = 90 
""" here m is a Identifie, 90 is a Literal - in nnormal terms m is variable we defined, 90 is a value we assigned to that variable and = is a operator assigning literals to identifiers """
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
        6 - Boolean ->

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

