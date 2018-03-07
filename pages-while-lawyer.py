import requests
from bs4 import BeautifulSoup

i = 0
while(True):
    try:
        if i == 0:
            url = "https://www.vermontjudiciary.org/opinions-decisions?facet_from_date=01%2F01%2F2014&facet_to_date=01%2F01%2F2016"
        else:
            url = "https://www.vermontjudiciary.org/opinions-decisions?facet_from_date=01/01/2014&facet_to_date=01/01/2016&search_api_fulltext=&page={}".format(i)

        r=requests.get(url)
        soup=BeautifulSoup(r.content,"html.parser")

        i += 1

    except:
      break
