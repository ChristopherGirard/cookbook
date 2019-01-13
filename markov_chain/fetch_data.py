from markov_python.cc_markov import MarkovChain 
import urllib2

response = urllib2.urlopen("https://en.wikibooks.org/wiki/Cookbook:Ingredients")
ingredients_html = response.read()

print ingredients_html