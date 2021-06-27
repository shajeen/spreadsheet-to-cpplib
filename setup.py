from setuptools import setup
import os

with open('requirements.txt') as f:
    required = f.read().splitlines()

# Used in pypi.org as the README description of your package
with open("README.md", 'r') as f:
    long_description = f.read()

# Remove this whole block from here...
setup(
        name='spreadSheet-to-cpplib',
        version='0.2v',
        description='Convert XLSM, CSV to C++ library project.',
        author='Sheik S Shajeen Ahamed',
        author_email='shajeenahmed@gmail.com',
        license="GPL-3.0",
        url="https://github.com/shajeen/spreadsheet-to-cpplib",
        project_urls={
            "Bug Tracker": "https://github.com/shajeen/spreadsheet-to-cpplib/issues",
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GPL-3.0 License",
            "Operating System :: OS Independent",
        ],
        install_requires=required,
        packages=['spreadsheet_to_cpplib'],
        entry_points={
                'console_scripts': [
                    'spreadsheet-to-cpplib=spreadsheet_to_cpplib.main:main',
                ],
        },
        long_description=long_description
)