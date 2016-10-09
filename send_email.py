import base64
import httplib2
from time import gmtime, strftime
from email.mime.text import MIMEText

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

EMAIL = "in06khattab@gmail.com"  # change this

# Path to the client_secret.json file downloaded from the Developer Console
CLIENT_SECRET_FILE = '/usr/share/adafruit/webide/repositories/my-pi-projects/Doorbell/client_secret_935106472194-ntvvnbqtgcpnd2qu7akrk6g8tu225br4.apps.googleusercontent.com.json'

# Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.compose'

# Location of the credentials storage file
STORAGE = Storage('gmail.storage')

# Start the OAuth flow to retrieve credentials
flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=OAUTH_SCOPE)
http = httplib2.Http()

# Try to retrieve credentials from storage or run the flow to generate them
credentials = STORAGE.get()
if credentials is None or credentials.invalid:
    credentials = run(flow, STORAGE, http=http)

# Authorize the httplib2.Http object with our credentials
http = credentials.authorize(http)

# Build the Gmail service from discovery
gmail_service = build('gmail', 'v1', http=http)

# create a message to send
message = MIMEText(
    "Hi, \n\nSomeone knocked on your door at" + strftime("%l:%M %p on %d-%m-%Y") + ".\n\nHave a great day!")
message['to'] = EMAIL
message['from'] = "doorbellding@gmail.com"
message['subject'] = "Ding Dong at " + strftime("%l:%M %p on %d-%m-%Y")
body = {'raw': base64.b64encode(message.as_string())}

# send it
try:
    message = (gmail_service.users().messages().send(userId="me", body=body).execute())
    print('Message Id: %s' % message['id'])
    print(message)
except Exception as error:
    print('An error occurred: %s' % error)
