import urllib
from bs4 import BeautifulSoup
import pandas as pd
Numbers=[]
State=[]
Capital=[]
D=[]
E=[]
Year=[]
G=[]
# We've now imported the two packages that will do the heavy lifting
# for us, reqeusts and BeautifulSoup

# Let's put the URL of the page we want to scrape in a variable
# so that our code down below can be a little cleaner

wikipedia_page = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

page = urllib.urlopen(wikipedia_page) 

# We now have the source of the page, let's ask BeaultifulSoup
# to parse it for us.

soup = BeautifulSoup(page,"lxml")

target_table_you_want_to_save=soup.find('table', class_='wikitable sortable plainrowheaders')

for row in target_table_you_want_to_save("tr"):

    cells = row.findAll('td')
    
    states=row.findAll('th') #To store second column data
    
    if len(cells)>0: #Only extract table body not heading
    
        Numbers.append(cells[0].find(text=True))
        State.append(states[0].find(text=True))
        Capital.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))

df=pd.DataFrame(Numbers, columns=['Number'])
df['State/UT']=State
df['Admin_Capital']=Capital
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=Year
df['Former_Capital']=G
df.to_dense().to_csv("save_table.csv", index = False, sep=',', encoding='utf-8')
