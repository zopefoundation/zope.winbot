==================
winbot maintenance
==================

I'm not the one who set winbot up, so this document is likely to be incomplete
or incorrect.

There's some extremely terse documentation about winbot's original setup
at http://docs.zope.org/zopetoolkit/process/winbotsetup.html


Connecting over RDP
-------------------

On a Linux machine you can use ::

    rdesktop -k en-us -g 1024x700 -u yourusername -p - winbot.zope.org

to connect (assuming you've got an account there, obviously).


Debugging failing builds
------------------------

You can find the project working trees in c:\\buildslave.  E.g. to run
zope.viewlet's tests with pdb, do this:

1. Open "Git Bash"
2. ``cd /c/buildslave/zope.viewlet/build``
3. ``bin/test --pdb``


Updating buildbot configuration
-------------------------------

After you commit any changes to this repository on GitHub, you have to go and
update buildbot's checked out copies by hand.

I haven't been able to figure out how yet.  The buildmaster directory appears
to be c:\\buildmaster, and it has all the \*.cfg files in it, but it is not a
git checkout.  This repository is checked out in c:\\1\\zope.winbot and seems
to be reasonably up-to-date (but not current).  I can run ``git pull`` in it.

Do I really have to copy the c:\\1\\zope.winbot\\buildmaster\\\*.cfg files
manually to c:\\buildmaster\\?

Buildbot itself is running as a Windows service "BuildBot", using the
"buildbot" user account.


Windows updates
---------------

These are done manually for some reason.  Don't forget to rdesktop in every
Tuesday and click the buttons!
