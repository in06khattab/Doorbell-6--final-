import urllib2


def check_internet():
    try:
        header = {"pragma": "no-cache"}  # Tells the server to send fresh copy
        req = urllib2.Request("http://www.google.com", headers=header)
        urllib2.urlopen(req, timeout=2)
        print( "you are connected")
        return True
    except urllib2.URLError as err:
        print(err)
        
        
print(check_internet())
