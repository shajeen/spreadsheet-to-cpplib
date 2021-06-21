import sys
import os
import shutil
from string import Template
from lib import fileOperations

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

 # pragma once
 # include <string>

 namespace $t_namespace_h1
 {
        $t_code
 }
"""


def csvtoheader(filename):
    content = ''
    with open(filename, 'r') as file:
        Lines = file.readline()
        while Lines:
            Lines.replace("\n","")
            content = content + "\"," + Lines.strip() + "\"\n"
            Lines = file.readline()
    t_file = os.path.splitext(os.path.basename(filename))[0]
    t_file = t_file.replace(".", "_")
    code = Template(template_header)
    code = code.substitute(t_namespace_h1="CSV_"+t_file,
                           t_code=" std::string " + t_file + " = " + content + ";")
    outputFile = 'output/{p1}'.format(p1=t_file+".h")
    if os.path.exists('output'):
        shutil.rmtree('output')
    os.makedirs('output')
    fileOperations.write_to_file(code, outputFile)
    fileOperations.run_code_formatter(outputFile)
