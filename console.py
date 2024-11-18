#!/usr/bin/python3
"""entry point of the command interpreter """
import cmd

from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


def parse(arg):
    """parse the user input"""
    if len(arg) == 0:
        print("** class name missing **")
        return False

    if arg.split()[0] not in globals():
        print("** class doesn't exist **")
        return False

    return True


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

    def do_create(self, arg):
        """create new instance of a class"""
        if parse(arg):
            obj_class = globals()[arg.split()[0]]
            new_instance = obj_class()
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """show the instance based on the class name"""
        if parse(arg):
            args = arg.split()
            if len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}{}".format(arg.split()[0], arg.split()[1])
                stored_obj = storage.all()
                if key in stored_obj:
                    print(stored_obj[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """ delete instance with class name """
        if parse(arg):
            args = arg.split()
            if len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}{}".format(arg.split()[0], arg.split()[1])
                stored_obj = storage.all()
                if key in stored_obj:
                    del stored_obj[key]
                    storage.save()
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
