This is a simple module that just extracts ip addresses using a simple regular expression.
Any form of 0.0.0.0 is considered valid so 999.999.999.999 is considered valid but 999.999.999.999.999 is not.
This includes a simple pytest unit test.
