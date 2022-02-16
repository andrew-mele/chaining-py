class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0
    
    def makeDeposit(self, amount):
        self.amount += amount
        return self

    def makeWithdrawal(self, amount):
        self.amount -= amount
        return self


    def displayUserAmount(self):
        print(f'User: {self.name}, Balance: ${self.amount} USD')
        return self



andrew = User('Andrew')

anna = User('Anna')

rob = User('Rob')

andrew.makeDeposit(20).makeDeposit(30).makeDeposit(500).makeWithdrawal(300).displayUserAmount()

anna.makeDeposit(50).makeDeposit(100).makeWithdrawal(75).makeWithdrawal(30).displayUserAmount()

rob.makeDeposit(5000).makeWithdrawal(500).makeWithdrawal(35).makeWithdrawal(405).displayUserAmount()
