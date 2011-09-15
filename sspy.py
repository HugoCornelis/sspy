#! /usr/bin/env python
import os
import sys

try:
    
    from sspy.launcher import main

except ImportError, e:

    sys.exit(e)
    
main()

