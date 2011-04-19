import os
from distutils.core import setup

import sspy.__cbi__ as cbi

NAME = cbi.GetPackageName()
VERSION = cbi.GetVersion()

AUTHOR = cbi.__author__
AUTHOR_EMAIL = cbi.__email__
LICENSE = cbi.__license__
URL = cbi.__url__
DOWNLOAD_URL = cbi.__download_url__

DESCRIPTION=""

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



OPTIONS={
    'sdist': {
        'formats': ['gztar','zip'],
        'force_manifest': True,
        },
        
    }

PY_MODULES=['sspy']

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
 
setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    keywords=KEYWORDS,
    url=URL,
    packages=['g3.sspy'],
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    options=OPTIONS,
    py_modules=PY_MODULES,
    setup_requires=[],
)

