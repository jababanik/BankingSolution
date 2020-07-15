from flask import Flask, flash, request, redirect
from flask import render_template
from BankBAL.SavingAccount import SavingAccounts
from BusinessEntities.BankEntities import CBusinessEntities
import os

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def ShowAllData():
    savobj = SavingAccounts()
    
    accdetails = savobj.mSearchDataAllBal()
    return render_template('ShowAllData.html', accdetails = accdetails)

@app.route('/SearchData/<string:accno>', methods = ["GET"]) # bydefault post method is used
def SearchData(accno):
    savobj = SavingAccounts()
    accdetail = savobj.mSearchDataBal(accno = accno)
    return render_template('SearchData.html', accdetail = accdetail)

@app.route('/add', methods = ["GET", "POST"])
def add():
    # request.querystring method for get method and request.form for post method
    if request.form:
        cbetobj = CBusinessEntities()
        cbetobj.mSetAccno(request.form.get("Acc_no")) # same as form name in html form, database col name
        cbetobj.mSetAccname(request.form.get("AccName"))
        cbetobj.mSetAcctype(request.form.get("TranType"))
        cbetobj.mSetAmount(request.form.get("Amount"))
        savobj = SavingAccounts()
        savobj.mInsertDataBal(cbetobj)
    return render_template('home.html')

@app.route('/updateData/<string:accno>', methods = ["GET", "POST"])
def updateData(accno):
    savobj = SavingAccounts()
    accdetail = savobj.mSearchDataBal(accno = accno)
    return render_template('Edit.html', accdetail = accdetail)

# check if data was entered or not so we take it to show data

@app.route('/update', methods = ["POST"])
def update():
    cbetobj = CBusinessEntities()
    cbetobj.mSetAccno(request.form.get("Acc_no")) # same as form name in html form, database col name
    cbetobj.mSetAccname(request.form.get("AccName"))
    cbetobj.mSetAcctype(request.form.get("TranType"))
    cbetobj.mSetAmount(request.form.get("Amount"))
    savobj = SavingAccounts()
    savobj.mUpdateDataBal(cbetobj)
    accdetails = savobj.mSearchDataAllBal()
    return render_template('ShowAllData.html', accdetails = accdetails)

@app.route('/DeleteData/<string:accno>', methods = ["GET", "POST"])
def DeleteData(accno):
    savobj = SavingAccounts()
    accdetail = savobj.mSearchDataBal(accno = accno)
    return render_template('Delete.html', accdetail = accdetail)

# check if data was entered or not so we take it to show data

@app.route('/delete', methods = ["GET","POST"])
def delete():
    accno = request.form.get("Acc_no")
    savobj = SavingAccounts()
    savobj.mDeleteDataBal(accno=accno)
    accdetails = savobj.mSearchDataAllBal()
    return render_template('ShowAllData.html', accdetails = accdetails)

# def HelloWOrld():
#     return "Welcome to my Firsst Flask App"
if __name__ == '__main__':
    app.run(debug = True)