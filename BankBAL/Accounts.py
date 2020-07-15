class CAccount:
    'This Class will act as base class for other classes'
    __balance = 0

    def __init__(self):
        self.__balance = 0

    def mdeposit(self, accno, accname, amount):
        pass

    def mwithdraw(self, accno, accname, amount):
        pass

    def mgetBalance(self):
        return self.__balance



