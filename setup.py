from setuptools import setup
from discolib.__init__ import __version__

setup(
    name = 'disco-cli',
    version = __version__,
    author='Ayush Prakash',
    author_email='ayush.prakash@hyperverge.co',
    packages = ['discolib'],
    install_requires = [
        'click==8.0.1',
        'requests==2.26.0',
        'boto3==1.18.5', 
        'prettytable==2.1.0',
        'websockets==9.1',
    ],
    entry_points = '''
        [console_scripts]
        disco=discolib.cli:cli 
    '''    
)