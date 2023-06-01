# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 17:42:21 2023

@author: Aneesh R Bhat
"""
import sys
from bs4 import BeautifulSoup

user_input = input('Enter the file name: ')
try:
    handle = open(user_input, 'r', encoding='utf8')
    soup = BeautifulSoup(handle, 'html.parser')
except FileNotFoundError:
    print('File not found: {}'.format(user_input))
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

md = open(bookTitle+'.md', 'w', encoding='utf8')
md.write('# ' + bookTitle + '\n')
md.write('---\n' + 'author: ')
for author in bookAuthors:
    md.write(author + ', ')

md.write('\n---\n')
for (chapter, notes) in notes.items():
    md.write('## ' + chapter + '\n')
    for note in notes:
        md.write('- ' + note + '\n')
    md.write('\n')
    
md.close()    
print('notes extracted')
    
        
        
    