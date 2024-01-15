# HolBnb

A Console Imitation of Airbnb

## Overview

HolBnb is a simple console application that mimics Airbnb, created for learning and practicing Python Object-Oriented Programming (OOP). This project is part of the Alx SE program by Holberton.

Through the console, you can perform various operations, including creating new objects, retrieving objects from a JSON file, updating object attributes, and destroying objects.

## Usage

To use HolBnb, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/oniaz/AirBnB_clone.git
   cd AirBnB_clone
   ```

2. Run the console:
   ```bash
   ./console.py
   ```

3. Available Commands:
   - `create`: Creates a new instance of a class.
   - `update`: Updates an instance attribute at a time.
   - `destroy`: Destroys an object.
   - `show`: Shows the string representation of an object.
   - `all`: Prints the string representation of all instances of a specified class. If no class is passed, it prints all instances, regardless of class type.
   - `help`: Displays information about available commands or a specific command.
   - `EOF`: End of file, quits the console.
   - `quit`: Quits the console.

## Examples

### create
Creates a new instance of a class.

#### Use:
```bash
create <class name>
```

#### Example:
```bash
(hbnb) create BaseModel
```

### update
Updates an instance attribute at a time.

#### Usage:
```bash
update <class name> <id> <attribute name> "<attribute value>"
```

#### Example:
```bash
(hbnb) update BaseModel 2a6ad74e-1a39-41ed-9a56-bc1766c2667a first_name "Endeavour Morse"
```

### destroy
Destroys an object.

#### Use:
```bash
destroy <class name> <object id>
```

#### Example:
```bash
(hbnb) destroy BaseModel 2a6ad74e-1a39-41ed-9a56-bc1766c2667a
```

### show
Shows the string representation of an object.

#### Use:
```bash
show <class name> <object id>
```

#### Example:
```bash
(hbnb) show BaseModel 2a6ad74e-1a39-41ed-9a56-bc1766c2667a
```

### all
Prints the string representation of all instances of a specified class. If no class is passed, it prints all instances, regardless of class type.

#### Use:
```bash
all <class name>
```
or
```bash
all
```

#### Example:
```bash
(hbnb) all BaseModel
```

### help
Display information about available commands or a specific command.

#### Use:
```bash
help <topic>
```

#### Example:
```bash
(hbnb) help
(hbnb) help destroy
```

### EOF
End of file, quits the console.

#### Example:
```bash
(hbnb) EOF
```

### quit
Quits the console.

#### Example:
```bash
(hbnb) quit
```
