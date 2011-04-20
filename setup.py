import os
import pdb
import sys
from distutils.core import setup
from distutils.command.install_data import install_data
import sspy.__cbi__ as cbi


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

# def fullsplit(path, result=None):
#     """
#     Split a pathname into components (the opposite of os.path.join) in a
#     platform-neutral way.
#     """
#     if result is None:
#         result = []
#     head, tail = os.path.split(path)
#     if head == '':
#         return [tail] + result
#     if head == path:
#         return result
#     return fullsplit(head, [tail] + result)

# django_dir = 'sspy'
# packages = []
# data_files = []
# for dirpath, dirnames, filenames in os.walk(django_dir):
#     for i, dirname in enumerate(dirnames):
#         if dirname.startswith('.'): del dirnames[i]

#         if '__init__.py' in filenames:
#             packages.append('.'.join(fullsplit(dirpath)))
#         elif filenames:
#             data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])


#-------------------------------------------------------------------------------


"""
Returns a list of all files matching the given file types.
"""
_file_types = ['.py', '.yml']

def find_files(root_directory, file_types=_file_types):

    package_files = []

    for path, directories, files in os.walk( root_directory ):

        for f in files:

            this_file = os.path.join(path, f)

            basename, extension = os.path.splitext( this_file )
            if extension in file_types:

                package_files.append(this_file)

    return package_files

#-------------------------------------------------------------------------------

def find_data_files(root_directory, file_types=_file_types):


    package_files = []

    for path, directories, files in os.walk( root_directory ):

        for f in files:

            this_file = os.path.join(path, f)

            basename, extension = os.path.splitext( this_file )
            if extension in file_types:

                package_files.append(this_file)

    return package_files



DATA_FILES=[('sspy/plugins',[]),
            ('sspy/plugins/inputs',[]),
            ('sspy/plugins/inputs/perfectclamp', ['input.py', 'input.yml']),
            ]
#pdb.set_trace()

#myfiles = find_files('sspy')
#-------------------------------------------------------------------------------
NAME = cbi.GetPackageName()
VERSION = cbi.GetVersion()
AUTHOR = cbi.__author__
AUTHOR_EMAIL = cbi.__email__
LICENSE = cbi.__license__
URL = cbi.__url__
DOWNLOAD_URL = cbi.__download_url__
DESCRIPTION="A pluggable scheduler for GENESIS"
LONG_DESCRIPTION=cbi.__description__

KEYWORDS="neuroscience neurosimulator simulator modeling GENESIS"

CLASSIFIERS = [
    'Development Status :: 0 - Alpha',
    'Environment :: Console',
    'Environment :: Desktop Application',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Developers',
    'Intended Audience :: Research',
    'Intended Audience :: Science',        
    'License :: OSI Approved :: GPL License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: Research :: Neuroscience',
]

DATA_FILES=[('sspy/plugins',[]),
            ('sspy/plugins/inputs',[]),
            ('sspy/plugins/inputs/perfectclamp', ['input.py', 'input.yml']),
            ]

OPTIONS={
    'sdist': {
        'formats': ['gztar','zip'],
        'force_manifest': True,
        },
    }

PLATFORMS=["Unix", "Lunix", "MacOS X"]

PY_MODULES=['sspy']

CMDCLASS = None

if sys.platform == "darwin": 
    CMDCLASS = {'install_data': osx_install_data} 
else: 
    CMDCLASS = {'install_data': install_data}


#-------------------------------------------------------------------------------

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    cmdclass=CMDCLASS,
    data_files=DATA_FILES,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    keywords=KEYWORDS,
    url=URL,
    packages=['sspy'],
#    package_data={'sspy' : DATA_FILES},
    package_dir={'sspy' : 'sspy'},
    classifiers=CLASSIFIERS,
    options=OPTIONS,
    platforms=PLATFORMS,
    py_modules=PY_MODULES,
)

