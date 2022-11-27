# HBnB
## _A simple AirBnB website clone_

![Alt](https://github.com/Bezawork-pr/AirBnB_clone/blob/master/65f4a1dd9c51265f49d0.png?raw=true)

![Build Status](https://img.shields.io/github/directory-file-count/Bezawork-pr/AirBnB_clone?style=flat-square) ![Build Status](https://img.shields.io/github/languages/count/Bezawork-pr/AirBnB_clone?color=red&style=flat-square) ![Build Status](https://img.shields.io/github/languages/top/Bezawork-pr/AirBnB_clone?color=green&style=flat-square)
The goal of the project is to deploy on your server a simple copy of the AirBnB website.
The complete web application is composed by:
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## The console

## Usage
`./console`
The above command runs the interactive console where all the models commands are executed. An example of its operation is illustrated below.
```sh
root@pc: ./console
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) all
["[User] (44329e56-4d12-4ec7-946e-11eb5cc1d779) {'id': '44329e56-4d12-4ec7-946e-11eb5cc1d779', 'created_at': datetime.datetime(2022, 11, 26, 18, 12, 2, 179761), 'updated_at': datetime.datetime(2022, 11, 26, 18, 12, 2, 179761)}"]
(hbnb) quit
root@pc:
```
With the assumption that we have an object called `My_Model`, the following a descriptions of the console commands:
`./all`
Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.
The printed result is a list of strings.
If the class name doesn't exist, it prints `** class doesn't exist **` (ex: $ all MyModel)
`./create`
Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
If the class name is missing, it prints `** class name missing **` (ex: $ create)
If the class name doesn't exist, it prints `** class doesn't exist **` (ex: $ create MyModel)
`./destroy`
Deletes an instance based on the class name and id (save the change into the JSON file). Ex: (hbnb) destroy BaseModel 1234-1234-1234

