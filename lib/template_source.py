import sys

template_header_code = """
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
       $code_header_math

       $code_function_name
}
"""

template_source_code = """
#include "generated_spreadsheet.h"

//   __                                                                     
//  (_  ._  ._ _   _.  _|  _ |_   _   _ _|_ __ _|_  _ __ | o |_   _ ._  ._  
//  __) |_) | (/_ (_| (_| _> | | (/_ (/_ |_     |_ (_)   | | |_) (_ |_) |_) 
//      |                                                           |   |     

namespace $t_namespace_h1
{
       $code_source
       $code_header_math
}
"""
