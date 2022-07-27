s = open('Файл для флешовских заданий 3.txt').readline()
count = 0
for l in range(1, 10):
        for i in range(len(s) + 1 - l):
            s1 = s[i: i + l]
            if s1.count('Z') == s1.count('X') == s1.count('C') == l // 3:
                count += 1
print(count)
