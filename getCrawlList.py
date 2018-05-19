
import unicodedata
import tomd
import pickle
import requests
import re
import mysql.connector
import SimulateChrome

class dbHelper:

    def __init__(self):
        self.connection = mysql.connector.connect(user="huangyun",password="huangyun",host="192.168.1.112",database="pythondb")
        self.cursor = self.connection.cursor()

    def getColumnList(self):
        args = [10]
        procedureName="getNewColumnList"
        self.cursor.callproc(procedureName,args )
        for resultset in self.cursor.stored_results():
            for datarow in resultset.fetchall():
                print( str(datarow[0])+":"+datarow[1]+":"+datarow[2])
                SimulateChrome.main(datarow[1],datarow[2])
                self.uptColumnStatus(datarow[0])

    def uptColumnStatus(self,columnId):
        args =[columnId,1]
        procedureName='uptColumnStatus'
        self.cursor.callproc(procedureName,args)
        self.connection.commit()


if __name__ =="__main__":
    dbHelperLocal =  dbHelper()
    dbHelperLocal.getColumnList();