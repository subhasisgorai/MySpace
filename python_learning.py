''' Harnessing Python: An overly simplified introduction to Python '''

''' For this course we would be using python 2.7 '''
''' Please note python 3 has been completely rewritten 
    and different from that of python 2 '''

''' @author: subhasis '''

''' Some demo on python print '''
''' all three results in same output '''

print 'Hello World'
print 'Hello', 'World'
print 'Hello',
print 'world'

''' some formatting '''
print 'My Name is %s, and age is %d' % ('Subhasis', 31)

''' same effect '''
print "My name is {}, and age is {}".format('Subhasis', 31)

''' can be indexed as well, but optional from python 2.7 '''
print "My name is {0}, and age is {2}".format('Subhasis', 31, 30)

''' little bit of formatting '''
print "My name is {:15}, and age is {:10}".format('Subhasis', 31)

''' Now name is center-justified, age left-justified '''
print "My name is {:^15}, and age is {:<10} years".format('Subhasis', 31)   

''' then how to do right justification? '''
print '{:>10}, {}'.format('Hello', 'World')

''' if we multiply 5 by 10, answer would be 50, what would happen if string is multiplied? Error??'''
print 'Subhasis ' * 5

''' string center example '''
city = 'Bangalore'
print city.center(40)

''' now with filler character '''
print city.center(40, '-')

''' cool, right, let's move on to input '''
''' taking user input via input function '''
age = input('What\'s your present age: ')
print age

''' what about raw_input '''
age = raw_input('What\'s is your present age: ')
print age

''' no difference right? let's see further ''' 

import fileinput  # will be using fileinput module
import json
from math import pi
import os
import pickle
import pprint
from random import shuffle
import re
import sys
import timeit
import types


radius = input('Enter radius of the circle: ')
print 'Area would be {}'.format(pi * radius ** 2)

''' perfect now let's try the same with raw_input '''
radius_raw = raw_input('Enter radius of the circle: ')
# print 'Area would be {}'.format(pi * radius_raw ** 2)
''' above expression results in an error since python 2 raw_input always returns string '''
radius = float(radius_raw)
result = "radius: {}\narea: {:.3f}".format(radius, pi * radius ** 2)
print result.upper()

test = input("Enter what you like: ")  # let's enter 5 + 2
print test

''' Did you notice the output? input() additionally tries to eval() the input as python expression '''

''' TIP: 
    1) multiple python command in same line should be separated by ';'
    2) single python command in multiple lines, should be connected by '\'
'''
print 'India'.center \
    (40, 'x')


''' Now we will see python datatypes, we will discuss common types we use in our day to day purpose
    four distinct numeric datatypes could be found
        1. int - plain integers, 32(can be 64?) bits of precision (sys.maxint tells max plain integer for current platform)
        2. long - unlimited precision
        3. float - floating point numbers, system specific floating point information could be found by running 'sys.float_info' [more here: http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html]
        4. complex - complex numbers with real and imaginary part, where each part is a floating point numbers, we will not discuss more about this.
    
    We will talk about unicode before we jump into strings. Few things to note,
        1. Computer deals with bytes, everything is byte in computer world irrespective of whether you save or transmit something over wire.
        2. Since bytes are meaningless, we assign convention to make value out of those bytes, the first such convention was ASCII. Now using 1 byte you can store 
            256 symbols which definitely are not adequate. People started using multiple character code (multiple set of mappings) but even that was not enough, even in a single language, number of characters 
            can certainly go beyond 256. World needs more. Single byte was not enough, then people landed up on 2 bytes based character coding, but even 65536 symbols were not enough.
        3. Here comes Unicode to save us, Unicode is nothing but a giant catalog that maps symbols (characters) to integers (code points). 1.1M code points, only 110K assigned so far. Then there is something
            called encodings, i.e. UTF-16, UTF-32, UCS-2, UCS-4, UTF-8, that represents unicode code points to bytes somehow and that is bidirectional. Among these encoding scheme UTF-8 is most popular, it's 
            variable length encoding scheme (different code point may need different number of bytes) where ASCII characters are still one byte. So far no unicode code point needs more than 4 bytes. (as of unicode 6.1)
            
    Now coming back to python, there are two distinct string datatypes, 
        1. str: stores sequence of bytes, 
        2. unicode: a sequence of unicode code points.
    
'''
my_string = 'Hello World' 
print type(my_string)  # should print out <type 'str'>
my_unicode = u'Hi \u2119\u01b4\u2602\u210c\xf8\u1f24'  # has unicode code points represented by \u followed by 4 digit hex string, 
                                                    # for more than 4 digit hex string you should use \U                                                    
print type(my_unicode)  # this should print out <type 'unicode'>
print len(my_unicode)  # should print out '9', there 9 unicode code points 

''' so remember there are bytes, there are code points, you should know what you are dealing with and keep them straight.
    Now there are two methods, .encode() & .decode() - encode converts unicode code points to bytes and decode does the vice-versa. 
'''

my_utf8 = my_unicode.encode('utf-8')
print len(my_utf8)  # has length of 19 bytes represented by \x hexadecimal string
print my_utf8

# >>> my_unicode.encode('ascii')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 3-8: ordinal not in range(128)
# Error because ascii codec does not support this

''' Now let's talk about implicit conversion, python 2 proves to be very handy here 
    If we are mixing unicode and byte string together, python tries to decode the byte string using sys default encoding
'''
mixed = u'Hello' + 'World'
print mixed  # print HelloWorld which is equivalent to u'Hello' + ('World'.decode('ascii')), where ascii is default encoding

print sys.getdefaultencoding()  # in case you don't know what's the system default encoding

''' There exists other string literals, like
    1. Raw String literal - When an 'r' or 'R' prefix is present, a character following a backslash is included in the string without 
        change, and all backslashes are left in the string. For example, the string literal r"\n" consists of two characters: 
        a backslash and a lowercase 'n'. String quotes can be escaped with a backslash, but the backslash remains in the string; 
        for example, r"\"" is a valid string literal consisting of two characters: a backslash and a double quote; 
        r"\" is not a valid string literal (even a raw string cannot end in an odd number of backslashes). 
        Specifically, a raw string cannot end in a single backslash (since the backslash would escape the following quote character). 
        Note also that a single backslash followed by a newline is interpreted as those two characters as part of the string, 
        not as a line continuation. [from python documentation]
    2. Docstring literal - a convenient notation to attach documentation with the python modules. 
    
    Raw string literal (prefixed by r) gets automatically encoded with 'string-escape', let's see an example.
'''
raw_str = r'Hello\nWorld'
print raw_str  # probably this is not the output you were expecting .. right? Now let's try to print it again
print raw_str.decode('string-escape')  # yay, now looks good, so what exactly had happened?

normal_str = 'Hello\nWorld'
en_str = normal_str.encode('string-escape')
print raw_str == en_str  # probably this explains what exactly had happened

''' Let's look at the sequence types of Python,
    1. strings, 2. unicode string this we have already discussed
    3. list - you may think this of as array, can be constructed with square brackets separating items with commas
    4. tuple - readonly array, separated with commas, with or without parentheses. Empty tuple must have enclosing parentheses,
                single item tuple must have a trailing comma.
    5. set - unordered collection of distinct hashable objects. Popularly used for duplicate removal, mathematical set operations.
    6. dict - python mapping type, key-value pair, keys should be hashable. It's also an unordered collection.
    
    Sequence types supports indexing, slicing & iteration.

'''

iterable = range(10)
print iterable
print iterable[:10:2]
test_list = iterable[::-1]
for i in test_list:
    print i,
print '\n'
lists = [[]] * 3
print lists  # basically it does a shallow copy now change the first item, it will have an effect on others
lists[0].append(5)
print lists

''' sort and sorted '''

items = [1, -2, 13, 11, 17, 21, 7, 8, 9, 8, 0]
shuffle(items)  # in-place shuffle
sorted_items = sorted(items)  # returns the items sorted
items.sort()  # sorts the items, but in-place sort
items.sort(reverse=True)  # Reverse in-place sort

# you can create list of different lists as well
lists = [[] for i in range(3)]
lists[0].append(3)
lists[1].append(4)
lists[2].append(5)
print lists 

test_tuple = 1, 2, 3, 4, 5  # creates a tuple, optionally you may enclose this with parentheses
print test_tuple

test_dict = dict()
test_dict[1] = 'one'
test_dict[2.0] = 'two'
''' Now we can use 1.0 to find out the value 'one', but it's not wise to use floating point numbers as key since computer stores 
    floating point numbers as approximation
'''
print test_dict[1.0]

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], (1, 2, 3)))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

print a == b == c == d == e

for i in a.items():
    print i


''' Dictionary has a has_key(key) method to check for existence of a key. This should be checked before running an update.
    dict has also got a setdefault(k, d) method which in case of D[k] returns the same result as it does for D.get(k,d). [More about get() later]. Basically, it sets D[k]=d if k not in D.
    While we try to access a value using its key D[k] it throws KeyError in case the key 'k' is not present in the dictionary, though we can gracefully handle this by using D.get(k, d), where it returns d 
    when k is not present in the dictionary. Let's see some examples.
        
'''
info = dict()  # same as {}
info['name'] = 'Subhasis'  # updating the key
info.setdefault('name', 'N/A')  # setting the default for key 'name'
print info['name']  # trying to access the key 'name'
del info['name']  # deleting the key 'name' now

# Now if we try to access key 'name' from the dict 'info' it will throw KeyError
# print info['name']
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# KeyError: 'name'

# But as mentioned earlier, we can gracefully handle this using get() by supplying a default value 
print info.get('name', 'N/A')

''' Other than this, there are boolean with True & False and also None type [None]
    Following are the Falsy types: None, False, Zero [0, 0L, 0.0, 0j], empty sequence i.e. [], (), '', empty mapping i.e. {}
    or any user defined class that returns zero or False for __len__() or __nonzero__().
    All other values are considered to be true.
'''

''' now let's look few utilities 
    printing number with different base
'''
number = 15
print bin(number)
print hex(number)
print oct(number)

''' now let's try the reverse '''
print int('1111', 2)
print int('f', 16)
print int('17', 8)

''' finding out ascii code of a english character '''
print ord('A')
# now reverse
print chr(65)

''' Now, briefly we will skim through the operators available with python. Nothing much changes here from that of the other
    conventional languages.
    1. Arithmatic operators - + - / * and // floor division
    2. Relational operators  == != > >= < <= <> (<> kindof deprecated)
    3. Logical operators and or not
    4. Bitwise operator &(and) |(or) ^(xor) ~(not) >>(right shft) <<(left shift)
    
    Now let's try few common bit manipulation techniques. 
''' 

print 0b111 >> 1
print 0b111 << 1
print bin(0b0110 + 0b0110)  # this is as simple as multiplying by 2, which is nothing but left shift by 1

test = 0b11101001
# 'get' bit operation, say 4th bit
i = 4
print 0 if test & (1 << i) == 0 else 1

# 'set' bit operation
print bin(test | (1 << i))

# 'clear' bit operation
i = 3
print bin(test & ~(1 << i))

# 'clear' all the bits from the most significant bit through i (inclusive)
test = 0b11111111
i = 4
mask = (1 << i) - 1
print bin(test & mask)

# 'clear' all the bits from i through 0 (inclusive)
mask = ~((1 << (i + 1)) - 1)
print bin(test & mask)

# update but operation [mix of clear bit followed by set bit]
toBeUpdatedWith = 0
print bin((~(1 << i) & test) | (toBeUpdatedWith << i))

''' Preamble: Twos-Complement
    Few words about two's complement and how numbers are represented internally in a computer. Without this, our discussion on bitwise operations would be incomplete.
    - Well, so, what does complement mean? 
    - Mathematically, it's technique used to subtract a number from other using only addition of positive numbers.
    - Cool, that's quite interesting but how would you do so?   
    - Well, there is something called 1's complement which is nothing but simply inverting the bits i.e. 0 to 1 & 1 to 0. This was not so useful, let's not discuss more. Then comes 2's complement. Which is nothing 
        but first computing 1's complement and then adding 1, that is, first get the binary representation of the number, flip the bits and then finally add one.
    - Why we are discussing all these?
    - Because 2's complement is the way every computer chooses to represent integers.
    - Why the hell is so difficult?
    - hold on, it is not as difficult as it seems to be. The technique I mentioned above is 2's complement representation of negative integers. While for zero & positive numbers the 2's complement is same as that of their
        binary representation. For example, if we were using 4-bit computers, 5 would be represented as 0101 (same as binary representation of decimal 5), 0 would be represented as 0000. While -5 would be stored as 1011.
        1011 is equivalent of [inverting bits of bin(5) + 1]. Now why such complicated stuff to store the negative numbers. Because, computers are little dumb, and they can't understand (-) minus sign before a number as 
        human do. In our 4-bit fictitious computer example if the most significant bit(hereafter we will call MSB) is 0 it signifies a positive number or zero, but if it's 1 it denotes a negative number. Even in the above 
        example for +5 (0101) and 0(0000) the MSB is zero, for -5 (1011) the most significant digit is 1. Right? So far so good.
      
      Now, coming to why such complications? How do we know this is mathematically correct. We will try to explain in simplified manner rather than getting into much complication.
      Do you recollect, how we used to compute 100 - 9 in our childhood days? For the Least Significant Bit (hereafter LSB), 0 - 9 we used to borrow from second LSB to simplify stuff, with that 0 - 9 becomes 10 - 9
        which we can compute easily result is 1 for the LSB. Now since we have borrowed, we have to additionally subtract 1 for second LSB place in the result. Again, for second LSB, 0 - 1 is difficult, but let's repeat
        the trick we did just sometime back, borrow from the subsequent LSB. In this way the result becomes 91.
      Now earlier example was with decimal numbers, but we can perform the same trick even with our binary representation. Let's explore another way. Subtraction we can think as addition of negative representation of 
        the number being subtracted, i.e. 9 - 5 can also be thought as 9 + (-5). Isn't it? Now how to compute -5? -5 can be computed as (0 - 5), that means 9 - 5 => 9 + (-5) => 9 + (0 - 5).
        So, basically, when you try to find negative of a number, you take the number and subtract it from zero.
        Now, with our same primitive 4-bit computer, we want to do the 0 - 5:
                
               (1)  (1)   (1)  (1)
               (1)x (1)x  (1)x (1)x
                0    0     0    0   => 0 (Decimal)
                0    1     0    1x  => 5 (Decimal)
              (-1)x (-1)x (-1)x   
               ---------------------
               1     0     1    1
        
      We may choose to go on further but since we are working with a very primitive 4 bit computer, bits beyond 4th would anyway be discarded. Given this fact, would there be any difference if we subtract 0101 from 
        10000(a 1 bit followed by 4 zero bits) rather than 0000. Practically nothing. If we do that the result would be same as that of earlier.
                
           1   0    0    0    0
               0    1    0    1
          ----------------------                 
               1    0    1    1
    
      Now 10000 could be represented as 1111 + 1. So the above, subtraction equation could be rewritten as follows,
      
                              1
            +  1    1    1    1
            -  0    1    0    1
          ----------------------                 
                
      In binary, when we subtract a number from a sequence of 1 bits, basically we get all the bits flip for the number being subtracted, i.e. 1111 - 0101 = 1010.
      So, effectively, the subtract operation of a number from 0 (sequence of 0 bits) is equivalent to flipping all the bits of the number and then adding 1. And this is what we do while finding out 2's complement of
      a number. I think now we know why all such complications. It's all because computers are not as intelligent as human beings!
      
      So few important things to remember:
          1) All the bitwise operators operated on numbers, but they treat them as sequence of bits rather than a single number.
          2) Computers represent integer in twos-complement binary form. Two's complement binary is very same as the classical binary representation for positives and zeros but little different for negative numbers.
          3) As per convention, for zero and positive numbers most significant bit is always zero, while for negative numbers it would be 1. 
          
          So in our fictitious, primitive 4 bit computer, 
              a. if we encounter 0101, applying rule #3 above, we know definitely it's going to be a positive number. Now applying Rule #2, the number the machine has tried would 
                  be (101)base2 i.e. 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 5.
              b. On the contrary, if we see 1011, by applying rule #3, we know the number is negative. Now to find out the actual number being stored, apply the same logic you had applied to find out 2's complement 
                  for a negative number, i.e with 011 first flip the bits, that is 100, then add 1 which results in 101. binary 101 means decimal 5. So the number was -5 represented in 2's complement form. 
    
'''

''' Few more operators
    Membership test operator - in, not in
    Comparison operator - cmp [python 2] boils down to __cmp__(self, other), that returns negative if self less than other,
        zero if self equals other, positive if self greater than other
    Identity operator - is, is not 
'''
test = [1 , 2, 3, 4, 5]
print 5 in test  # True
print 10 not in test  # True 
print cmp(5, 6)  # result -1

# Now let's see usage of 'continue' and 'pass' keyword

for i in range(5):
    if i % 2 == 0:
        continue  # we could have used 'pass' also
    else:
        print i 

i = True
if i is True:
    pass  # but we can't use continue here. you will get - SyntaxError: 'continue' not properly in loop
else:
    print 'Hello'

''' So basically pass can serve as placeholder for any dummy code in Python
    There are usual if-else, for, while constructs like any other languages but there is no 'for (i=0; i<10; i++)' construct.
    You must have already noticed there is no braces for code block, all happens through indentation. 
    There could be 'else' block for while, let's see that in action.
'''    
i = 1
while i <= 5:
    print i
    i += 1
else:
    print 'reached the limit'
# if 'break' encountered inside while loop, both the rest of the while loop and else block does not get executed

name, age, location = 'Subhasis', 32, 'Bangalore, India'
# This is called parallel assignment

# Now we will see how zip can be used to create tuple; how tuple could be transformed to a dict and vice-versa.
keys = ['name', 'age', 'location']
values = ['Subhasis', 32, 'Bangalore, India']
# zip supports parallel iteration, zipping keys, values will create a tuple
tuples = zip(keys, values)
# tuples, the variable, is a list of tuples, now we will create a dict out of it
info = dict(tuples)
# now how to get back the list of tuples again from the dict
tuples_back = info.items()

# before moving on to the next topic let's see how to form a set, which is unordered collection of hashable objects
test_list = [1, 2, 3, 4, 5, 4, 2, 7, 9, 0, ]
test_set = set(test_list)
print test_set

# now let's try to create a set out of a tuple.
test_tuple = (1, 2, 2, 3, 4, 3, 3, 5, 5, 4, 1)
test_set = set(test_tuple)
# Are you expecting an error since tuple is unmodifiable? But it gets executed without any issue, because it creates a set out of the tuple rather try removing duplicates from tuple.
# Two objects are different, even the following says that.
print id(test_set) == id(test_tuple)

''' We will look at List, Dictionary and Set comprehension. These are very important features supported in Python.
'''
# Let's say we are given with a list of heterogeneous types, the job is to iterate, take the numeric types and find out the their squares.  

sample_list = [1, 2, 11, 7, 'Subhasis', 'a', '11', 14, 17]

# The simplest solution would be
result = []
for item in sample_list:
    if type(item) == types.IntType:
        result.append(item ** 2)
print 'Original list: {}, list after processing: {}'.format(sample_list, result)

# Too much of code for such a small thing, let's make it little simpler & crispy
# let's try to filter based on type. More about lambda coming soon, as of now think them as a shorthand notation to declare pure functions. 
filter(lambda item: type(item) == types.IntType, sample_list)

# Cool, now let's try find out the square of each of the items
# We will be using map() which transforms every item in a sequence. Simple .. isn't it?
map(lambda item: item ** 2, filter(lambda item: type(item) == types.IntType, sample_list))

# But I feel still this is lil complex, particularly in such cases list comprehension proves to be very handy.
[item ** 2 for item in sample_list if type(item) == types.IntType]

# List Comprehension provides us with an efficient way to iterate over individual list items and apply certain operation if the optional predicate expression is satisfied.
# In the above example, we are iterating 'sample_list', individual items will be stored in 'item', calculating square on individual item is the operation & check for IntType is the optional predicate.
# Important thing to note here is the result is also a sequence. Whenever, the requirement is to get sequence then only we should go with comprehension.
# Let's take one more problem, Given a list of Strings, change the items to upper case.
sample_list = ['abc', 'def', 'test', 'cat', 'mat', 'python']
result_list = [item.upper() for item in sample_list]
print 'Original list: {}, list after processing: {}'.format(sample_list, result_list)

# Let's move on to dictionary & set comprehension, very similar to list comprehension, only difference is intermediate sequence would be of type dict & set respectively.
# dictionary & set comprehension are comparatively new and were introduced in python 2.7. Let's see a few examples.
# We have already seen 'zip' in action.

keys = ['name', 'age', 'location']
values = ['Subhasis', 32, 'Bangalore, India']
info = dict(zip(keys, values))
print info
# Output would be {'age': 32, 'name': 'Subhasis', 'location': 'Bangalore, India'}
# We will try to simulate this using dictionary comprehension.

info = None
info = {key : value for (key, value) in zip(keys, values)}
# yay! the result is same. Note curly braces, the main difference from list comprehension.

# We have seen how to create a Set. We can pass a list as set's constructor argument. i.e.
names = ['Tom', 'Harry', 'John', 'Fred', 'Harry']
names = set(names)
print names
# Output would be set(['Fred', 'Harry', 'John', 'Tom'])
# We can also simulate the same thing in following way
names = {'Tom', 'Harry', 'John', 'Fred', 'Harry'}  # use curly braces instead of square braces

# We can also achieve the same using Set comprehension
names = ['Tom', 'Harry', 'John', 'Fred', 'Harry']
names = {item for item in names}

# Before we move on to our next topic, let's see how Python supports Compound Comprehension
# Let's take an example,
result = []
for i in range(1, 6):
    for j in range(1, 6):
        if j % 2 == 0:  # if j is even
            result.append('{} x {} = {}'.format(i, j, i * j))
print result

# now using compound list comprehension
result = ['{} x {} = {}'.format(i, j, i * j) for i in range(1, 6) for j in range(1, 6)  if j % 2 == 0 ]
print result

# So while writing compound comprehension, always remember: 
# [transformation for outer-loop [optional predicate] for inner-loop [optional predicate]]

# we will try to solve a problem using compound comprehension. We will transpose a 2-D matrix
sample_matrix = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]


# print the matrix before transposing [more about pretty print later]
pprint.pprint(sample_matrix, width=32)

# now let's try to transpose the given matrix
transposed_matrix = [[row[col] for row in sample_matrix] for col in range(3)]

# here we pretty print the transposed matrix
pprint.pprint(transposed_matrix, width=32)


''' Functional Programming & Python
    Before starting let's define what is functional programming, as Wikipedia says, 
    "In computer science, Functional Programming is a programming paradigm, a style of building structure and elements of computer programs, that
    treats computation as the evaluation of mathematical functions and avoids state and mutable data. Functional programming emphasizes functions that
    produce results that depend only on their inputs and not on the program state - pure mathematical functions. It's a declarative programming paradigm,
    which means programming is done with expressions. In functional code, the output value of a function depends only on the arguments that are input to the
    function, so calling a function f twice with the same value of an argument x will produce the same result f(x) for both the times"
'''
'''    
    When writing functional style programs, you will often need lil functions that act as predicates or combine the elements in some way, 
    if there is a Python built-in or a module function that's suitable you don't need to define a new function at all
'''
lines = [' This is Subhasis ', ' He is from West Bengal ', ' He is working as a Software Engineer in Bangalore ']
print(lines)
stripped_lines = [line.strip() for line in lines]
print(stripped_lines)

files = ['james.txt', 'abc.txt', 'julie.txt', 'mikey.txt', 'sarah.txt', 'xyz.txt']
existing_files = filter(os.path.exists, files)  # 'os.path.exists' test whether the file exists, returns False for broken symbolic links

''' Now if the function does not exist then we need to write it. One way to write is using lambda statement. lambda takes a number
    of parameter and an expression combining these parameters, and creates small function that returns the value of the expression 
'''
lambda_even_finder = lambda x: [i for i in x if i % 2 == 0]
lambda_even_finder([i for i in range(21)])
# should output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

lambda_adder = lambda x, y: x + y
print(lambda_adder(5, 6))

# an alternative could be using the regular def statement to define a full fledged function
def adder(x, y):
    return x + y

# lambdas are very handy in certain cases, i.e. while sorting list of objects or dictionaries. Let's see an example.
students = [{'name':'Test1', 'roll_number': 5, 'marks' : 90}, {'name':'Test2', 'roll_number': 1, 'marks' : 85},
            {'name':'Test3', 'roll_number': 3, 'marks' : 92}, {'name':'Test4', 'roll_number': 4, 'marks' : 60},
            {'name':'Test5', 'roll_number': 2, 'marks' : 82}]

# Now try to sort the Students by ascending order of their roll number
sorted_student_roll_asc = sorted(students, cmp=lambda x, y : cmp(x['roll_number'], y['roll_number']))

# Now try to sort the Students by descending order of their marks
sorted_student_marks_desc = sorted(students, cmp=lambda x, y : cmp(y['marks'], x['marks']))

# Here we will see one very helpful module called PrettyPrint. This pretty prints nested arrays.

pp = pprint.PrettyPrinter()
pp.pprint(sorted_student_marks_desc)

''' Which one is preferable? lambda is good but quite restricted, the result has to be computable as a single expression, which means 
    you can't have complicated multi-way if... elif... else ... comparisons or try .. except statements. If you try to do too much in a 
    lambda statement, you'll end up with an overly complicated expression that's hard to read.
    We will finish our functional programming discussion with map-reduce which is a very popular programming paradigm.
    map - applies some sort of transformation on individual items
    reduce - tries to apply some sort of aggregate function on the entire sequence.
    We will not go into further details since map-reduce itself is a huge topic and out of the scope of present discussion.
    Let's try to solve a small problem - we are given with a sequence of numbers, we have to square it and find out the minimum.
      
'''
test_list = [-2, -2.25, -0.000005, 5, 7, 5.25, 9, 10]

intermediate_list = map(lambda x: pow(x, 2), test_list)
final_result = reduce(lambda x, y: x if x < y else y, intermediate_list)
print final_result

''' A brief introduction to Regular Expression (regex)
    We all know Regular Expressions, in fact we all use regex in our day to day life.
    I will touch few important aspects on how to use regex in Python.
    Well, let's start. Normally regex matches only once, not necessarily words bounded by word boundary i.e. it matches substring.
    Python 're' module provides regex support.
'''
match = re.search('ample', 'A sample sentence with sample words')  # re.search(pattern, text), match object stores the search result
# matched? let's check whether match is None or not. If not null(None) then pattern was present in the text.
if match:
    print 'pattern \'{}\' present'.format(match.group())  # prints search result, matched string
    print 'start index {}'.format(match.start())  # start index of first match
    print 'end index {}'.format(match.end())  # end index exclusive
    print 'start index & end index {}'.format(match.span())
    print match.groups()  # tuple of groups, though not present in this example.
else:
    print 'match not found!'
    
# Well let's try to put this in a function, such that we can invoke it again and again. That would be helpful in subsequent discussion.
def find_match(pattern, text):
    match = re.search(pattern, text)
    if match:
        print 'pattern \'{}\' present, at starting index {}'.format(match.group(), match.start())
    else:
        print 'match not found'
# coool, now we are ready to explore further        
    
''' We briefly skim through meta-characters & basic patterns
        . - matches any characters except line break
        \w - matches any word-character (alpha-numeric & underscore)
        \W - matched non-word character
        \s - matches any whitespace character (spaces, tabs)
        \S - matches non white space character
        \t - matches tab
        \n - matches new line
        \r - matches return
        \d - matches decimal numbers 0-9
    besides these, other characters are mostly ordinary characters.
    
    Next, we will see anchors
        \b - matches word boundary
        \B - matches non-word boundary
        ^ - matches beginning of a string
        $ - matches end of a string
    '\' is used to cease the specialness of a special character. For example, \$ does not match end of string, rather it matches literal $ string
    
    Quantifiers:
        ? - 0 or 1 occurrence of preceeding token
        * - 0 or more occurrence(s) of preceeding token
        + - 1 or more occurrence(s) of preceeding token 
         Interesting thing is all these quantifiers are greedy. What does that mean? Let's see. 
'''
find_match('a+', 'Subhaaaasis')
# What would be the expected output? a? or aaaa? let's see
# Output: pattern 'aaaa' present, at starting index 4 - but even only one 'a' also matches the pattern!? '+' matches 1 or more occurrences. Then why 'aaaa'? Because the matching is 
#    greedy (leftmost occurrence & largest substring), it tries to match as much as possible. 

''' continuing from earlier section:
        ? switches off the greedy mode. *? & +? are lazy match counterpart of * & + respectively. i.e. "find_match('a+?', 'Subhaaaasis')" will output "pattern 'a' present, at starting index 4" 
        {x,y} - specifies minimum(x) & maximum(y) numbers of character set to be matched. i.e. "find_match('o{2}', 'Google')" will have an output "pattern 'oo' present, at starting index 1"
    
    Character sets with square bracket []
        matches any single character present in the character set specified, i.e. [\w'-] matches any word character, single quote, or hyphen. Here, - signifies range, ^ means not i.e. [^f-m] matches 
        any single character that is not in the range f-m. We can specify multiple ranges as well, i.e. [A-Za-z0-9] matches single character/digit either in A-Z or a-z or 0-9.
        
    Group Extraction:
        Let's say given the following sentence: Subhasis's email id is subhasig@yahoo-inc.com and cell number: +91-988-6549-365. He stays in Bangalore.
        Now we need to extract email-id, cell number and location. Can we solve this based on the discussion we had so far? Well, I think we can form individual patterns to match, but extracting all these
        information in single execution could be little difficult.
        'Group' in regex allows to cherry-pick parts of the matching text. For group extraction we use parenthesis (). Basically we need to write a pattern as per the information we are looking for, additionally
        we should put parenthesized groups for the parts we are interested in.
        We have to enhance find_match method a bit to get the groups info back, let's name it find_match_with_groups(pattern, text)
        
'''
def find_match_with_groups(pattern, text):
    match = re.search(pattern, text)
    if match:
        return match.groups()
    return None

test_str = 'Subhasis\'s email id is subhasig@yahoo-inc.com and cell number: +91-988-6549-365. He stays in Bangalore.'
groups = find_match_with_groups(r'([\w.-]+@[\w.-]+).+(\+\d{1,2}-\d{3}-\d{4}-\d{3}).*stays\sin\s(\w+)', test_str)

# Here first group tries to match Email Id, second one tries to match Cell Number & third one looks for location.
# The returned groups variable would be a tuple of these three extracted information. We preferred to take the pattern as raw string that takes care of backslashes without the need of escaping.
    
''' findall() is another very powerful function of python re module, unlike the search() method it matches all the matches. Parenthesis grouping could also be used with findall().
    While searching or compiling, additionally we can also pass flags like IGNORECASE, DOTALL, MULTILINE, VERBOSE etc.
    As we saw, Regex patterns are written in a highly specialized language that gets compiled into bytecodes and then executed by Regex Engine. If we plan to use a particular pattern again and again it's always
    better to compile it first and then use rather than compiling on the fly. Underlying engine may apply certain optimization, caching etc which may lead to performance boost (though might not be very significant).
    In fact, it's possible to tune the regex pattern in a certain way such that it produces more efficient bytecode that runs faster.
'''
test_str = 'cat on mat'
pattern = re.compile(r'(\wat)')
match = re.search(pattern, test_str)
print type(match)  # <type '_sre.SRE_Match'>
print 'First match [{}]'.format(match.group())  # First match [cat]

matches = re.findall(pattern, test_str)
print type(matches)  # <type 'list'>
print matches  # ['cat', 'mat']

''' We will try to measure the benefit of compiling pattern for a repetitive search, even if it could be miniscule. Let's see.
    We will be using timeit module for this empirical measurement. Before doing the experimentation let's have a quick review of the important timeit APIs.
        1) timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000)
            create a timer instance with given statement to test, setup code, timer function & number of executions
        2) timeit.repeat(stmt='pass', setup='pass', timer=<default times>, repeat=3, number=1000000)
            very similar to the last method except the experimentions to be repeated for specified number of times.
        Setup statement would be executed only once, and then it will return the time it takes to execute the main statement for the spcified number of time in seconds as float. For repeat, it would be repeated 
        multiple number of times as specified and finally list of results would be returned.
        By default, GC would be temporarily turned off during the experimentation. This could be advantageous since the independent timiings would be more comparable. But disadvantage is that GC could be an important
        factor of the performance of the statement being measured. Though GC could be programmatically turned on. Anyways, let's do the experimentation now.
'''
timeit.repeat(stmt='import re;test_str = "cat on mat"; match = re.findall(r"(\wat)", test_str)', number=1000000, repeat=3)  # without pattern compilation
# on my Mac, I got the following result: [3.028794050216675, 3.0810179710388184, 3.0683610439300537]
# now, we will be trying with pattern precompilation as a setup step
timeit.repeat(stmt='test_str = "cat on mat";matches = re.findall(pattern, test_str)', setup='import re; pattern = re.compile(r"(\wat)")', number=1000000, repeat=3)  
# And, I got the following result: [2.2225019931793213, 2.140566825866699, 2.146172046661377] # some improvement over the earlier one

''' We will see (+) & (-)ve lookahead & lookbehind
    While matching a pattern regex engine can be also look ahead or look behind as well. Let's take an example, given a sample string +91-3244-275597 which is an Indian landline number. We have to find out the STD code.
    How we can extract that? Let's see, basically we have to extract the digits, preceded by +91- and followed by '-' and couple of digits.
    Going by the above logic let's try to form the following pattern: r'(?<=\+91-)(\d+)(?=-\d+), here (?<=pattern1) asserts positive look behind, (?=pattern2) assert positive lookahead.  
'''    
sample_str = '+91-3244-275597'
match = re.search(r'(?<=\+91-)(\d+)(?=-\d+)', sample_str)
match.group()  # should show 3244 which is the STD code

# let's try out one more example. We will try to extract host name i.e. yahoo, gmail from a given email id
sample_str = 'subhasig@yahoo-inc.com'
match = re.search(r'(?<=@)(.+)(?=\.com)', sample_str)  # should display 'yahoo-inc'

''' (?<!pattern1) asserts negative lookbehind, (?!pattern2) asserts negative lookahead '''

''' Remembering pattern that matched already: Backreferencing in action 
    How we can check whether a given 5 letter word is a palindrome using regex? 
    Regex allows us to remember whatever pattern already matched, and we can refer them in future using index. Let's see an example. 
'''
test_str = 'Id:12345, Name: Subhasis'
# Let's say we want to format the Id by putting it inside square bracket i.e. 'Id:[12345], Name: Subhasis'
# How we will proceed?
# Step 1: let's write a pattern that matches the id in the example string
pattern = re.compile(r'(\d+)')
# Step 2: we can use regex sub to do the substitution, pretty easy .. isn't it? But how to refer to the matchstring while specifying the replacement? As I was telling, we can refer the first matched string by \1,
#            second matched string by \2, and so on .. here we are interested in the first and only matched numeric Id.
formatted_str = re.sub(pattern, r'[\1]', test_str)
print formatted_str
# Output: 'Id:[12345], Name: Subhasis'

''' One more stuff we keep on doing in our day to day life - in-place find/replace in a file. Assuming we have a file named 'sample.txt' in the current 
    directory. We will try to replace 'test' with 'TEST' in-place. [very similar to: sed -i 's/TEST/test/g' sample.txt]
'''
for line in fileinput.input('sample.txt', inplace=True):
    print line.replace('test', 'TEST'),  # note the ',' at the end, this is to suppress unwanted newlines, try out without the ',' :-)
fileinput.close()

''' File Handling
'''
data = open('sample.txt')
print data.readline()  # read the first line
print data.readline()  # now read the next line
data.seek(0)  # return to the beginning of the file
data.seek(25)  # seek to offset 25
print data.read(4)  # read 4 bytes of data
data.close()  # close the file

''' open returns a file handler, open can take an optional second argument which specifies the mode in which the file would be opened.
    'r' means file only to be read, 'w' for only writing, 'a' is for appending, 'r+' opens file for read/write. Default mode is 'r'.
    Let's append some text to a sample file called test.txt.
'''
fh = open('test.txt', 'a')
fh.write('let\'s put some more sample text')
fh.close()

# Now let's verify what we just wrote
fh = open('test.txt')
for line in fh:
    print line
fh.close()

''' Things might go wrong - handling exceptional situations
    The try-except combination, try executes problematic code which might result in some errors, except executes recovery code in case of any error 
'''
start = 10.0
step = 5
for i in range(10):
    try:
        'start: {}, step: {}'.format(start, step)
        step -= 1
        print start / step
    except:
        print 'error occurred, recovering'
        pass

''' try-catch-finally: reading file in a safe manner
'''
try:    
    fh = open('test.txt')
    for line in fh:  # reading file, line by line
        print line 
except IOError as err:  # in case of IOError, recovery code can be placed here 
    print 'File Read IO Error {}'.format(str(err))
finally:  # this part gets executed irrespective of whether error happens or not
    if 'fh' in locals():
        fh.close()

# The above code can be simplified using with, finally to close the file handle is also automatically taken care of

try:
    with open('test.txt') as fh:
        for line in fh:
            print line
except IOError as err:
    print 'File read IO Error {}'.format(str(err))

''' Preserving Objects & Data: Serialization - Pickling with Python
    Whatever objects, data we construct in runtime go off as soon as Python interpreter stops. If we need to retain the object hierarchy or data across multiple
    executions we need to store them somehow on disk. This process is called Serialization, and reverse process is known as Deserialization. Through Serialization 
    process object hierarchy is converted into byte stream which we can persist on disk. Python ships with standard library for this purpose, it is called Pickle. 
    Pickling is the process of Serializing & Unpickling is process Desrializing. Once we pickle our data or object hierarchy to a file, it is persistent and ready 
    to be read or consumed by the same or even other program at a later point of time.     
'''
students_data = [{'name':'Test1', 'roll_number': 5, 'marks' : 90}, {'name':'Test2', 'roll_number': 1, 'marks' : 85},
            {'name':'Test3', 'roll_number': 3, 'marks' : 92}, {'name':'Test4', 'roll_number': 4, 'marks' : 60},
            {'name':'Test5', 'roll_number': 2, 'marks' : 82}]  # our old student data, which we will save it on disk

try:
    with open('pickle_test', 'wb') as pickle_file:  # w for write and b for binary mode
        pickle.dump(students_data, pickle_file)
except IOError as err:
    print 'File IO Error {}'.format(str(err))
    
# now the data is persisted and safe until your hard disc crashes!
try:
    with open('pickle_test', 'rb') as pickle_file:
        students_dup_data = pickle.load(pickle_file)
except IOError as err:
    print 'File IO Error {}'.format(str(err))

pp.pprint(students_dup_data)  # yay! we got back the same data

'''
    Instead of persisting the data in binary format using Pickle, we may try out serializing it in JSON format.
    JSON is text-based, readable, portable, interoperable, compact and becoming standard of late. We can make use of json module for this. Let's see an example. 
'''
serialized_str = json.dumps(students_data)

# now we can store this serialized string into a json file
try:
    with open('students_data.json', 'w') as json_file:
        json_file.write(serialized_str)
except IOError as err:
    print 'File IO Error {}'.format(str(err))

# Now we will try to get our data back
try:
    with open('students_data.json', 'r') as json_file:
        students_file_data = [] 
        for line in json_file:
            students_file_data.append(line)
        retrieved_json_str = ''.join(students_file_data)
        students_dup_data = json.loads(retrieved_json_str)
except IOError as err:
    print 'File IO Error {}'.format(str(err))

pp.pprint(students_dup_data)  # we got our students data back


''' Python Namespaces & Scoping
    Everything in Python is an Object, be it a number, literal, list, function, dictionary or class - everything! So whenever we do some kind of computations we create lot of 
    objects, and every such objects need some names, names are kind of handles to the objects, without name they will be just simply dangling around in the wild. There would be 
    name for variables, name for functions and so on. Scope defines the part of program over which a name holds good. Let's take an example,

        >>> def sample_func():
        ...     test = 'abc'
        ...     print test
        ... 
        >>> sample_func()
        abc
        >>> test
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'test' is not defined
    
    We have defined a function called sample_func, we went ahead and defined a variable named 'test', that points a string literal 'abc'. Later when we executed the function and within
    the function scope tried to access 'test' it was very much accessible. But when tried to access from outside the function it blew off. This is the significance of scoping, variable 
    definition 'test' was valid within the function scope but when tried to access from outside globally the definition does not hold good.
    
    Python has namespaces, which are nothing but containers or simply can be thought of a dictionaries containing the mapping of names and objects. As mentioned earlier, such mappings
    allow us to access objects through their names. The tricky part is multiple such containers or namespaces can coexist independently at a given moment. Moreover, these namespaces are 
    organized hierarchically, we will know about this hierarchy very soon. Now, given a variable name, it could be cumbersome for Python to decide which dictionary to perform the look up,
    or if at all multiple dictionaries need to be queried, then in which order. 'Scoping' defines this, it defines the hierarchy and order. 
    There could be four scopes:
        1) Local - when a function or class method is invoked, it creates its own local namespace within the namespace it (function or method) resides. The container or dictionary mapping 
            contents for local scope can be listed down using locals() i.e. print locals()
        2) Enclosed - for inner function inside another function, Enclosed Scope could be the enclosing function's namespace.
        3) Global - the uppermost level when a script executes. It encloses Local & Enclosed scopes. But it does not spill over into other files, print globals() prints global namespace contents 
        4) Built-in - Special namespace reserved for Python.
    
    The order Python searches different levels of namespaces is defined by LEGB-rule, which directs the order namespace-hierarchy would be searched.
        Local -> Enclosed -> Global -> Built-in
     
'''

test_var = 5
def test_scope1():
    test_var = 10  # defining a new local variable test_var which will shadow the global test_var
    print test_var, '[local scope]' 
test_scope1()
print test_var, '[global scope]'
# Here is the output, which is in accordance with LEGB rule. Note that, global test_var remains unaffected  
# 10 [local scope]
# 5 [global scope]

# But it is also possible to modify global variable from within a function, but we have to be explicit here, inside the function we have to explicitly point to the global variable. Let's see
test_var = 5
def test_scope2():
    global test_var # telling python we are trying to refer the global variable, please note 'global' keyword
    test_var += 1
print test_var, '[global scope]'
test_scope2()
print test_var, '[global scope]'  
# This time global variable was modified from within the local scope inside a function, output was:
# 5 [global scope]
# 6 [global scope]

# While modifying global variable from local scope, we have to explicitly specify that, but when reading python automatically query global scope if variable not present in local scope as per LEGB
test_var = 5
def test_scope3():
    print test_var, '[local scope]'  # as per the LEGB rule, here test_var would be read from global scope since it's not present in local namespace 
test_scope3()
print test_var, '[global scope]'  
# Output:
# 5 [local scope]
# 5 [global scope]
  
# If we are not very careful, while modifying global variable it may fail catastrophically raising UnboundLocalError
test_var = 4
def test_scope4():
    test_var += 1
test_scope4()
# Output
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in test_scope4
# UnboundLocalError: local variable 'test_var' referenced before assignment

# Let's wrap this topic up with an example

test_var = -17
def outer_function():
    def abs(var):
        print 'custom abs() implementation being invoked'
        return var if var > 0 else -1 * var  # amateur implementation, not for serious usage :-)  
    test_var = -12  # will shadow the global 'test_var'
    def inner_function():
        global abs  # linking to global abs i.e. __builtins__'s abs, without this abs(var) from enclosed scope would be available though 
        print test_var  # 'test_var' from Enclosed scope as per LEGB rule
        # test_var += 1 # this will result in UnboundLocalError: local variable referenced before assignment, though we could have pointed to
                        # global 'test_var', but with Python 2, we can't update Enclosed scope 'test_var'. Python3 has introduced 'nonlocal' keyword
                        # apart from 'global', through that we can refer to Enclosed scope's 'test_var' 
        print abs(test_var)  # global __builtins__
    inner_function()
    print test_var  # local version of 'test_var'
    print abs(test_var)  # local version of abs() would be invoked here

outer_function()
print test_var
print abs(test_var)


''' Classy Python: Encapsulating data & behavior in Classes
    As I mentioned even earlier, everything in Python is an object, and classes define the blueprints for objects. The primary purpose of class is to bundle data & relevant behavior together.
    Along with the encapsulation, it helps organizing the code for better maintainability, manageability & readability; it also helps reducing complexity by providing certain degree of abstraction. By bundling 
    logically relevant data & behavior together it makes components more cohesive. Well, all these are generic benefits of Object Oriented Programming (OOP). In general, OOP allows us to think the problem 
    domain in terms of Objects, by doing this it helps reducing the gap between Software Objects & actual Real World entities. This makes Software Design & modeling easy.
    Along with a bunch of built-in classes Python allows users to define their own classes as well.
    
    Let's assume we have got an assignment to develop a new software to manage Retail. What would be the probable use cases, we have to manage inventory, sales of goods, billing, compute taxes etc etc. 
    Definitely we are not going to develop the full-fledged running software here, that would be too much in the present context. We will try to model a few entities and segregate responsibilities to them.
    
'''
''' Let's create a class for items, we will create multiple instances of Item class to prepare Inventory. '''
class Item:
    def __init__(self, item_code, item_desc, item_category, item_price, item_uom, quantity):
        self.item_code = item_code
        self.item_desc = item_desc
        self.item_category = item_category
        self.item_price = item_price
        self.item_uom = item_uom 
        self.quantity = quantity
    
    def __str__(self):
        return 'Item Details: code [{}], description [{}], category [{}], price [{}], unit of measurement [{}], stock [{}]'.format(self.item_code, self.item_desc, self.item_category, self.item_price, self.item_uom, self.quantity)
        
        

# Item type or Category, ideally should be an enum or constants
class ItemType:
    BOOK, FOOD, MEDICINE, COSMETICS, MEDIA, GROCERY, MISC = range(7)

class UnitOfMeasurement:
    UNIT, KG, LITRE, PACK = range(4)

''' Following class is a logical representation of Store Inventory, there should be always only one instance of this class across a particular store.
    We will try to model this class as a Singleton.
'''
class StoreInventory:
    def __init__(self):
        self.items = list()
        self.load_items()
        
    def add(self, item):
        self.items.append(item)        
            
    def load_items(self):
        # loads some sample items and create inventory for the store
        # placeholder for actual implementation, ideally should be loaded from DB or some sort of external store.
        self.add(Item(1, 'Python Book', ItemType.BOOK, 10.50, UnitOfMeasurement.UNIT, 25))
        self.add(Item(1, 'Music CD', ItemType.MEDIA, 15.00, UnitOfMeasurement.UNIT, 20))
        self.add(Item(1, 'Perfume', ItemType.COSMETICS, 50.00, UnitOfMeasurement.UNIT, 10))
        self.add(Item(1, 'Painkiller', ItemType.MEDICINE, 2.00, UnitOfMeasurement.UNIT, 100))
        self.add(Item(1, 'Bread', ItemType.FOOD, 3.00, UnitOfMeasurement.UNIT, 25))
        self.add(Item(1, 'Imported Chocolate', ItemType.FOOD, 11.00, UnitOfMeasurement.PACK, 20))
        self.add(Item(1, 'Sugar', ItemType.FOOD, 3.00, UnitOfMeasurement.KG, 50))
        
    def search_item_by_code(self, item_code):
        for item in self.items:
            if item.item_code == item_code:
                return item
        
    def print_inventory(self):
        print 'Printing Store Inventory:'
        for item in self.items:
            print str(item)
        print '[End]'
        
'''' Let's design a shopping cart now 
'''
class ShoppingCart:
    def __init__(self, inventory):
        self.items = list()
        self.inventory = inventory
    
    def add_to_cart(self, item_code, qty):
        inventory_item = self.inventory.search_item_by_code(item_code)
        if inventory_item and inventory_item.quantity >= qty:
            inventory_item.quantity -= qty
            self.items.append(Item(inventory_item.item_code, inventory_item.item_desc, inventory_item.item_category, inventory_item.item_price, inventory_item.item_uom, qty))
            
    def remove_from_cart(self, item_code, qty):
        for item in self.items:
            if item.item_code == item_code:
                break
        if item and item.quantity >= qty:
            item.quantity -= qty
            inventory_item = self.inventory.search_item_by_code(item_code)
            if inventory_item:
                inventory_item.quantity += qty
    
                 
''' Now we will have a POS Terminal for checking out & billing etc
'''
class POSTerminalEnhanced:
    def check_out(self, cart):
        bill_amount = self.print_bill(cart)
        self.receive_cash(bill_amount)
    
    def print_bill(self, cart):
        running_balance = 0.0
        print '{:<20} {:<15} {:<15} {:<10}'.format('Item', 'Rate', 'Quantity', 'Amount')
        for item in cart.items:
            print '{:<20} {:<15} {:<15} {:<10}'.format(item.item_desc, item.item_price, item.quantity, item.item_price * item.quantity)
            running_balance += item.item_price * item.quantity
        print '{:>52} {:<10}'.format('Total:', running_balance)
        return running_balance
    
    def receive_cash(self, amount):
        print 'Receiving cash for the bill: ${}'.format(amount)
        pass  
            
''' Let's test whatever we have done so far
'''
        
inventory = StoreInventory() # create a store inventory
inventory.load_items()       # initialize with the items

print 'Stock before transaction: '
inventory.print_inventory()  # print inventory details
print '\n\n'

cart = ShoppingCart(inventory) # initialize a shopping cart with the inventory
cart.add_to_cart(1, 2)         # let's do some shopping
cart.add_to_cart(2, 2)

terminal = POSTerminalEnhanced()    # initializing a POS terminal
terminal.check_out(cart)    # now it's time to check out, print the bill and pay.

print 'Stock after transaction: '
inventory.print_inventory() # now printing inventory again to check stock count
print '\n\n'

''' We promised to have the StoreInventory as singleton, but still it's not a singleton you may
    instantiate as many as instances you want. So how to do that?
    Let's first define a function like this.
'''
def singleton(cls):
    singleton_instances = {}                    # creates a dictionary
    def getInstance():                          # inner function, checks for the 'cls' to be present and returns,   
        if cls not in singleton_instances:      # if not creates a new instance, caches it in the dictionary and 
            singleton_instances[cls] = cls()    # returns the instance
        return singleton_instances[cls]
    return getInstance                          # returns the inner function

''' Now the above function will help us creating singleton class. How? Let's see.
    Let's define a class called Counter. The purpose is it will maintain a global counter.
    It would be a singleton, even if we try to create more instances it will return us the 
    same instance. That's quite expected behavior, without which it's impossible to maintain 
    a global counter. 
'''
class Counter:
    def __init__(self):
        self.count = 0      # initializes the instance variable 'count' with zero in the constructor
    def inc(self, step=1):  # method to increment the counter value  
        self.count += step

''' If the Counter is not singleton and we create as many as counter instances we wish, then the
    entire purpose of a global counter is lost. Let's play a cool trick. Let's wrap the Counter class with
    singleton method we had defined earlier.
'''
print type(Counter)     # prints <type 'classobj'>     
Counter = singleton(Counter)
print type(Counter)     # prints <type 'function'>

''' The trick is here the Counter is not referring to a class.
    Rather it's decorated with a function, which when executed in turn returns the cached
    instance of the given class if it has been created once earlier. 
'''
counter1 = Counter()
counter1.inc(2)
counter1.inc()
print counter1.count
counter2 = Counter()
# does the above statement creates a new instance altogether? Definitely not. Try to check the count variable of counter2.
print counter2.count    # it still prints 3
print counter1 == counter2      # print True, so we now sure counter1 and counter2 points to 
                                # same object, and Counter is indeed bahaves as a Singleton
                                
''' Let's revisit the function singleton, it maintains a cache of objects, and returns a reference to an inner function
    which when executed returns cached instance for a given class marked for singleton, if it's a cache miss, it will create an instance, 
    caches it for future use and returns the newly created instance. Nothing unusual .. right? But if you closely observe the function
    definition, you will notice certain nuances. Firstly, when 'cls' & 'singleton_instances' are accessed from the inner function, they are
    not defined locally, naturally as LEGB-rule depicts, enclosing scope would be looked at, and they are found over there.So far so good.
    But, did you notice one thing, if you consider from the perspective of variable lifetime, it's little odd. Why?
    When you execute singleton function, you merely get a reference to the inner getInstance function. While the outer function is being executed
    it's natural that 'cls' & 'singleton_instances' would be live, but when we get a reference to the inner function, outer function execution is already
    over. 'cls' & 'singleton_instances' should not exist anymore when we execute inner getInstance outside from the scope of singleton function, and
    should have failed catastrophically raising an error.
    But that didn't happened practically, we saw this worked just fine. 
    The reason being, inner functions remember their enclosing namespace as it was during the definition rather till the time inner function was returned. 
    This is known as 'Closure' and is very powerful of Python.
    
    We will do little more refinement in our singleton trick before we move on.
    Did you notice this? 
    Counter = singleton(Counter)
    Looks like it's an added overhead, if you forget to assign back the wrapped class to the original reference all hell will break loose. Isn't it?
    Decorators are perfect here to save us. They are nothing but a syntactic sugar.  
    What is a syntactic sugar? Borrowing from Wikipedia: "In computer science, syntactic sugar is syntax within a programming language that is designed to 
    make things easier to read or to express. It makes the language "sweeter" for human use: things can be expressed more clearly, more concisely, or in 
    an alternative style that some may prefer.
    Let's see how we can take leverage from decorators here, how decorators can simplify this.
    Nothing much, you have to just annotate Counter with @singleton while defining, that's all
    i.e. 
    @singleton
    class Counter
    and now we can safely omit the following statement
    Counter = singleton(Counter)
    Python will manage the rest of the things on our behalf.
    

    Now in order to make the StoreInventory class as singleton we need to just annotate it with @singleton
    Example:
    @singleton
    class StoreInventory:
        def __init__(self):
        self.items = list()
        ...
        
    Well, now we have a working Retail solution. We have modeled Item, Inventory, Shopping Cart, POS Terminal etc. Moreover we have designed Store Inventory
    as Singleton. All is well, retailers are pretty happy with our solution.
    Unfortunately our happiness didn't last long. Real world is not so simple! All of a sudden Government mandates all the retailers to enforce Taxes.
    Now while selling items you have to collect tax, the taxation rules are as follows:
        1) There would be basic sales tax applicable on almost all the items at 10% rate.
        2) For imported item there would be an additional import duty of 6%.
        3) Few items are exempted from tax i.e. medicine, books etc.
    Our solution is broken now, it can't be extended to support the taxes out of the box. We will try to build the tax support, we will also try to make it extensible such that if
    tomorrow Government may scrap certain taxes or introduce few more it should continue to work. Even tax rates keep on changing over the time.
    For building our tax model we would be leveraging Decorator Pattern [https://en.wikipedia.org/wiki/Decorator_pattern].
    Fundamentally, Decorator Pattern embellishes an ordinary object by wrapping it with decorators which allows new behaviors to be added dynamically to the original core object.
    Let's see why I feel this pattern is going to be well-suited in our tax scenario.
    Basic Sales Tax could be thought of as the base object, other additional taxes i.e. Import Duty could be designed to be decorators.  
    
'''
        
''' Packing and unpacking arguments in Python
'''       

# example of unpacking
def test_fun(a, b, c, d):
    print a, b, c, d        

my_list = [1, 2, 3, 4]
print test_fun(*my_list)

# example of packing 
def sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print sum(1, 2, 3, 4, 5)

# ** is used for dictionary

def fun_unpack(a, b, c):
    print a, b, c
    
new_dict = {'a': 1, 'b': 2, 'c': 3}
fun_unpack(**new_dict)

def fun(**kwargs):
    print type(kwargs)
    print kwargs
    
fun(name='Subhasis', age=35, city='Bangalore')
