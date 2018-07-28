"""
Luke Mains
2018.06.24

This will be my code to complete the python challenge from http://www.pythonchallenge.com/.

For solutions, replace 'pc' with 'pcc' in the url's
"""

# Imports
import requests
import urllib.request
import urllib.parse
import re
from collections import Counter
import pickle
import zipfile
from PIL import Image
from PIL import PngImagePlugin

# Level 0 - http://www.pythonchallenge.com/pc/def/0.html
"""
print(2**38)
"""

# Level 1 - http://www.pythonchallenge.com/pc/def/map.html
"""
message = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. ' \
          'bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. ' \
          'sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

alphabet = 'abcdefghijklmnopqrstuvwxyz'
replacements = 'cdefghijklmnopqrstuvwxyzab'.upper()

for i in range(len(alphabet)):
    message = message.replace(alphabet[i], replacements[i])

print(message)

I hope you didn't translate it by hand. 
That's what computers are for. Doing it 
in by hand is inefficient and that's
why this text is so long. Using string.maketrans() 
is recommended. Now apply on the url.
"""

# Level 2 - http://www.pythonchallenge.com/pc/def/ocr.html
"""
page = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
content = page.content.decode('utf-8')

# Find index of the mess string.
start = content.rfind('<!--') + len('<!--')
end = content.rfind('-->')

mess = content[start:end]

C = Counter(mess)

for char, count in C.items():
    print(char, count)
"""

# Level 3 - http://www.pythonchallenge.com/pc/def/equality.html
"""
page = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
content = page.content.decode('utf-8')


mess = content[content.find('<!--\n')+5:content.find('-->')]

for item in re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', mess):
    print(item[4], end='')
"""

# Level 4 - http://www.pythonchallenge.com/pc/def/linkedlist.php - click the picture
"""
page_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
linked_list_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
test_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

page = requests.get(linked_list_url)
content = page.content.decode('utf-8').strip()
next_node = re.findall(r'\d\d\d\d\d', content)
last_node = next_node

for i in range(250):
    print(i, end=': ')
    try:
        last_node = next_node
        regex = re.findall(r'and the next nothing is \d+', content)
        next_node = re.findall(r'\d+', regex[0])
        page = requests.get(test_url + next_node[0])
        content = page.content.decode('utf-8').strip()
        print(content)
    except IndexError:
        if content == 'Yes. Divide by two and keep going.':
            next_node = [str(int(last_node[0])//2)]
            page = requests.get(test_url + next_node[0])
            content = page.content.decode('utf-8').strip()
            print(content)
        else:
            print('index error')
"""

# Level 5 - http://www.pythonchallenge.com/pc/def/peak.html - "Pickle"
"""
url = 'http://www.pythonchallenge.com/pc/def/banner.p'

page = urllib.request.urlopen(url)
p = pickle.load(page)
for element in p:
    print(''.join([e[1] * e[0] for e in element]))
"""

# Level 6 - http://www.pythonchallenge.com/pc/def/channel.html
"""
There is a picture of a zipper so I assume it's a zip file. I went to 
http://www.pythonchallenge.com/pc/def/channel.zip and downloaded a file.
""""""
with zipfile.ZipFile('channel.zip') as myzip:
    # with myzip.open('readme.txt') as f:
    #    print(f.read().decode('utf-8'))
    # Start from 90052

    infolist = myzip.infolist()

    f = '90052'
    for i in range(910):
        for item in infolist:
            if item.filename == f+'.txt':
                print(item.comment.decode(), end='')

        zip_file = myzip.open(f + '.txt')
        text = zip_file.read().decode()
        regex = re.findall(r'nothing is \d+', text)
        next_nothing = re.findall(r'\d+', regex[0])
        f = next_nothing[0]
"""

# TODO Level 7 - http://www.pythonchallenge.com/pc/def/oxygen.html
url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
page = requests.get(url)
content = page.content

im = Image.open('oxygen.png')
im.load()
im.show()

input("Holding program to show image.")

"""
critical_chunks = ['IHDR', 'PLTE', 'IDAT', 'IEND', 'PLTE']
ancillary_chunks = ['bKGD', 'cHRM', 'dSIG', 'eXIf', 'gAMA', 'hIST', 'iCCP', 'iTXt', 'pHYs', 'sBIT', 'sPLT', 'sRGB', 'sTER', 'tEXt', 'tIME', 'tRNS', 'zTXt']

indexes = {}
for item in critical_chunks + ancillary_chunks:
    index = content.find(item.encode('ascii'))
    if index != -1:
        indexes[item] = index

lines = []
last_index = 0
for index in sorted(indexes.values()):
    lines.append(content[last_index:index])
    last_index = index

for line in lines:
    print(line)
"""
