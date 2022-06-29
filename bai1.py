# -*- coding: utf-8 -*-
import json
# Đọc file
fobj = open('input.txt')
c = json.load(fobj)
# Ghi file và xử lý
with open('output.txt', 'w') as wfobj:
    for a, b in c.items():
        wfobj.write('\n')
        if((a != "Moi_Quan_He")):
            wfobj.write("Bang "+a + '\n')
        else:
            wfobj.write(a)
            wfobj.write('\n')
        for x, y in b.items():
            result = ' '.join([x, y])
            wfobj.write(result + '\n')
wfobj.close()
list = []
fobj.close()
