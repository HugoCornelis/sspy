"""!
@package launcher
@file launcher.py

@brief This program starts the command line process for sspy
"""
import getopt
import optparse
import os
import pdb
import sys


try:
    import yaml
except ImportError:
    sys.exit("Need PyYaml http://pyyaml.org/\n")


from __cbi__ import PackageInfo

_package_info = PackageInfo()


#---------------------------------------------------------------------------

def usage():

    print "usage: %s [OPTIONS]" % (sys.argv[0])

    print "\nStartup:"
    print " -v, --version\t\tcurrent version number."
    print " -h, --help\t\tprint this help."
    print " --shell\t\tStarts the interactive shell."
#    print " -b, --background\tgo to background after startup."

    print "\nScheduling:"
    print " --builtins\t\tgive help about supported builtin simulation configurations."
    print " --optimize\t\tturn on the schedule optimizer."
    print " --emit-output\t\tfiles to write to stdout after the simulation finishes."
    print " --emit-schedules\tprint schedules to stdout instead of running them."
    print " --model-directory\tname of the directory where to look for non-std models."
    print " --model-filename\tfilename of the model description file (when using a builtin configuration)."
    
    print "\nProtocol Options:"
    print " --perfectclamp\t\tset the command voltage for the perfect clamp protocol."
    print " --pulsegen-width1\tset the pulse width for the pulsegen protocol."
    sys.exit(2)

#---------------------------------------------------------------------------

from optparse import OptionParser

from sspy import SSPy

def main(cwd=os.getcwd()):


    try:
        path = os.path.dirname(__file__)
        os.chdir(path)
    except:
        pass

    usage = "%s [OPTIONS] <files>" % sys.argv[0]

    parser = OptionParser(usage)
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose",
                      help="show verbose output")

    parser.add_option("-s", "--shell", action="store_true", dest="shell",
                      help="starts the interactive shell")

    parser.add_option("-o", "--stdout", action="store_true", dest="stdout",
                      help="show verbose output")

    parser.add_option("-d", "--model-directory", dest="model_directory", type="string",
                      help="name of the directory where to look for non-std models")

    parser.add_option("-f", "--model-filename", dest="model_filename", type="string",
                      help="filename of the model description file (when using a builtin configuration).")

#     parser.add_option("-n", "--model-name", dest="model_name", type="string",
#                       help="Name of the model to start simulating.")

    (options, args) = parser.parse_args()
    
    #---------------------------------------------
    # This is simply to ensure that the invoking
    # directory is used for relative paths. 
    os.chdir(cwd)
    #---------------------------------------------

    shell = False
    stdout = False
    verbose = False
    more_verbose = False

    configuration = None
    model_directory = None
    model_filename = None
    model_name = None
    shell_batch_file = None

    
    if not parser.shell is None:
        
        shell = False

    if not parser.stdout is None:
        
        stdout = False

    if not parser.verbose is None:
        
        verbose = False
        
    if not parser.model_directory is None:
        
        model_directory = None

    if not parser.model_filename is None:
        
        model_filename = None

#     if not parser.model_name is None:
        
#         model_name = None

#     if not parser.shell_batch_file is None:
        
#         shell_batch_file = None


    for opt, arg in opts:

        if opt in ('-h', '--help'):

            usage()

        elif opt in ('--model-directory'):

            model_directory = arg
            
        elif opt in ('--model-filename'):

            model_filename = arg

        elif opt in ('--model-name'):

            model_name = arg

        elif opt in ('-V', '--version'):

            print "version %s (%s)" % (_package_info.GetVersion(), _package_info.GetRevisionInfo())

            sys.exit(0)

        elif opt in ('-v', '--verbose'):

            verbose = True

        elif opt in ('-vv', '--more-verbose'):

            verbose = True
            
        elif opt in ('--shell',):

            shell = True
            
        else:
            
            assert False, "unhandled option %s" % opt

    # here process the extra args at the tail end of the command
    if len(args) > 0:

        for a in args:

            if os.path.isfile( a ):

                configuration = a

                args.remove(a)

        if len(args) > 0:

            print "Unprocessed arguments: ",
        
            for a in args:

                print "%s " % a,

            print ""
        

    scheduler = SSPy(verbose=verbose)

    # Add in the parsed arguments via the top level
    # sspy api. This try exception block will kill
    # the program is any errors occur.
    try:

        if not configuration is None:

            scheduler.Load(configuration)

        

    except Exception, e:

        print e
        
        sys.exit(1)


    if shell:

        from sspy.shell import SSPyShell
        
        sspy_shell = SSPyShell(scheduler=scheduler)

        sspy_shell.cmdloop()

    else:
        
        # Running sspy after all options have been set
        
        scheduler.Run()
