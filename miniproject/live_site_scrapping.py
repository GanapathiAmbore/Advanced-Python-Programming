from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
url='https://www.python.org/'
page=urlopen(url)
page_soup=soup(page,'html.parser')
p_tag=page_soup.find('div',{'class':'introduction'})
print(p_tag.find('p').text)
