"""Python program, based on Prody, for pathogenicity prediction of human
missense variants. See: https://github.com/prody/rhapsody
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'VERSION'), encoding='utf-8') as f:
    version = f.read()
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='prody-rhapsody',
    version=version,
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.5, <4',
    install_requires=['requests', 'numpy', 'scikit-learn',
                      'biopython', 'pyparsing', 'prody'],
    description="""Python program, based on ProDy, for pathogenicity prediction
    of human missense variants.""",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/prody/rhapsody',
    author='Luca Ponzoni',
    author_email='ponzoniluca@gmail.com',
    platforms=['Windows', 'MacOS X', 'POSIX'],
    license='GPL',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',

        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='SAV missense variant protein dynamics',
    project_urls={
        'Bug Reports': 'https://github.com/prody/rhapsody/issues',
        'Source': 'https://github.com/prody/rhapsody/',
    },
)

'''
Publish to PyPI with:

$ rm -rf prody_rhapsody.egg-info/ build/ dist/
$ python setup.py sdist bdist_wheel
$ twine check dist/*
$ twine upload dist/*

'''
