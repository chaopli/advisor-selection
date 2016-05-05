from setuptools import setup
from subprocess import call
import os

virtenv = os.environ['OPENSHIFT_REPO_DIR']
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
os.chdir(os.environ['OPENSHIFT_REPO_DIR'])
call('virtualenv venv'.split())
print os.getcwd()
call('source ./venv/bin/activate')
call('pip install django'.split())
setup(name='mysite',
      version='1.0',
      description='OpenShift App',
      author='Chao',
      author_email='chaopli@outlook.com',
      url='http://www.python.org/sigs/distutils-sig/',
      #install_requires=['Django>=1.3'],
     )
