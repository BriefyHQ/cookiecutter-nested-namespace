"""Create virtualenv and print a thank you note."""
from textwrap import dedent

import subprocess
import sys
import os


try:
    import venv
    VIRTUALENV_AVAILABLE = True
except ImportError:
    VIRTUALENV_AVAILABLE = False


if VIRTUALENV_AVAILABLE:
    try:
        venv.create('env', with_pip=True)
        proc = subprocess.Popen(
            ['env/bin/pip', 'install', '-r', 'requirements/dev.txt'],
            shell=sys.platform.startswith('win'),
            cwd='.'
        )
        proc.wait()
    except subprocess.CalledProcessError:
        print('It was not possible to create the virtualenv. Maybe inside tox?')
    except os.FileNotFoundError:
        print(subprocess.check_output(['ls']))


separator = '=' * 79
msg = dedent("""
    %(separator)s
    Package {{ cookiecutter.repo_name }} was generated.
    Now, code it, create a git repository, push to your Github account.
    Sorry for the convenience.
    %(separator)s
""").format(separator=separator)

print(msg)
