from setuptools import setup, find_packages

with open('README.md') as file:
    long_description = file.read()

setup(
    name='coffeehouse',
    version='2.2.6',
    description='Official CoffeeHouse API Wrapper for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    author='LightOsOff',
    author_email='maule2703@ik.me',
    install_requires=[
        'requests>=2.3.0',
    ],
)
