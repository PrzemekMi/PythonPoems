
#data = opener.open('https://milosc.info/boleslaw-lesmian/').read().decode()
#data = opener.open('https://najpiekniejsze-wiersze-o-milosci-u.manifo.com/').read().decode()
#data = opener.open('https://mypoeticside.com/poets/' + writer).read().decode()

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import re
#this trick the server to think that we are connecting from a web browser
class AppURLopener(urllib.request.FancyURLopener): 
    version = "Mozilla/5.0" 
opener = AppURLopener()
writer = "edgar-allan-poe-poems"
data = opener.open('https://mypoeticside.com/poets/' + writer).read().decode()



#search and save the poem links 
soup =  BeautifulSoup(data, 'html.parser')
poem_list = soup.find(class_="list-poems")
links = poem_list.findAll('a')
#results = ["https:"+link.get('href') for link in links]
results = [
'https://milosc.info/boleslaw-lesmian/czasami-mojej-slepej/',
'https://milosc.info/boleslaw-lesmian/dwoje-ludzienkow/',
'https://milosc.info/boleslaw-lesmian/dzis-w-naszego-spotkania/',
'https://milosc.info/boleslaw-lesmian/gad/',
'https://milosc.info/boleslaw-lesmian/gdy-domdlewasz-na-lozu/',
'https://milosc.info/boleslaw-lesmian/gdybym-spotkal-ciebie/',
'https://milosc.info/boleslaw-lesmian/haslo-nasze-ma-dla-nas/',
'https://milosc.info/boleslaw-lesmian/ja-tu-stoje-za-drzwiami/',
'https://milosc.info/boleslaw-lesmian/lubie-szeptac-ci-slowa/',
'https://milosc.info/boleslaw-lesmian/mrok-na-schodach-pustka-w-domu/',
'https://milosc.info/boleslaw-lesmian/nad-ranem/',
'https://milosc.info/boleslaw-lesmian/niewiedza/',
'https://milosc.info/boleslaw-lesmian/noca/',
'https://milosc.info/boleslaw-lesmian/noca-umowiona/',
'https://milosc.info/boleslaw-lesmian/o-zmierzchu/',
'https://milosc.info/boleslaw-lesmian/pieszczota/',
'https://milosc.info/boleslaw-lesmian/po-ciemku/',
'https://milosc.info/boleslaw-lesmian/po-ciemku/',
'https://milosc.info/boleslaw-lesmian/powiesc-o-rozumnej-dziewczynie/',
'https://milosc.info/boleslaw-lesmian/pozarze-piersny/',
'https://milosc.info/boleslaw-lesmian/romans/',
'https://milosc.info/boleslaw-lesmian/schadzka/',
'https://milosc.info/boleslaw-lesmian/sledza-nas/',
'https://milosc.info/boleslaw-lesmian/smierc-wtora/',
'https://milosc.info/boleslaw-lesmian/sniez-sie-w-duszy-mojej/',
'https://milosc.info/boleslaw-lesmian/tajemnica/',
'https://milosc.info/boleslaw-lesmian/taka-cisza-w-ogrodzie/',
'https://milosc.info/boleslaw-lesmian/twoj-portret-z-lat-dziecinnych/',
'https://milosc.info/boleslaw-lesmian/ty-pierwej-mgly-dosiegasz/',
'https://milosc.info/boleslaw-lesmian/ty-przychodzisz-jak-noc-majowa/',
'https://milosc.info/boleslaw-lesmian/usta-i-oczy/',
'https://milosc.info/boleslaw-lesmian/w-malinowym-chrusniaku/',
'https://milosc.info/boleslaw-lesmian/w-polu/',
'https://milosc.info/boleslaw-lesmian/we-snie/',
'https://milosc.info/boleslaw-lesmian/wieczorem/',
'https://milosc.info/boleslaw-lesmian/wiersz-ksiezycowy/',
'https://milosc.info/boleslaw-lesmian/wracam-wracam-po-dlugiej/',
'https://milosc.info/boleslaw-lesmian/wyszlo-z-boru-slepawe/',
'https://milosc.info/boleslaw-lesmian/wyznanie/',
'https://milosc.info/boleslaw-lesmian/wyznanie-spoznione/',
'https://milosc.info/boleslaw-lesmian/z-dlonmi-tak-splecionymi/',
'https://milosc.info/boleslaw-lesmian/zaklecie/',
'https://milosc.info/boleslaw-lesmian/wyznanie-spoznione/',
'https://milosc.info/boleslaw-lesmian/z-dlonmi-tak-splecionymi/',
'https://milosc.info/boleslaw-lesmian/zaklecie/',
'https://milosc.info/boleslaw-lesmian/zazdrosc-moja/',
'https://milosc.info/boleslaw-lesmian/zazdrosnicy-daremnie-chca/',
'https://milosc.info/boleslaw-lesmian/zmienionaz-po-rozlace/',
'https://milosc.info/boleslaw-lesmian/zmierzch/',
'https://milosc.info/boleslaw-lesmian/zmierzch-bezpowrotny/',
'https://milosc.info/boleslaw-lesmian/zmory-wiosenne/',
'https://milosc.info/boleslaw-lesmian/com-uczynil-zes-nagle-pobladla/'
]

pattern=re.compile(r"\>(.*?)\<",)

#saves the title and content of each poem
titles = []
corpus = []
lines = []
corpusstring = ''
for page in results:
    data = opener.open(page).read().decode()
    soup = BeautifulSoup(data, 'html.parser')
   # title = soup.find(class_='title-poem')     
    title = soup.find(class_='schema-desc')
    poem = soup.find(class_='text')
    titles.append(title.getText())

    instructions = soup.find(itemprop="text")
    out = re.findall("\>(.*?)\<", str(instructions))
    corpusstring = '\n'.join(out)
    corpus.append(corpusstring)

#print("Line", [out.strip('\'') for s in out]) 
result = pd.DataFrame.from_dict({'title' : titles, 'text' : corpus})

#poems = pd.DataFrame.from_dict({'title' : titles, 'text' : corpus}, orient='index')
#result = poems.transpose()

result.to_csv('poems.csv')