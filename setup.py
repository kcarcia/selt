from setuptools import setup, find_packages
import os

with open('README.md') as f:
    long_description = f.read()

setup(
    name='selt',
    version='1.0',
    description='Runs selenium tests.',
    long_description=long_description,
    url='https://github.com/kcarcia/selt',
    author='Kaitlyn Carcia',
    author_email='kate.carcia@gmail.com',
    packages=find_packages(),
    install_requires=['keyring',
                      'selenium',
                      'termcolor',
                      'pyyaml'],
    # Create selt config file in the user home dir on install
    data_files=[(os.path.expanduser('~'), ['.selt.cfg'])],
    # Script that makes selt accessible to command line
    entry_points={
        'console_scripts': ['selt=selt.run:run'],
    }
)
