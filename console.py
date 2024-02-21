#!/usr/bin/env python3
""" Console Module """
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter."""
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

    def __init__(self):
        super().__init__()
        if not sys.stdin.isatty():
            self.prompt = ''

    def preloop(self):
        """Prints prompt if in non-interactive mode."""
        if not self.prompt:
            print(self.prompt, end='')

    def postcmd(self, stop, line):
        """Prints prompt if in non-interactive mode."""
        if not self.prompt:
            print(self.prompt, end='')
        return stop

    def default(self, line):
        """Handles unknown commands."""
        cmd, arg, line = self.parseline(line)
        if cmd in self.classes and arg in self.dot_cmds:
            getattr(self, 'do_' + arg)(cmd)
        else:
            print("*** Unknown syntax:", line)

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        try:
            print(obj_dict[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        obj_list = []
        for key, obj in storage.all().items():
            if not arg or arg == key.split('.')[0]:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key, None)
        if obj:
            setattr(obj, args[2], args[3].strip("\"'"))
            obj.save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

