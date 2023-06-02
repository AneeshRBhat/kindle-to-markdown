# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 17:42:21 2023

@author: Aneesh R Bhat
"""
import sys
from bs4 import BeautifulSoup

getHTML = input('Enter the file name: ')
MD_path = input('Enter the path to send the markdown file to: ')
try:
    handle = open(getHTML, 'r', encoding='utf8')
    try: 
        soup = BeautifulSoup(handle, 'html.parser')
    except NameError:
        print("BeautifulSoup library not installed")
        sys.exit()
except FileNotFoundError:
    print('File not found: {}'.format(getHTML))
    sys.exit()



notes = dict()
tags = soup('div')
bookTitle = ''
bookAuthors = []
sectionHeading = ''
for tag in tags:
    if tag.get('class')[0] == 'sectionHeading' and tag.contents[0].strip not in notes:
        heading = tag.contents[0].strip()
        notes[heading] = notes.get(heading, list())
        sectionHeading = heading
    elif tag.get('class')[0] == 'bookTitle':
        bookTitle = tag.contents[0].strip()
        
    elif tag.get('class')[0] == 'authors':
        authors = tag.contents[0].strip()
        bookAuthors = authors.split(', ')
        
    elif tag.get('class')[0] == 'noteText':
        notes[sectionHeading].append(tag.contents[0].strip())
    
    else: 
        continue

bookPath = MD_path + '/' + bookTitle + '.md'
try:
    md = open(bookPath, 'w', encoding='utf8')
except FileNotFoundError:
    print("Invalid path")
    sys.exit()
md.write('---\n' + 'author: ')
for author in bookAuthors:
    md.write(author + ', ')

md.write('\n---\n')
for (chapter, notes) in notes.items():
    md.write('# ' + chapter + '\n')
    for note in notes:
        md.write('- ' + note + '\n')
    md.write('\n')
    
md.close()    
print('notes extracted')
    
        
        
    