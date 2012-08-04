#!/usr/bin/python3

import glob
import os
import re

TITLE = re.compile(".*<title>(.*)</title>")
BODY = re.compile("<!--PageText-->(.*)<div id=\"footer\"", re.DOTALL)

def process(f, index):
    with open(f, 'r', encoding='iso-8859-1') as file:
        content = file.read()
        m = TITLE.search(content)
        if m:
            title = m.groups()[0].replace('Vitis-tct : Main - ', '')
            filename = os.path.basename(f).replace('.html', '')
            print(filename, ':')
            print(title)
        m2 = BODY.search(content)
        if m2:
            body = m2.groups()[0]
            body = body.replace('/site/Main/', '/').replace('/HomePage/', '/HomePage')
            print(body)
    output_filename = "article{0:02}".format(index)
    with open(output_filename + '.body.html', 'tw', encoding='utf-8') as body_out:
        body_out.write(body)
    with open(output_filename + '.title.txt', 'tw', encoding='utf-8') as title_out:
        title_out.write(title)
    with open(output_filename + '.url.txt', 'tw', encoding='utf-8') as url_out:
        url_out.write(filename)
   
os.chdir('/home/flo/backup/www.vitis-tct.be/converted')
files = [f for f in glob.iglob("/home/flo/backup/www.vitis-tct.be/site/Main/*") if os.path.isfile(f)]
for i,f in enumerate(files):
    process(f, i)



