

# $Format: "AC_INIT(${package}, ${label}, ${email})"$
AC_INIT(sspy, alpha, hugo.cornelis@gmail.com)


AC_MSG_CHECKING(whether we build universal binaries.)
AC_ARG_WITH(universal,
[AS_HELP_STRING([--with-universal],
              [Build universal binaries on Mac OS X.])],
[ case "$val" in
  no)

    AC_MSG_RESULT(no)
    OSX_UNIVERSAL="no"

    ;;
  *)

    AC_MSG_RESULT(yes)
    OSX_UNIVERSAL="yes"

    ;;
  esac ],
  AC_MSG_RESULT(no)
  OSX_UNIVERSAL="no"
)
AC_SUBST(OSX_UNIVERSAL)


dnl Obtain operating system information.
AC_CANONICAL_TARGET

AC_CONFIG_SRCDIR(./sspy)



# $Format: "AM_INIT_AUTOMAKE(${package}, ${label})"$
AM_INIT_AUTOMAKE(sspy, alpha)

AC_PATH_PROGS(PERL, perl perl5)

AC_PATH_PROGS(DOXYGEN,doxygen,["NULL"])


dnl Check for Python and it's headers
AM_PATH_PYTHON(,[],[
   echo "Python is not installed."
   exit -1
])


AC_MSG_CHECKING([Checking OS])
AC_MSG_RESULT([Host is running $host_os.])
case "$host_os" in

  darwin*)

    

  ;;

  *) #default settings (Linux 2.6)

  ;;
esac



AC_CONFIG_FILES([Makefile
])

AC_OUTPUT




