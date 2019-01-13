from markov_python.cc_markov import MarkovChain 
import urllib2

response = urllib2.urlopen("https://en.wikibooks.org/wiki/Cookbook:Ingredients")
ingredients_html = response.read()
"""
"Imports the HTML code into a variable.

"For ingredients, the important line is this one:
<li><a href="/wiki/Cookbook:Maple_Syrup" title="Cookbook:Maple Syrup">Maple syrup</a></li>

"<li></li> is a list

"<a href="" title=""></a> is a link

"What we need is between both: <li><a href"" title="">MapleSyrup</a></li>
"""
