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
  text = "|".join(text.text_content() for text in root_nomination.xpath("//tr[td]"))
  unique_id = "|".join(text.partition("NominationID=")[2]+url for text in root_nomination.xpath("//tr/td/div/a/@href"))
  movie = "|".join(text.text_content().partition(" -- ")[2] for text in root_nomination.xpath("//tr[td]"))
  for text in root_nomination.xpath("//tr/td[1]"):
    print text
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

    
    
  #nominations_nominees = "|".join(text for text in root_nomination.xpath("//tr[td]"))
  
  #root_nomination.xpath("//dl/table")
  #print nominations
  #for nomination in nominations:
   # nomination_text = nomination.text_content()
    #nomination_id = nomination.xpath("//tr/td/div/a/@href")
    #print nomination_id
  break  
    
 # for nomination in nomination:
  #  nomination_id = nominations.partition("NominationID=")[2]
   # unique_id = "ID"+nomination_id+url
  
  #Get movies for each nomination
  #for row in root_nomination.xpath("//tr[1]")]:
  #  nominated_movies = row.text_content().partition(" -- ")[2]
#    nomination_win = 
 # print nominated_movies

  #nominations = root_nomination.xpath("//td/div/a/@href")
  #for nomination in nominations:
   # nomination_id = nomination.partition("NominationID=")[2]
    #nomination_url = "http://awardsdatabase.oscars.org/ampas_awards/BasicSearch?action=searchLink&displayType=6&BSNominationID="+nomination_id
    #nomination_list.append(nomination_url)
  
  
    
    #Get whether the nomination was a win
    
    #Trace each nomination to its award & year id, for future reference
    #award_nomination_dictionary.update({url : nomination_id})
  #break
#Get the actual nominees for each nomination ID

#Save the data


  

# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
