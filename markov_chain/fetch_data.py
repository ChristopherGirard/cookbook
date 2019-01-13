from markov_python.cc_markov import MarkovChain 
import urllib2

response = urllib2.urlopen("https://en.wikibooks.org/wiki/Cookbook:Ingredients")
html = response.read()

print html