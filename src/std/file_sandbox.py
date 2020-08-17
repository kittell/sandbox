f = open('testfile.txt', 'w+')

for i in range(10):
    f.write('line' + str(i) + '\r\n')
    
f.close()