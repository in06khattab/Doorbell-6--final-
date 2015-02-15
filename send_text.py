 #!/usr/bin/env python
import urllib
  
def sendSMS(to, message, hash):
    params = urllib.urlencode({'to': to, 'message' : message, 'hash': hash})
    f = urllib.urlopen('http://www.smspi.co.uk/send/', params)
    return (f.read(), f.code)
  
resp, code = sendSMS('07982721214', 'Testing', '34d7baa8713936f8cbe8419d508f8257')
print resp