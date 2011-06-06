#! /usr/bin/env python
"""

This script had an IO error when performing a
Heccer Dump. The gdb traces reveals it gets stuck
with 0% CPU activity when run in verbose mode. This
stall does not seem to always happen.

GDB stack:

(gdb) where
#0  0xb7f49430 in __kernel_vsyscall ()
#1  0xb7e49583 in write () from /lib/tls/i686/cmov/libc.so.6
#2  0xb7de2b9c in _IO_file_write () from /lib/tls/i686/cmov/libc.so.6
#3  0xb7de3d17 in _IO_do_write () from /lib/tls/i686/cmov/libc.so.6
#4  0xb7de36f0 in _IO_file_overflow () from /lib/tls/i686/cmov/libc.so.6
#5  0xb7de2805 in _IO_file_xsputn () from /lib/tls/i686/cmov/libc.so.6
#6  0xb7db80b3 in vfprintf () from /lib/tls/i686/cmov/libc.so.6
#7  0xb7e702d7 in __fprintf_chk () from /lib/tls/i686/cmov/libc.so.6
#8  0xb7833f31 in HeccerVMDump (pvm=0x9a257e8, pfile=0xb7ed24c0, iSelection=6225920) at /usr/include/bits/stdio2.h:98
#9  0xb7827264 in HeccerDump (pheccer=0x99c2a10, pfile=0xb7ed24c0, iSelection=6225920) at heccer.c:567
#10 0xb77fac64 in _wrap_HeccerDump (self=0x0, args=0x997f39c) at ./heccer_wrap.c:9072
#11 0x080cea39 in PyEval_EvalFrameEx ()
#12 0x080cfbf5 in PyEval_EvalFrameEx ()
#13 0x080cfbf5 in PyEval_EvalFrameEx ()
#14 0x080cfbf5 in PyEval_EvalFrameEx ()
#15 0x080cfbf5 in PyEval_EvalFrameEx ()
#16 0x080d0345 in PyEval_EvalCodeEx ()
#17 0x080ce728 in PyEval_EvalFrameEx ()
#18 0x080d0345 in PyEval_EvalCodeEx ()
#19 0x080d0557 in PyEval_EvalCode ()
#20 0x080edf8f in PyRun_FileExFlags ()
#21 0x080ee25a in PyRun_SimpleFileExFlags ()
#22 0x080595e7 in Py_Main ()
#23 0x08058962 in main ()


"""
import pdb
import os

from test_library import add_sspy_path

add_sspy_path()

from sspy import SSPy 


scheduler = SSPy()

try:
    
    scheduler.Load("./yaml/purk_test_segment.yml")

except Exception, e:

    print "Error while loading schedule file: %s" % e



scheduler.Run()


print "Done!"
