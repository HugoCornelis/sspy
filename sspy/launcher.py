"""!
@package launcher
@file launcher.py

@brief This program starts the command line process for sspy
"""
import getopt
import sys
import pdb


try:
    import yaml
except ImportError:
    sys.exit("Need PyYaml http://pyyaml.org/\n")

from __cbi__ import GetVersion
from __cbi__ import GetRevisionInfo


#---------------------------------------------------------------------------

def usage():

    print "usage: %s [OPTIONS]" % (sys.argv[0])

    print "\nStartup:"
    print " -v, --version\t\tcurrent version number."
    print " -h, --help\t\tprint this help."
    print " -b, --background\tgo to background after startup."

    print "\nScheduling:"
    print " --builtins\t\tgive help about supported builtin simulation configurations."
    print " --optimize\t\tturn on the schedule optimizer."
    print " --emit-output\t\tfiles to write to stdout after the simulation finishes."
    print " --emit-schedules\tprint schedules to stdout instead of running them."
    
    print "\nProtocol Options:"
    print " --perfectclamp\t\tset the command voltage for the perfect clamp protocol."
    print " --pulsegen-width1\tset the pulse width for the pulsegen protocol."
    sys.exit(2)

#---------------------------------------------------------------------------


from sspy import SSPy

def main():


    try:
        path = os.path.dirname(__file__)
        os.chdir(path)
    except:
        pass

    if len(sys.argv) < 2:

        usage()

    try:

        command_options = ["steps", "time", "time-step",
                           "version", "help", "background", "builtins", "optimize",
                           "emit-schedules", "emit-output",
                           "perfectclamp", "pulsegen-width1", "verbose"]

        opts, args = getopt.getopt(sys.argv[1:], ":hvV", command_options)
        
    except getopt.GetoptError, err:
        #print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()

        
    stdout = False
    verbose = False

    for opt, arg in opts:

        if opt in ('-V', '--version'):

            print "version %s (%s)" % (GetVersion(), GetRevisionInfo())

            sys.exit(0)

        elif opt in ('-v', '--vebose'):

            verbose = True


        elif opt in ('-h', '--help'):

            usage()
            
        else:
            
            assert False, "unhandled option %s" % opt


    scheduler = SSPy(verbose=verbose)

    print "Start sspy here"


