class atm:
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    def cashWithdrawl(self):
        print("The cash is withdrawn succesfully")
    def cashDeposit(self):
        print("The cash has been deposited succesfully")

myCard = atm(123456789, 456)
print(myCard.cardNumber)