# -*- coding: utf-8 -*- 
# @Time : 2020/9/11 19:26 
# @Author : wednes 
# @File : study.py
"""
webdriver中的目录结构
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.mobile import Mobile
from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.remote import file_detector
# from selenium.webdriver.remote.errorhandler import Mobile
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.html5.application_cache import proxy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import ui
from selenium.webdriver.support import color
from selenium.webdriver.support import abstract_event_listener as ael
from selenium.webdriver.support import event_firing_webdriver as efw
from selenium.webdriver.support import events
from selenium import webdriver

import queue

import unittest
unittest.IsolatedAsyncioTestCase
unittest.FunctionTestCase
unittest.TestResult
unittest.BaseTestSuite

unittest.SkipTest

unittest.TestCase
unittest.TestSuite
unittest.TestRunner
unittest.TestLoader

# from unittest.util import TestLoader

li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
#      0   1   2   3   4   5   6   7   8   9   10  11 12  13  14  15  16
#    -17 -16 -15 -14 -13  -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
"""

"""
# print(li[:-1])#['a', 'b', 'c', 'd', 'e', 'f']
# print(li[::-1])#['g', 'f', 'e', 'd', 'c', 'b', 'a']
# print(li[::1])#['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(li[:-2:-2])#['g']
# print(li[::-2])#['g', 'e', 'c', 'a']
# print(li[-1])#g
"""

"""
# print(li[:1:1])#['a']
# print(li[:2:1])#['a', 'b']
# print(li[:3:1])#['a', 'b', 'c']
# print(li[:4:1])#['a', 'b', 'c', 'd']
# print(li[:5:1])#['a', 'b', 'c', 'd', 'e']
# print(li[:6:1])#['a', 'b', 'c', 'd', 'e', 'f']
# print(li[:7:1])#['a', 'b', 'c', 'd', 'e', 'f', 'g']
"""

"""
# print(li[:1:2])#['a']
# print(li[:2:2])#['a']
# print(li[:3:2])#['a', 'c']
# print(li[:4:2])#['a', 'c']
# print(li[:5:2])#['a', 'c', 'e']
# print(li[:6:2])#['a', 'c', 'e']
# print(li[:7:2])#['a', 'c', 'e', 'g']
"""

"""
# print(li[:1:3])#['a']
# print(li[:2:3])#['a']
# print(li[:3:3])#['a']
# print(li[:4:3])#['a', 'd']
# print(li[:5:3])#['a', 'd']
# print(li[:6:3])#['a', 'd']
# print(li[:7:3])#['a', 'c', 'g']
"""

"""
# print(li[:1:-1])#['q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c']
# print(li[:2:-1])#['q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd']
# print(li[:3:-1])#['q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e']
# print(li[:4:-1])#['q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f']
# print(li[:5:-1])#['q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g']
"""

"""
# print(li[:1:-2])#['q', 'o', 'm', 'k', 'i', 'g', 'e', 'c']
# print(li[:2:-2])#['q', 'o', 'm', 'k', 'i', 'g', 'e']
# print(li[:3:-2])#['q', 'o', 'm', 'k', 'i', 'g', 'e']
# print(li[:4:-2])#['q', 'o', 'm', 'k', 'i', 'g']
# print(li[:5:-2])#['q', 'o', 'm', 'k', 'i', 'g']
"""

"""
# print(li[:1:-3])#['q', 'n', 'k', 'h', 'e']
# print(li[:2:-3])#['q', 'n', 'k', 'h', 'e']
# print(li[:3:-3])#['q', 'n', 'k', 'h', 'e']
# print(li[:4:-3])#['q', 'n', 'k', 'h']
# print(li[:5:-3])#['q', 'n', 'k', 'h']
"""

"""
# print(li[:-1])
# print(li[:-1:1])#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
# print(li[:-1:2])#['a', 'c', 'e', 'g', 'i', 'k', 'm', 'o']
# print(li[:-1:3])#['a', 'd', 'g', 'j', 'm', 'p']
# print(li[:-1:4])#['a', 'e', 'i', 'm']
# print(li[:-1:5])#['a', 'f', 'k', 'p']
"""

"""
# print(li[:-1:-1])#[]
# print(li[:-1:-2])#[]
# print(li[:-1:-3])#[]
# print(li[:-1:-4])#[]
# print(li[:-1:-5])#[]
"""

"""
# print(li[:-2:-1])#['q']
# print(li[:-3:-2])#['q']
# print(li[:-4:-3])#['q']
# print(li[:-5:-4])#['q']
# print(li[:-6:-5])#['q']
"""

"""
# print(li[:-3:-1])#['q', 'p']
# print(li[:-4:-2])#['q', 'o']
# print(li[:-5:-3])#['q', 'n']
# print(li[:-6:-4])#['q', 'm']
# print(li[:-7:-5])#['q', 'l']
"""

"""
# print(li[:-4:-1])#['q', 'p', 'o']
# print(li[:-5:-2])#['q', 'o']
# print(li[:-6:-3])#['q', 'n']
# print(li[:-7:-4])#['q', 'm']
# print(li[:-8:-5])#['q', 'l']
# print(li[:-8:-2])#['q', 'o', 'm', 'k']

s = "k:1|k1:2|k2:3|k3:4"

d = {}
a = s.split("|")
for items in a:
    k, v = items.split(":")
    print(k)
    print(v)
    d[k] = int(v)
print(d)
''' '''
sn = s.split('|')
print(sn)
sm = []
for y in sn:
    sm.append(y.split(":"))
print(sm)
for i in range(len(sm)):
    sm[i][1] = int(sm[i][1])
print(sm)
print(dict(sm))

# 前后没有下划线的是公有方法
#
# 前边有一个下划线的为私有方法或属性，子类无法继承
#
# 前边有两个下划线的 一般是为了避免于子类属性或者方法名冲突，无法在外部直接访问
#
# 前后都有双下划线的为系统方法或属性
#
# 后边单个下划线的可以避免与系统关键词冲突

# isinstance() 与 type() 区别：
#
# type() 不会认为子类是一种父类类型，不考虑继承关系。
#
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
#
# 如果要判断两个类型是否相同推荐使用 isinstance()。

# 就是如果一个类实现了call方法，那么他的对象就可以像函数一样表示。就可以把它的对象当成函数

# file_input = driver.find_element_by_name('profilePic')
# file_input.send_keys("path/to/profilepic.gif")
# Generally it's better to wrap the file path in one of the methods
# in os.path to return the actual path to support cross OS testing.
# file_input.send_keys(os.path.abspath("path/to/profilepic.gif"))

#如果在条件句前忘记加if可以在结束后加上.if和Tab键，可以自动补全
#not main while par() print

#Ctrl+Shift+n  查找Python中的lib
#Ctrl+f  查找当前文件

# 在Python2中，整数值的大小有内部限制。但在Python3中取消了这一限制。
# 这意味着没有明确定义的限制，但是可用地址空间的大小根据运行Python的机器形成了一个实际的限制。

# 在Python中，如何将十六进制值a5表示为基数为16的整数常量？  x0a5
# print(int('a5',16))#十六进制转成十进制
# print(hex(165))#十进制转成十六进制为 x0a5

'''
importModule
'''
# 如何在Python中表示常量浮点值3.2 × 10的-12次幂方 ：3.2e-12
# print(r'foo\\bar\nbaz')
# 引入自己写的模块时，如果模块更改了需要用重新加载
# import importlib
# importlib.reload(module)

'''
requests
'''
# Even though the requests library has a beautifully simple API,
# abstracts the complexity of HTTP, focuses on interaction with services
# and is the de facto standard for HTTP requests in Python

'''
Status codes
'''
# 1xx: An informational response which indicates that the request was received and understood.
# 2xx: Indicates that the action requested by the client was received, understood and accepted.
# 3xx: Indicates that the client must take additional action to complete the request.
# 4xx: Intended for situations in which the error seems to have been caused by the client.
# 5xx: Occurs when the server fails to fulfill a request

# The response of a request often has some valuable information,
# known as a payload, in the request body.
# response = requests.get('https://api.github.com')
# response.json() returns the response content as a dict object.
# response.text returns the response content as a string object.
# response.content returns the response content as a bytes object.

'''
Authentication
'''
# You can implement authentication in several ways such as getpass() to get the user’s input,
# using HTTPBasicAuth or by creating a custom class as follows:
# from requests.auth import HTTPBasicAuth
# from getpass import getpass
# requests.get('https://api.github.com/user',auth = HTTPBasicAuth('username', getpass()))

'''
Performance
'''
# The importance of the correct measures can be briefly understood as follows:
# Timeouts:
#     If your application waits too long for a response, the background jobs could hang.
# Session objects:
#     You need them to improve the performance and continuity of requests.
# Max retries:
#     If your request fails, you would want your application to retry, but just a limited number of times.

'''
Concurrency
'''
# I/O-Bound programs spend most of their time waiting for external operations to complete,
# usually I/O. CPU-Bound programs spend most of their time doing computations.
'''Asyncio
Multiprocessing
Threading
Dictionaries'''
# CPU-Bound programs spend most of their time doing computations.
# Multiprocessing allows parts of the computation to be split up and run on different CPUs.
# The other forms of Python concurrency all run on a single CPU
'''
One process for each CPU to create if you’re going to use the multiprocessing library 
'''
# If your program is CPU-bound, having one process run on each CPU will likely produce good results.
# If you use fewer processes and you will have CPUs sitting idle. While if you use more processes,
# at least one of the CPUs will need to swap processes in and out which takes time away from computing
'''
asynico
'''
# The asyncio library runs on a single CPU in a single Python interpreter.
# It is possible to combine asyncio with multiprocessing
#     to get multiple CPUs working on the problem
'''
Control Structure
'''
# Control structures determine which statements in the program will be executed
# and in what order, allowing for statements to be skipped over or executed repeatedly
# The order of execution of statements in a program is called control flow.
'''
Indentation
'''
# No specific token denotes the end of a block in Python.
# In Python, blocks are defined by indentation in accordance with the off-side rule.
# When a statement occurs on a line which is indented less than the previous one,
# it indicates the end of a block.
'''
Dictionaries
'''
# Python dictionaries are similar to lists in that they are mutable and can be nested to
#       any arbitrary depth (constrained only by available memory).
# A dictionary can contain any type of Python object, including another dictionary.
#       The keys in a given dictionary do not need to be the same type as one another, nor do the values.
# Dictionary elements are accessed by key. Unlike with list indexing, the order of the items
#       in a dictionary plays no role in how the items are accessed.
#       Even though dictionary access does not rely on item order,
#       as of version 3.7 the Python language specification does guarantee that
#       the order of items in a dictionary is maintained once the dictionary is created.
'''
Each of these creates the dictionary shown(Defining a Dictionary)
'''
# Specifying a list of comma-separated <key>: <value> pairs enclosed in curly braces
# Passing a list of tuples to the built-in dict() function
# Passing keyword arguments to the dict() function (if the key values are simple strings)
# Creating an empty dictionary and then assigning the key-value pairs individually
'''
use the del statement to remove an entry from a dictionary
'''
'''
Restrictions on Dictionary Keys
'''
# The following are all immutable objects:
#     Object	        Type
#     'foo'	            string
#     len	            built-in function
#     (3+2j)	        complex
#     ('foo', 'bar')	tuple
# An object of an immutable type is hashable, and can serve as a dictionary key.
#   ['foo', 'bar'] is a list and dict(foo=1, bar=2) is a dictionary.
# These are both unhashable, mutable container types. They can’t be dictionary keys.
# Recall that these restrictions apply to dictionary keys only.
# A dictionary value can be any type whatsoever.
'''
Operators and Built-in Functions
'''
# 'z' in x[2] >>> Fasle
# while x[2] is indeed a dictionary as {'foo': 1, 'bar': {'x': 10, 'y': 20, 'z': 30}, 'baz': 3}
# 'z' in x[2]['bar'] >>> True
# 'z' is a key in x[2]['bar'] as {'x': 10, 'y': 20, 'z': 30}
'''
The dict.pop() method removes an entry from a dictionary
'''
# Remember that the argument passed to .pop() is the key for the entry you want to delete, not the value
'''
Each of these creates a copy of d1
'''
# d1 can be passed directly as an argument to dict() to create a new dictionary.
#     The REPL output shows that the resulting d2 is a copy—it has the same value as d1,
#     but is not the same object
# d1.items() returns a list of tuples containing the key-value pairs in d1.
#     That is also a valid argument to pass to dict() to create a copy of d1
# The first statement creates an empty dictionary in d2.
#     Then d2.update(d1) merges entries from d1 into d2, which creates a copy of d1.
'''
Basics of Iterating Through a Dictionary
'''
# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# for key in a_dict:
#     print(key, '->', a_dict[key])
##  color -> blue
##  fruit -> apple
##  pet -> dog
'''
Iterating Over Items
'''
# d_items = a_dict.items()
# print(d_items)
##  dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])
# for item in a_dict.items():
#     print(item)
##  ('color', 'blue')
##  ('fruit', 'apple')
##  ('pet', 'dog')
'''
Iterating Over Keys
'''
# The object returned by .keys() here provided a dynamic view on the keys of a_dict.
# This view can be used to iterate through the keys of a_dict.
## the_values = a_dict.values()
## for value in a_dict.values(): print(value)
#the_values holds a reference to a view object containing the values of a_dict.
#As any view object, the object returned by .values() can also be iterated over.
# In this case, .values() yields the values of a_dict
'''
Modifying Keys and Values
'''
# You will face a RuntimeError for the given piece of code:
#     for key in a_dict.keys():
#         if key == 'fruit':
#             del a_dict[key]
# because .keys() returns a dictionary-view object, which yields keys on demand one at a time,
# and if you delete an item (del prices[key]), then Python raises a RuntimeError,
# because you’ve modified the dictionary during iteration
'''
the following are correct ways to use a dictionary
'''
# 1,
#         new_dict = {}
#         for key, value in a_dict.items():
#             new_dict[value] = key
#
#         new_dict = {}
#         for key, value in a_dict.items():
#             if value <= 2:
#                 new_dict[key] = value
#
#         total_income = 0.00
#         for value in incomes.values():
#             total_income += value
# 2，
#         a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
#         new_dict = {k: v for k, v in a_dict.items() if v <= 2}
#
#         a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
#         new_dict = {value: key for key, value in a_dict.items()}
#
#         objects = ['blue', 'apple', 'dog']
#         categories = ['color', 'fruit', 'pet']
#         a_dict = {key: value for key, value in zip(categories, objects)}
'''
Python Built-In Functions and Libraries
iter() can’t be used to iterate over items in a dictionary
'''
# Python’s map() is defined as map(function, iterable, ...) and returns an iterator
#     that applies function to every item of iterable, yielding the results on demand.
# filter() is a built-in function that you can use to iterate through a dictionary in Python
#     and filter out some of its items. This function is defined as filter(function, iterable)
#     and returns an iterator from those elements of iterable for which function returns True.
# You can use itertools.cycle(iterable), which makes an iterator returning elements from iterable and
#     saving a copy of each.When iterable is exhausted,cycle() returns elements from the saved copy.
# itertools also provides chain(*iterables), which gets some iterables as arguments and
#     makes an iterator that yields elements from the first iterable until it’s exhausted,
#     then iterates over the next iterable and so on, until all of them are exhausted.
'''
Lambda expression abuses
'''
# Lambda functions are easy to read if they are used appropriately.
# Compare the following snippets and see how:
#         >>> numbers = [1, 2, 3]
#         >>> # Difficult to read
#         >>> print(list(map(lambda x: x + 1, numbers)))  [2, 3, 4]
#         >>> # Better to the eye:
#         >>> print([x + 1 for x in numbers])  [2, 3, 4]
# You should be mindful about using lambdas as it can be a pain for another developer
#     to read/debug. If there is anything complicated you might need to do,
#     it’s better to use a regular function definition with a proper name instead
'''
useful of Lambda expression
'''
# Lambda functions are used for functional programming.
# They can be useful as quick, throwaway single line functions.
# They are useful in allowing quick calculations or processing as the input to other functions.
'''
Lambda syntax
'''
# A lambda function can’t contain the return statement. In a lambda function,
#     statements like return, pass, assert, or raise will raise a SyntaxError exception
'''
Alternatives to using lambdas
'''
# Higher-order functions like map(), filter(), and functools.reduce() can be converted to
#     more elegant forms with slight twists of creativity, in particular with list comprehensions
#     or generator expressions.
# The built-in function map() takes a function as a first argument and applies it to each of
#     the elements of its second argument, an iterable.
# The built-in function filter() can be converted into a list comprehension. It takes a predicate
#     as a first argument and an iterable as a second argument. It builds an iterator
#     containing all the elements of the initial collection that satisfies the predicate function.
# Similar to map() and reduce() each element of the iterable, reduce() applies the function
#     and accumulates the result that is returned when the iterable is exhausted
'''
Lambda arguments -- >> (lambda x: (x + 3) * 5 / 2)(3)
'''
# A Python lambda expression consists of:
#         The Keyword: lambda
#         A bound variable: x
#         A body: (x + 3) * 5 / 2
# Regarding the second bracket of 3, ((lambda x: (x + 3) * 5 / 2)(3)):
# Reduction is a lambda calculus strategy to compute the value of the expression.
#     It consists of substituting the argument 3 for x.
# Overall, the run of this lambda function happens with 3 being passed into it as an argument.
#     You can calculate it in the following way:
#         x + 3 → 3 + 3 = 6
#         5 / 2 = 2.5
#         6 * 2.5 = 15.0
'''
Uses of lambda expressions
'''
# Consider the following list as an input: my_list = ['Real', ' Python']
# translate the following function to an anonymous lambda function:
#     def func(x):
#        return ''.join(x)
# You should do this in the same way as see in the example. The keyword will be lambda,
#     bound variable will be x and the body will be ''.join(x). So, the final result will be:
#         lambda x: ''.join(x)
'''
Map with lambda
'''
# Consider the following list as an input: numbers = [1, 2, 3]
# map() allows you to apply a function to every item of an iterable.
#         map(lambda x: x, numbers)  >>>  [1, 2, 3]
#         list(map(lambda x: x % 2 == 0, numbers))  >>>  [False, True, False]
#                 output True or False depending on it’s success with division by 2
#         list(map(lambda x: x, numbers))   >>>  <map object at 0x7fe395945910>
#                 output the location of the map() object
'''
Reduce with lambda
'''
# Consider the following code snippet:
#         from functools import reduce
#         numbers = [1, 2, 3]
#         reduce(lambda x, y: x + y, numbers)    >>>  6
# reduce() applies the function cumulatively to the items of the given sequence.
#     Hence, it becomes 1 + 2 = 3 and then 3 + 3 = 6
'''
Filter with lambda
'''
# Consider the following list as an input: numbers = [1, 2, 3]
# the following would produce the result: [2]
#     list(filter(lambda x: x % 2 == 0, numbers))
#     list(filter(lambda x: (x + 1) * 3 / 3 % 3 == 0, numbers))
'''
Lists are Ordered, Lists Can Contain Arbitrary Objects
'''
# A list is an ordered collection of objects. The order of the elements is
#     an innate characteristic of the list.
# A list may contain any number of elements (constrained by the computer’s memory, of course),
#     of any type. The same object may occur any number of times.
'''
List Elements Can Be Accessed by Index
'''
# Assume the following list definition: a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
#     max(a[2:4] + ['grault']) >>> 'qux'
#     a[2:4] returns the slice ['baz', 'qux']. The + operator concatenates,
#     so the argument to max() is ['baz', 'qux', 'grault'].
#     The maximum value (for strings, the latest in alphabetical order) is 'qux'
'''
Lists Can Be Nested
'''
# Consider the following nested list definition: x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
# the expression that returns the 'z' in 'baz'
#         x[1][2][1][2]
#         x[1][2][1][-1]
# expression returns the list ['baz', 2.718]
#             x[1][2][1:3]
#             x[1][2][1:]
'''
Lists Are Mutable
'''
#1, List a is defined as follows: a = [1, 2, 3, 4, 5]
# the following statements that remove the middle element 3 from a so that it equals [1, 2, 4, 5]
#     del a[2]     The del command simply removes the specified list item.
#         This is arguably the most straightforward way to remove the middle item from a.
#     a[2:3] = []   a[2:3] represents the slice of a consisting of the single element 3.
#         The slice assignment a[2:3] = [] replaces that slice with an empty list,
#         which effectively removes that element
#     a.remove(3)   The .remove() method removes the specified argument from the target list,
#         if it is present.This is a nice way to remove an item from a list by specifying its value,
#         rather than its index in the list
#2, List a is defined as follows: a = ['a', 'b', 'c']
# adds 'd' and 'e' to the end of a, so that it then equals ['a', 'b', 'c', 'd', 'e']
#     a += ['d', 'e']  The += augmented assignment operator expects an iterable as the second operand.
#         It iterates over the second operand and adds the resulting items to the end of the target operand
#     a += 'de'  Remember that when Python iterates over a string, the result is a list of the component
#         characters. Thus, this statement also appends the list ['d', 'e']
#     a[len(a):] = ['d', 'e']  a[len(a):] designates an empty slice at the end of a.
#         This assignment replaces that slice with ['d', 'e']
#3, You have a list a defined as follows: a = [1, 2, 7, 8]
# using slice assignment that will fill in the missing values so that a equals [1, 2, 3, 4, 5, 6, 7, 8]
#     a[2:2] = [3, 4, 5, 6]   a[2:2] designates the empty slice of the original a between values 2 and 7.
#         The assignment statement shown inserts the items in [3, 4, 5, 6] into that location
'''
Defining and Using Tuples
'''
# That’s the main difference between tuples and list: tuples are immutable.
# Tuples can be indexed, though. And remember that even though tuples are defined using parentheses,
# tuple indexing uses square brackets just like list indexing
# To distinguish this from a singleton tuple,you need to include a trailing comma before the closing parenthesis
#     t = ('foo',)
#     >>> t   ('foo',)
#     >>> type(t)  <class 'tuple'>
# This is also one of those cases where you can leave the parentheses off.The trailing comma causes
# Python to assume a tuple
#     t = 'foo',
#     >>> t     ('foo',)
#     >>> type(t)    <class 'tuple'>
'''
Tuple Assignment, Packing, and Unpacking
'''
# Consider this assignment statement: a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)[1::3]
# The slice expression on the right side of the assignment produces the tuple (2, 5, 8)
# The assignment is thus equivalent to this compound tuple packing/unpacking assignment: a, b, c = (2, 5, 8)
'''
Python Operators and Expressions
'''
#1, The objects that operators act on are called operands.
# An expression involving operators and operands is called an expression.
# 操作符作用的对象称为操作对象。涉及运算符和操作数的表达式称为表达式。
#2, the value of the expression 100 / 25 is 4.0
# the result of standard division is always float.
# The value of 100 // 25 (integer division) is 4
#3, Internal representation of float objects is not precise(精确的),
#     so they can’t be relied on to equal exactly what you think they will:
#         >>> 1.1 + 2.2 == 3.3    False
# You should instead compute whether the numbers are close enough
#     to one another to satisfy a specified tolerance:
#         >>> tolerance = 0.00001
#         >>> abs((1.1 + 2.2) - 3.3) < tolerance  True
#4, Consider the following code snippet: x = 10.0  y = (x < 100.0) and isinstance(x, float)
# After these are executed, what is the value of y
#     This is a case where the terms of the expression, (x < 100.0) and isinstance(x, float),
#     are both not only truthy, but actually equal to the Python value True.
#     The expression is therefore also True.
#5, 'None'  >>> truthy      0.000001  >>> truthy      True    >>> truthy
# 0       >>> falsy       False     >>> falsy       []      >>> falsy
# The Python object None is falsy, but the non-empty string 'None' is truthy.
# 0.000001, a non-zero numeric value, is also truthy. But barely.
#6, when non-Boolean objects are joined by and or or,
# the result is not necessarily equal to either of the Python values True or False
# For two non-Boolean values a and b:
#         If a is	        a or b is	        a and b is
#         truthy	        a	                b
#         falsy	            b	                a
#7, The function sqrt() from the math module computes the square root of a number.
#     x = -100
#     from math import sqrt
#     x > 0 and sqrt(x) Will this highlighted line of code raise an exception?
#         In the highlighted line, x > 0 is False.
#         The expression is already known to be falsy at that point.
#         Due to short-circuit evaluation, sqrt(x) (which would raise an exception) is not evaluated
'''
Implicit Line Continuation
'''
# Any statement containing an opening parenthesis ('('), square bracket ('['),
#     or curly brace ('{') is understood by the Python interpreter to be incomplete
#     and may be continued across lines until the corresponding parenthesis, bracket or brace is encountered.
#     Because parentheses, brackets and braces are so integral to Python syntax,
#     this gives you ample opportunity for implicit line continuation.
# Grouping parentheses around an entire expression may be syntactically unnecessary,
#     but often are included anyhow so the statement may be continued across lines.
# PEP 8 recommends using implicit line continuation when feasible
'''
Explicit Line Continuation
'''
# Explicit line continuation is achieved by specifying a backslash character (\)
#     at the end of each line that is to be continued.
# Remember that the backslash must be the final character on a continued line.
#     There can’t be anything following it—not even whitespace
'''
Multiple Statements Per Line
'''
# Placing more than one statement on a line is generally discouraged by PEP 8.
#     In cases where you might consider it,there is often a more Pythonic way to accomplish what you want.
# On the other hand, PEP 8 also says “A Foolish Consistency is the Hobgoblin of Little Minds.”
#     It is well to know when it might be appropriate to be inconsistent.
#     Above all, readability is what is most important
'''
Line Continuation
'''
# The Style Guide for Python Code is outlined in PEP 8.
# Related information on Docstring Conventions is specified in PEP 257.
# For a list of other PEPs, see the Index of PEPs
'''
Comments
'''
# A comment may appear at the end of a statement, and on a line by itself.
#     A comment may also appear within a statement that spans multiple lines by implicit line continuation.
# But a comment can’t follow the backslash character that signifies explicit line continuation.
#     With explicit line continuation, the backslash character must be the final character on the line
# PEP 8 recommends that use of free-standing triple-quoted string literals
#     be reserved for function docstrings.
# It can be useful to comment out a block of code with triple-quoting temporarily,
#     for testing or debugging purposes. But in general, block comments should be written with
#     a # character at the start of each line
'''
Whitespace
'''
# There should not be whitespace immediately inside curly braces, nor immediately before a colon
# Colons in slice notation should have equal amounts of space on each side.
#     When a slice parameter is omitted, the space is omitted
# Whitespace between a function or method name and the opening parenthesis is definitely frowned upon
# PEP 8 specifically recommends against whitespace between the trailing comma
#     and closing parenthesis when defining a singleton tuple
# Whitespace immediately before a semicolon is not recommended
# leading whitespace in front of a statement is significant.
#     Indentation is used to determine grouping of statements
#     You can’t just indent statements at will in Python.
'''
Sets in Python
'''
# A Python set is a well-defined collection of distinct objects, called elements or members.
# Sets are unordered. Set elements are unique–if you try to add an element to a set a second time,
#     it has no effect.
# A set itself may be modified, but the elements contained in a set must be immutable
#     (actually hashable, but for the types you are familiar with so far,
#     immutable and hashable are effectively the same thing).
'''
Defining a Set
s = {'a', 'b', 'c'}
s = set(['a', 'b', 'c'])
s = set('abc')
s = {'a', 'b', 'c','a', 'b', 'c'} >>> 实际内存中是 {'a', 'b', 'c'}
'''
# The simplest way to define a set is to specify the set elements in curly brackets
# You can also define a set with the built-in set() function.
#     The argument should be an iterable that yields the elements of the set
# When using the set() function, you can’t specify the set elements individually.
#     The argument to set() must be a single iterable
# s = {('a', 'b', 'c')} actually does define a set.
#     It contains a single element—the tuple ('a', 'b', 'c')
'''
Operators vs. Methods
'''
# You have a set s defined as follows: s = {100, 200, 300}
# the following statements correctly produce the union of s and the set {300, 400, 500}
#         >>> s.union({300, 400, 500})        >>>{400, 100, 500, 200, 300}
#         >>> s.union(set([300, 400, 500]))   >>>{400, 100, 500, 200, 300}
#         >>> s.union([300, 400, 500])        >>>{100, 200, 300, 400, 500}
#         >>> s | {300, 400, 500}             >>>{400, 100, 500, 200, 300}
#         >>> s | set([300, 400, 500])        >>>{400, 100, 500, 200, 300}
# The argument specified to the .union() method can be either a set or an iterable.
#     Thus all of the above work.
# (Yes, it’s a little strange that the resulting set doesn’t display the same in all cases.
#     Remember, sets are unordered: these are all the same set.)
# The operands specified for the | operator must be sets. Both of the above are acceptable
'''
Available Operators and Methods
'''
#1, {'b', 'a', 'r'} & set('qux')  >>>  set()
# The & operator denotes set intersection. The two sets in question, {'b', 'a', 'r'} and {'q', 'u', 'x'},
#     do not have any characters in common, so the intersection is the empty set.
# If you chose {} as the answer, you probably forgot that {} denotes an empty dictionary, not an empty set
#2, {1, 2, 3, 4, 5} - {3, 4} ^ {5, 6, 7}   >>> {1, 2, 6, 7}
# The - operator denotes set difference and the ^ operator denotes symmetric difference.
#     Set difference has a higher precedence, so that is performed first:
#         >>> {1, 2, 3, 4, 5} - {3, 4}   >>> {1, 2, 5}
#     Then the symmetric difference is computed between that result and {5, 6, 7}
#         >>> {1, 2, 5} ^ {5, 6, 7}  >>> {1, 2, 6, 7}
#3, (x & y <= x) and (x & y <= y) is True for any sets x and y?  >>> True
#     x & y is theintersectionofx and y.By definition,
#     it will contain only elements that are in both x and y.
#4, Python provides both the .issubset() method and <= operator
#     to test whether a set is a subset of another set.
# But to test for proper subset, the < operator is the only option
'''
Modifying a Set
'''
# Suppose a set s is defined as follows:  s = {'foo', 'bar', 'baz', 'qux'}
# the following remove element 'bar' from s
#     s -= {'bar'}  s.difference_update({'bar'})
#         Both the -= augmented assignment operator and the .difference_update() method
#         update s by removing the elements found in the specified set—'bar' in this case
#     s.discard('bar')
#         This is straightforward: the .discard() method simply removes the specified object from s.
#         Recall that .discard() quietly does nothing if the set does not contain the object to remove.
#         The .remove() method also removes an object from a set,
#         but raises an exception if it is not a member of the set
#     s &= {'foo', 'baz', 'qux'}
#         The &= augmented assignment operator updates s, retaining only elements found in both s
#         and the specified set. Because 'bar' is not in the specified set, it is effectively removed from s.
'''
Frozen Sets
'''
# Frozen sets are immutable, so the modifying methods available for standard sets
#     are not available for (frozen(sets)).
# Frozen sets can beused in situations where an immutable object is required, like a
#         member of a set or a dictionary key
# There is no built-in Python syntax for defining a frozen set like there is with a standard set.
#     The only way is to use the frozenset() function
# f |= {'foo'} does not raise an exception.
#     The |= augmented assignment operator does not modify f directly in this example.
#     Rather, it creates a new frozen set equal to the original f with 'foo' added
