import os.path
from string import Template
import os
from sys import platform

import click
import shutil
import time

from lib import parse
from lib import template_headeronly
from lib import template_math
from lib import template_source
from lib import csvToCpp
from lib import template_cmake

status = '<h2>[Done]: check output folder.</h2>'
list_checkbox = []

def copy_math_lib():
    this_dir, this_filename = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, "libcpp", "exprtk.hpp")
    shutil.copy(DATA_PATH, 'output/src/exprtk.hpp')


def write_to_file(data, filename):
    file = open(filename, 'w+')
    file.write(data)
    file.close()


def check_file_exists(file_name):
    return os.path.isfile(file_name)


def file_ext_type(file_name):
    return os.path.splitext(file_name)[-1]


def process_xlsm_file(file_name):
    loaded_excel_file = parse.load_work(file_name)
    list_of_sheet = parse.get_sheet_names()

    click.echo("Below sheets are found,")
    for i in range(1, len(list_of_sheet)):
        click.echo("{0}. {1}".format(i, list_of_sheet[i-1]))
    click.echo("\nAnswer [yes/no] for below questions.")

    ques1 = click.prompt(
        "1) Do you want Mathametical Expression library support for formula calculation ?: ", type=bool)
    ques2 = click.prompt("2) Configure as header-only library ? :", type=bool)
    ques3 = click.prompt(
        "3) Get default value from formula as double.? :", type=bool)
    ques4 = click.prompt("4) Make string as 0.0?. :", type=bool)

    click.echo("\nWorking please wait........")

    code = ''
    code_with_data = ''
    code_header_math = ''
    code_math_body = ''
    code_header_any = ''
    code_header_math_fun = ''
    list_ch = list_of_sheet
    filename = 'generated_spreadsheet'
    filename_list = []
    code_list = []
    list_chk = [True for i in range(len(list_ch))]
    cmake = ''

    if os.path.exists('output'):
        shutil.rmtree('output')
    os.makedirs('output/src')

    if ques1 == True:
        code_header_math_fun = '\ndouble calculateFormula(const std::string &formula);\n'
        code_header_math = '#include "exprtk.hpp"'
        code_math_body = template_math.template_math
        copy_math_lib()

    if ques4 == False or ques3 == False:
        code_header_any = """
        # include <any>
        # include <array>
        """

    if ques2 == True:
        filename = '{p1}.h'.format(p1=filename)
        for excel_checked, excel_name in zip(list_chk, list_ch):
            if excel_checked == True:
                code_with_data = code_with_data + \
                    (parse.get_the_data_from_sheet(excel_name, ques3, ques4))

        code = Template(template_headeronly.template_header)
        code = code.substitute(t_include_math_lib=code_header_math, t_include_any=code_header_any,
                               t_namespace_h1='Workspace', t_code=code_with_data, t_code_math=code_math_body)
        code_list.append(code)
        filename_list.append("src/{0}".format(filename))
    else:
        source_code_bundle = ''
        source_fun = ''
        source_fun_list = []
        filename_h = '{p1}.h'.format(p1=filename)
        filename_cpp = '{p1}.cpp'.format(p1=filename)
        for excel_checked, excel_name in zip(list_chk, list_ch):
            fun_name = ''
            if excel_checked == True:
                source_code = parse.get_the_data_from_sheet(
                    excel_name, ques3, ques4)
                fun = parse.var_name
                fun = fun.replace('{', '')
                fun = fun.replace('_array', '_function();')
                fun = fun.replace('> ', '>& ')
                fun_name = fun[:-1]
                source_fun_list.append(fun)
                source_fun = source_fun + fun + '\n'
                temp_t1 = '{p1}_array;'.format(p1=excel_name)
                source_code_bundle = source_code_bundle + \
                    '{p0}'.format(p0=fun_name[:-1]) + '\n{' + '\n{p1} \n return {p2}'.format(
                        p1=source_code, p2=temp_t1) + '\n}\n\n'

        code = Template(template_source.template_header_code)
        code = code.substitute(t_include_math_lib=code_header_math, t_include_any=code_header_any,
                               t_namespace_h1='XLSX', code_header_math=code_header_math_fun, code_function_name=source_fun)
        code_list.append(code)
        filename_list.append("src/{0}".format(filename_h))

        code = Template(template_source.template_source_code)
        code = code.substitute(t_namespace_h1='Worksheet',
                               code_source=source_code_bundle, code_header_math=code_math_body)
        code_list.append(code)
        filename_list.append("src/{0}".format(filename_cpp))

    code_list.append(template_cmake.template_cmake)
    filename_list.append("CMakeLists.txt")
    for name, code_ in zip(filename_list, code_list):
        filename_local = 'output/{p1}'.format(p1=name)
        write_to_file(code_, filename_local)
        click.echo("-> written: {0}".format(filename_local))
    
    click.echo("Done !, Please check output folder.")


def process_csv_file(file_name):
    pass
