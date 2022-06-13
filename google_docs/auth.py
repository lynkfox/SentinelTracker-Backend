from __future__ import print_function

import os.path

import boto3
import json
import mysql.connector
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google_aws_common import SqlTables 
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


def get_google_credentials_through_oath2():
    """
    uses Oath2 and logs a user into the google api services.
    """
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def get_mysql_client():

    client = boto3.client("secretsmanager")

    response = client.get_secret_value(
        SecretId="InstanceSecret478E0A47-adqUOEATZRYd"
    )

    secrets = json.loads(response['SecretString'])

    return mysql.connector.connect(
        host=secrets['host'], user=secrets['username'], password=secrets['password'], database=SqlTables.STATISTICS_DB_NAME
    )
