#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests 
from sys import argv 
from bs4 import BeautifulSoup

uol = []
g1 = []
r7 = []
estadao = []
veja = []
elpais = []
carta_capital = []
cnn_brasil = [] 
terra = []
bbc = [] 
ig = []
olhar_digital = []
exame = []

sky_news = []
guardian = []
cnn = []
nbc = []
cbs = []
abc = []
reuters = []
new_york_times = []
euronews = []
wp = []
foxnews = []
wallstreet = []

def search_wall_street():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.wsj.com/news/world?mod=nav_top_section", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'WSJTheme--headline--7VCzo7Ay'}):
        wallstreet.append("WallStreet] "+item.text.strip())

def search_abc():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.abc.net.au/news/world", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'CardLayout_content__bev76'}):
        abc.append("ABCNEWS] "+item.text.strip())

def search_fox_news():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.foxnews.com/", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'title'}):
        foxnews.append("FoxNEWS] "+item.text.strip())

def search_wp():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.washingtonpost.com/", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'card-left card-text no-bottom'}):
        wp.append("WP NEWS] "+item.text.strip())

def search_euronews():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.euronews.com/news/international", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'m-object__title__link'}):
        euronews.append("EuroNEWS] "+item.text.strip())

def search_new_york_times():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.nytimes.com/international/section/world", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'css-14g652u e1y0a3kv0'}):
        new_york_times.append("NYT NEWS] "+item.text.strip())

def search_cbs():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.cbsnews.com/world/", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'item__hed'}):
        cbs.append("CBS NEWS] "+item.text.strip())

def search_reuters():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.reuters.com/", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__heading_5_and_half__3YluN heading__base__2T28j heading_5_half media-story-card__heading__eqhp9'}):
        reuters.append("Reuters NEWS] "+item.text.strip())

def search_nbc():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.nbcnews.com/world", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'wide-tease-item__headline'}):
        nbc.append("NBC NEWS] "+item.text.strip())

def search_cnn():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://edition.cnn.com/", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'container__text container_lead-plus-headlines__text'}):
        cnn.append("CNN NEWS] "+item.text.strip())

def search_sky_news():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://news.sky.com/world", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'sdc-site-tile__headline'}):
        sky_news.append("Sky NEWS] "+item.text.strip())

def search_guardian():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.theguardian.com/international", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'u-faux-block-link__overlay js-headline-text'}):
        guardian.append("Guadian NEWS] "+item.text.strip())

def search_exame():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://exame.com/ultimas-noticias/", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'touch-area'}):
        exame.append("Exame NEWS] "+item.text.strip())

def search_olhar_digital():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://olhardigital.com.br/", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'cardV2-title'}):
        olhar_digital.append("OD NEWS] "+item.text.strip())

def search_ig():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://odia.ig.com.br/", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'title'}):
        ig.append("IG NEWS] "+item.text.strip())

def search_bbc():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.bbc.com/portuguese/topics/cz74k717pw5t", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'promo-text'}):
        bbc.append("BBC NEWS] "+item.text.strip()) 


def search_terra():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.terra.com.br/noticias/", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'card-news__text--title main-url card-news__url'}):
        terra.append("TERRA NEWS] "+item.text.strip()) 

def search_cnn_brasil():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.cnnbrasil.com.br/", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'home__title'}):
        cnn_brasil.append("CNN NEWS] "+item.text.strip()) 

def search_carta_capital():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.cartacapital.com.br/mais-recentes/", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'l-list__text'}):
        carta_capital.append("[Carta Capital NEWS] "+item.text.strip())       


def search_elpais():
    
    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://elpais.com/america/", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'c_d'}):
        elpais.append("[Elpais NEWS] "+item.text.strip())

def search_veja():

    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://veja.abril.com.br", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'title'}):
        veja.append("[Veja NEWS] "+item.text.strip())

def search_estadao(): 

    headers = {'Content-Type': 'text/html'}

    html = requests.get("https://www.estadao.com.br", headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all(attrs={'class':'headline'}):
        estadao.append("[Estadao NEWS] "+item.text.strip())

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
    if agencia == "estadao":
        search_estadao()
        for item in estadao:
            print item
    if agencia == "veja":
        search_veja()
        for item in veja:
            print item 
    if agencia == "elpais":
        search_elpais()
        for item in elpais:
            print item
    if agencia == "cartacapital":
        search_carta_capital()
        for item in carta_capital:
            print item
    if agencia == "cnnbrasil":
        search_cnn_brasil()
        for item in cnn_brasil:
            print item
    if agencia == "terra":
        search_terra()
        for item in terra:
            print item
    if agencia == "bbc":
        search_bbc()
        for item in bbc:
            print item
    if agencia == "ig":
        search_ig()
        for item in ig:
            print item
    if agencia == "olhardigital":
        search_olhar_digital()
        for item in olhar_digital:
            print item
    if agencia == "exame":
        search_exame()
        for item in exame:
            print item
    if agencia == "guardian":
        search_guardian()
        for item in guardian:
            print item
    if agencia == "skynews":
        search_sky_news()
        for item in sky_news:
            print item
    if agencia == "cnn":
        search_cnn()
        for item in cnn:
            print item
    if agencia == "nbc":
        search_nbc()
        for item in nbc:
            print item
    if agencia == "reuters":
        search_reuters()
        for item in reuters:
            print item
    if agencia == "cbs":
        search_cbs()
        for item in cbs:
            print item
    if agencia == "nyt":
        search_new_york_times()
        for item in new_york_times:
            print item
    if agencia == "euronews":
        search_euronews()
        for item in euronews:
            print item
    if agencia == "wp":
        search_wp()
        for item in wp:
            print item
    if agencia == "foxnews":
        search_fox_news()
        for item in foxnews:
            print item
    if agencia == "abc":
        search_abc()
        for item in abc:
            print item
    if agencia == "wallstreet":
        search_wall_street()
        for item in wallstreet:
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

search(argv[1])