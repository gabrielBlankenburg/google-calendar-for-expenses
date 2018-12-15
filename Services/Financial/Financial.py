class Financial:
	def calculate(self, income, expenses):
		incomeTotal = 0
		expensesTotal = 0

		for i in income:
			incomeTotal += float(i)

		for i in expenses:
			expensesTotal += float(i)

		return incomeTotal - expensesTotal