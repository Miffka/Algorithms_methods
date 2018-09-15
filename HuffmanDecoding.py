#-*-coding:utf8;-*-
#qpy:3
#qpy:console

codes = [] # создаем список для считывания кодировок
codesD = {} # и словарь для тех же целей в формате КОД:БУКВА
s = "" # строка с ответом
code = "" 

k, l = input().split()
k = int(k)
l = int(l)

# считываем список кодировок
for i in range(k):
    codes.append([i for i in input().split(": ")])

# читаем строку с кодировкой
sc = input()

# заполняем словарь кодировок
for i in range(k):
    codesD[codes[i][1]] = codes[i][0]

for i in sc:
    code += i
    if code in codesD.keys():
        s += codesD[code]
        code = ""

print(s)