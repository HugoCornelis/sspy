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


    def help_help(self):
        print "help"

#---------------------------------------------------------------------------
# hello (template)

    def do_hello(self, arg):
        print "hello again", arg, "!"

    # using these as templates
    def help_hello(self):
        print "usage: hello [message]",
        print "-- prints a hello message"

#---------------------------------------------------------------------------
# version

    def do_version(self, arg):
        
        print "%s (%s)" % (self._scheduler.GetVersion(), self._scheduler.GetRevisionInfo())

    def help_version(self):
        print "usage: version",
        print "-- prints the version"

#---------------------------------------------------------------------------
# quit
    def do_quit(self, arg):
        sys.exit(1)


    def help_quit(self):
        print "usage: quit",
        print "-- terminates the application"

#---------------------------------------------------------------------------
# shell
    def do_shell(self, arg):
        "Run a shell command"
        print "running shell command:", line
        output = os.popen(arg).read()
        print output

    def help_shell(self):
        print "usage: shell [command]",
        print "-- Executes a shell command"


#---------------------------------------------------------------------------
# input_add
    def do_input_add(self, arg):
        "Run a shell command"
        print "Input add %s" % arg

    def help_input_add(self):
        print "usage: input_add [input]",
        print "-- Adds an input"
        
#---------------------------------------------------------------------------
# run

    def do_run(self, arg):

        time = float(arg)
        
        try:
            
            sspy.Run(time)

        except Exception,e:

            print "%s" % e
            

    def help_run(self):
        print "usage: run [modelname] [time]",
        print "-- runs a simulation"
        
#---------------------------------------------------------------------------
#----                       End Commands                              ------
#---------------------------------------------------------------------------



#---------------------------------------------------------------------------
#----                    Gshell Commands                              ------
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
# ce 
    def do_ce(self, arg):
        print "change element not working yet"

    def help_ce(self):
        print "usage: ce [element name]",
        print "-- change the current element"



#---------------------------------------------------------------------------
# check
    def do_check(self, arg):
        print "check the model"

    def help_check(self):
        print "usage: check [model name]",
        print "-- check the model simulation status"


#---------------------------------------------------------------------------
# component_load
    def do_component_load(self, arg):
        print "component load doesn't work yet"

    def help_component_load(self):
        print "usage: component_load [component name]",
        print "-- Loads a component"



#---------------------------------------------------------------------------
# create
    def do_create(self, arg):
        print "create a compartment"

    def help_create(self):
        print "usage: create [type] [element name]",
        print "-- create a compartment element in the current service"



#---------------------------------------------------------------------------
# delete
    def do_delete(self, arg):
        print "delete a compartment"

    def help_delete(self):
        print "usage: delete [element name]",
        print "-- delete a compartment element in the current service"



#---------------------------------------------------------------------------
# echo
    def do_echo(self, arg):
        print "%s" % arg

    def help_echo(self):
        print "usage: echo [text]",
        print "-- echo some text given on the command line"

#---------------------------------------------------------------------------
# exit
    def do_exit(self, arg):
        sys.exit(1)


    def help_exit(self):
        print "usage: exit",
        print "-- terminates the application"

#---------------------------------------------------------------------------
# explore
    def do_explore(self, arg):
        print ""


    def help_explore(self):
        print "usage: explore",
        print "-- Displays the morphology from the model loaded in the service"


#---------------------------------------------------------------------------
# heccer_set_timestep
    def do_heccer_set_timestep(self, arg):
        print "Sets the heccer timestep"


    def help_heccer_set_timestep(self):
        print "usage: heccer_set_timestep [timestep value]",
        print "-- Sets the timestep for the heccer solver"

#---------------------------------------------------------------------------
# input_add
    def do_input_add(self, arg):
        print "Adds an input to a compiled solver"


    def help_input_add(self):
        print "usage: input_add [input protocol type] [element name] [parameter]",
        print "-- Adds an input of the given protocol type to the path",
        print "   in elment name with the given parameter."


#---------------------------------------------------------------------------
# input_delete
    def do_input_delete(self, arg):
        print "Deletes an input"


    def help_input_delete(self):
        print "usage: input_delete [element name]",
        print "-- Deletes an input"

#---------------------------------------------------------------------------
# input_show
    def do_input_show(self, arg):
        print "Shows all inputs"


    def help_input_show(self):
        print "usage: input_show",
        print "-- Shows all loaded inputs"


#---------------------------------------------------------------------------
# inputclass_add
    def do_inputclass_add(self, arg):
        print "Add an input plugin"


    def help_inputclass_add(self):
        print "usage: inputclass_add [input plugin]",
        print "-- Adds an input plugin to the input registry."


#---------------------------------------------------------------------------
# inputclass_delete
    def do_inputclass_delete(self, arg):
        print "Delete an input plugin"


    def help_inputclass_delete(self):
        print "usage: inputclass_delete [input plugin]",
        print "-- Deletes an input plugin from the input registry."

#---------------------------------------------------------------------------
# inputclass_show
    def do_inputclass_show(self, arg):
        print "Show all loaded inputs"


    def help_inputclass_show(self):
        print "usage: inputclass_show",
        print "-- Show all loaded input plugins."


#---------------------------------------------------------------------------
# inputclass_template_show
    def do_inputclass_template_show(self, arg):
        print "Show all registered input plugins"


    def help_inputclass_template_show(self):
        print "usage: inputclass_template_show",
        print "-- Show all registered input plugins."


#---------------------------------------------------------------------------
# library_show
    def do_library_show(self, arg):
        print "Shows the library on all paths"


    def help_library_show(self):
        print "usage: library_show [sub directory]",
        print "-- Show the model library."

#---------------------------------------------------------------------------
# list
    def do_list(self, arg):
        print "list available items"


    def help_list(self):
        print "usage: list [type]",
        print "-- Lists all available items or items of a partiular type"
        print "   must be one of commands, components, documentation, functions, "
        print "   inputclass_templates, inputclasses, physical, section, structure, verbose"


#---------------------------------------------------------------------------
# list_elements
    def do_list_elements(self, arg):
        print "Lists all elements in the loaded service"


    def help_list_elements(self):
        print "usage: list_elements [element name, wildcard]",
        print "-- List all elements in the loaded service."


#---------------------------------------------------------------------------
# model_parameter_add
    def do_model_parameter_add(self, arg):
        print "Sets a model parameter"


    def help_model_parameter_add(self):
        print "usage: model_parameter_add [element name] [parameter] [value]",
        print "-- Sets a model parameter."


#---------------------------------------------------------------------------
# model_parameter_show
    def do_model_parameter_show(self, arg):
        print "Shows all parameters for a model element."


    def help_model_parameter_show(self):
        print "usage: model_parameter_show [element name]",
        print "-- Shows all parameters for a model element."



#---------------------------------------------------------------------------
#----                    End Gshell Commands                          ------
#---------------------------------------------------------------------------


#---------------------------------------------------------------------------
#----                           Shortcuts                               ----
#---------------------------------------------------------------------------

    do_q = do_quit
    help_q = help_quit
    

#---------------------------------------------------------------------------
#----                       End Shortcuts                               ----
#---------------------------------------------------------------------------




if __name__ == '__main__':
    GShell().cmdloop()
