# This is a comment

# to declare a variable we use = 
# snake case
my_number = 5

# console.log equivalent is print()
# print(my_number)

# data_types this is a falsey value, like NaN, null
this_variable_has_none = None

# print(this_variable_has_none)

# True and False are capitalized
this_is_true = True
this_is_false = False

# print(this_is_false)

# Numbers - int, float, complex (3 +2i)
example_int = 4
example_float = 15.3
example_complex = 3+2j

quotient = example_float / example_int
# this is a float
# print(quotient)

# using // operator this return the floored quotient
quotient_floored = example_float // example_int
# print(quotient_floored)
# print(type(quotient_floored))

# exponents
product = 5 ** 2 # 5 * 5
# print(product)
huge_number = 2 ** 999 
# print(huge_number)

# Strings
string_of_words = "aces of spades. seems useful."

# list of split strings
# print(string_of_words.split(' '))
# the index of first occurence
# print(string_of_words.index('c'))

# .upper() .lower() .capitalize()
# print(string_of_words.capitalize())
# print(string_of_words)

# print(string_of_words.upper())

# in keyword will check substrings, we can also use this in lists
true_or_not = "eggs" in "green eggs and ham"
# print(true_or_not)

# in javascript arr.length() gives us a length
# in python len(arr)



# print(len(string_of_words))
my_string = "this is so cool"

# my_string(start:end:step)
# print(my_string[0:-1:2])
# print(my_string[0:4])
# print(my_string[::4])

# print(my_string[4: ])
# print(my_string[-1])

# print(my_string[::-1])

# SPRINT 2
# Lists Dictionairies String Interpolation and Control Flow

our_array = [1, 2, 3, 4, 5]

# python getting length
print(len(our_array))


# how would i get the last element
print(our_array[-1])

# does not mutate so we do a reassignment
our_array = our_array[::-1]

# mutates our array, most methods will mutate our list
our_array.sort()

# python instead of push we have append(), instead of pop we have pop
our_array.append(6)

# remove the last element from the list, and save it this new variable
my_last_item = our_array.pop()
our_array.pop()
# lets insert 100 as the second item in the list
our_array.insert(1, 100)
print(our_array)


# DICTIONARIES

# make your keys strings
cat = {
    'name': 'Hamlet',
    'breed': 'Tabby',
    'fav_food': None
}
print(cat)

# python is not going to support dot notation for grabbing properties from a dict.
print(cat['breed'], cat['fav_food'])

# bracket notation for accessing and adding new properties
cat['age'] = 25

print(cat)
# use string interpolation to get two properties
# the f out front says this is a "formatted string"
# interpolate the values in the {}
my_cat_message = f'The name is {cat.get("name")} and the breed is {cat["breed"]}.'

# formatting inline after the string tell it the arguments to pass in
using_template = "The name is {} and the breed is {}".format(cat['name'], cat['breed'])

# reassignment
# using_template = using_template.format(cat['name'], cat['breed'])
print(using_template)

# Control flow if: elif: else:


are_vip = True
active = "busy"
# we use the : and then indentation for this block of code to run
if (active == "full" and not are_vip):
    print('hey we are full up')
elif (active == 'busy' and not are_vip):
    print('please wait for 10 minutes')
else:
    print('Come on in, you are vip')

# if (thisIsTrue) {
#     console.log('woo')
# } else if (isThisTrue){

# } else {

# }

# Sprint 3 LOOPS FUNCTIONS
veggies = ['carrots', 'kale', 'spinach']
# for in loop

for veggie in veggies:
    print(f"I love {veggie}")

# with the iterator using key word enumerate
for index, veggie in enumerate(veggies):
    print(f"{index}. I love {veggie}")

cool_info = {
  'name': 'Sophia',
  'error_catcher': True,
  'code_monster': 'yep that is me'
}

# for in loop get access to the keys of the dictionary
for key in cool_info:
    print(key, cool_info[key])

# to loop through the avlues of a dictionary
for value in cool_info.values():
    print(value)

for i in range(10):
    print(i)

# range( start, stop, step)
for i in range(5, 10, 2):
    print(i)
print('-------------')
print(i)

# let i = 5;
# for (let i = 0; i < 10; i++) {
#   // some statements
# }
# // Here i is 5

i = 5
for i in range(10):
    print(i)
    i=5 #the final reassignment

print(i)

# functions
# function (), const coolArrow = ()=> {}

# def
def gather_input(default_name = 'Bobby'):
    your_name = default_name
    friend = input("Enter your friends name: ")
    print(f"Hello {friend}. {your_name} says hi!")

gather_input('James')
gather_input()

def veggie_love_list_function(veggie):
  return (f"I love {veggie}")
veggie_love_list = map(veggie_love_list_function, veggies)
print(list(veggie_love_list))






