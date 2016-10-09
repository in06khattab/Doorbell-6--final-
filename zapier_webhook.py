#!/usr/bin/env python
import requests, time
import sys
import os
from time import gmtime, strftime

message= {'key1': sys.argv[1], 'key2': strftime("%d.%m.%Y")}  # strftime("%l:%M %p on %d.%m.%Y")
r = requests.post('https://zapier.com/hooks/catch/oq4af0/', data=message)
# print r.status_code
print r.content