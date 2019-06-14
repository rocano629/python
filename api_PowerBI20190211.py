import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import time
import random
import pyodbc
import sys

##class for data_generation


def data_generation():

  
    conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=PHLSQLSRV01\SPROD_RPT01;"
    "Database=AE_DASHBOARD;"
    "Trusted_Connection=yes;"
    )

    cursor = conn.cursor()
    cursor.execute("EXEC uspAEDashboardGetSummaryStreaming")
    
    for row in cursor:
        total = row
    
    rowAsList = [x for x in row]

    return [row[0], row[1],row[2], row[3]] 




if __name__ == '__main__':

    REST_API_URL = 'https://api.powerbi.com/beta/cd2b9300-f45b-433a-a80d-1aeb781aa03c/datasets/caa159aa-f238-445c-afbf-9cfc4f1a0cc8/rows?key=vBJQ4LLBlRik9FsqVc%2FmPfhkZkgnpMW%2FOhKzAHcw%2FObgKY0kc4glWAXuTMCs%2BuwNTsm%2F6NskxbdxQ5kIlqAv0Q%3D%3D'

    while True:
        data_raw = []
        for i in range(1):
            try:
                row = data_generation()
                data_raw.append(row)
                print("Raw data - ", data_raw)
            except:
                e = sys.exc_info()[0]
                print( "<p>Error: %s</p>" % e )

        # set the header record
        HEADER = ["total","LeadsUS","LeadsEMEA","LeadsAPAC"]

        data_df = pd.DataFrame(data_raw, columns=HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        print("JSON dataset", data_json)

        # Post the data on the Power BI API
        try:
            req = requests.post(REST_API_URL, data_json)
        except:
            e = sys.exc_info()[0]
            print( "<p>Error: %s</p>" % e )

        print("Data posted in Power BI API")
        time.sleep(10)

