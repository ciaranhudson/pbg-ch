# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 10:10:08 2020
B8IT102 Programming Essentials (B8IT102_1920_TME2)
CA 1 - 10 Function Calculator

Revised as CA03 in subsequent module

- Original functions replaced with lambda code
- code written to receive lists from user
- but could not get lists received from user working with my code

- more work is required so that the calculator can use lists and call the generator

@author: chudson

Ciarán Hudson
10379554

"""


from functools import reduce


# def add(first, second):
#     return first + second

## lambda test
add = lambda x,y : x+y

# ## using reducer to add. this code is not working as part of the calculator my code cannot handle lists
# adder = reduce(lambda x, y : x+y, [25 , 52, 73])
# print (list(adder))


# def sub(first, second):
#     return first - second

sub = lambda x,y : x-y

# def mult(first, second):
#     return first * second

mult = lambda x,y : x*y


# def div(first, second):
#     return first / second

div = lambda x,y : x/y


# def square_root(first):
#     return first**0.5

square_root = lambda x : x**0.5


# def square(first):
#     return first**2

square = lambda x : x**2



# def inv(first):
#     return 1 / first

inv = lambda x : 1/x


def kilometres(x):
    return(round((float(x)/0.621371),2))


# ## I can't get this code working with lists the user inputs rather than a defined list
# kilometres = lambda x : round((float(x)/0.621371),2)

# distances = (5, 10)

# k = map(kilometres, distances)

# print(list(k))




# ## code to get the user to enter a list 
# ## I had planned to use this input with my code because i don't know how to handle lists    
# ## based on https://pynative.com/python-accept-list-input-from-user/
# numberList = []
# n = int(input("How many numbers in your list : "))
# for i in range(0, n):
#     print("Enter number ", i +1, ":")
#     item = int(input())
#     numberList.append(item)
# print("Thanks, your list is ", numberList)
    

# ## list comprehension with filter pythagorean triplets
# n= 30
# triplet_comp = [(x,y,z) for x in range (1,n) for y in range (x,n) for z in range (y,n) if x**2 + y**2 == z**2]


# # generator comprehension because brackets chnaged to ()
# triplet_comp = ((x,y,z) for x in range (1,n) for y in range (x,n) for z in range (y,n) if x**2 + y**2 == z**2)
# for triplet in triplet_comp:
#     print(triplet)



    


## practice
# def gen_pythagorean_triplets(max_value):
#     for x in range(1,max_value):
#         for y in range(x, max_value):
#             for z in range(y, max_value):
#                 if x**2 + y** 2 == z**2:
#                     yield (x,y,z)
# triplets = gen_pythagorean_triplets(500)
# for triplet in triplets:
#     print(triplet)

                    



def operator_menu():
    print('1 or add or + to do addition')
    print('2 or sub or - to do subtraction')
    print('3 or mult or * to multiply')
    print('4 or div or / to divide')
    print('5 or sqrt to perform square root')
    print('6 or square to square')
    print('7 or inverse to return the 1/x')
    print('8 or km to convert from miles to kilometres')
    # print('9 or pyth to generate pythagorean triplets')  ## code will be added in once probs resolved re lists and calling object

def process_operation():
    first_number = float(input('Enter number?'))
    operator_menu()
    func = input('Enter operator?')
    if func not in ['sqrt', 'square', '5', '6', '7', 'inverse','8', 'km']: ## I would add , '9', 'pyth' if I could get my calcuator to handle them
        second_number = float(input('Enter another number?'))
    if func in ['1', '+', 'add']:
        print(add(first_number, second_number))
    if func in ['2', '-', 'sub']:
        print(sub(first_number, second_number))
    if func in ['3', '*', 'mult']:
        print(mult(first_number, second_number))
    if func in ['4', '/', 'div']:
        print(div(first_number, second_number))
    if func in ['5', 'sqrt']:
        print(square_root(first_number))
    if func in ['6', 'square']:
        print(square(first_number))
    if func in ['7', 'inverse']:
        print(inv(first_number))
        
        
    ## I have not figured out how to populate the calculator with a list 
    ## so cannot input list to mapper K above rather than defined list D
    ## so calculator can only convert 1 inut at a time        
    if func in ['8', 'km']:
        print(round(kilometres(first_number),2))
    ## I'm not abnle to call the object using this code so cannot use my generator    
    # if func in ['9', 'pyth']:
    #     print(triplet_comp(first_number))



def process():
    go_again = ''
    while go_again != 'n':
        process_operation()
        go_again = input('Would you like to continue (y/n)?')

process()