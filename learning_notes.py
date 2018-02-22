import random
import sys
import os

print("Hello World")        # outputs Hello World

# comment

"""
multi line
comment
"""

name = "Jesse"
print(name)     # outputs the string name (which is Jesse)

# Data types: Numbers, Strings, Lists, Tuples, Dictionaries


#####################################################################
# arithmetic operators: +,-,*,/,%,**,//
#####################################################################

print("5 + 2 = ", 5 + 2)      # addition, outputs 7
print("5 - 2 = ", 5 - 2)      # subtraction, outputs 3
print("5 * 2 = ", 5 * 2)      # multiplication, outputs 10
print("5 / 2 = ", 5 / 2)      # division, outputs 2.5
print("5 % 2 = ", 5 % 2)      # modulus, outputs 1
print("5 ** 2 = ", 5 ** 2)    # exponent, outputs 25
print("5 // 2 = ", 5 // 2)    # floor division, outputs 2


#####################################################################
# Strings
#####################################################################

quote = "\"This is a quote\""
print(quote)                # outputs "This is a quote"
multi_line_string = """This is a 
multi line string"""
print(multi_line_string)    # outputs This is a multi line string (on multiple lines)
new_string = quote + multi_line_string
print(new_string)           # outputs "This is a quote"This is a multi line string (on multiple lines)

print("%s %s this is a string %s" % (quote, "and also", new_string))
# outputs "This is a quote" Made up on the spot string "This is a quote"This is a multi line string (on multiple lines)

print("I don't like ", end="")
print("newlines")           # outputs I don't like newlines (all onto one line)

print("\n" * 5)                 # outputs five blank newlines

print(r"\"This \t will be an example \n string\"")  # the r creates a raw string which will ignore all escape characters
print("\"This \t will be \\an example \n string\"")   # \t will create a tab, "\" is an escape character

phrase = "Hello World"
print(phrase[0:5])          # outputs just Hello

spam = phrase.upper()
print(spam)             # outputs HELLO WORLD

spam = phrase.lower()
print(spam)             # outputs hello world

spam = phrase.capitalize()
print(spam)             # outputs Hello world

"Hello" in "Hello World"            # this is True
"cats" not in "cats and dogs"       # this is False



#####################################################################
# lists
#####################################################################

grocery_list = ["Juice", "Bananas", "Apples", "Beer",
                "Pizza", "Milk"]

print(grocery_list)        # outputs the list of grocery_list
print("The first item on my list is", grocery_list[0])
# outputs the string then juice (index 0 is the 1st item, 1 is the 2nd, etc...

grocery_list[0] = "Soda"
print("The first item on my list is", grocery_list[0])
# outputs the string then Soda (index 0 is the 1st item, 1 is the 2nd, etc...

print(grocery_list)        # outputs the list of grocery_list (it's been updated)
print(grocery_list[1:3])   # outputs the list start at index 1 to 3 (not including 3)

other_events = ["Wash Car", "Pick up Kids", "Cash Check"]

to_do_lists = [grocery_list, other_events]   # adds the grocery list and other events list together as a list of lists
print(to_do_lists)
print(to_do_lists[1][2])    # outputs cash check(first pulls from list in index 1 then item at index 2

grocery_list.append("Carrots")
print(grocery_list)         # outputs the updated grocery list with carrots at the end

grocery_list.insert(1, "Pickle")
print(grocery_list)         # outputs the updated grocery list with Pickle at index 1 (2nd item)

grocery_list.remove("Pickle")
print(grocery_list)         # outputs the updated grocery list with Pickle removed

grocery_list.sort()
print(grocery_list)         # outputs the sorted list (alphabetized

grocery_list.reverse()
print(grocery_list)         # outputs the list with the items order reversed

del grocery_list[4]
print(grocery_list)         # outputs the list with item at index 4 removed (no more Beer :(  )

to_do_list_2 = other_events + grocery_list
print(to_do_list_2)         # outputs both lists as new single list

print(len(to_do_list_2))    # outputs the number of items in the list (9)

print(max(to_do_list_2))    # outputs what ever item is highest (in this case alphabetically, Wash car)
print(min(to_do_list_2))    # outputs what ever item is lowest (in this case alphabetically, Apples)

print(to_do_list_2)         # outputs the to_do_list_2
del to_do_list_2[0:2]       # deletes items from index 0 to index 2 not including 2
print(to_do_list_2)         # outputs the updated list with the deleted items


#####################################################################
# Tuples (these are like lists but cannot be changed
#####################################################################

pi_tuples = (3, 1, 4, 1, 5, 9)
print(pi_tuples)            # outputs the tuple (3, 1, 4, 1, 5, 9)

new_list = list(pi_tuples)
print(new_list)             # outputs the list [3, 1, 4, 1, 5, 9]

new_tuple = tuple(new_list)
print(new_tuple)            # outputs the tuple (3, 1, 4, 1, 5, 9)

print(len(pi_tuples))       # outputs the length of the tuple
print(min(pi_tuples))       # outputs the lowest number of the tuple
print(max(pi_tuples))       # outputs the highest number of the tuple
print(pi_tuples[4])         # outputs the item at index 4 which is 5


#####################################################################
# Dictionaries
#####################################################################

super_heroes = {"Batman" : "Bruce Wayne",
                "Iron Man" : "Tony Stark",
                "Hulk" : "Bruce Banner",
                "Super Man" : "Clark Kent",
                "Spider-man" : "Peter Parker"}

print(super_heroes["Batman"])          # outputs Bruce Wayne
print(super_heroes.get("Iron Man"))    # outputs Tony Stark
del super_heroes["Hulk"]               # deletes "Hulk" : "Bruce Banner" from the dictionary

super_heroes["Spider-man"] = "Deter Dark"        # changes "Spider-man" : "Peter Parker" to "Spider-man" : "Deter  Dark"

print(len(super_heroes))        # outputs 4 (since Hulk was deleted)

print(super_heroes.keys())      # outputs dict_keys(['Batman', 'Iron Man', 'Super Man', 'Spider-man'])
print(super_heroes.values())    # outputs dict_values(['Bruce Wayne', 'Tony Stark', 'Clark Kent', 'Deter Dark'])


#####################################################################
# Conditionals
#####################################################################

age = 21

if age > 16:
    print("You are old enough to drive")
else :
    print("You are not old enough to drive")

if age >= 21 :
    print("You are old enough to drive a semi")
elif age >= 16 :
    print("You are old enough to drive a car")
else:
    print("You are not old enough to drive")

if (age >= 1) and (age <= 18):                    # once condition is met, it will not check the rest of the conditions
    print("You get to have a birthday party")
elif (age == 21) or (age >= 65):
    print("You get a birthday party")
elif not (age == 30):
    print("You do not get a party")
else :
    print("You get a party yay")


#####################################################################
# Loops
#####################################################################





