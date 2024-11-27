import os
import re
ffreader = open('ff.txt',mode='r',encoding='utf-8')
ffwriter = open('ffwriter.txt',mode='w',encoding='utf-8')
lines = ffreader.readlines()
newline = ' '
for line in lines:
    newline = re.search(r'^[\u4e00-\u9fa5]+：', line)
    if newline:
        ffwriter.write(line)
ffreader.close()
ffwriter.close()


