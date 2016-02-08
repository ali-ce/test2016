import scraperwiki
import lxml.html
import requests
import json
import urllib

#Build queries 1: list URLS of awards per year
year_list = []
this_edition = 87
current_edition = 1
while current_edition <= this_edition:
  year_url = "http://awardsdatabase.oscars.org/ampas_awards/BasicSearch?action=searchLink&displayType=1&BSFromYear="+str(current_edition)
  current_edition = current_edition+1
  year_list.append(year_url)
#Build queries2: list of URLS per single award per year

award_list=[]
for year in year_list:
  html_year = requests.get(year).text
  root_year = lxml.html.fromstring(html_year)
  category_temp = root_year.xpath("//dl/div[1]/a/@href")[0]
  category_id = category_temp.partition("CategoryExact=")[2].partition("&")[0]
  print category_id
  break



#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
