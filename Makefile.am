SUBDIRS = \
	. 

EXTRA_DIST = \
	genesis3 \
	doxygen.cfg 

#check_SCRIPTS = $(srcdir)/tests/neurospaces_harness

TESTS = /usr/local/bin/neurospaces_harness


all:
	echo "Nothing to build"


clean: clean-local
#	$(RM) -f $(top_builddir)/sspy/*.pyc
#	$(RM) -rf $(top_builddir)/epydocs
#	$(RM) -rf $(top_builddir)/docs/html


clean-local:
	$(RM) -rf $(top_builddir)/docs/html
	$(RM) -rf $(top_srcdir)/tests/html
	$(RM) -f $(top_srcdir)/sspy-*.tar.gz
	echo "Removing all compiled byte code files"
	$(RM) `find . -name "*.pyc"`
	$(RM) -rf $(top_builddir)/build
	$(RM) -rf $(top_builddir)/dist/
	$(RM) -rf $(top_builddir)/html

dist-hook:
	echo "not needed"

epydoc: epydoc.cfg
	epydoc --config epydoc.cfg

build-osx:
	$(PYTHON) dist/osx/setup.py py2app



# Create a deb package
pkg-deb: dist
	echo "No deb built for this package"

# create an rpm package
pkg-rpm: dist
	echo "No rpm built for this package"



test:
	neurospaces_harness



html-upload-prepare:
	( cd tests && ./tests_2_html --introduction introduction.html )
	rm -fr html/htdocs/neurospaces_project/ssp/
	mkdir -p html/htdocs/neurospaces_project/ssp
	mkdir -p html/htdocs/neurospaces_project/ssp/html_source
	tar cfh - tests/html | ( cd html/htdocs/neurospaces_project/ssp && tar vxf - )

doxygen: doxygen.cfg
	$(DOXYGEN) doxygen.cfg

docs-level1:

docs-level2:

docs-level3: html-upload-prepare
	echo "Converted the regression tests to HTML"

docs-level4:

docs-level5:

docs-level6: doxygen
	echo "Doxygenized source code"

docs-level7:

docs: docs-level1 docs-level2 docs-level3 docs-level4 docs-level5 docs-level6 docs-level7
