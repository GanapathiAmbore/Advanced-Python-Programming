from bs4 import BeautifulSoup as soup
'''file=open('basic.html','r')
page_soup=soup(file,'html.parser')
h1_tag=page_soup.find('h1')
print(h1_tag.get_text())
'''
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
'''page_soup=soup(html_doc,'html.parser')
p_tags=page_soup.find_all('p')
for text in p_tags:
    print(text.get_text())'''
file=open('basic.html','r')
page_soup=soup(file,'html.parser')
div_tag=page_soup.find_all('ul')
print(div_tag[1])


