class CompoundInterest:
    def __init__(self, p, r, t, m = 0):
        self.p = p
        self.r = r
        self.n = 12
        self.t = t
        self.m = m

    
    def calculator(self):
        return round(self.p * (1 + self.r/self.n )**(self.n * self.t), 2)

    def calculator_with_contributions(self):
        final_amount_from_contributions =  (self.m * ((((1 + (self.r / self.n)) ** (self.t * self.n)) - 1) / (self.r / self.n))) * (1 + (self.r / self.n))
        return round(final_amount_from_contributions + self.calculator(), 2)

