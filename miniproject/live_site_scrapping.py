from urllib.request import urlopen#this help us to open the page
from bs4 import BeautifulSoup as soup#this help us grab page source
import json
page_url='https://www.flipkart.com/search?q=samsung+m31&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_2_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_2_na_na_na&as-pos=4&as-type=RECENT&suggestionId=samsung+m31&requestId=4f73f33a-6b2f-4fcc-acc0-3c1bf6a9d39c&as-searchtext=sa'
page=urlopen(page_url)#opening the page url
page_source=soup(page,'html.parser')#page source
main_div=page_source.find_all('div',{'class':'bhgxx2 col-12-12'})
final_list=[]
for div in main_div[3:27]:
    reviews=div.find('div',{'class':'hGSR34'})
    reviews_dict={}
    if reviews is None:
        pass
    else:
        reviews_dict['review']=reviews.text
    tmp={}
    tmp['title']=div.find('div',{'class':'_3wU53n'}).text.replace('(','').replace(')','')
    tmp['price']=div.find('div',{'class':'_1vC4OE _2rQ-NK'}).text.replace('₹','')
    tmp.update(reviews_dict)
    final_list.append(tmp)
file=open('price.json','w')
file.write(json.dumps(final_list,indent=4))

assignment_link='https://www.flipkart.com/search?q=lg+tvs&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=lg+tvs%7CTVs&requestId=ccfb2739-b7f9-451b-b08a-603b0b204841&as-searchtext=lg%20tvs'