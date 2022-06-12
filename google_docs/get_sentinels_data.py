from __future__ import print_function
from auth import get_google_credentials_through_oath2, get_mysql_client
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



# The ID of a sample document.
DOCUMENT_ID = '1bVppJL4rC5lWULLGZ7AP5xH6YZLYsv86Wme1SpU6agE'
RANGE = 'Form Responses 4!A1:AL20'


def main():

    client=get_mysql_client()

    creds = get_google_credentials_through_oath2()

    try:
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=DOCUMENT_ID,
                                    range=RANGE).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        first_row = True
        for row in values:
            if first_row:
                column_name_mapping = {index: value for index, value in enumerate(row)}
                first_row = False
            else:
                for index, column in enumerate(row) :
                    print(f"{column_name_mapping.get(index)}: {column}")

    except HttpError as err:
        print(err)




if __name__ == '__main__':
    main()