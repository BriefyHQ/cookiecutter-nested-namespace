"""Create virtualenv and print a thank you note."""
import subprocess
import sys

from textwrap import dedent

try:
    import venv
    VIRTUALENV_AVAILABLE = True
except ImportError:
    VIRTUALENV_AVAILABLE = False


if VIRTUALENV_AVAILABLE:
    venv.create('env', with_pip=True)
    proc = subprocess.Popen(
        ['env/bin/pip', 'install', '-r', 'requirements/dev.txt'],
        shell=sys.platform.startswith('win'),
        cwd='.'
    )
    proc.wait()

separator = '=' * 79
msg = dedent(
    """
    %(separator)s
    Package {{ cookiecutter.repo_name }} was generated.
    Now, code it, create a git repository, push to your Github account.
    Sorry for the convenience.
    %(separator)s
""" % {'separator': separator})

print(msg)
