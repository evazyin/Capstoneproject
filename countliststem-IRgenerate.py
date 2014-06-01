'''version2 4/22
1 read in a list of keyword
2 read in a preprocessed dataset (this time stem and lower case)
3 do rough search
4 generate two corpus: IR(temporary) and EC(from IR, temporary, should not be)(in another file for EC)
'''

file = open('D:/uw course/capstone/mypersonality/status_a_stem.txt','r')
file1 = open('D:/uw course/capstone/mypersonality/wordlist_stem.txt','r')
file2 = open('D:/uw course/capstone/mypersonality/IRtest3.txt','w')
#file3 = open('D:/uw course/capstone/mypersonality/ECtest2.txt','w')

total = -1 #header only status_a.csv have one line for header
nostalgic = 0
keywordstr = file1.readline()
keywordlist = keywordstr.split(",")
#print(keywordlist[1])

while 1:   
    line = file.readline()
    if not line:
        break
    
    #lineStr = str( line, encoding='latin-1' )

    defaultsenti = 0
    for i in range(0,len(keywordlist)-1):
        if line.find(keywordlist[i])>-1:
            defaultsenti+=1
    if defaultsenti > 0:
        nostalgic+=1
        file2.write(line)
        file2.write('\n')
    total+=1


    '''if (lineStr.find('do you remember when')>-1)|(lineStr.find('down memory lane')>-1)|(lineStr.find('flashback')>-1)|(lineStr.find('go back in time')>-1)|(lineStr.find('good old days')>-1)|(lineStr.find('I miss those days')>-1)|(lineStr.find('nostalgic')>-1)|(lineStr.find('recollect')>-1)|(lineStr.find('redolent of')>-1)|(lineStr.find('relive the past')>-1)|(lineStr.find('reminiscent')>-1)|(lineStr.find('when we were younger')>-1)|(lineStr.find('those were the days')>-1):
        nostalgic+=1
    total+=1'''
    #file1.write('%d %d\n' %(total, nostalgic))
    
    '''print(total)
    print(lineStr)
    if nostalgic == 1:
        break'''
    
    del line
    

file.close()
file1.close()
file2.close()
#file3.close()
print(total)
print(nostalgic)




