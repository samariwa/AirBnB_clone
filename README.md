### First step: Write a command interpreter to manage your AirBnB objects.
1. put in place a parent class (called BaseModel) 
	A. initialization
	B. serialization
	C. deserialization 
		=>create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
2. create all classes used for AirBnB 
	A. User
	B. State
	C. City
	D. Place
		=> inherit from BaseModel
3. create the first abstracted storage engine of the project: File storage.
4. create all unittests to validate all our classes and storage engine.

### What does the command interpreter do?
	A. Create a new object 
	B. Retrieve an object from a file
	C. Do operations on objects
	D. Update attributes of an object
	E. Destroy an object

### Goal of the project
1. How to create a Python package
2. How to create a command interpreter in Python using the cmd module
3. What is Unit testing and how to implement it in a large project
4. How to serialize and deserialize a Class
5. How to write and read a JSON file
6. How to manage datetime
7. What is an UUID
8. What is *args and how to use it
9. What is **kwargs and how to use it
10. How to handle named arguments in a function

### Requirements
#### Python Scripts
A. Allowed editors: vi, vim, emacs
B. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
C. All your files should end with a new line
D. The first line of all your files should be exactly #!/usr/bin/python3
E. A README.md file, at the root of the folder of the project, is mandatory
F. Your code should use the pycodestyle (version 2.8.*)
G. All your files must be executable
H. The length of your files will be tested using wc
I. All your modules should have a documentation 
J. All your functions (inside and outside a class) should have a documentation 
 => NOTE - Length of Documentation will be verified

#### Python Unit Tests
A. Allowed editors: vi, vim, emacs
B. All your files should end with a new line
C. All your test files should be inside a folder tests
D. You have to use the unittest module
E. All your test files should be python files
F. All your test files and folders should start by test_
G. Your file organization in the tests folder should be the same as your project
H. All your tests should be executed by using this command: python3 -m unittest discover tests
I. You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
J. All your modules should have a documentation
K. All your classes should have a documentation 
L. All your functions (inside and outside a class) should have a documentation 


### More Info
1. Your shell should work both interactive and non-interactive
2. All tests should also pass in non-interactive mode


