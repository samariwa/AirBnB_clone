# HBnB
## _A simple AirBnB website clone_

![Alt](https://github.com/Bezawork-pr/AirBnB_clone/blob/master/65f4a1dd9c51265f49d0.png?raw=true)

![Build Status](https://img.shields.io/github/directory-file-count/Bezawork-pr/AirBnB_clone?style=flat-square) ![Build Status](https://img.shields.io/github/languages/count/Bezawork-pr/AirBnB_clone?color=red&style=flat-square) ![Build Status](https://img.shields.io/github/languages/top/Bezawork-pr/AirBnB_clone?color=green&style=flat-square)\
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
With the assumption that we have an object called `My_Model`, the following a descriptions of the console commands:\
`./all`\
Prints all string representation of all instances based or not on the class name. Ex: (hbnb) all BaseModel or (hbnb) all.\
The printed result is a list of strings.\
If the class name doesn't exist, it prints `** class doesn't exist **` (ex: (hbnb) all MyModel)\
`./create`\
Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: (hbnb) create BaseModel\
If the class name is missing, it prints `** class name missing **` (ex: (hbnb) create)\
If the class name doesn't exist, it prints `** class doesn't exist **` (ex: (hbnb) create MyModel)\
`./destroy`\
Deletes an instance based on the class name and id (save the change into the JSON file). Ex: (hbnb) destroy BaseModel 1234-1234-1234\
`./show`\
Prints the string representation of an instance based on the class name and id. Ex: (hbnb) show BaseModel 1234-1234-1234.\
If the class name is missing, it prints `** class name missing **` (ex: (hbnb) show)\
If the class name doesn't exist, it prints `** class doesn't exist **` (ex: (hbnb) show MyModel)\
If the id is missing, print `** instance id missing **` (ex: (hbnb) show BaseModel)\
If the instance of the class name doesn't exist for the id, it prints `** no instance found **` (ex: (hbnb) show BaseModel 121212)\
`./update`\
Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"\
Usage: update <class name> <id> <attribute name> "<attribute value>"\
Only one attribute can be updated at the time\
You can assume the attribute name is valid (exists for this model)\
The attribute value must be casted to the attribute type\
If the class name is missing, it prints `** class name missing **` (ex: (hbnb) update)\
If the class name doesn't exist, it prints `** class doesn't exist **` (ex: (hbnb) update MyModel)\
If the id is missing, it prints `** instance id missing **` (ex: (hbnb) update BaseModel)\
If the instance of the class name doesn't exist for the id, print ** no instance found ** (ex: (hbnb) update BaseModel 121212)\
If the attribute name is missing, it prints `** attribute name missing **` (ex: (hbnb) update BaseModel existing-id)\
If the value for the attribute name doesn't exist, it prints `** value missing **` (ex: (hbnb) update BaseModel existing-id first_name)\
All other arguments should not be used (Ex: (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com")\
id, created_at and updated_at can't be updated. You can assume they won't be passed in the update command\
Only simple arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime\
`quit`\
exits the program\
`help`\
Shows the various functionalities\

