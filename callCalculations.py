import calCulations

# we able to import modules from different ways here some -> see below
# type-1 -> from calculation import calCulations - this means path of directory = /calculation/calCulations.py
# type-2 -> import calculation.calCulations - this also address the same directory = /calculation/calCulations.py

# if we use type-2 -> calculation.calCulations.add(1, 1) - then we need address like that

# type-3 -> using as keyword -> aliases -> import calculation.calCulations as myMaths -> myMaths.add(1, 1)
# type-4 -> from calculation import calCulations as myMath

# whenever we importing modules in python, a __pycache__ folder created automatically by python interpreter, It contains the compiled bytecode of the module, which can be used to speed up subsequent imports of the same module.

add = calCulations.add(1, 1)
print(add)
sub = calCulations.sub(5, 2)
print(sub)
multiply = calCulations.multiply(2, 2)
print(multiply)
division = calCulations.division(10, 2)
print(division)
