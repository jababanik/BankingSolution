from BankBAL.SavingAccount import SavingAccounts
from BusinessEntities.BankEntities import CBusinessEntities
from tkinter import *
parent = Tk()
import tkinter.messagebox
beobj = CBusinessEntities()
#beobj1 = CBusinessEntities()
# beobj1 = {}
def depositClick():
    tkinter.messagebox.showinfo("Deposit", txtaccno.get() )
def withdrawClick():
    pass
def balanceClick():
    pass
def mInsertData():
    mBindData()
    savobjbal=  SavingAccounts(beobj.mGetAccno(), beobj.mGetAccname(), beobj.mGetAcctype(), beobj.mGetAmount())
    savobjbal.mInsertDataBal(beobj)
def mUpdateData():
    mBindData()
    savobjbal = SavingAccounts(beobj.mGetAccno(), beobj.mGetAccname(), beobj.mGetAcctype(), beobj.mGetAmount())
    savobjbal.mUpdateDataBal(beobj)
def mDeleteData():
    mBindData()
    savobjbal =  SavingAccounts(beobj.mGetAccno(), beobj.mGetAccname(), beobj.mGetAcctype(), beobj.mGetAmount())
    mydata = savobjbal.mDeleteDataBal(beobj.mGetAccno())
def mSelectAll():
    savobjbal = SavingAccounts(beobj.mGetAccno(), beobj.mGetAccname(), beobj.mGetAcctype(), beobj.mGetAmount())
    mydata=savobjbal.mSearchDataAllBal()

def mSelectOne():
    mBindData()

    # beobj.mSetAccno(txtaccno.get())
    savobjbal = SavingAccounts(beobj.mGetAccno(), beobj.mGetAccname(), beobj.mGetAcctype(), beobj.mGetAmount())
    # print(beobj.mGetAccno())
    d = savobjbal.mSearchDataBal(beobj.mGetAccno())
    #txtaccno.insert(0,d["Acc_no"])
    txtname.insert(0, d["Acc_Name"])
    txtacctype.insert(0,d["Acc_Type"])
    txtamt.insert(0, d["Amount"])

def mBindData():
    #beobj= CBusinessEntities()
    beobj.mSetAccno(txtaccno.get())
    beobj.mSetAccname(txtname.get())
    beobj.mSetAcctype(txtacctype.get())
    beobj.mSetAmount(txtamt.get())
def mShowData():
    mBindData()
    savobjbal=  SavingAccounts(beobj.mGetAccno(), beobj.mGetAccname(), beobj.mGetAcctype(), beobj.mGetAmount())
    d = savobjbal.mSearchDataBal(beobj.mGetAccno())  
    textaccno = beobj.mGetAccno()
    textname = beobj.mGetAccname()
    textacctype = beobj.mGetAcctype()
    txtamt = beobj.mGetAmount()
    
lblbankname = Label(parent, text="ABC Bank Ltd")
lblbankname.grid(row=0, column=1)
lblaccno = Label(parent, text="Account No").grid(row=1, column=1)
lblname = Label(parent, text="Account Holder Name").grid(row=2, column=1)
lblacctype = Label(parent, text="Account Type").grid(row=3, column=1)
lblamt = Label(parent, text="Amount").grid(row=4, column=1)
txtaccno = Entry(parent)
txtaccno.grid(row=1, column=2)
txtname = Entry(parent)
txtname.grid(row=2, column=2)
txtacctype = Entry(parent)
txtacctype.grid(row=3, column=2)
txtamt = Entry(parent)
txtamt.grid(row=4, column=2)

btndeposit = Button(parent, text="Deposit", command=depositClick)
btndeposit.grid(row=5, column=1, columnspan=3)
btnwithdraw = Button(parent, text="Withdraw", command=withdrawClick)
btnwithdraw.grid(row=5, column=2)
btnbalance = Button(parent, text="Balance", command=balanceClick)
btnbalance.grid(row=5, column=3)
btnInsertData = Button(parent, text="Add", command=mInsertData)
btnInsertData.grid(row=6, column=1)
btnUpdateData = Button(parent, text="Update", command=mUpdateData)
btnUpdateData.grid(row=6, column=2)
btnDeleteData = Button(parent, text="Delete", command=mDeleteData)
btnDeleteData.grid(row=6, column=3)
btnSearchAllData = Button(parent, text="Search All", command=mSelectAll)
btnSearchAllData.grid(row=6, column=4)
btnSearchOneData = Button(parent, text="Search Single", command=mSelectOne)
btnSearchOneData.grid(row=6, column=5)
parent.mainloop()

