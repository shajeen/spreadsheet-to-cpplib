# spreadsheet-to-cpplib
Convert XLSM, CSV to C++ library project.

### How it works

```bash
(venv) PS E:\github\personal\spreadsheet-to-cpplib> python .\spreadsheet-to-cpplib.py --file="sample/sample1.xlsm"
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|S|p|r|e|a|d|S|h|e|e|t|-|t|o|-|c|p|p|l|i|b|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Below sheets are found,
1. Sheet1
2. Sheet2

Answer [yes/no] for below questions.
1) Do you want Mathametical Expression library support for formula calculation ?: : yes
2) Configure as header-only library ? :: no
3) Get default value from formula as double.? :: yes
4) Make string as 0.0?. :: yes

Working please wait........
-> written: output/src/generated_spreadsheet.h
-> written: output/src/generated_spreadsheet.cpp
-> written: output/CMakeLists.txt
Done !, Please check output folder.
(venv) PS E:\github\personal\spreadsheet-to-cpplib>
```

### Bug report

if you face any issue or need any kind of other help. Please raise a issue.

### Contributing

Please read the [CONTRIBUTING](https://github.com/shajeen/spreadsheet-to-cpplib/blob/main/CONTRIBUTING.md) before raising the PR.

