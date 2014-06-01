#revised 4/14/2014 import keywordlist
import codecs

file2= open('D:/uw course/capstone/mypersonality/postsfound.txt','w')
#file = codecs.open('D:/uw course/capstone/mypersonality/status_b.csv',errors='ignore')
file = codecs.open('C:/Downloads/fb_status_a.csv',errors='ignore')
file1 = open('D:/uw course/capstone/mypersonality/wordlist.txt')

total = -1 #header only status_a.csv have one line for header
nostalgic = 0
keywordlist = file1.readline()
keywords = keywordlist.split(",")
print(keywords)
while 1:   
    line = file.readline()
    if not line:
        break
    
    lineStr = str( line, encoding='latin-1' )

    defaultsenti = 0
    for i in range(0,len(keywords)-1):
        if lineStr.find(keywords[i])>-1:
            defaultsenti+=1
    if defaultsenti > 0:
        nostalgic+=1
        #print(line[2])
        file2.write(line[2])
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
    del lineStr

file.close()
file1.close()
file2.close()
print(total)
print(nostalgic)




