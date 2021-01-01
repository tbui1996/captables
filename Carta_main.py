import os
import pandas as pd
import datetime
from datetime import datetime as dt
import json
import numpy as np
import sys

class CSV_reader(object):
    def __init__(self):
        fileinput = str(input("Enter the full path and name of your capitalization .csv file: "))
        if not ".csv" in fileinput:
            fileinput += ".csv"
        try:
            with open(fileinput) as f:
                self.data = pd.read_csv(fileinput)
        except FileNotFoundError:
            print('File does not exist')
            sys.exit()

    def readCLI(self):
        if len(sys.argv) != 2:
            dateobject = dt.today().strftime('%Y-%m-%d')
            return dateobject
        else:
            dt_obj = datetime.datetime.strptime(sys.argv[1], '%m/%d/%Y')
            dt_str = datetime.datetime.strftime(dt_obj, '%Y-%m-%d')
            return dt_str

    def dateFormat_forJSON(self):
        if len(sys.argv) != 2:
            dateobject=dt.today().strftime('%m/%d/%Y')
            return dateobject
        else:
            dt_obj = datetime.datetime.strptime(sys.argv[1], '%m/%d/%Y')
            dt_str = datetime.datetime.strftime(dt_obj, '%m/%d/%Y')
            return dt_str

    def beginAnalyzing(self):
        date_tocompare_against = self.readCLI()
        date_pandas = pd.to_datetime(date_tocompare_against)
        self.data['INVESTMENT DATE'] = pd.to_datetime(self.data['INVESTMENT DATE'])
        df = self.data[self.data['INVESTMENT DATE'] < pd.to_datetime(date_pandas)]
        cash_raised = df['CASH PAID'].sum()
        total_number_of_shares = df['SHARES PURCHASED'].sum()
        return df, cash_raised, total_number_of_shares

    def Build_DataTable(self):
        df = self.beginAnalyzing()
        sharespurchased = df[0].groupby('INVESTOR')['SHARES PURCHASED'].sum()
        ownership = (sharespurchased/df[2])*100
        summarization = df[0].groupby('INVESTOR').agg(shares_purchased=pd.NamedAgg(column='SHARES PURCHASED', aggfunc=sum),
                                                      cash_paid=pd.NamedAgg(column='CASH PAID', aggfunc=sum))
        summarization['ownership'] = ownership
        return summarization

    def write_to_json(self):
        datetime = self.dateFormat_forJSON()
        cashraised = self.beginAnalyzing()
        ownership = self.Build_DataTable()
        ownership_tojson = ownership.reset_index().to_json(orient="records")
        parsed_data = json.loads(ownership_tojson)
        output_jsonfile = {
            "date": datetime,
            "cash_raised": cashraised[1],
            "total_number_of_shares": cashraised[2],
            "ownership": parsed_data
        }
        return output_jsonfile

    def AskUserForOutputFileLocationAndFileName(self):
        jsonfile_output = self.write_to_json()
        myDir = input("Enter the full path where you want to save the file. For example, C:/Users/username/desktop : ")
        while not os.path.exists(myDir):
            print("Invalid path")
            myDir = input("Enter the full path where you want to save the file. For example, C:/Users/username/desktop : ")
        filename = input("Enter the name for your summary cap table output .json file. For example, CapTable.json : ")
        if not ".json" in filename:
            filename += ".json"
        with open(os.path.join(myDir, filename), 'w') as out_file:
            json.dump(jsonfile_output, out_file, cls=NpEncoder)
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


if __name__ == "__main__":
    csv = CSV_reader()
    dateinput = csv.readCLI()
    stru, x, y = csv.beginAnalyzing()
    summarization = csv.Build_DataTable()
    csv.write_to_json()
    csv.AskUserForOutputFileLocationAndFileName()
