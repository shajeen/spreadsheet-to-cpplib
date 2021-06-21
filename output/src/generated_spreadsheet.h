
// automatic generated file

/*
 ******************************************************************
 *           C++ Spreadsheet-to-libcpp Library                    *
 *                                                                *
 * Convert XLSM, CSV to C++ library project.                      *
 * URL: https://github.com/CodeAvailable/spreadsheet-to-cpplib    *
 ******************************************************************
*/

//  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
//  |S|p|r|e|a|d|S|h|e|e|t|-|t|o|-|c|p|p|l|i|b|
//  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

 #pragma once
 #include <vector>
 #include <string>
 #include "exprtk.hpp"
 

 namespace Workspace
 {
        
double calculateFormula(const std::string &formula)
{
	double result{ 0 };
	typedef exprtk::expression<double> expression_t;
	typedef exprtk::parser<double> parser_t;

	std::string expression_string = formula;
	expression_t expression;
	parser_t parser;

	if (parser.compile(expression_string, expression))
	{
		result = expression.value();
	}

	return result;
}


        std::vector<std::vector<double>> Instructions_array
{
{ 0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,1,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,2,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 },
{ 0.0,3,0.0,0.0 },
{ 0.0,0.0,0.0,0.0 }
};
std::vector<std::vector<double>> Orders_array
{
{ 0.0,0.0,0.0,0.0 },
{ 10001,0.0,0.0,51 },
{ 10002,0.0,0.0,93 },
{ 10003,0.0,0.0,46 },
{ 10004,0.0,0.0,62 },
{ 10005,0.0,0.0,49 },
{ 10006,0.0,0.0,53 },
{ 10007,0.0,0.0,47 },
{ 10008,0.0,0.0,76 },
{ 10009,0.0,0.0,114 },
{ 10010,0.0,0.0,57 }
};
std::vector<std::vector<double>> Lists_array
{
{ 0.0,0.0,0.0,0.0,0.0,0.0,0.0 },
{ 0.0,3,0.0,0.0,0.0,6,4 },
{ 0.0,0.0,0.0,0.0,0.0,3,3 },
{ 0.0,0.0,0.0,0.0,0.0,1,1 },
{ 0.0,0.0,0.0,0.0,0.0,5,4 },
{ 0.0,0.0,0.0,0.0,0.0,4,4 },
{ 0.0,0.0,0.0,0.0,0.0,2,2 },
{ 0.0,0.0,0.0,0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0,0.0,0.0,0.0 },
{ 0.0,0.0,0.0,0.0,0.0,0.0,0.0 }
};
std::vector<std::vector<double>> MyLinks_array
{
{ 0.0,0.0,0.0 },
{ 0.0,0.0,0.0 },
{ 0.0,0.0,0.0 },
{ 0.0,0.0,0.0 },
{ 0.0,0.0,0.0 },
{ 0.0,0.0,0.0 },
{ 0.0,0.0,0.0 },
{ 0.0,0.0,0.0 },
{ 0.0,0.0,0.0 }
};

 }
