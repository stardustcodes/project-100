class ATM(object):
    def __init__(self, card, card_number, pin_number):
        self.card=card 
        self.card_number=card_number
        self.pin_number=pin_number

    def CashWithdrawal(self):
        print("Withdraw cash.")

    def BalanceEnquiry(self):
        print("Show user's balance.")
        