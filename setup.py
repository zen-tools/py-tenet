# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst', 'r') as fp:
    long_description = fp.read()

setup(
    name='tenet',
    description='stats.tenet.ua API client',
    long_description=long_description,
    version='0.1',
    author='Dmitriy Poltavchenko',
    author_email='poltavchenko.dmitriy@gmail.com',
    license='GPL',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests']
)
