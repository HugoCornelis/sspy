SUBDIRS = \
	. 

nobase_dist_python_DATA = \
	sspy/__cbi__.py	\
	sspy/__init__.py \
	sspy/analyzer.py \
	sspy/errors.py \
	sspy/launcher.py \
	sspy/launcher_old.py \
	sspy/plugin.py \
	sspy/plugins/inputs/perfectclamp/input.py \
	sspy/plugins/inputs/perfectclamp/input.yml \
	sspy/plugins/inputs/pulsegen/input.py \
	sspy/plugins/inputs/pulsegen/input.yml \
	sspy/plugins/outputs/line/output.py \
	sspy/plugins/outputs/line/output.yml \
	sspy/plugins/outputs/live_output/output.py \
	sspy/plugins/outputs/live_output/output.yml \
	sspy/plugins/outputs/output/output.py \
	sspy/plugins/outputs/output/output.yml \
	sspy/plugins/outputs/script_out/output.yml \
	sspy/plugins/outputs/script_out/script_output.py \
	sspy/plugins/services/heccer_intermediary/heccer_intermediary.py \
	sspy/plugins/services/heccer_intermediary/service.yml \
	sspy/plugins/services/nmc/service.py \
	sspy/plugins/services/nmc/service.yml \
	sspy/plugins/solvers/chemesis3/solver.py \
	sspy/plugins/solvers/chemesis3/solver.yml \
	sspy/plugins/solvers/heccer/solver.py \
	sspy/plugins/solvers/heccer/solver.yml \
	sspy/registry.py \
	sspy/save.py \
	sspy/schedulee.py \
	sspy/shell/__init__.py \
	sspy/shell/commands.yml \
	sspy/shell/interface.py \
	sspy/launcher_old.py

EXTRA_DIST = \
	bin/sspy \
	doxygen.cfg \
	clean.py \
	setup.py \
	uninstall.py

#check_SCRIPTS = $(srcdir)/tests/neurospaces_harness

TESTS = /usr/local/bin/neurospaces_harness

setup: setup.py
	echo "no op"
	$(PYTHON) setup.py build
	$(PYTHON) setup.py build_py

install-exec-hook:
	echo "no install"
	$(PYTHON) setup.py install

uninstall-hook:
#	echo "no uninstall"
	$(PYTHON) uninstall.py

all: setup


clean: clean-local


clean-local:
	$(RM) -rf $(top_builddir)/docs/html
	$(RM) -rf $(top_srcdir)/tests/html
	$(RM) -rf $(top_srcdir)/sspy-*.tar.gz
	$(RM) -rf $(top_srcdir)/sspy-*	
	echo "Removing all compiled byte code files"
	$(RM) `find . -name "*.pyc"`
	$(PYTHON) clean.py
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
