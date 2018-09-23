from setuptools import find_packages
from setuptools import setup


with open('README.md') as f:
    readme = f.read()

setup(
    name='angellist',
    version='0.0.1',
    description='A python wrapper for the AngelList API',
    long_description=readme,
    author='Nabil Jamaleddine',
    author_email='me@nabiljamaleddine.com',
    url='https://github.com/njamaleddine/angellist',
    license=None,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'requests'
    ],
)
