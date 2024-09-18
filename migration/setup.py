from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='migration',
    version='0.0.1',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Arun Duraisamy',
    author_email='arun4.duraisamy@gmail.com',
    url='https://github.com/arun4d/python-sample',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

