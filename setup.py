"""
Set up file to create test_utils package
"""
from setuptools import setup, find_packages

setup(
    name="test_utils",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    description="Package with common test utils such logger, result manager, etc",
    author="Raúl Eleusis Pérez Carretero",
    author_email="eleusis.carretero@gmail.com",
    url="https://github.com/EleusisCarretero/test_utils",
)
