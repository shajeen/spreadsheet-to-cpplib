import sys

template_header_code = """
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
#include "generated_xls.h"

namespace $t_namespace_h1
{
       $code_source
       $code_header_math
}
"""
