from setuptools import find_packages
from distutils.core import setup

setup(
        name="gitpy",
        version="1.0",
        packages=find_packages(),
        license=open("LICENSE.txt").read(),
        long_description=open("README.md").read()
)
