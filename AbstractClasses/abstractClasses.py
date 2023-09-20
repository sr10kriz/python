from abc import (
    ABC,
    abstractmethod,
)  # from abc module we extract ABC class and a abstractmethod, we may able to get the all classes and methods that are available in abc module using - from abc import * , why we extract neccessary classes, methods from abc module is to use our memory location well -> (especially in big projects)

""" Abstract Classes - its all about privacy of Parent Class, which means If we create Abstract Classes, it doesn't allow us to create instance for the parent class, and Methods & Attributes of Parent Class should be implemented in Sub-Classes,

Two things to remember for Creating Abstract Classes
1 - I dont want allow any users to create object for my parent class 
2 - All the methods & Attributes that are present in Parent Class should be implemented in Child Class"""

# def funtion_name():
# pass # here this pass keyword - its a empty function its gonna return nothing


class SuperClass(
    ABC
):  # here we inherited the SuperClass Class from ABC Base Class - now its a Abstract Class, we not able to create instance for the SuperClass Class
    # def __init__(self):
    #     print("PARENT INIT") # here the constructor is not needed, we dont create a instance for the class

    @abstractmethod  # here functionOne its a abstract method now,
    def functionOne(self):
        # print("FUNCTION ONE")
        pass

    @abstractmethod  # here functionTwo its a abstract method now,
    def functionTwo(self):
        # print("FUNCTION TWO")
        pass


# OVERALL - we create a Abstract Class with Abstract Methods
# from now on - functionOne(), functionTwo"() - its a mandatory, if someone creating a child class from this parent class(abstract class) they have define functionOne(), functionTwo() inside their class its mandatory

# if not - we got the TypeError, whatever the abstract methods we created in our Abstract Class, we need define all the abstract methods in our inherited class, if one method is missing we got the TypeError which contains which method is can't instantiate

""" File "D:\py\basics\AbstractClasses\abstractClasses.py", line 40, in <module>
    super = SuperClass()
            ^^^^^^^^^^^^
TypeError: Can't instantiate abstract class SuperClass with abstract methods functionOne, functionTwo """


class ChildClass(SuperClass):
    def __init__(self, side):
        print("CHILD INIT")
        self.__side = side

    def functionOne(self):
        return print(self.__side * self.__side)

    def functionTwo(self):
        return print(4 * self.__side)


# super = SuperClass() # we need to remove this one, coz we made this one as Abstract, so we are not gonna create instance for this, if we do create a instance for the Abstract Class, we got the TypeError
""" File "D:\py\basics\AbstractClasses\abstractClasses.py", line 54, in <module>
    SuperClass()
TypeError: Can't instantiate abstract class SuperClass with abstract methods functionOne, functionTwo """

child = ChildClass(10)
child.functionOne()  # now the functionOne() implemented from a ChildClass
child.functionTwo()  # now the functionTwo() implemented from a ChildClass

# childCl = ChildClass()
# in this eg, we create a Parent Class and a Child Class (and the Child Class is inherited from Parent class), so if we use childCl.functionOne() or childCl.functionTwo() - we create a instance for ChildClass, and call use methods that are available in Parent Class, but the instance, it directly use the methods from Parent Class becoz we inherited the ChildClass from ParentClass,
# here we want to implement those methods that are available in Parent Class should be implemented in subclasses which means Child Class, thats were Abstract Classes are come into play

# to use Abstract Classes we need to
# import abc module
# And a Class ABC from abc module - here ABC is our Abstract Base Class
# And a Method abstractmethod from abc module - this method used as a decorator
# finally we need inherit SuperClass from Absract Class
