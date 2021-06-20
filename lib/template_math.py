import sys

template_math = """
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
"""
