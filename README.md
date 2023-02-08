# AirBnB Clone ― The ALX-Holberton BnB

## Description of the project
The goal of the project is to deploy a replica of the [Airbnb Website](https://www.airbnb.com/) using my server. The final version of this project will have:
- A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)
- A website (front-end) with static and dynamic functionalities
- A comprehensive database to manage the backend functionalities
- An API that provides a communication interface between the front and backend of the system.

The project's implementation will happen in the following phases:
## Phase One
The first phase is to manipulate a powerful storage system to give an abstraction between objects and how they are stored and persisted. To achieve this, I will:
- put in place a parent class (called ```BaseModel```) to take care of the initialization, serialization and deserialization of my future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (```User, State, City, Place…```) that inherit from ```BaseModel```
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine
- Create a data model
- Manage (create, update, destroy, etc) objects via a console/command interpreter
- Store and persist objects to files (JSON files)
S
## Description of the command interpreter
| Commands  | Description |
| ------------- | ------------- |
| ```quit```  | Quits the console  |
| ```Ctrl+D```  | Quits the console  |
| ```help``` or ```help <command>```  | Displays all commands or Displays instructions for a specific command
| ```create <class>```  | Creates an object of type , saves it to a JSON file, and prints the objects ID
| ```show <class> <ID>```  | Shows string representation of an object
| ```destroy <class> <ID>```  | Deletes an objects
| ```all or all <class>```  | Prints all string representations of all objects or Prints all string representations of all objects of a specific class
| ```update <class> <id> <attribute name> "<attribute value>"```  | Updates an object with a certain attribute (new or existing)
| ```<class>.all()```  | Same as all ```<class>```
| ```<class>.count()```  | Retrieves the number of objects of a certain class
| ```<class>.show(<ID>)```  | Same as show ```<class> <ID>```
| ```<class>.destroy(<ID>)```  | Same as destroy ```<class> <ID>```
| ```<class>.update(<ID>, <attribute name>, <attribute value>```  | Same as update ```<class> <ID> <attribute name> <attribute value>```
| ```<class>.update(<ID>, <dictionary representation>)```  | Updates an objects based on a dictionary representation of attribute names and values

## General Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
## Final Product
![alt](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU65GPZGY3%2F20210226%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210226T091352Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8ad0ced94d77d100be587f30d4af3734acf12d2b05b803b084cd11ce51bf68f4)
## Data Diagram
![alt](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/99e1a8f2be8c09d5ce5ac321e8cf39f0917f8db5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU65GPZGY3%2F20210226%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210226T091352Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a4013a9239416a982d703d1ac725e63a9b35593900d197534d087b71f813441c)
