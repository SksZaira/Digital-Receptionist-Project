import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
scope = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file']
cred = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(cred)
sheet = client.open('Contact Information (Responses)').sheet1
# data = sheet.get_all_records()
# print(data)
data = sheet.get_all_values()
headers = data.pop(0)

df = pd.DataFrame(data, columns=headers)
print(df)

# def appendRow(val):
#     sheet.append_row(val)
# def if_motion():
#     state = G.input(2)
#     if state == 1:
#         return True
#     else:
#         return False

# def send_data_to_cloud(tsk):
#     aio = Adafruit_IO.Client("Zaira","aio_bBxI16gQjOR39CwS64EBMXB2m8aT")
#     aio.send('visitors',tsk)
# a=67
# send_data_to_cloud(a)