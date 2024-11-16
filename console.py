#!/usr/bin/python3
"""entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """defines the cmd commands with default prompy (hbnb)"""
    prompt = "(hbnb) "

    def emptyline(self):
        """ Do nothing """
        pass

    def do_quit(self, arg):
        """ Quits the program"""
        return True

    def do_EOF(self, arg):
        """ Quits the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
