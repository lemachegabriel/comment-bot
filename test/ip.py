import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from pprint import pprint


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)

client = gspread.authorize(creds)

sheet = client.open("users").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records
obj1 = json.dumps(data)
obj = json.loads(obj1)
pprint(data)
for emails in obj1:
    print(obj('Email'))


'''
row = sheet.row_values(2)  # Get a specific row
col = sheet.col_values(1)  # Get a specific column
cell = sheet.cell(1,2).value  # Get the value of a specific cell



insertRow = ["hello", 5, "red", "blue"]
sheet.add_rows(insertRow, 4)  # Insert the list as a row at index 4

sheet.update_cell(2,2, "CHANGED")  # Update one cell

numRows = sheet.row_count  # Get the number of rows in the sheet
'''