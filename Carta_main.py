import sys
import csv
import os
from itertools import combinations
import pandas as pd
import datetime
from datetime import datetime as dt
from datetime import date
import calendar
import json
import numpy as np

filename = "test.json"
class CSV_reader(object):
    def __init__(self):
        fileinput = str(input("Which file do you want?(Must enter full file path location):"))
        if not ".csv" in fileinput:
            fileinput += ".csv"
        self.data = pd.read_csv(fileinput)

    def readCLI(self):
        if len(sys.argv) != 2:
            dateobject=dt.today().strftime('%Y-%m-%d')
            return dateobject
        else:
            dt_obj = datetime.datetime.strptime(sys.argv[1], '%m/%d/%Y')
            dt_str = datetime.datetime.strftime(dt_obj, '%Y-%m-%d')
            return dt_str

    def beginAnalyzing(self):
        date_tocompare_against = self.readCLI()
        date_pandas = pd.to_datetime(date_tocompare_against)
        self.data['INVESTMENT DATE'] = pd.to_datetime(self.data['INVESTMENT DATE'])
        df = self.data[self.data['INVESTMENT DATE'] < pd.to_datetime(date_pandas)]
        cash_raised = df['CASH PAID'].sum()
        total_number_of_shares = df['SHARES PURCHASED'].sum()
        return df, cash_raised, total_number_of_shares

    def ownership(self):
        df = self.beginAnalyzing()
        sharespurchased = df[0].groupby('INVESTOR')['SHARES PURCHASED'].sum()
        #sharespurchased = df[0].groupby('INVESTOR').apply(lambda x: x.to_json(orient='records'))
        cashpaid = df[0].groupby('INVESTOR')['CASH PAID'].sum()
        ownership = (sharespurchased/df[2])*100

        summarization = df[0].groupby('INVESTOR').agg(
            shares_purchased=pd.NamedAgg(column='SHARES PURCHASED',     aggfunc=sum),
            cash_paid=pd.NamedAgg(column='CASH PAID', aggfunc=sum))
        summarization['ownership'] = ownership
        return sharespurchased, cashpaid, ownership, summarization

    def write_to_json(self):
        datetime = self.readCLI()
        cashraised = self.beginAnalyzing()
        cashraised_tojson = cashraised[0].to_json()
        ownership = self.ownership()
        ownership_tojson = ownership[3].to_json(orient="index")
        parsed = json.loads(ownership_tojson)
        print(json.dumps(parsed, indent=4))

        obj ={
            "date": datetime,
            "cash_raised": cashraised[1],
            "total_number_of_shares": cashraised[2],
            "ownership":[{
                "investor": parsed
            }]
        }
        with open(filename, "w") as out_file:
            json.dump(obj, out_file, cls=NpEncoder)
        return filename


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

#used mainly for debugging#
if __name__ == "__main__":
    csv = CSV_reader()
    dateinput = csv.readCLI()
    #print(dateinput+"\n")
    stru,x,y = csv.beginAnalyzing()
    #print(stru)
    #print(x)
    #print(y)
    #print(str(csv.ownership())+"\n")
    sharespurchased, cashpaid, ownership, summarization = csv.ownership()
    #print(sharespurchased)
    #print(cashpaid)
    #print(ownership)
    print((csv.write_to_json()))

