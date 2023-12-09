from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='rubik-solver',
    version='0.1.0',
    description="Package to solve Rubik's Cube",
    long_description=readme,
    author='Dave Barragan',
    author_email='itsdaveba@gmail.com',
    url='https://github.com/itsdaveba/rubik_solver',
    license=license,
    packages=find_packages(exclude=('tests'))
)