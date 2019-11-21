PythonWin 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:22:17) [MSC v.1500 32 bit (Intel)] on win32.
Portions Copyright 1994-2018 Mark Hammond - see 'Help/About PythonWin' for further copyright information.
>>> None
>>> [1,2,3,4,5,6,7,8,9,10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> L = [1,2,3,4,5]
>>> print L
>>> print L
[1, 2, 3, 4, 5]
>>> l = [1,2,3,4,"five"]
... 'five
Traceback (  File "<interactive input>", line 2
    'five
        ^
SyntaxError: EOL while scanning string literal
>>> '
>>> l = [1,2,3,4,"five"]
... 'five
>>> L = [1,2,3,4,"five"]
>>> print L
[1, 2, 3, 4, 'five']
>>> P = ['apple',"kiwi","orange"]
>>> print P
['apple', 'kiwi', 'orange']
>>> G = 
Traceback (  File "<interactive input>", line 1
    G =
      ^
SyntaxError: invalid syntax
>>>G = [1,2,3,P]
>>> print G
Traceback (most recent call last):
  File "<interactive input>", line 1, in <module>
NameError: name 'G' is not defined
>>> print G[0]
Traceback (most recent call last):
  File "<interactive input>", line 1, in <module>
NameError: name 'G' is not defined
>>> G = [1,2,3,P]
>>> print G[0]
1
>>> print G[3]
['apple', 'kiwi', 'orange']
>>> print G[3][1]
kiwi
>>> print G[3][1][1]
i
>>> print G[-2:-1]
[3]
>>> print G
[1, 2, 3, ['apple', 'kiwi', 'orange']]
>>> print L + P
[1, 2, 3, 4, 'five', 'apple', 'kiwi', 'orange']
>>> print L * 2
[1, 2, 3, 4, 'five', 1, 2, 3, 4, 'five']
>>> ['apple', 'kiwi', 'orange', 'banana', 'pear', 'watermelon']
['apple', 'kiwi', 'orange', 'banana', 'pear', 'watermelon']
['apple', 'kiwi', 'orange', 'banana', 'pear', 'watermelon']
1
>>> L.count('apple')
1
>>> print len(L)
6
>>> 
>>> import math
>>> dir(math)
['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', 'WichmannHill', '_BuiltinMethodType', '_MethodType', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_acos', '_ceil', '_cos', '_e', '_exp', '_hashlib', '_hexlify', '_inst', '_log', '_pi', '_random', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'division', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'jumpahead', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> import random
>>> random.randrange(0,10)
9
>>> range(0,10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> random.randrange(0,10)
3
>>> random.randrange(0,10)
8
>>>
# true or false

