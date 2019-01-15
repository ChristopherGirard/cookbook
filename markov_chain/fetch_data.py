import urllib2
from bs4 import BeautifulSoup

class FetchData:
  
  def fetch_ingredients(self):
    response = urllib2.urlopen("https://en.wikibooks.org/wiki/Cookbook:Ingredients")
    fetched_ing = response.read()
    ingr_list = []
    
    with open("Ingredients HTML.html", "w") as ing_html:
    	ing_html.write(fetched_ing)
    
    with open("Ingredients HTML.html") as html_file:
    	soup = BeautifulSoup(html_file, features="lxml")
    
    for each in soup.find_all("a", string=True):
      if each.parent.name == "li":
        ingr_list.append(each.get_text())
        #print ("Added %s") % each.get_text()
    
      if each.get_text() == "Zucchini":
      	break
    
    with open("Ingredients HTML.html", "w") as ing_html:
    	ing_html.write(", ".join(ingr_list)) 

  def fetch_name():
  	pass

  def fetch_procedures():
  	pass
  
  def fetch_units():
  	pass


#exemple of mc flow
# mc.add_file("Ingredients HTML.html")
# print mc.generate_text(max_length=5)


#---------------------------
#      -Debug Print-       |
#---------------------------
# print
# print ("Ingredient list:")
# print
# for each in ingr_list:
# 	print each + (","),
#---------------------------