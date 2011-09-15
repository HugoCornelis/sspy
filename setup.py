import imp
import os
import pdb
import re
import sys
from commands import getoutput

from distutils.core import setup
from distutils.command.install_data import install_data
#from setuptools import setup, find_packages

# This will work for both setuptools and distutils
# main difference is that if distutils is imported then
# the bdist_egg option is not available.
try:
    
    from setuptools import setup, find_packages, Extension

except ImportError:

    from distutils.core import setup
    from distutils.core import Extension
    
    def find_packages():

        return ['sspy']
    

# import the cbi module. We use this since the check
# for the compiled swig nmc_base gives an error
cbi = imp.load_source('__cbi__', os.path.join('genesis3', 'sspy', '__cbi__.py'))

_package_info = cbi.PackageInfo()

#-------------------------------------------------------------------------------

#
# This is borrowed from django's setup tools
# taken from here http://code.djangoproject.com/browser/django/trunk/setup.py
#
class osx_install_data(install_data):
    # On MacOS, the platform-specific lib dir is /System/Library/Framework/Python/.../
    # which is wrong. Python 2.5 supplied with MacOS 10.5 has an Apple-specific fix
    # for this in distutils.command.install_data#306. It fixes install_lib but not
    # install_data, which is why we roll our own install_data class.
	
    def finalize_options(self):
        # By the time finalize_options is called, install.install_lib is set to the
        # fixed directory, so we set the installdir to install_lib. The
        # install_data class uses ('install_data', 'install_dir') instead.
        self.set_undefined_options('install', ('install_lib', 'install_dir'))
        install_data.finalize_options(self)


#-------------------------------------------------------------------------------

"""
Function for reading in a file and outputting it as a string. 
"""
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#-------------------------------------------------------------------------------


# This is borrowed from django's setup tools
def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

#-------------------------------------------------------------------------------

def good_file(p):

    if p[0] == '.' or p[-1] == '~' or p[0] == '#' or p[-1] == '#':

        return False

    else:

        return True

#-------------------------------------------------------------------------------

"""
Returns a list of all files matching the given file types.
"""
_file_types = ['.py', '.yml']

def find_files(root_directory, file_types=_file_types):

    package_files = []

    for path, directories, files in os.walk( root_directory ):
        
        for f in files:
            
            path_parts = fullsplit( os.path.join(path, f) )

            path_parts.pop(0)

            this_file = '/'.join(path_parts)

            basename, extension = os.path.splitext( this_file )
            
            if extension in file_types:

                package_files.append(this_file)

    return package_files

#-------------------------------------------------------------------------------
NAME = _package_info.GetName()
VERSION = _package_info.GetVersion()
AUTHOR = cbi.__author__
AUTHOR_EMAIL = cbi.__email__
LICENSE = cbi.__license__
URL = "http://pypi.python.org/pypi/sspy"
DOWNLOAD_URL = "http://pypi.python.org/pypi/sspy"
DESCRIPTION="A pluggable scheduler for the GENESIS3 neurosimulator"
LONG_DESCRIPTION=cbi.__description__

KEYWORDS="neuroscience neurosimulator simulator modeling GENESIS"

# Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

PACKAGE_FILES=find_files('sspy')

OPTIONS={
    'sdist': {
        'formats': ['gztar','zip'],
        'force_manifest': True,
        },
    }

PLATFORMS=["Unix", "Lunix", "MacOS X"]


CMDCLASS = None
if sys.platform == "darwin": 
    CMDCLASS = {'install_data': osx_install_data} 
else: 
    CMDCLASS = {'install_data': install_data}

#-------------------------------------------------------------------------------
args = {}

args['name']=NAME
args['version']=VERSION
args['author']=AUTHOR
args['author_email']=AUTHOR_EMAIL
args['cmdclass']=CMDCLASS
args['description']=DESCRIPTION
args['long_description']=LONG_DESCRIPTION
args['license']=LICENSE
args['keywords']=KEYWORDS
args['url']=URL
args['packages']=['sspy']
args['package_data']={'sspy': PACKAGE_FILES }
args['classifiers']=CLASSIFIERS
args['options']=OPTIONS
args['platforms']=PLATFORMS
args['scripts']=['sspy.py']

setup(**args)

