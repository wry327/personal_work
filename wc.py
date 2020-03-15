import re
import easygui as g
f = open('my file.c','r',encoding='utf-8')
content = f.read()
contents = []
count_letter = 0
count_line = 0
contents.extend(content)
for i in contents:
    if i != ' ' and i != '\n':
        count_letter += 1
    if i == '\n':
        count_line += 1
f.close()
import easygui as g
choice = (g.buttonbox(msg = '您想查看什么内容？',title = '',choices = ('字符数','单词数','行数')))
if(choice == '字符数'):
    g.msgbox(msg = '文件中的字符数为:{}'.format(count_letter),title = '')
elif(choice == '单词数'):
    g.msgbox(msg = '文件中的单词数为:{}'.format(len(re.split(r'[\s]',content)),title = ''))
else:
    g.msgbox(msg = '文件中的行数为:{}'.format(count_line + 1),title = '')
