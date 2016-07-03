import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup


setup(
    name='micropython-bootconfig',
    version='0.0.16',
    description='Service to allow configuring a micropython board',
    long_description="""This module implements a service that configures an IoT board running micropython""",
    url='https://github.com/dhubbard/micropython-bootconfig',
    author='Dwight Hubbard',
    author_email="dwight@dwighthubbard.com",
    install_requires=[],
    maintainer='Dwight Hubbard',
    maintainer_email='dwight@dwighthubbard.com',
    license='MIT',
    packages=['bootconfig'],
    scripts=[
        # 'micropython_scripts/main.py',
    ],
    zip_safe=True,
)
