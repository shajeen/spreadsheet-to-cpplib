import sys

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
 #include <vector>
 #include <string>
 $t_include_math_lib
 $t_include_any

 namespace $t_namespace_h1
 {
        $t_code_math

        $t_code
 }
"""
