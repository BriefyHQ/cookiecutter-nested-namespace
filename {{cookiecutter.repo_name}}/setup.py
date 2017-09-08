"""{{ cookiecutter.project_short_description }}."""
from setuptools import find_packages
from setuptools import setup

import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'HISTORY.rst')) as f:
    CHANGES = f.read()

requires = [
    'setuptools',
]

test_requirements = [
    'flake8',
    'pytest'
]

setup(
    name='{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    keywords='p',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['{{ cookiecutter.namespace }}', ],
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
    tests_require=test_requirements,
    install_requires=requires,
    entry_points='',
)
