password = 'swordfisssh'

if password == 'swordfish':
    print('Access granted')
elif password == 'swordfissh':
    print('close but no cigar')
else:
    print('wrong password')

spam = 0
while spam < 5:
    print('Hello world')
    spam = spam + 1

name = ''
while name != 'your name':
    print('please type your name')
    name = input()
print('Thank you')