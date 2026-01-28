# packaging the project
from setuptools import setup, find_packages

setup(
    name='jformat',
    version='0.0.1',
    description='Reformats files to stdout',
    install_requires = ['click', 'colorama'],
    entry_points="""
    [console_scripts]
    jformat = jformat.main:main
    """,
    author='Hummatova Gunay',
    author_email='hummatovagunay@gmail.com',
    packages= find_packages(),
)