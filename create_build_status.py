#!python2.7
import os

COLUMNS = (
    ('t', 'Travis',
     'https://api.travis-ci.org/zopefoundation/%s.png?branch=master',
     'https://travis-ci.org/zopefoundation/%s'
     ),
    ('w26', 'Win 2.6',
     'http://winbot.zope.org/buildstatusimage?builder=%s_py_265_32&number=-1',
     'http://winbot.zope.org/builders/%s_py_265_32/builds/-1'
     )
)


def get_projects():
    prj_path = os.path.join(
        os.path.dirname(__file__), 'buildmaster', 'project-list.cfg')
    with open(prj_path, 'r') as file:
        projects = [line.split(',')[0]
                    for line in file
                    if line.strip() and not line.startswith('#')]
    return projects

def create_status_file(projects):
    links = []
    rows = []

    for idx, prj in enumerate(projects):
        row = [prj]
        for col in COLUMNS:
            name = '%s%i' %(col[0], idx)
            row.append('|%s|_' %name)
            links.append((name, col[2] %prj, col[3] %prj))
        rows.append(row)

    o  = '============\n'
    o += 'Build Status\n'
    o += '============\n'
    o += '\n'

    headers = [('Project Name', max(len(p) for p in projects))]
    headers += [(col[1], max([len(i[idx+1])+3 for i in rows]+[len(col[1])]))
                for idx, col in enumerate(COLUMNS)]

    #import pdb; pdb.set_trace()
    o += ' '.join(['='*w for t, w in headers]) + '\n'
    o += ' '.join([t+' '*(w-len(t)) for t, w in headers]) + '\n'
    o += ' '.join(['='*w for t, w in headers]) + '\n'

    for row in rows:
        o += ' '.join(
            [('%s' % t) +' '*(headers[i][1]-len(t))
             for i, t in enumerate(row)])
        o += '\n'

    o += ' '.join(['='*w for t, w in headers]) + '\n'
    o += '\n'

    for name, img, href in links:
        o += '.. |%s| image:: %s\n' %(name, img)
        o += '.. _%s: %s\n' %(name, href)
        o += '\n'

    with open('README.rst', 'w') as file:
        file.write(o)

def main():
    projects = get_projects()
    create_status_file(projects)

if __name__ == '__main__':
    main()
