Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print('hello world')
hello world
>>> x=20
>>> print(x)
20
>>> x=20.5
>>> print(x)
20.5
>>> x=1j
>>> print(x)
1j
>>> x=["apple","banana","cherry"]
>>> print(x)
['apple', 'banana', 'cherry']
>>> x=("apple","banana","cherry")
>>> print(x)
('apple', 'banana', 'cherry')
>>> x=range(6)
>>> print(x)
range(0, 6)
>>> x={"apple","banana","cherry"}
print(x)
{'apple', 'cherry', 'banana'}
x=frozenset({"apple","banana","cherry"})
print(x)
SyntaxError: multiple statements found while compiling a single statement
x=frozenset({"apple","banana","cherry"})
print(x)
frozenset({'apple', 'cherry', 'banana'})
x=true
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x=true
NameError: name 'true' is not defined. Did you mean: 'True'?
x=True
print(x)
True
x=b"hello"
print(x)
b'hello'
x=bytearray(5)
print(x)
bytearray(b'\x00\x00\x00\x00\x00')
x=memoryview(byte(5))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x=memoryview(byte(5))
NameError: name 'byte' is not defined. Did you mean: 'bytes'?
x=memoryview(bytes(5))
print(x)
<memory at 0x0000021D5F382F80>
x=none
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    x=none
NameError: name 'none' is not defined. Did you mean: 'None'?
x=None
print(x)
None
