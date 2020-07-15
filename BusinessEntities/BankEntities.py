class CBusinessEntities:
    #Data Members
    __accno = 0
    __accname=''
    __acctype=''
    __amount=0.0
    def __init__(self):
        __accno = 0
        __accname=''
        __acctype=''
        __amount=0.0
    # Get and Set Methods
    def mSetAccno(self,accno):
        self.__accno=accno
    def mGetAccno(self):
        return self.__accno
    def mSetAccname(self,accname):
        self.__accname=accname
    def mGetAccname(self):
        return self.__accname
    def mSetAmount(self, amount):
         self.__amount=amount
    def mGetAmount(self):
        return self. __amount
    def mSetAcctype(self,acctype):
        self.__acctype=acctype
    def mGetAcctype(self):
        return self.__acctype
    def mGetAcctype(self):
        return self.__acctype

