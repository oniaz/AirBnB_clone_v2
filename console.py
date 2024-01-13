#!/usr/bin/python3
"""Console module. """
####
import sys
sys.path.insert(1, "/Users/omnia/Desktop/AirBnB_clone")
####


import cmd


class HBNBCommand(cmd.Cmd):
    """ Console class.

    Methods:
        misc:
            emptyline
            do_EOF
            do_quit
    """
    prompt = '(hbnb)'

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
