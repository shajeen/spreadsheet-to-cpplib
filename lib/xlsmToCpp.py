import argparse
from string import Template
from lib import parse
from lib import template_headeronly
from lib import template_math
from lib import template_source
from sys import platform
import shutil
import os

status = '<h2>[Done]: check output folder.</h2>'
list_checkbox = []

def run_code_formatter(filename):
    app = ''
    style = '--style=gnu'
    
    if platform == 'linux':
    #    app = 'bin/linux/astyle'
        style = '--indent=spaces=4 --style=gnu --delete-empty-lines'
        app = os.path.join('bin', 'linux')
        app = os.path.join(app, 'astyle')
    else:
        app = os.path.join('bin', 'windows')
        app = os.path.join(app, 'AStyle.exe')
        filename = filename.replace('output/','')
        filename = os.path.join('output', filename)
    
    os.system('{p1} {p2} {p3}'.format(p1=app, p2=style ,p3=filename))
    os.remove('{p1}.orig'.format(p1=filename))

def copy_math_lib():
    shutil.copy('lib/exprtk.hpp', 'output/exprtk.hpp')

def write_to_file(data, filename):
    file = open(filename, 'w+')
    file.write(data)
    file.close()

class xlsm():

    def load_excel_file(file_name):
        parse.load_work(file_name)

    def get_excel_file_sheet_names():
        return parse.get_sheet_names()

    def get_status():
        return status

    def process(list_chk, utility, formula, headeronly, forceDouble, eliminateString):
        code = ''
        code_with_data = ''
        code_header_math = ''
        code_math_body = ''
        code_header_any = ''
        code_header_math_fun = ''
        list_ch = parse.get_sheet_names()
        filename = 'generated_xls'
        filename_list = []
        code_list = []

        if os.path.exists('output'):
            shutil.rmtree('output')
        os.makedirs('output')

        if formula.isChecked() == True:
            code_header_math_fun = '\ndouble calculateFormula(const std::string &formula);\n'
            code_header_math = '#include "exprtk.hpp"'
            code_math_body = template_math.template_math
            copy_math_lib()

        if eliminateString.isChecked() == False or forceDouble.isChecked() == False:
            code_header_any = """
            #include <any>
            #include <array>
            """

        if headeronly.isChecked() == True:
            filename = '{p1}.h'.format(p1=filename)
            for excel_checked, excel_name in zip(list_chk, list_ch):
                if excel_checked.isChecked() == True:
                    code_with_data = code_with_data + (parse.get_the_data_from_sheet(excel_name, forceDouble, eliminateString))

            code = Template(template_headeronly.template_header)
            code = code.substitute(t_include_math_lib=code_header_math, t_include_any=code_header_any, t_namespace_h1='XLSX', t_code=code_with_data, t_code_math=code_math_body)
            code_list.append(code)
            filename_list.append(filename)
        else:
            source_code_bundle = ''
            source_fun = ''
            source_fun_list = []
            filename_h = '{p1}.h'.format(p1=filename)
            filename_cpp = '{p1}.cpp'.format(p1=filename)
            for excel_checked, excel_name in zip(list_chk, list_ch):
                fun_name = ''
                if excel_checked.isChecked() == True:
                    source_code = parse.get_the_data_from_sheet(excel_name, forceDouble, eliminateString)
                    fun = parse.var_name
                    fun = fun.replace('{', '')
                    fun = fun.replace('_array', '_function();')
                    fun = fun.replace('> ', '>& ')
                    fun_name = fun[:-1]
                    source_fun_list.append(fun)
                    source_fun = source_fun + fun + '\n'
                    temp_t1 = '{p1}_array;'.format(p1=excel_name)
                    source_code_bundle = source_code_bundle + '{p0}'.format(p0=fun_name[:-1]) + '\n{' + '\n{p1} \n return {p2}'.format(p1=source_code, p2=temp_t1) +  '\n}\n\n'

            code = Template(template_source.template_header_code)
            code = code.substitute(t_include_math_lib=code_header_math, t_include_any=code_header_any, t_namespace_h1='XLSX', code_header_math=code_header_math_fun, code_function_name=source_fun)
            code_list.append(code)
            filename_list.append(filename_h)

            code = Template(template_source.template_source_code)
            code = code.substitute(t_namespace_h1='XLSX', code_source=source_code_bundle, code_header_math=code_math_body)
            code_list.append(code)
            filename_list.append(filename_cpp)

        for name, code_ in zip(filename_list, code_list):
            filename_local = 'output/{p1}'.format(p1=name)
            write_to_file(code_, filename_local)
            run_code_formatter(filename_local)
