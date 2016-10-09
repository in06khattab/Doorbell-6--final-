import os
EMAIL = 'in06khattab@gmail.com'

os.system('sudo echo "jjj" | sendxmpp -v -t ' + EMAIL)  # send hangouts message
print(EMAIL)