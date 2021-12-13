
class MortgageCalculator:
    def __init__(self):
        self.r = float(input("What is the annual rate, percent? "))/100/12
        self.p = int(input("What is the amount to be lent? "))
        self.n = int(input("What is the period of the mortgage, years? "))*12

    def calculate_payment(self):
        return str(round((self.r/(1-(1+self.r)**-self.n))*self.p, 2))

    def __repr__(self):
        return "You want to take a loan of ${loan} for {years} years. Your monthlty payment will be ${payment}.".format(loan=self.p, years=self.n/12, payment=self.calculate_payment())


calc = MortgageCalculator()
print(calc)
