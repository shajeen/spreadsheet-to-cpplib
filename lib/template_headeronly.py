import sys

template_header = """
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
