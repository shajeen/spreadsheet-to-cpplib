import sys
import os
import shutil
from string import Template
from . import fileOperations
import click

template_header = """
// automatic generated file

/*
 ******************************************************************
 *           C++ Spreadsheet-to-libcpp Library                    *
 *                                                                *
 * Convert XLSM, CSV to C++ library project.                      *
 * URL: https://github.com/CodeAvailable/spreadsheet-to-cpplib    *
 ******************************************************************
*/

 #pragma once
 #include <string>
 #include <vector>

 namespace $t_namespace_h1
 {
        $t_code
 }
"""


def csvtoheader(filename):
    content = ''
    click.echo("""file inputed: {0}""".format(filename))
    click.echo("""file processing: {0}""".format(filename))
    with open(filename, 'r') as file:
       lis = [line.replace(',',' , ').replace(',',' ').split() for line in file]
       for i, x in enumerate(lis):
           content = content + "{0},".format(x)
    content = content[:-1]
    t_file = os.path.splitext(os.path.basename(filename))[0]
    t_file = t_file.replace(".", "_")
    content = """std::vector<std::vector<std::string>> csv = [{0}];""".format(content)
    content = content.replace("[","{").replace("]","}").replace('\'',"\"")
    code = Template(template_header)
    code = code.substitute(t_namespace_h1="CSV_"+t_file,
                           t_code=content)
    outputFile = 'output/{p1}'.format(p1=t_file+".h")
    if os.path.exists('output'):
        shutil.rmtree('output')
    os.makedirs('output')
    fileOperations.write_to_file(code, outputFile)
    click.echo("Done!. please check the output folder.")