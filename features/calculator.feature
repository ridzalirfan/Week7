Feature: Calculator
	Validate all operations by the calculator.

	Background: Common Steps
		Given the calculator is initialised

	Scenario: Addition
		When I add 5 and 2
		Then the result should be 7

	Scenario: Subtraction
		When I subtract 10 from 50
		Then the result should be 40

	Scenario: Multiplication
		When I multiply 5 and 3
		Then the result should be 15

	Scenario: Division
		When I divide 10 by 5
		Then the result should be 2


#
