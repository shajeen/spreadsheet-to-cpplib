# Spreadsheet to C++ Library

[![PyPI version](https://badge.fury.io/py/spreadsheet-to-cpplib.svg)](https://badge.fury.io/py/spreadsheet-to-cpplib)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A powerful Python tool that converts spreadsheets (XLSM, CSV) into C++ library projects with full CMake support. Transform your spreadsheet calculations into high-performance C++ code with mathematical expression support.

![Tool Demo](https://user-images.githubusercontent.com/2623563/123547683-5a419d00-d77f-11eb-851d-cb4af8273df9.PNG)

## ✨ Features

- **Multi-format Support**: Convert XLSM and CSV files to C++ libraries
- **CMake Integration**: Generates complete CMake projects ready to build
- **Mathematical Expressions**: Optional support for formula calculations using C++ Mathematical Expression Toolkit
- **Header-only Option**: Generate header-only libraries for easy integration
- **Flexible Output**: Choose between source/header pairs or header-only libraries
- **Formula Preservation**: Maintain spreadsheet formulas as executable C++ code
- **Type Safety**: Configurable type handling for strings and numeric values

## 🚀 Quick Start

### Installation

Install from PyPI (recommended):
```bash
pip install spreadsheet-to-cpplib
```

Install from source:
```bash
pip install git+https://github.com/shajeen/spreadsheet-to-cpplib.git
```

### Basic Usage

```bash
# Convert an Excel file
spreadsheet-to-cpplib --file="your_spreadsheet.xlsm"

# Convert a CSV file
spreadsheet-to-cpplib --file="your_data.csv"
```

The tool will prompt you with configuration questions and generate the C++ library in an `output/` directory.

## 📋 Configuration Options

When you run the tool, it will ask you several questions to customize the output:

| Question | Description | Options |
|----------|-------------|---------|
| **Mathematical Expression Support** | Include C++ Mathematical Expression Toolkit for formula calculations | `yes` / `no` |
| **Header-only Library** | Generate as header-only library (easier integration) | `yes` / `no` |
| **Formula as String** | Keep formulas as strings in the generated code | `yes` / `no` |
| **String to Zero Conversion** | Convert string values to 0.0 in numeric contexts | `yes` / `no` |

## 📁 Project Structure

```
your-project/
├── src/
│   └── spreadsheet_to_cpplib/     # Main source code
├── docs/                          # Documentation
├── tests/                         # Test files
├── example/                       # Usage examples
│   ├── csv_example/
│   └── xlsm_example/
├── pyproject.toml                 # Modern Python packaging
├── setup.py                       # Legacy setup (for compatibility)
├── README.md                      # This file
├── LICENSE                        # GPL-3.0 license
├── CONTRIBUTING.md                # Contribution guidelines
└── CODE_OF_CONDUCT.md            # Community guidelines
```

## 📖 Examples

### Excel (XLSM) Example
```bash
spreadsheet-to-cpplib --file="financial_model.xlsm"
```

This will create a C++ library with:
- Generated header and source files
- CMake configuration
- Mathematical expression support (if enabled)
- Preserved formulas as C++ functions

### CSV Example
```bash
spreadsheet-to-cpplib --file="data_table.csv"
```

Output includes:
- Structured C++ classes representing your data
- Accessor methods for each column
- Type-safe data handling

## 🔧 Development

### Prerequisites
- Python 3.8 or higher
- pip or poetry for dependency management

### Setting up Development Environment

```bash
# Clone the repository
git clone https://github.com/shajeen/spreadsheet-to-cpplib.git
cd spreadsheet-to-cpplib

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src/

# Type checking
mypy src/
```

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/spreadsheet_to_cpplib
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Quick Contribution Steps

1. **Open an Issue**: Describe your proposed changes or bug report
2. **Fork & Clone**: Fork the repository and clone your fork
3. **Create Branch**: Create a feature branch for your changes
4. **Make Changes**: Implement your changes with tests
5. **Test**: Ensure all tests pass and add new tests as needed
6. **Submit PR**: Create a pull request with a clear description

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

## 📚 Documentation

- **[User Guide](docs/user-guide.md)**: Detailed usage instructions
- **[API Documentation](docs/api.md)**: Developer reference
- **[Examples](example/)**: Sample projects and use cases
- **[Wiki](https://github.com/shajeen/spreadsheet-to-cpplib/wiki)**: Additional documentation and tutorials

## 🐛 Bug Reports & Feature Requests

- **[Report a Bug](https://github.com/shajeen/spreadsheet-to-cpplib/issues/new?assignees=shajeen&labels=bug&template=bug_report.md&title=)**
- **[Request a Feature](https://github.com/shajeen/spreadsheet-to-cpplib/issues/new?assignees=shajeen&labels=enhancement&template=feature_request.md&title=)**
- **[View Open Issues](https://github.com/shajeen/spreadsheet-to-cpplib/issues)**

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 👥 Authors & Contributors

- **Sheik S Shajeen Ahamed** - *Creator & Maintainer* - [@shajeenahamed](https://twitter.com/shajeenahamed)

See the list of [contributors](https://github.com/shajeen/spreadsheet-to-cpplib/contributors) who participated in this project.

## 🙏 Acknowledgments

- [C++ Mathematical Expression Toolkit](http://www.partow.net/programming/exprtk/) for formula evaluation support
- [OpenPyXL](https://openpyxl.readthedocs.io/) for Excel file processing
- [Pandas](https://pandas.pydata.org/) for data manipulation

## 🔗 Links

- **Project Homepage**: [https://github.com/shajeen/spreadsheet-to-cpplib](https://github.com/shajeen/spreadsheet-to-cpplib)
- **PyPI Package**: [https://pypi.org/project/spreadsheet-to-cpplib/](https://pypi.org/project/spreadsheet-to-cpplib/)
- **Documentation**: [Wiki](https://github.com/shajeen/spreadsheet-to-cpplib/wiki)

---

**⭐ If this project helped you, please consider giving it a star on GitHub!**