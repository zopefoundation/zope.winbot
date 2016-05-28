# collect supported python versions for project-list.cfg

# first parameter must be a PATH to a local checkout of all projects
# handy helper: https://github.com/mgedmin/cloneall

import os
import re
import sys

localCheckouts = sys.argv[1]

platforms = ('2.7', '3.3', '3.4', '3.5')

projects = open("project-list.cfg", "rb").readlines()
projects = [x.strip() for x in projects]

output = []

for project in projects:
    if not project or project.startswith('#'):
        output.append(project)
        continue  # comment or empty line

    parts = project.split(',')
    projectName = repourl = versions = opts = ''
    if len(parts) == 4:
        projectName, repourl, versions, opts = parts
    elif len(parts) == 3:
        projectName, repourl, versions = parts
    elif len(parts) == 2:
        projectName, repourl = parts
    else:
        print "Failed on line %s, ignoring", project
        continue
    project = project.strip()
    repourl = repourl.strip()

    localPath = os.path.join(localCheckouts, projectName)
    if os.path.exists(localPath):
        setuppy = os.path.join(localPath, 'setup.py')
        if os.path.exists(setuppy):
            content = open(setuppy, "rb").read()
            versions = []
            # this is damn ugly, but does the job
            for m in re.finditer(r"Programming Language :: Python :: (\d.\d)",
                                 content):
                ver = m.group(1)
                if ver in platforms:
                    versions.append(ver)
            version = ';'.join(versions)
    line = "%s,%s,%s,%s" % (projectName, repourl, version, opts)
    output.append(line)

open("project-list.cfg", "wb").write("\n".join(output))
