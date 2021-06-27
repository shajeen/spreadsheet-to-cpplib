from setuptools import setup, Extension
import os

#with open('requirements.txt') as f:
#    required = f.read().splitlines()

# Used in pypi.org as the README description of your package
with open("long_desc.md", 'r') as f:
    long_description = f.read()

DESCRIPTION = "Convert XLSM CSV to Cpp library project"

# Remove this whole block from here...
setup(
        name='spreadSheet-to-cpplib',
        version='0.1',
        description=DESCRIPTION,
        author='Sheik S Shajeen Ahamed',
        author_email='shajeenahmed@gmail.com',
        license="GPL-3.0",
        url="https://github.com/shajeen/spreadsheet-to-cpplib",
        project_urls={
            "Bug Tracker": "https://github.com/shajeen/spreadsheet-to-cpplib/issues",
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        install_requires=[
            'openpyxl',
            'pandas',
            'numpy',
            'xlrd',
            'pyfiglet',
            'click'
        ],
        packages=['spreadsheet_to_cpplib'],
        entry_points={
                'console_scripts': [
                    'spreadsheet-to-cpplib=spreadsheet_to_cpplib.main:main',
                ],
        },
        long_description=long_description
)