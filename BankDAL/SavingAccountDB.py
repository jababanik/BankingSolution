from BusinessEntities.BankEntities import CBusinessEntities
from pymongo import MongoClient
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient(port=27017)
db = client.BankingDB
class SavingAccDB:

    def mInsertData(self,cbeobj= CBusinessEntities()):
        accobj={'Acc_no':  cbeobj.mGetAccno(),
                'Acc_Name': cbeobj.mGetAccname(),
                'Acc_Type': cbeobj.mGetAcctype(),
                'Amount': cbeobj.mGetAmount()
                }
        db.Account.insert_one(accobj)
    def mUpdateData(self,  cbeobj= CBusinessEntities()):
        db.Account.update_one({'Acc_no':  cbeobj.mGetAccno()},{"$set":
                              {'Acc_Name': cbeobj.mGetAccname(),
                              'Acc_Type': cbeobj.mGetAcctype(),
                              'Amount': cbeobj.mGetAmount()}},
                              upsert = True
                              )
    def mDeleteData(self, accno):
        del_record = db.Account.delete_many({"Acc_no": accno})
    def mSearchDataSingle(self, accno):
        singlerecord = db.Account.find_one({'Acc_no' : accno})
        return singlerecord
    def mSearchDataAll(self):
        allrecord = db.Account.find()
        return allrecord