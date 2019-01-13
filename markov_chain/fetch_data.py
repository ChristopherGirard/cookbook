from markov_python.cc_markov import MarkovChain 
import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen("https://en.wikibooks.org/wiki/Cookbook:Ingredients")
fetched_ing = response.read()
ingr_list = []

with open("Ingredients HTML.html", "w") as ing_html:
	ing_html.write(fetched_ing)

with open("Ingredients HTML.html") as html_file:
	soup = BeautifulSoup(html_file, features="lxml")

with open("Ingredients HTML.html", "w") as ing_html:
	ing_html.write(str(soup))

for each in soup.find_all("a", string=True):
  if each.parent.name == "li":
    ingr_list.append(each.get_text())
    #print ("Added %s") % each.get_text()

  if each.get_text() == "Zucchini":
  	break

# print
# print ("Ingredient list:")
# print
# for each in ingr_list:
# 	print each + (","),