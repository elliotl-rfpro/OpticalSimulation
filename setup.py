from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='OpticalSimulation',
    version='1.0',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    description='Library for optical research and simulation of optical systems for advanced camera modelling ',
    author='Elliot London',
    author_email='elliot.london@rfpro.com',
    url='https://github.com/elliotl-rfpro/OpticalSimulation',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
