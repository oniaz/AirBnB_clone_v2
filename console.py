#!/usr/bin/python3
"""Console module. """


import cmd
import shlex

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

from models import storage


class HBNBCommand(cmd.Cmd):
    """ Console class.

    Methods:

        AirbnB mangemnet:
            create
            show
            destroy
            all
            update

        misc:
            emptyline
            do_EOF
            do_quit
    """
    prompt = '(hbnb)'
    classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
        ]

    def do_create(self, line):
        """Creates a new isntance of a class.

        Use:
            create <class name>
        Example:
            (hbnb)create BaseModel
        """
        args = shlex.split(line)

        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{args[0]}()")
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Shows the string representation of an object using the object class
        name and object id.

        Use:
            show <class name> <object id>
        Example:
            (hbnb)show BaseModel 2a6ad74e-1a39-41ed-9a56-bc1766c2667a
        """
        args = shlex.split(line)

        try:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
        except (IndexError):
            print("** class name missing **")
            return
        try:
            args[1]
        except (IndexError):
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
        else:
            print(instances[key])

    def do_destroy(self, line):
        """ Destroys an Object using the object class name and object id.

        Use:
            destroy <class name> <object id>

        Example:
            (hbnb)destroy BaseModel 2a6ad74e-1a39-41ed-9a56-bc1766c2667a
        """
        args = shlex.split(line)

        try:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
        except (IndexError):
            print("** class name missing **")
            return
        try:
            args[1]
        except (IndexError):
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in FileStorage._FileStorage__objects:
            print("** no instance found **")
        else:
            del FileStorage._FileStorage__objects[key]
            storage.save()

    def do_all(self, line):
        """Prints the string representation of all instances of a specified
        class. If no class is passed, it prints all instances, regardless of
        class type.

        Use:
            all <class name>
            all
        Example:
                (hbnb)all BaseModel
                (hbnb)all
        """
        args = shlex.split(line)
        if args:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            str_list = []
            instances = storage.all()
            for key, value in instances.items():
                if value.to_dict()["__class__"] == args[0]:
                    str_list.append(value.__str__())
            print(str_list)

        else:
            str_list = []
            instances = storage.all()
            for key, value in instances.items():
                str_list.append(value.__str__())
            print(str_list)

    def do_update(sel, line):
        """ Updates ones instance attribute at a time.

        Use:
            update <class name> <id> <attribute name> "<attribute value>"

        Example:
            (hbnb)update BaseModel 2a6ad74e-1a39-41ed-9a56-bc1766c2667a
            first_name "Endeavour Morse"
        """
        args = shlex.split(line)

        # class name
        try:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
        except (IndexError):
            print("** class name missing **")
            return

        # id
        try:
            obj = f"{args[0]}.{args[1]}"
            if obj not in FileStorage._FileStorage__objects:
                print("** no instance found **")
                return
        except (IndexError):
            print("** instance id missing **")
            return

        # attribute name
        if len(args) < 3:
            print("** attribute name missing **")
            return
        # attribute value
        elif len(args) < 4:
            print("** value missing **")
            return

        attribute = args[2].replace("\"", "")
        value = args[3].replace("\"", "")
        obj = FileStorage._FileStorage__objects[obj]
        setattr(obj, attribute, value)
        obj.save()

    def emptyline(self):
        """Does nothing. """
        pass

    def do_EOF(self, line):
        """End of file, quits the console."""
        return True

    def do_quit(self, line):
        """"Quit command, quits the console. """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
