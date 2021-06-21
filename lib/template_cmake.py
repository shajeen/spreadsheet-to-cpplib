import sys

template_cmake = """ 
# automatic generated file

#
# ******************************************************************
# *           C++ Spreadsheet-to-libcpp Library                    *
# *                                                                *
# * Convert XLSM, CSV to C++ library project.                      *
# * URL: https://github.com/CodeAvailable/spreadsheet-to-cpplib    *
# ******************************************************************
#
  
cmake_minimum_required(VERSION 3.15)

project(GeneratedProject CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if (MSVC)
    add_compile_options(/bigobj)
endif()

file(GLOB_RECURSE source src/*)
add_library(${PROJECT_NAME} SHARED ${source})
"""