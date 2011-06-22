"""!

An interactive shell for use with the sspy scheduler.
Mirrors functionality provided by the gshell. 

"""
import cmd
import os
import pdb
import re
import shlex # for more complex string splitting
import sys


# Local imports
from interface import SSPYInterface





class SSPyShell(cmd.Cmd):
    """!

    
    """

    def __init__(self, scheduler=None,
                 intro='Welcome to the SSPy shell. Type help or ? to list commands.\n',
                 prompt='sspy> ',
                 verbose=True):
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

        # some internal cached lists for auto completion
        self._element_list = []
        self._library_list = []

        self._scheduler = scheduler


        # Set up the library list via the default ndf library path
        # should probably iterate through the env variables
        if len(self._library_list) == 0:

            path = os.path.join('/',
                           'usr',
                           'local',
                           'neurospaces',
                           'models',
                           'library'
                           )
            
            self._library_list = self._get_ndf_library_list(path,
                                                            ['.ndf'])


#---------------------------------------------------------------------------
# All shell helper methods should be private
#---------------------------------------------------------------------------

    def _get_ndf_library_list(self, path, ext):
        """!

        """
        files = []
        
        for dirpath, dirnames, filenames in os.walk(path):

            for f in filenames:

                head, tail = os.path.splitext(f)

                if tail in ext:

                    this_file = os.path.join(dirpath, f)

                    # first remove the path part since the model
                    # container doesn't need it.
                    if this_file.startswith(path):
                        
                        this_file = this_file.replace(path, '')

                        this_file = this_file.lstrip(os.sep)

                    files.append(this_file)

        return files

#---------------------------------------------------------------------------

    def _get_completions(self, token, text='', items=[]):

        if token == '':

            return []
        
        offs = len(token) - len(text)

        completions = [ f[offs:] for f in items
                        if f.startswith(token)

                        ]

        return completions
        
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
#----                           Commands                              ------
#---------------------------------------------------------------------------

    def do_EOF(self, arg):
        return True

    def help_EOF(self, arg):

        print "Just processes an empty line"
        
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
        
        version = self._scheduler.Version()

        print "%s" % version
        
    def help_version(self):
        print "usage: version",
        print "-- prints the version"

#---------------------------------------------------------------------------
# quit
    def do_quit(self, arg):
        
        self._scheduler = None

        sys.exit(1)


    def help_quit(self):
        print "usage: quit",
        print "-- terminates the application"

#---------------------------------------------------------------------------
# shell
    def do_shell(self, arg):
        """Run a shell command"""
        print "running shell command:", arg
        output = os.popen(arg).read()
        print output
        
    def help_shell(self):
        print "usage: shell [command]",
        print "-- Executes a shell command"


#---------------------------------------------------------------------------
# input_add
    def do_input_add(self, arg):
        """Add an input"""
        print "Input add %s" % arg

    def help_input_add(self):
        print "usage: input_add [input]",
        print "-- Adds an input"

    def complete_input_add(self, text, line, begidx, endidx):

        tokens = line.split()

        trailing_space = False

        try:
            
            trailing_space = line[-1].isspace()

        except IndexError:

            pass

        
        if len(tokens) == 1:

            completions = self._element_list[:]
            
        elif len(tokens) == 2 and not trailing_space:
        # Here we autocomplete the ndf file
        
            completions = self._get_completions(tokens[1], text, self._element_list)

        else:

            return []

        return completions


#---------------------------------------------------------------------------
# output_add
    def do_output_add(self, arg):
        """Add an input"""
        print "Input add %s" % arg

    def help_output_add(self):
        print "usage: output_add <output name> [element name] [parameter]",
        print "-- Adds an output"

    def complete_output_add(self, text, line, begidx, endidx):

        tokens = line.split()

        trailing_space = False

        try:
            
            trailing_space = line[-1].isspace()

        except IndexError:

            pass

        
        if len(tokens) == 1:

            completions = self._element_list[:]
            
        elif len(tokens) == 2 and not trailing_space:
        # Here we autocomplete the ndf file
        
            completions = self._get_completions(tokens[1], text, self._element_list)

        else:

            return []

        return completions
    
#---------------------------------------------------------------------------
# run

    def do_run(self, arg):
        """Runs a loaded schedule """

        args = arg.split()

        time = None
        steps = None
        modelname = None
        
        num_args = len(args)
        
        if num_args > 2 or num_args == 0:

            self.help_run()

            return

        if num_args == 1:

            try:
                
                time = float(arg[0])

            except ValueError, e:

                print "Invalid simulation time: %s" % args[0]

                return

        elif num_args == 2:

            modelname = args[0]

            self.SetModelName(modelname)
            
            try:
                
                time = float(args[1])

            except ValueError, e:

                print "Invalid simulation time: %s" % args[0]

                return
            
        try:

            self._scheduler.Run(time=time)

        except Exception, e:

            print "%s" % e
        
        
    def help_run(self):

        print "usage: run [modelname] [time or steps] value",
        print "-- runs a simulation\n"
        print ""


#---------------------------------------------------------------------------
# list_solver_plugins

    def do_list_solver_plugins(self, arg):

        verbose = False
        
        if arg == 'verbose' or arg == 'v':

            verbose = True
            
        self._scheduler.ListSolverPlugins(verbose)
        
    # using these as templates
    def help_list_solver_plugins(self):
        print "usage: list_solver_plugins [v, verbose]",
        print "-- Lists the registered solver plugins"


#---------------------------------------------------------------------------
# list_service_plugins

    def do_list_service_plugins(self, arg):

        verbose = False
        
        if arg == 'verbose' or arg == 'v':

            verbose = True

        self._scheduler.ListServicePlugins(verbose)

    def help_list_service_plugins(self):
        print "usage: list_service_plugins [v, verbose]",
        print "-- Lists the registered service plugins"


#---------------------------------------------------------------------------
# list_output_plugins

    def do_list_output_plugins(self, arg):

        verbose = False
        
        if arg == 'verbose' or arg == 'v':

            verbose = True
            
        self._scheduler.ListOutputPlugins(verbose)

    def help_list_output_plugins(self):
        print "usage: list_output_plugins [v, verbose]",
        print "-- Lists the registered output plugins"


#---------------------------------------------------------------------------
# list_input_plugins

    def do_list_input_plugins(self, arg):

        verbose = False
        
        if arg == 'verbose' or arg == 'v':

            verbose = True

        self._scheduler.ListInputPlugins(verbose)

    def help_list_input_plugins(self):
        print "usage: list_input_plugins [v, verbose]",
        print "-- Lists the registered input plugins"


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
# create_service
    def do_create_service(self, arg):

        print "Not implemented yet"

    def help_create_service(self):
        print "usage: create_service [type] [name]",
        print "-- Creates a new service"

#---------------------------------------------------------------------------
# create_model_container
    def do_create_model_container(self, arg):

        if arg is None or arg == "":

            print "Need a name for the new model container"
            
        try:
            
            self._scheduler.CreateService(name=arg,
                                          type="model_container",
                                          verbose=True)

        except Exception, e:

            print e
            
    def help_create_model_container(self):
        print "usage: create_model_container [name]",
        print "-- Creates a new model container"
        
        print """
This command will create a service object via the default
model container plugin.
"""

#---------------------------------------------------------------------------
# create_output
    def do_create_output(self, arg):

        if arg is None or arg == "":

            self.help_create_output()

            return

        try:
            
            tokens = shlex.split(arg)
        except ValueError, e:

            print "Error: %s" % e

            return
        
        if len(tokens) > 2:

            self.help_create_output()

            return


        output_name = tokens[0]

        output_file = None
        
        try:

            output_file = tokens[1]
            
        except IndexError:

            output_file = None

        
        try:
            
            this_output = self._scheduler.CreateOutput(name=output_name,
                                                       type="double_2_ascii",
                                                       verbose=True)

            if not output_file is None:
                
                this_output.SetFilename(output_file)
            
        except Exception, e:

            print e
            
    def help_create_output(self):
        print "usage: create_output [name] [file]",
        print "-- Creates a new double_2_ascii output object"
        
        print """
Currently creates a double_2_ascii object as a default. 
"""

#---------------------------------------------------------------------------
# create
    def do_create(self, arg):
        print "create a compartment"

    def help_create(self):
        print "usage: create [type] [element name]",
        print "-- create a compartment element in the current service"

#---------------------------------------------------------------------------
# create_solver
    def do_create_solver(self, arg):
        print "create a solver, not working yet"

    def help_create_solver(self):
        print "usage: create_solver [type] [solver name]",
        print "-- create a solver"
        print """
Creates a solver of the indicated type with the given name.
        """

#---------------------------------------------------------------------------
# create_solver_heccer
    def do_create_solver_heccer(self, arg):

        if arg is None or arg == "":

            print "Need a name for the new model container"
            
        try:
            
            my_heccer = self._scheduler.CreateSolver(arg, 'heccer', verbose=True)

        except Exception, e:

            print e
        
    def help_create_solver_heccer(self):
        print "usage: create_solver [type] [solver name]",
        print "-- create a heccer solver"
        print """
Creates a heccer solver with the given name with default arguments.
        """

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

        self._scheduler.load_input(arg)

    def help_inputclass_add(self):
        print "usage: inputclass_add [input plugin file or directory]",
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

        for e in self._element_list:

            if not arg is None or arg != "":

                if e.startswith(arg):

                    print "%s" % e

            else:
                
                print "%s" % e


    def help_list_elements(self):
        print "usage: list_elements [element name]",
        print "-- List all accessible elements in the loaded service."
        print """

If given no arguments it will print out all elements from the given
model. Passing an element path as an argument will cause the function
to print only elements that are prefixed by the argument.

Autocompletion is available to use for autocompleting an element path
argument.

        """



    def complete_list_elements(self, text, line, start_index, end_index):

        tokens = line.split()

        if len(tokens) == 1:

            completions = self._element_list[:]
            
        elif len(tokens) == 2:
        # Here we autocomplete an element
        
            completions = self._get_completions(tokens[1], text, self._element_list)

        else:

            return []

        return completions
    
#---------------------------------------------------------------------------
# model_parameter_add
    def do_model_parameter_add(self, arg):

        if arg is None or arg == "":

            self.help_model_parameter_add()

            return

        tokens = arg.split()

        if len(tokens) != 3:

            self.help_model_parameter_add()

            return

        else:

            path = tokens[0]
            parameter = tokens[1]
            value = tokens[2]

            try:

                self._scheduler.SetParameter(path, parameter, value)

            except Exception, e:

                print e

                return


    def help_model_parameter_add(self):
        print "usage: model_parameter_add [element name] [parameter] [value]",
        print "-- Sets a model parameter."

    def complete_model_parameter_add(self, text, line, start_index, end_index):

        if line is None or line == "":

            self.help_model_parameter_add()

            return

        tokens = line.split()

        trailing_space = False

        try:
            
            trailing_space = line[-1].isspace()

        except IndexError:

            pass
        
        if len(tokens) == 1:

            completions = self._element_list[:]
            
        elif len(tokens) == 2 and not trailing_space:
        
            completions = self._get_completions(tokens[1], text, self._element_list)

        else:

            return []

        return completions

#---------------------------------------------------------------------------
# model_parameter_show
    def do_model_parameter_show(self, arg):
        print "Shows all parameters for a model element."


    def help_model_parameter_show(self):
        print "usage: model_parameter_show [element name]",
        print "-- Shows all parameters for a model element."


#---------------------------------------------------------------------------
# model_state_load
    def do_model_state_load(self, arg):
        print "Load a model state"


    def help_model_state_load(self):
        print "usage: model_state_load [model state file]",
        print "-- Load a model and its state from a file."


#---------------------------------------------------------------------------
# model_state_save
    def do_model_state_save(self, arg):
        print "Save a model state"


    def help_model_state_save(self):
        print "usage: model_state_save [model state file]",
        print "-- Save a model and its state to a file."


#---------------------------------------------------------------------------
# morphology_list_spine_heads
    def do_morphology_list_spine_heads(self, arg):
        print "Lists all spine heads in a morphology"


    def help_morphology_list_spine_heads(self):
        print "usage: morphology_list_spine_heads",
        print "-- Lists all spine heads in a morphology."


#---------------------------------------------------------------------------
# morphology_summarize
    def do_morphology_summarize(self, arg):
        print "Summarizes info about a morphology"


    def help_morphology_summarize(self):
        print "usage: morphology_summarize",
        print "-- Outputs a summary of the morphology of the model in the",
        print "loaded service"


#---------------------------------------------------------------------------
# ndf_load
    def do_ndf_load(self, arg):

        if arg == "" or arg is None:

            self.help_ndf_load()

            return

        
        services = self._scheduler.GetLoadedServices()


        this_model_container = None
        
        if len(services) == 0:

            try:
                
                this_model_container = self._scheduler.CreateService(type="model_container",
                                                                     verbose=True)

            except Exception, e:

                print e

                return
                
        else:

            this_model_container = services[0]
                        

        this_model_container.Load(arg)

        # Now we set a list of cached elements and
        # a list of model files from the library
        print "caching model elements"
        
        self._element_list = this_model_container.GetElements()

        return
        

    def help_ndf_load(self):
        print "usage: ndf_load [filename]",
        print "-- Loads an ndf file into all loaded model container services."
        print """
Loads an ndf file from the model container services model library. If a
model container has not been created it will create a default one with
the name 'model_container'.

        """
        
    def complete_ndf_load(self, text, line, start_index, end_index):

        tokens = line.split()

        trailing_space = False

        try:
            
            trailing_space = line[-1].isspace()

        except IndexError:

            pass

        
        if len(tokens) == 1:

            completions = self._library_list[:]
            
        elif len(tokens) == 2 and not trailing_space:
        # Here we autocomplete the ndf file
        
            completions = self._get_completions(tokens[1], text, self._library_list)

        else:

            return []

        return completions



#     def complete_add(self, text, line, begidx, endidx):
#         mline = line.partition(' ')[2]
#         offs = len(mline) - len(text)
#         return [s[offs:] for s in completions if s.startswith(mline)]


#     def complete_greet(self, text, line, begidx, endidx):
#         if not text:
#             completions = self.FRIENDS[:]
#         else:
#             completions = [ f
#                             for f in self.FRIENDS
#                             if f.startswith(text)
#                             ]
#         return completions
    


#---------------------------------------------------------------------------
# ndf_save
    def do_ndf_save(self, arg):
        print "Saves an ndf file"


    def help_ndf_save(self):
        print "usage: ndf_save [filename]",
        print "-- Save an ndf file from the model in the service."

#---------------------------------------------------------------------------
# npy_load
    def do_npy_load(self, arg):
        print "Loads an npy file into the appropriate service"


    def help_npy_load(self):
        print "usage: npy_load [filename]",
        print "-- Loads an npy file into a service."

#---------------------------------------------------------------------------
# service_query
    def do_service_query(self, arg):
        print "Adds a new output"


    def help_service_query(self):
        print "usage: service_query [name] [query command]",
        print "-- Sends a query command to the indicated service."


#---------------------------------------------------------------------------
# service_new
    def do_service_new(self, arg):
        print "Creates a service with default options"


    def help_service_new(self):
        print "usage: service_new [name]",
        print "-- Create a service with default options."

#---------------------------------------------------------------------------
# service_new
    def do_service_new(self, arg):
        print "Creates a service with default options"


    def help_service_new(self):
        print "usage: service_new [name]",
        print "-- Create a service with default options."


#---------------------------------------------------------------------------
# service_load
    def do_service_load(self, arg):
        print "Loads a service with default options"


    def help_service_load(self):
        print "usage: service_load [name]",
        print "-- Loads a service with default options."


#---------------------------------------------------------------------------
# service_show
    def do_service_show(self, arg):

        self._scheduler.ListLoadedServices(arg)

    def help_service_show(self):
        print "usage: service_show [v, verbose]",
        print "-- Lists all loaded serices."


#---------------------------------------------------------------------------
# solver_show
    def do_solver_show(self, arg):

        self._scheduler.ListLoadedSolvers(arg)

    def help_solver_show(self):
        print "usage: solver_show [v, verbose]",
        print "-- Lists all loaded solver."


#---------------------------------------------------------------------------
# input_show
    def do_input_show(self, arg):

        self._scheduler.ListLoadedInputs(arg)

    def help_input_show(self):
        print "usage: input_show [v, verbose]",
        print "-- Lists all loaded inputs."


#---------------------------------------------------------------------------
# output_show
    def do_output_show(self, arg):

        self._scheduler.ListLoadedOutputs(arg)

    def help_output_show(self):
        print "usage: output_show [v, verbose]",
        print "-- Lists all loaded outputs."

#---------------------------------------------------------------------------
#----                           End Commands                          ------
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
