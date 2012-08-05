#!/usr/bin/python3

"""Simple script to write title, url, and HTML body content of HTML files
to separate numberd files.

Allows to do custom replacements.

Note on security: we assume that your input files are correctly HTML-encoded,
and contain no harmful code.
If your input data is different, then take precautions!
"""

import glob
import os
import re

# make sure that these folders exist
static_dump_dir = '~/site-dump'
processed_dir = '~/site-dump/processed'

title_prefix_to_remove = 'Site: Main - '
html_replacements = {
    '/site/' : '/',
    '/HomePage/' : '/HomePage'
}

# regular expression to parse out the title of the page
TITLE = re.compile(".*<title>(.*)</title>")
# regular expression to parse out the content HTML of the page
BODY = re.compile("<!--PageText-->(.*)<div id=\"footer\"", re.DOTALL)

def process(index, file):
    """Parse out title, filename, body and do necessary replacements"""
    with open(f, 'r', encoding='iso-8859-1') as file:
        content = file.read()
        match = TITLE.search(content)
        if match:
            title = match.groups()[0]
            title = title.replace(title_prefix_to_remove, '')
            filename = os.path.basename(f).replace('.html', '')
            print(filename, ':', title)
        match2 = BODY.search(content)
        if match2:
            body = match2.groups()[0]
            for old,new in html_replacements.items():
                body = body.replace(old, new)
            print(body)

    # write body, title and URL to separate numbered files
    output_filename = "article{0:05}".format(index)
    with open(output_filename + '.body.html', 'tw', encoding='utf-8') as body_out:
        body_out.write(body)
    with open(output_filename + '.title.txt', 'tw', encoding='utf-8') as title_out:
        title_out.write(title)
    with open(output_filename + '.url.txt', 'tw', encoding='utf-8') as url_out:
        url_out.write(filename)

if __name__ == '__main__':
    os.chdir(processed_dir)
    for i,file in enumerate(f for f in glob.iglob(static_dump_dir + "/*") if os.path.isfile(f))
        process(i, file)


