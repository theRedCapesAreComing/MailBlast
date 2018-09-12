'''
Created on Sep 11, 2018

@author: vinay
'''
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a simple spreadsheet
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'


def main():
    """
    Shows basic usage of the Sheets API.
    prints values from a sample spreadsheet.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials_sheets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))
    
    # Call the Sheets API
    SPREADSHEET_ID = '1Yld-GRY7YSvyJhydSJgbWOzDyR2F5RWCSaaugWcFL20'
    RANGE_NAME = 'IIT!E2:E4'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    
    values = result.get('values', [])
    
    if not values:
        print('No data found.')
    else:
        print('Email ID:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4. 
            print('%s' % (row[0]))
            
if __name__ == '__main__':
    main()
