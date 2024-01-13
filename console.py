#!/usr/bin/python3
"""Console module. """
####
# import sys
# sys.path.insert(1, "/Users/omnia/Desktop/AirBnB_clone")
####


import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


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

    def __init__(self):
        """"
        """
        super().__init__()
        self.classes = ["BaseModel"]

    def do_create(self, line):
        """Creates a new isntance of a class.

        Use:
            create <class name>
        Example:
            (hbnb)create BaseModel
        """
        args = line.split()

        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
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
        args = line.split()

        try:
            if args[0] not in self.classes:
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
            reupload = BaseModel(**instances[key])
            print(reupload)

    def do_destroy(self, line):
        """ Destroys an Object using the object class name and object id.

        Use:
            destroy <class name> <object id>

        Example:
            (hbnb)destroy BaseModel 2a6ad74e-1a39-41ed-9a56-bc1766c2667a
        """
        args = line.split()

        try:
            if args[0] not in self.classes:
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
        args = line.split()
        if args:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            str_list = []
            instances = storage.all()
            for key, value in instances.items():
                if value["__class__"] == args[0]:
                    b = BaseModel(**value)
                    str_list.append(b.__str__())
            print(str_list)

        else:
            str_list = []
            instances = storage.all()
            for key, value in instances.items():
                b = BaseModel(**value)
                str_list.append(b.__str__())
            print(str_list)

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
