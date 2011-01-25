

# $Format: "AC_INIT(${package}, ${label}, ${email})"$
AC_INIT(sspy, alpha, hugo.cornelis@gmail.com)

dnl Obtain operating system information.
AC_CANONICAL_TARGET

AC_CONFIG_SRCDIR(./sspy)



# $Format: "AM_INIT_AUTOMAKE(${package}, ${label})"$
AM_INIT_AUTOMAKE(sspy, alpha)


dnl Check for Python and it's headers
AM_PATH_PYTHON(,[],[
   echo "Python is not installed."
   exit -1
])

AC_MSG_CHECKING([Python prefix is ])
  AC_MSG_RESULT(['$PYTHON_PREFIX'])

dnl
dnl This is a forced fix to make sure a mac installation gets the proper
dnl python executable. Unless the macpython installer was run, the autotools
dnl python macro won't look for python in the proper path. 
dnl 
case "$host_os" in
  darwin*)

    PYTHON_PREFIX='/Library/Frameworks/Python.framework/Versions/Current'
    AC_SUBST(PYTHON_PREFIX)
    
    PYTHON=$PYTHON_PREFIX/bin/python
    AC_SUBST(PYTHON)

    AC_CHECK_PROG(HAVE_PYTHON_CONFIG, python-config, "yes", "no",[$PYTHON_PREFIX/bin])
    AC_MSG_CHECKING([python-config present])
    AC_MSG_RESULT([$HAVE_PYTHON_CONFIG])
  ;;
  *)

    AC_CHECK_PROG(HAVE_PYTHON_CONFIG, python-config, "yes", "no")
    AC_MSG_CHECKING([python-config present])
    AC_MSG_RESULT([$HAVE_PYTHON_CONFIG])

  ;;
esac


if test "$HAVE_PYTHON_CONFIG" == "yes"; then

  # This is to set the proper python-config for getting the 
  # proper flags and prefixes

  
  AC_MSG_CHECKING([Python config location])
  PYTHON_CONFIG=$PYTHON-config
  AC_SUBST(PYTHON_CONFIG)
  AC_MSG_RESULT([$PYTHON_CONFIG])


  AC_MSG_CHECKING([Python prefix is])
  PYTHON_PREFIX=`$PYTHON_CONFIG --prefix`
  AC_SUBST(PYTHON_PREFIX)
  AC_MSG_RESULT([$PYTHON_PREFIX])


  AC_MSG_CHECKING([Python includes are])
  PYTHON_INCLUDE=`$PYTHON_CONFIG --include`
  AC_SUBST(PYTHON_INCLUDE)
  AC_MSG_RESULT([$PYTHON_INCLUDE])


  AC_MSG_CHECKING([Python libs are])
  PYTHON_LIBS=`$PYTHON_CONFIG --libs`
  AC_SUBST(PYTHON_LIBS)
  AC_MSG_RESULT([$PYTHON_LIBS])


  AC_MSG_CHECKING([Python cflags are])
  PYTHON_CFLAGS=`$PYTHON_CONFIG --cflags`
  AC_SUBST(PYTHON_CFLAGS)
  AC_MSG_RESULT([$PYTHON_CFLAGS])


  AC_MSG_CHECKING([Python ldflags are])
  PYTHON_LDFLAGS=`$PYTHON_CONFIG --ldflags`
  AC_SUBST(PYTHON_LDFLAGS)
  AC_MSG_RESULT([$PYTHON_LDFLAGS])

  AC_MSG_CHECKING([Python executable is])
  PYTHON_EXE=$PYTHON_PREFIX/bin/python
  AC_SUBST(PYTHON_EXE)
  AC_MSG_RESULT([$PYTHON_EXE])


else

  # This is legacy to make sure that systems with python
  # that do not have python-config can get the python info
  # This has always been a bit error prone, particularly if the 
  # user has more than one python version installed.

  PYTHON_PREFIX=`echo $PYTHON | sed -e "s,[[^/]]*$,,;s,/$,,;s,^$,.,"`
  PYTHON_PREFIX=`echo $PYTHON_PREFIX | sed -e "s,[[^/]]*$,,;s,/$,,;s,^$,.,"`
  AC_SUBST(PYTHON_PREFIX)

  AC_MSG_CHECKING([Python prefix is])
  AC_MSG_RESULT([$PYTHON_PREFIX])

  PYTHON_HEADERS='$(PYTHON_PREFIX)/include/python$(PYTHON_VERSION)'
  AC_SUBST(PYTHON_HEADERS)

  AC_MSG_CHECKING([Python includes are])
  PYTHON_INCLUDE='-I$(PYTHON_HEADERS)'
  AC_SUBST(PYTHON_INCLUDE)
  AC_MSG_RESULT([$PYTHON_INCLUDE])

  AC_MSG_CHECKING([Python ldflags are])
  PYTHON_LIBS='-L$(pyexecdir)/../config'
  AC_SUBST(PYTHON_LIBS)
  AC_MSG_RESULT([$PYTHON_LIBS])
				
  PYTHON_EXE='$(PYTHON_PREFIX)/bin/python'
  AC_SUBST(PYTHON_EXE)
fi


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



