#!/usr/bin/env python

import os
from setuptools import setup



if __name__ == '__main__':

    dirName = os.path.dirname(__file__)
    if dirName and os.getcwd() != dirName:
        os.chdir(dirName)

    SHORT_DESCRIPTION = 'A tool which reads input from stdin and converts it to a JIRA table'

    try:
        with open('README.rst', 'rt') as f:
            long_description = f.read()
    except:
        long_description = SHORT_DESCRIPTION


    setup(name='toJiraTable',
            version='1.1.0',
            scripts=['toJiraTable'],
            author='Tim Savannah',
            author_email='kata198@gmail.com',
            maintainer='Tim Savannah',
            url='https://github.com/kata198/toJiraTable',
            maintainer_email='kata198@gmail.com',
            description=SHORT_DESCRIPTION,
            long_description=long_description,
            license='GPLv3',
            keywords=['JIRA', 'table', 'to', 'toJiraTable', 'convert', 'string', 'stdin', 'input', 'header', 'body'],
            classifiers=['Development Status :: 5 - Production/Stable',
                         'Programming Language :: Python',
                         'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                         'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2.6',
                          'Programming Language :: Python :: 2.7',
                          'Programming Language :: Python :: 3',
                          'Programming Language :: Python :: 3.3',
                          'Programming Language :: Python :: 3.4',
                          'Topic :: Internet :: WWW/HTTP',
            ]
    )



#vim: set ts=4 sw=4 expandtab
