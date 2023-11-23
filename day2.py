num1 = 10 
num2 = -33
num3 = 30 
num4 = float(num1)
print(type(num1))
print(type(num4))
#floats they have a decimal!
num5 = 5.0
print(type(num5))

#math operations
print('/n Math Operators')

#add +
print(num1 + num3 )

#subtract -

print(num3 - num1)
print(30 -10)

#multiply *
print(num1*num3)

#divide 
print(type(num3/num1))

# floor division // always results in a integer!
print(27 // 5)
print(25 // 5)

#modulo % always results in a integer!
print(27 % 5)
print(25 % 5)

#side-bar: = vs ==
# = this is assigning a value (Make this equal to)
# == this is checking for equality (is this qual to????)checking for type and value equality
# will always result in a boolean
#Also comparison operator:
# == equal 
# != Not equal
# <
# >
# <= 
# >= 

# This is an important one!
# even or odd?

print(26 % 2 == 0)
print(27 % 2 != 0)

print(27 % 2 == 1)


# exponents **

print(5 ** 5)

#side-bar variable naming conventions:
# int ('33')
# int = 56 
# int ('987435')
# dont use pre defined character set (functions, classes etc)

#Strings
#indexed, iterable, immuteable 
# It's a bunch of characters inside of quotes...

st1 = "this is a string"
st2 = "This is tool "
St3 = "So's this"

# Double or single quotes are fine just make sure that the other kind surrounds their use inside or use an escape character
st4 = "so\"s this "
print(type(st1))
print(st1[2])
print("string[0]")


#concatenation a fancy way of saying adding strings together
print(st1 + "." + st2)
f_string = f"this is an f-string that also has this from python --> .{num2 + 100}"
print(f_string)
f_name = "steve"
print("hello({f_name.title())!")


#methos vs functions 
# methods and function are the same thing


r_exp.remove (1)
my_list.append
