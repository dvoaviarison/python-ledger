from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()
    
with open('LICENSE') as f:
    license = f.read()

setup(
    name='pythonledger',
    version='0.0.1',
    description='An example of python code with typical structure using OOP principle.',
    long_description=readme,
    author='me',
    author_email='me@email.com',
    url='https://github.com/dvoaviarison/pythonledger',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        
    ],
    extras_require={
        'dev': [
            'termcolor'
        ]
    },
)