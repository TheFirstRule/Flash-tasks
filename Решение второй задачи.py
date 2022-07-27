f = open('Файл для флешовских заданий 2.txt')
ch = ''
flag = 0
k = 0
for line in f:
    s = line
    if 'S' in s and 'F' in s:
        for i in range(len(s)):
            if s[i].isdigit() == False:
                if s[i] != 'F':
                    ch = ''
                    flag = 0
                if s[i] == 'S':
                    flag = 1
            if s[i].isdigit() == True and flag == 1:
                ch += s[i]
            if s[i] == 'F' and ch != '':
                if int(ch) % 1007 == 0:
                    print(ch)
                    k += 1
                    ch = ''
                    break
            if s[i] == 'F':
                ch = ''
print(k)

