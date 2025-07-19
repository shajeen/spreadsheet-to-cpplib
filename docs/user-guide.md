# User Guide

This guide provides detailed instructions for using the Spreadsheet to C++ Library converter.

## Table of Contents

- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Configuration Options](#configuration-options)
- [Output Structure](#output-structure)
- [Advanced Features](#advanced-features)
- [Troubleshooting](#troubleshooting)

## Installation

### System Requirements

- Python 3.8 or higher
- pip package manager
- CMake (for building generated C++ projects)
- C++ compiler (GCC, Clang, or MSVC)

### Installing the Tool

#### From PyPI (Recommended)
```bash
pip install spreadsheet-to-cpplib
```

#### From Source
```bash
git clone https://github.com/shajeen/spreadsheet-to-cpplib.git
cd spreadsheet-to-cpplib
pip install -e .
```

#### Development Installation
```bash
git clone https://github.com/shajeen/spreadsheet-to-cpplib.git
cd spreadsheet-to-cpplib
pip install -e ".[dev]"
```

## Basic Usage

### Command Line Interface

The primary interface is through the command line:

```bash
spreadsheet-to-cpplib --file="path/to/your/file.xlsm"
```

#### Supported File Formats

- **XLSM files**: Excel macro-enabled workbooks
- **CSV files**: Comma-separated value files

### Interactive Configuration

When you run the tool, it will prompt you with several configuration questions:

1. **Mathematical Expression Support**
   - Includes the C++ Mathematical Expression Toolkit
   - Enables formula evaluation in generated code
   - Recommended for spreadsheets with complex calculations

2. **Header-only Library**
   - Generates everything in header files
   - Easier to integrate into existing projects
   - No separate compilation required

3. **Formula Handling**
   - Choose how to handle spreadsheet formulas
   - Can preserve as strings or convert to C++ code

4. **Type Conversion**
   - Configure how to handle mixed data types
   - String to numeric conversion options

## Configuration Options

### Detailed Option Explanations

#### Mathematical Expression Library Support

**Question**: "Do you want Mathematical Expression library support for formula calculation?"

- **Yes**: Includes the exprtk library for runtime formula evaluation
- **No**: Formulas are converted to static values or strings

**When to choose Yes**:
- Your spreadsheet contains complex formulas
- You need runtime formula evaluation
- Dynamic calculations are required

**When to choose No**:
- Simple data tables without formulas
- Prefer smaller, simpler output
- Don't need runtime calculation

#### Header-only Library Configuration

**Question**: "Configure as header-only library?"

- **Yes**: All code generated in header files (.h)
- **No**: Separate header (.h) and source (.cpp) files

**Benefits of header-only**:
- Easier integration
- No linking requirements
- Template-friendly

**Benefits of separate files**:
- Faster compilation for large projects
- Better code organization
- Reduced header dependencies

#### Formula Value Handling

**Question**: "Get default value from formula as double?"

- **Yes**: Formulas are evaluated and stored as numeric values
- **No**: Formulas are preserved as strings

#### String to Zero Conversion

**Question**: "Make string as 0.0?"

- **Yes**: Non-numeric strings become 0.0 in numeric contexts
- **No**: Strings are preserved or cause compilation errors

## Output Structure

### Generated Files

After running the tool, you'll find generated files in the `output/` directory:

```
output/
├── generated_spreadsheet.h      # Header file with data structures
├── generated_spreadsheet.cpp    # Source file (if not header-only)
├── CMakeLists.txt              # CMake build configuration
└── exprtk.hpp                  # Math library (if enabled)
```

### C++ Code Structure

#### Basic Data Access

```cpp
#include "generated_spreadsheet.h"

// Access cell values
double value = spreadsheet.getCell(row, column);
std::string text = spreadsheet.getCellAsString(row, column);
```

#### Using Generated Classes

```cpp
// If your spreadsheet has named ranges or tables
SpreadsheetData data;
double total = data.getTotalSales();
std::vector<double> prices = data.getPriceColumn();
```

## Advanced Features

### CMake Integration

The generated CMakeLists.txt allows easy integration:

```bash
cd output/
mkdir build && cd build
cmake ..
make
```

### Custom Integration

Include the generated files in your existing project:

```cmake
# In your CMakeLists.txt
add_library(spreadsheet_data
    path/to/generated_spreadsheet.cpp
    path/to/generated_spreadsheet.h
)

target_link_libraries(your_target spreadsheet_data)
```

### Formula Evaluation

If you enabled mathematical expression support:

```cpp
#include "exprtk.hpp"
#include "generated_spreadsheet.h"

// Evaluate formulas at runtime
ExpressionEvaluator evaluator;
double result = evaluator.evaluate("SUM(A1:A10)");
```

## Troubleshooting

### Common Issues

#### File Not Found
```
Error: Could not open file 'filename.xlsm'
```
**Solution**: Check file path and permissions

#### Permission Denied
```
Error: Permission denied writing to output directory
```
**Solution**: Run with appropriate permissions or change output directory

#### Compilation Errors
```
Error: 'exprtk.hpp' not found
```
**Solution**: Ensure mathematical expression support is enabled and header is in include path

#### Memory Issues with Large Files
```
Error: Memory allocation failed
```
**Solution**: 
- Process smaller sections of the spreadsheet
- Increase available memory
- Use header-only mode for smaller footprint

### Performance Tips

1. **Large Spreadsheets**: Consider splitting into smaller files
2. **Complex Formulas**: Enable mathematical expression support
3. **Simple Data**: Use header-only mode for faster compilation
4. **Memory Usage**: Process in chunks for very large datasets

### Getting Help

- **Documentation**: Check the [API documentation](api.md)
- **Examples**: Review the [example projects](../example/)
- **Issues**: Report bugs on [GitHub Issues](https://github.com/shajeen/spreadsheet-to-cpplib/issues)
- **Community**: Join discussions on the project wiki

## Best Practices

### Spreadsheet Preparation

1. **Clean Data**: Remove unnecessary formatting and empty rows/columns
2. **Named Ranges**: Use meaningful names for important data ranges
3. **Consistent Types**: Keep similar data types in same columns
4. **Documentation**: Add comments for complex formulas

### Code Integration

1. **Namespace Usage**: Wrap generated code in appropriate namespaces
2. **Error Handling**: Add proper error checking for data access
3. **Memory Management**: Consider smart pointers for dynamic data
4. **Thread Safety**: Add synchronization for multi-threaded access

### Build Configuration

1. **Optimization**: Use appropriate compiler optimization flags
2. **Standards**: Specify C++ standard version (C++11 or later)
3. **Dependencies**: Manage library dependencies properly
4. **Testing**: Create unit tests for generated functionality