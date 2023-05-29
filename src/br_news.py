#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests 
from sys import argv 
from bs4 import BeautifulSoup

uol = []
g1 = []
r7 = []

# r7-flex-title-h3__link

def search_r7(): 

    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.r7.com", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'widget-8x1-c__title'}):
        r7.append("[R7 NEWS] "+item.text.strip())

def search_g1():

    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://globo.com/", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'post__title'}):
        g1.append("[O GLOBO] "+item.text.strip())
        
    html = requests.get("https://ge.globo.com/", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'feed-post-body-title gui-color-primary gui-color-hover'}):
        g1.append("[GE NEWS] "+item.text.strip())

def search_uol():

    headers = {'Content-Type': 'text/html'}
    html = requests.get("https://www.uol.com.br", headers=headers)
    
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'headlineHorizontalAvatar__content__title'}):
        uol.append("[UOL NEWS] " + item.text.strip())
        
        
def search(agencia):
    if agencia == "uol":
        search_uol()
        for item in uol:
            print item
    if agencia == "g1":
        search_g1()
        for item in g1:
            print item     
    if agencia == "r7":
        search_r7()
        for item in r7:
            print item    
        

def banner(): 
    print """

 _______                       
 \      \   ______  _  ________
 /   |   \_/ __ \ \/ \/ /  ___/
/    |    \  ___/\     /\___ \ 
\____|__  /\___  >\/\_//____  >
        \/     \/           \/ 

"""

if len(argv) < 2:
    banner()
    print "Usage: python news.py <agencia>\n\n"
    exit()

html = search(argv[1])
print html