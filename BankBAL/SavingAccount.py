from BankBAL.Accounts import CAccount
from BusinessEntities.BankEntities import CBusinessEntities
from BankDAL.SavingAccountDB import SavingAccDB

class SavingAccounts(CAccount):
    'Saving Accounts Class'
    # Data Members
    __balance = 0.0

    # Constructor Regions
    
    # def __init__(self):
    #     __balance =0.0
    # def Contructor1(self, accno, accname, acctype, amount):
        # objbst = CBusinessEntities()
        # objbst.mSetAccno(accno)
        # objbst.mSetAccname(accname)
        # objbst.mSetAcctype(acctype)
        # objbst.mSetAmount(amount)
        # self.__balance = amount

    def __init__(self, accno = None, accname= str(), acctype = str(), amount= float()):
        objbst = CBusinessEntities()
        objbst.mSetAccno(accno)
        objbst.mSetAccname(accname)
        objbst.mSetAcctype(acctype)
        objbst.mSetAmount(amount)
        self.__balance = amount

    # Method Region
    def mDeposit(self, accno, accname, amount):
        self.__balance += float(amount)

    def mWithdraw(self, accno, accname, amount):
        self.__balance -= float(amount)

    def mGetBalance(self):
        return self.__balance
    def mInsertDataBal(self, beobj = CBusinessEntities()):
        savobj=SavingAccDB()
        savobj.mInsertData(beobj)
    def mUpdateDataBal(self,beobj = CBusinessEntities()):
        savobj = SavingAccDB()
        savobj.mUpdateData(beobj)
    def mDeleteDataBal(self, accno):
        savobj = SavingAccDB()
        savobj.mDeleteData(accno=accno)
    def mSearchDataBal(self,accno):
        savobj = SavingAccDB()
        return savobj.mSearchDataSingle(accno = accno)
    def mSearchDataAllBal(self):
        savobj=SavingAccDB()
        return savobj.mSearchDataAll()