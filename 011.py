"""
Module to calculate compound Interest.
"""

class CompoundInterest:
    rate:float = 0
    principal:float = 0
    amount:float = 0
    interest:float = 0
    time:float = 0
    time_counter:int = 0

    def __init__(self, rate:float=0, principal:float=0, time:float=0):
        self.rate = rate
        self.principal = principal
        self.time = time

    def calculate_amount(self):
        self.amount = self.principal * (
            (
                1 + (
                        self.rate/100
                    )
            )**self.time
        )
        return self.amount

    def alt_amount(self):
        while self.time_counter < self.time:
            self.amount = self.principal + ((self.rate/100)*self.principal)
            self.principal = self.amount
            self.time_counter = self.time_counter + 1
        
        self.time_counter = 0
        return self.amount

        


def main():
    rate = 8.22 #in percantage
    principal = 10_000_000 #amount to check
    time = 15 #in years
    amt = CompoundInterest(rate=rate, principal=principal, time=time)
    amount = amt.calculate_amount()
    alt_amount = amt.alt_amount()


    print(amount)
    print(alt_amount)

if __name__=="__main__":
    main()


