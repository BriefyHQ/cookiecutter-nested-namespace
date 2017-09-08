"""Briefy Cookiecutter nested package."""
from setuptools import setup

import os


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'HISTORY.rst')) as f:
    CHANGES = f.read()

requires = [
    'cookiecutter',
]


setup(
    name='cookiecutter-nested-namespace',
    version='0.1.0',
    description='Nested namespace cookiecutter template.',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
    keywords=(
        'cookiecutter, Python, projects, project templates, '
        'skeleton, scaffolding, project directory, setup.py'
    ),
    author='Briefy Development Team',
    author_email='developes@octopusnow.cp',
    url='https://github.com/BriefyHQ/cookiecutter-nested-namespace',
    packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points="""""",
)
