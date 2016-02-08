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
#Get info about each nomination for that category & year combination
for url in award_list:
  # Go to first nomination and get the nominee(s)name
  html_nomination = requests.get(url).text
  root_nomination = lxml.html.fromstring(html_nomination)
  print root_nomination
  nominees = root_nomination.cssselect("b a")
  print nominees
  break
  

# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
