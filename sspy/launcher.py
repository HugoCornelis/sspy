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


def main():


    try:
        path = os.path.dirname(__file__)
        os.chdir(path)
    except:
        pass

    try:

        command_options = ["version", "help", "background", "builtins", "optimize",
                           "emit-schedules", "emit-output",
                           "perfectclamp", "pulsegen-width1"]

        opts, args = getopt.getopt(sys.argv[1:], ":hv", command_options)
        
    except getopt.GetoptError, err:
        #print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()

        
    stdout = False

    for opt, arg in opts:

        if opt in ('-v', '--version'):

            print "version 0.1"


        elif opt in ('-h', '--help'):

            usage()
            
        else:
            
            assert False, "unhandled option %s" % opt


    print "Start sspy here"


