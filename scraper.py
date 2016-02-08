import scraperwiki
import lxml.html
import requests
import json
import urllib

#Build queries 1: list URLS of awards per year
year_list = []
this_edition = 87
start_edition = 1
while start_edition <= this_edition:
  year_url = "http://awardsdatabase.oscars.org/ampas_awards/BasicSearch?action=searchLink&displayType=1&BSFromYear="+str(start_edition)
  start_edition = start_edition+1
  year_list.append(year_url)
  break
#Build queries 2: list of URLS per single award per year
award_list=[]
for url in year_list:
  html_year = requests.get(url).text
  root_year = lxml.html.fromstring(html_year)
  category_id = root_year.xpath("//dl/div[1]/a/@href")[0].partition("CategoryExact=")[2].partition("&")[0]
  award_url = url+"&BSCategoryExact="+category_id
  award_list.append(award_url)
  break
#Get nominations for each category & year combination
for url in award_list:
  html_nomination = requests.get(url).text
  root_nomination = lxml.html.fromstring(html_nomination)
  text = "|".join(text.text_content() for text in root_nomination.xpath("//tr"))
  unique_id = "|".join(text.partition("NominationID=")[2]+url for text in root_nomination.xpath("//tr/td/div/a/@href"))
  movie = "|".join(text.text_content().partition(" -- ")[2] for text in root_nomination.xpath("//tr"))
  win_list=[]
  for text in root_nomination.xpath("//tr"):
    temp = text.text_content()
    if temp[1] is "*":
      win = "Yes"
    else:
      win = "No"
    win_list.append(win)
  award_winner = "|".join(word for word in win_list)
  print award_winner
  break
  #Iterate in each row to get the clean names of the nominees for each nominations
  nominee_url_list=[]
  for url in root_nomination.xpath("//tr/td/div/a/@href"):
    nominations_url ="http://awardsdatabase.oscars.org/ampas_awards/BasicSearch?action=searchLink&displayType=6&BSNominationID="+url.partition("NominationID=")[2]  
    nominee_url_list.append(nominations_url)
  nominee_list=[]
  for url in nominee_url_list:
    html_nominees = requests.get(url).text
    root_nominees = lxml.html.fromstring(html_nominees)
    nominees = ";".join(name.text_content() for name in root_nominees.xpath("//b/a"))
    nominee_list.append(nominees)
  nominees = "|".join(nominee for nominee in nominee_list)
  #Save to DB
  #data = {
   # 'ID' : unique_id,
    #'Text' : text,
    #'Movie' : movie,
    #'Winner' : award_winner,
    #'Nominees' : nominees
    #}
  #scraperwiki.sqlite.save(unique_keys=["ID"], data=data)
  #data={}
  #break
  print unique_id
  print text
  print movie
  print award_winner
  print nominees
  break
