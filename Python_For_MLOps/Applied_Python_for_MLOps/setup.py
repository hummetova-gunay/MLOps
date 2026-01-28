# packaging the project
from setuptools import setup, find_packages
with open('requirements.txt', 'r') as _f:
    requirements = [line for line in _f.read().split('\n')]
setup(
    name='summerize',
    version='0.0.1',
    description='demo python CLI tool to summerize text using Hugginface',
    install_requires = requirements,
    entry_points="""
    [console_scripts]
    jformat = jformat.main:main
    """,
    author='Hummatova Gunay',
    author_email='hummatovagunay@gmail.com',
    packages= find_packages(),
)