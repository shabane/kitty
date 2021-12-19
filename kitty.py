#!/bin/python3
import requests
import sys

link = sys.argv[1]
posTs = link.find('.ts')
sli = link[posTs-3:posTs]


nums = list(range(10))
count = []
for a in nums:
    for b in nums:
        for c in nums:
            count.append(str(a)+str(b)+str(c))

tmp = ''
for i in count[1:290]:
    tmp = link.replace(sli, i)
    with open('1.ts', 'ab') as fli:
        res = requests.get(tmp)
        print(i, res.status_code)
        fli.write(res.content)

print('done, what are you wating for ?')