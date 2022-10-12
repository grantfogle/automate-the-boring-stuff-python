helloFile = open('/Users/grantfogle/Desktop/workspace/learnings/automate-the-boring-stuff/hello.txt')

print(helloFile.read())

helloFile = open('/Users/grantfogle/Desktop/workspace/learnings/automate-the-boring-stuff/hello.txt', 'w')
helloFile.write('Heyyyyyyy\n')
helloFile.write('BACOOOON\n')
helloFile.close()