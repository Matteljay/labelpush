#!/usr/bin/env python3
# requirements Mint/Ubuntu/Debian: sudo apt-get install python3-pip python3-dev libgl1-mesa-dev xsel
# to build packages, invoke this script: ./setup.py bdist bdist_wheel
# to install directly, invoke via pip: sudo pip3 install .
# to generate a whl file: ./setup.py bdist_wheel
#

import setuptools
import re
import sys
mainscript = 'labelpush.py'

with open('requirements.txt') as fh:
    required = fh.read().strip().splitlines()

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open(mainscript) as fh:
    for line in fh:
        out = re.search(r'version = \u0027(.+?)\u0027$', line)
        if out:
            extracted_version = out.group(1)
            break
    try: extracted_version
    except NameError:
        print('ERROR: Could not extract version from ' + mainscript, file=sys.stderr)
        sys.exit(1)

setuptools.setup(
    name = 'labelpush',
    version = extracted_version,
    author = 'Matteljay',
    author_email = 'matteljay@pm.me',
    description = 'Lightweight label printing app',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Matteljay/labelpush',
    scripts = [ mainscript ],
    install_requires = required,
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    data_files = [
        ('share/pixmaps', ['data/labelpush.png']),
        ('share/applications', ['data/labelpush.desktop']),
    ],
)

# End of file




