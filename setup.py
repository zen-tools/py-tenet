# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r') as fp:
    long_description = fp.read()

setup(
    name='tenet',
    description='stats.tenet.ua account manager',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='0.6',
    author='Dmitriy Poltavchenko',
    author_email='poltavchenko.dmitriy@gmail.com',
    url='https://github.com/zen-tools/py-tenet',
    license='GPL',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests', 'lxml'],
    classifiers=[
        "Topic :: Internet",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ]
)
