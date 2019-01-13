from markov_python.cc_markov import MarkovChain 
import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen("https://en.wikibooks.org/wiki/Cookbook:Ingredients")
fetched_ing = response.read()

with open("Ingredients HTML.html", "w") as ing_html:
	ing_html.write(fetched_ing)

with open("Ingredients HTML.html") as html_file:
	soup = BeautifulSoup(html_file, features="lxml")

with open("Ingredients HTML.html", "w") as ing_html:
	ing_html.write(str(soup))

for each in soup.find_all("a", string=True):
  print(each.get_text())



"""
"Imports the HTML code into a variable.

"For ingredients, the important line is this one:
<li><a href="/wiki/Cookbook:Maple_Syrup" title="Cookbook:Maple Syrup">Maple syrup</a></li>

"<li></li> is a list

"<a href="" title=""></a> is a link

"What we need is between both: <li><a href"" title="">MapleSyrup</a></li>
"""


