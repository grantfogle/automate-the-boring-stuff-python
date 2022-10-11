import re
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print(isPhoneNumber('720-489-9099'))
print(isPhoneNumber('cash'))

message = 'Call me at 720-940-2355 for a good time, or at 420-879-2345'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number is found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find number')    

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search(message)
print(mo.group())
print(phoneNumberRegex.findall(message))