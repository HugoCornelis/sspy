

# $Format: "AC_INIT(${package}, ${label}, ${email})"$
AC_INIT(sspy, python-2, rodrigueza14@uthscsa.edu)

dnl Obtain operating system information.
AC_CANONICAL_TARGET

AC_CONFIG_SRCDIR(./sspy)



# $Format: "AM_INIT_AUTOMAKE(${package}, ${label})"$
AM_INIT_AUTOMAKE(sspy, python-2)


dnl Check for Python
AM_PATH_PYTHON(,[],[
   echo "Python is not installed."
   exit -1
])


case $PYTHON_PREFIX in
  *)   
    PYTHON_PREFIX=`echo $PYTHON | sed -e "s,[[^/]]*$,,;s,/$,,;s,^$,.,"`
    PYTHON_PREFIX=`echo $PYTHON_PREFIX | sed -e "s,[[^/]]*$,,;s,/$,,;s,^$,.,"`
    PYTHONHOME=$PYTHON_PREFIX
    AC_SUBST(PYTHON_PREFIX)
    AC_SUBST(PYTHONHOME)

    AC_MSG_CHECKING([Python header location])
    PYTHON_HEADERS='$(PYTHON_PREFIX)/include/python$(PYTHON_VERSION)'
    AC_SUBST(PYTHON_HEADERS)
    AC_MSG_RESULT([$PYTHON_PREFIX/include/python$PYTHON_VERSION])

    PYTHON_EXE='$(PYTHON_PREFIX)/bin/python'
    AC_SUBST(PYTHON_EXE)
  ;;
esac




AC_PATH_PROGS(PERL, perl perl5)

AC_PATH_PROGS(DOXYGEN,doxygen,["NULL"])




AC_MSG_CHECKING([Checking OS])
AC_MSG_RESULT([Host is running $host_os.])
case "$host_os" in

  darwin*)

    

  ;;

  *) #default settings (Linux 2.6)

  ;;
esac



AC_OUTPUT(Makefile
)



