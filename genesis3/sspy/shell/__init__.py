"""!

An interactive shell for use with the sspy scheduler.
Mirrors functionality provided by the gshell. 

"""
import cmd
import os
import pdb
import sys
# Local imports
#import sspy


def parse(arg):
    """

    Borrowed from the Python.org Turtle Shell example
    
    Convert a series of zero or more numbers to an argument tuple
    """
    return tuple(map(int, arg.split()))


class GShell(cmd.Cmd):
    """!

    
    """

    def __init__(self, scheduler=None,
                 intro='Welcome to the GENESIS 3 shell. Type help or ? to list commands.\n',
                 prompt='genesis3> ',
                 verbose=False):
        """

        @param scheduler The sspy schedule object to wrap around
        @param intro The intro text to use when starting the shell
        @param prompt The text for the command line prompt.
        """

        cmd.Cmd.__init__(self)

        # This is just an import test of readline to warn the user
        # so they know that autocompletion will not work if this is not
        # found
        try:

            import readline

        except ImportError:

            print "The readline module for python is not installed, autocompletion will not work."

        self.verbose = verbose

        self.intro = intro
        self.prompt = prompt

        self.histfile = None
        
        self._scheduler = scheduler

#---------------------------------------------------------------------------
#----                           Commands                              ------
#---------------------------------------------------------------------------


#---------------------------------------------------------------------------
# hello (template)

    def do_hello(self, arg):
        print "hello again", arg, "!"

    # using these as templates

    def help_hello(self):
        print "syntax: hello [message]",
        print "-- prints a hello message"

#---------------------------------------------------------------------------
# version

    def do_version(self, arg):
        
        print "%s (%s)" % (self._scheduler.GetVersion(), self._scheduler.GetRevisionInfo())

    def help_version(self):
        print "syntax: version",
        print "-- prints the version"

#---------------------------------------------------------------------------
# quit
    def do_quit(self, arg):
        sys.exit(1)


    def help_quit(self):
        print "syntax: quit",
        print "-- terminates the application"

#---------------------------------------------------------------------------
# shell
    def do_shell(self, arg):
        "Run a shell command"
        print "running shell command:", line
        output = os.popen(arg).read()
        print output

    def help_shell(self):
        print "syntax: shell [command]",
        print "-- Executes a shell command"


#---------------------------------------------------------------------------
# input_add
    def do_input_add(self, arg):
        "Run a shell command"
        print "Input add %s" % arg

    def help_input_add(self):
        print "syntax: input_add [input]",
        print "-- Adds an input"
        
#---------------------------------------------------------------------------
# hello (template)

    def do_hello(self, arg):
        print "hello again", arg, "!"

    # using these as templates

    def help_hello(self):
        print "syntax: hello [message]",
        print "-- prints a hello message"
        
#---------------------------------------------------------------------------
#----                       End Commands                              ------
#---------------------------------------------------------------------------



#---------------------------------------------------------------------------
#----                           Shortcuts                               ----
#---------------------------------------------------------------------------

    do_q = do_quit
    

#---------------------------------------------------------------------------
#----                       End Shortcuts                               ----
#---------------------------------------------------------------------------




if __name__ == '__main__':
    GShell().cmdloop()
