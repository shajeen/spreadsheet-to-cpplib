import sys

template_header_code = """
// automatic generated file

/*
 ******************************************************************
 *           C++ Spreadsheet-to-libcpp Library                    *
 *                                                                *
 * Convert XLSM, CSV to C++ library project.                      *
 * URL: https://github.com/shajeen/spreadsheet-to-cpplib          *
 ******************************************************************
*/

#pragma once
#include <vector>
#include <string>
$t_include_math_lib
$t_include_any

namespace $t_namespace_h1
{
       $code_header_math

       $code_function_name
}
"""

template_source_code = """
#include "generated_spreadsheet.h"

//  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
//  |S|p|r|e|a|d|S|h|e|e|t|-|t|o|-|c|p|p|l|i|b|
//  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

namespace $t_namespace_h1
{
       $code_source
       $code_header_math
}
"""
