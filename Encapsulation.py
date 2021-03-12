class Account(Exception):
    pass

class bank_account():
    def __init__(self, accnum):
        self.__accnum = accnum
        self.__balance = 0

    @property
    def accnum(self):
        return self.__accnum

    @property
    def balance(self):
        return self.__balance

    @accnum.setter
    def accnum(self, amount):
        raise Account("Cannot change account number")

    @accnum.deleter
    def accnum(self):
        if self.__balance > 0:
            raise Account("Cannot delete account with balance greater than Zero")

    @balance.setter
    def balance(self, amount):
        if (self.__balance + amount) < 0:
            raise Account("Cannot go into negative balance")
        elif amount >= 100000:
            print(f"please note the large amount of {amount} will be logged")
            self.__balance += amount
        else:
            self.__balance += amount

    @balance.deleter
    def balance(self):
        raise Account("Cannot delete account balance field")


acc1 = bank_account('123456')
print(acc1.accnum)

acc1.balance = 1000
print(acc1.balance)

try:
    acc1.balance = -1200
except Account as e:
    print(e)

try:
    acc1.accnum = '45789'
except Account as e:
    print(e)

acc1.balance = 100000
print(acc1.balance)

try:
    del acc1.accnum
except Account as e:
    print(e)
