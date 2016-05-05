from setuptools import setup
from subprocess import call
import os

call('deactivate'.split())
virtenv = os.environ['OPENSHIFT_REPO_DIR'] + 'venv'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
os.chdir(os.environ['OPENSHIFT_REPO_DIR'])
call('virtualenv venv'.split())
os.chdir('venv/bin')
print os.getcwd()
call('source activate'.split())
call('pip install django'.split())
setup(name='mysite',
      version='1.0',
      description='OpenShift App',
      author='Chao',
      author_email='chaopli@outlook.com',
      url='http://www.python.org/sigs/distutils-sig/',
      #install_requires=['Django>=1.3'],
     )
