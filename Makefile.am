SUBDIRS = \
	. 

EXTRA_DIST = \
	doxygen.cfg \
	docs	

#check_SCRIPTS = $(srcdir)/tests/neurospaces_harness

TESTS = /usr/local/bin/neurospaces_harness


all:
	echo "Nothing to build"


clean: clean-local
	$(RM) -f $(top_builddir)/sspy/*.pyc
#	$(RM) -rf $(top_builddir)/epydocs
#	$(RM) -rf $(top_builddir)/docs/html


clean-local:
	$(RM) -rf $(top_builddir)/docs/html

doxygen: doxygen.cfg
	$(DOXYGEN) doxygen.cfg

epydoc: epydoc.cfg
	epydoc --config epydoc.cfg

build-osx:
	$(PYTHON) dist/osx/setup.py py2app

test:
	neurospaces_harness
