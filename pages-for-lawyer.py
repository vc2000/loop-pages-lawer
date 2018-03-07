import requests

base_url = "https://www.vermontjudiciary.org/opinions-decisions?facet_from_date="
big_lis=[]

for num in range(0,42):
    if num == 0:
        r=requests.get(base_url+"01%2F01%2F2014&facet_to_date=01%2F01%2F2016")
    else:
        r=requests.get(base_url+"=01/01/2014&facet_to_date=01/01/2016&search_api_fulltext=&page="+str(num))


### do whatever you like!!
