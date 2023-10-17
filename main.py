
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)
for i in range(1,len(contacts_list)):
    for y in range(0, 3):
        if " " in contacts_list[i][y]:
            sp = re.split(" ", contacts_list[i][y])
            #print(sp)
            for j in range(len(sp)):
                contacts_list[i][y+j] = sp[j]
    #print(contacts_list[i])
for el in contacts_list:
    pattern = r"(\+7|8)?\s*(495|\(495\))\s*\-*(\d{,3})\-*(\d{,2})\-*(\d+)\s*\(*(доб\.*\s*\d{0,4})*\)*"
    num = re.sub(pattern, r"+7(495)\3-\4-\5 \6", el[5])
    #print(num)
    el[5] = num
    #print(el)
#pprint(sorted(contacts_list))
sp = sorted(contacts_list)
#pprint(sp)

contacts_list_new = []
for el in sp:
    for j in range(1,len(sp)):
        if el[0] == sp[j][0]:
            for n, inf in enumerate(sp[j]):
                if inf != "":
                    el[n] = inf

[contacts_list_new.append(x) for x in sp if x not in contacts_list_new]
pprint(contacts_list_new)
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(contacts_list_new)

