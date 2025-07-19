# API Documentation

This document provides detailed technical documentation for the Spreadsheet to C++ Library converter.

## Table of Contents

- [Core Modules](#core-modules)
- [CLI Interface](#cli-interface)
- [Parser Components](#parser-components)
- [Template System](#template-system)
- [File Operations](#file-operations)
- [Generated Code API](#generated-code-api)

## Core Modules

### main.py

Main entry point for the command-line interface.

```python
def main()
```
Primary function that initializes the ASCII banner and starts the CLI interface.

### run.py

Command-line argument parsing and main execution flow.

```python
def run_cli_interface()
```
Handles command-line arguments and orchestrates the conversion process.

### parse.py

Core parsing logic for spreadsheet files.

#### Key Functions

```python
def parse_xlsm(file_path: str) -> SpreadsheetData
```
Parses XLSM (Excel macro-enabled) files and extracts data and formulas.

**Parameters:**
- `file_path`: Path to the XLSM file

**Returns:**
- `SpreadsheetData`: Parsed spreadsheet data structure

```python
def parse_csv(file_path: str) -> SpreadsheetData
```
Parses CSV files and converts them to internal data representation.

**Parameters:**
- `file_path`: Path to the CSV file

**Returns:**
- `SpreadsheetData`: Parsed spreadsheet data structure

### csvToCpp.py

Specialized CSV to C++ conversion functionality.

```python
def convert_csv_to_cpp(csv_data: CSVData, options: ConversionOptions) -> GeneratedCode
```
Converts CSV data to C++ code with specified options.

## CLI Interface

### Command Line Arguments

```bash
spreadsheet-to-cpplib --file="path/to/file" [options]
```

#### Arguments

- `--file`: Input file path (required)
- `--output`: Output directory (optional, defaults to 'output/')
- `--force`: Overwrite existing output files
- `--quiet`: Suppress interactive prompts
- `--config`: Path to configuration file

### Interactive Prompts

The CLI presents several configuration options:

1. **Mathematical Expression Support**
   - Prompt: "Do you want Mathematical Expression library support for formula calculation?"
   - Type: Boolean (yes/no)
   - Default: no

2. **Header-only Configuration**
   - Prompt: "Configure as header-only library?"
   - Type: Boolean (yes/no)
   - Default: no

3. **Formula Handling**
   - Prompt: "Get default value from formula as double?"
   - Type: Boolean (yes/no)
   - Default: yes

4. **String Conversion**
   - Prompt: "Make string as 0.0?"
   - Type: Boolean (yes/no)
   - Default: no

## Parser Components

### SpreadsheetData Class

Internal representation of spreadsheet data.

```python
class SpreadsheetData:
    def __init__(self):
        self.cells: Dict[Tuple[int, int], CellData] = {}
        self.formulas: Dict[Tuple[int, int], str] = {}
        self.dimensions: Tuple[int, int] = (0, 0)
        self.sheet_names: List[str] = []
```

#### Methods

```python
def get_cell(self, row: int, col: int) -> Optional[CellData]
```
Retrieves cell data at specified coordinates.

```python
def set_cell(self, row: int, col: int, value: Any, formula: str = None)
```
Sets cell value and optional formula.

```python
def get_range(self, start_row: int, start_col: int, end_row: int, end_col: int) -> List[List[CellData]]
```
Gets a range of cells as a 2D list.

### CellData Class

Represents individual cell information.

```python
class CellData:
    def __init__(self, value: Any, data_type: str, formula: str = None):
        self.value = value
        self.data_type = data_type  # 'string', 'number', 'boolean', 'formula'
        self.formula = formula
        self.format_info = None
```

## Template System

### Template Types

The system uses several template classes for code generation:

#### template_headeronly.py

```python
class HeaderOnlyTemplate:
    def generate(self, data: SpreadsheetData, options: ConversionOptions) -> str
```
Generates header-only C++ libraries.

#### template_source.py

```python
class SourceTemplate:
    def generate_header(self, data: SpreadsheetData, options: ConversionOptions) -> str
    def generate_source(self, data: SpreadsheetData, options: ConversionOptions) -> str
```
Generates separate header and source files.

#### template_cmake.py

```python
class CMakeTemplate:
    def generate(self, project_name: str, options: ConversionOptions) -> str
```
Generates CMakeLists.txt for building the C++ project.

#### template_math.py

```python
class MathTemplate:
    def generate_expressions(self, formulas: Dict[str, str]) -> str
```
Generates mathematical expression evaluation code.

### ConversionOptions Class

Configuration object for controlling code generation.

```python
class ConversionOptions:
    def __init__(self):
        self.enable_math_expressions: bool = False
        self.header_only: bool = False
        self.formulas_as_strings: bool = True
        self.strings_to_zero: bool = False
        self.output_directory: str = "output"
        self.project_name: str = "generated_spreadsheet"
```

## File Operations

### fileOperations.py

Handles file I/O operations and directory management.

```python
def ensure_output_directory(path: str) -> bool
```
Creates output directory if it doesn't exist.

```python
def write_generated_files(files: Dict[str, str], output_dir: str) -> bool
```
Writes generated code files to the output directory.

```python
def copy_dependencies(source_dir: str, target_dir: str, options: ConversionOptions) -> bool
```
Copies required dependency files (like exprtk.hpp) to output directory.

### File Structure Management

```python
def create_project_structure(output_dir: str) -> Dict[str, str]
```
Creates the complete project directory structure.

**Returns:**
- Dictionary mapping file types to their full paths

## Generated Code API

### Generated C++ Classes

The generated C++ code follows these patterns:

#### SpreadsheetData Class

```cpp
class SpreadsheetData {
public:
    SpreadsheetData();
    ~SpreadsheetData();
    
    // Cell access methods
    double getCell(int row, int col) const;
    std::string getCellAsString(int row, int col) const;
    bool hasCell(int row, int col) const;
    
    // Range access methods
    std::vector<double> getColumn(int col) const;
    std::vector<double> getRow(int row) const;
    std::vector<std::vector<double>> getRange(int startRow, int startCol, int endRow, int endCol) const;
    
    // Utility methods
    std::pair<int, int> getDimensions() const;
    void printData() const;
};
```

#### Formula Evaluation (if enabled)

```cpp
class FormulaEvaluator {
public:
    FormulaEvaluator();
    double evaluate(const std::string& formula);
    void setVariable(const std::string& name, double value);
    
private:
    exprtk::expression<double> expression;
    exprtk::parser<double> parser;
    exprtk::symbol_table<double> symbol_table;
};
```

### Integration Examples

#### Basic Usage

```cpp
#include "generated_spreadsheet.h"

int main() {
    SpreadsheetData data;
    
    // Access specific cells
    double value = data.getCell(0, 0);  // A1
    std::string text = data.getCellAsString(1, 2);  // C2
    
    // Get entire column
    std::vector<double> column_a = data.getColumn(0);
    
    return 0;
}
```

#### With Formula Evaluation

```cpp
#include "generated_spreadsheet.h"

int main() {
    SpreadsheetData data;
    FormulaEvaluator evaluator;
    
    // Set up variables for formula evaluation
    evaluator.setVariable("A1", data.getCell(0, 0));
    evaluator.setVariable("B1", data.getCell(0, 1));
    
    // Evaluate formula
    double result = evaluator.evaluate("A1 + B1 * 2");
    
    return 0;
}
```

### CMake Integration

The generated CMakeLists.txt provides these targets:

```cmake
# Main library target
add_library(spreadsheet_data ${SOURCES})

# Example executable (if examples are generated)
add_executable(spreadsheet_example example.cpp)
target_link_libraries(spreadsheet_example spreadsheet_data)

# Testing target (if tests are enabled)
add_executable(spreadsheet_tests tests.cpp)
target_link_libraries(spreadsheet_tests spreadsheet_data)
```

## Error Handling

### Exception Types

The system defines several custom exceptions:

```python
class SpreadsheetParseError(Exception):
    """Raised when spreadsheet parsing fails"""
    pass

class CodeGenerationError(Exception):
    """Raised when C++ code generation fails"""
    pass

class FileOperationError(Exception):
    """Raised when file operations fail"""
    pass
```

### Error Recovery

The system includes error recovery mechanisms:

1. **Partial parsing**: Continue processing despite cell-level errors
2. **Graceful degradation**: Fall back to simpler code generation if advanced features fail
3. **Validation**: Check generated code syntax before writing files

## Extensibility

### Adding New File Formats

To add support for new spreadsheet formats:

1. Create a new parser module in the `src/spreadsheet_to_cpplib/` directory
2. Implement the required parsing interface
3. Register the new format in the main dispatcher

### Custom Templates

To create custom code generation templates:

1. Inherit from the base template class
2. Implement the required generation methods
3. Register the template with the template manager

### Plugin System

The system supports plugins for extending functionality:

```python
def register_plugin(plugin_class: Type[Plugin]) -> None
```
Registers a new plugin for additional processing capabilities.