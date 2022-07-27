text = open('Файл для флешовских заданий 1.txt')
s = text.readline()
sim, num, maxsim, maxnum = '','','','0'
for i in range(len(s)):
    if s[i].isdigit() == False:
        if num != '':
            if int(num) > int(maxnum):
                maxnum = num
                maxsim = sim
        num = ''
        sim = s[i]
    if s[i].isdigit() == True:
        if sim != '':
            num += s[i]
print(maxsim,maxnum, sep = '')
