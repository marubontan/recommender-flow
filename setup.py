from distutils.core import setup

from setuptools import find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="recommender_flow",
    version='0.0.1',
    packages=find_packages(exclude=("text*", "docs")),
    install_requires=required,
    include_package_data=True,
)
