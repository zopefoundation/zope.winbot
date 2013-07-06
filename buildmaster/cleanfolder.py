# Delete everything reachable from the directory named in 'top',
# assuming there are no symbolic links.
# CAUTION:  This is dangerous!  For example, if top == '/', it
# could delete all your disk files.
import os
import sys
import stat

is_win32 = sys.platform == 'win32'

top = sys.argv[1]

for root, dirs, files in os.walk(top, topdown=False):
    for name in files:
        fname = os.path.join(root, name)
        if is_win32:
            os.chmod(fname, stat.S_IWRITE)
        try:
            os.remove(fname)
        except WindowsError:
            pass
        print "erase %s" % fname
    for name in dirs:
        dname = os.path.join(root, name)
        try:
            os.rmdir(dname)
        except WindowsError:
            pass
        print "rmdir %s" % dname
