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
                 prompt='genesis3> '):
        """

        @param scheduler The sspy schedule object to wrap around
        @param intro The intro text to use when starting the shell
        @param prompt The text for the command line prompt.
        """

        cmd.Cmd.__init__(self)


        self.intro = intro
        self.prompt = prompt

        self.histfile = None
        
        self._scheduler = scheduler

#---------------------------------------------------------------------------
#----                           Commands                              ------
#---------------------------------------------------------------------------

    def do_hello(self, arg):
        print "hello again", arg, "!"
        pdb.set_trace()


    def help_hello(self):
        print "syntax: hello [message]",
        print "-- prints a hello message"


    def do_quit(self, arg):
        sys.exit(1)


    def help_quit(self):
        print "syntax: quit",
        print "-- terminates the application"


#---------------------------------------------------------------------------


    def do_shell(self, line):
        "Run a shell command"
        print "running shell command:", line
        output = os.popen(line).read()
        print output

    def help_shell(self):
        print "syntax: shell [command]",
        print "-- Executes a shell command"


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
