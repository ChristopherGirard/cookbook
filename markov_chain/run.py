from random import randint
import fetch_data
from markov_python.cc_markov import MarkovChain

mc = MarkovChain(2)
FetchData = fetch_data.FetchData()

#maybe take off self for __init__
FetchData.fetch_ingredients()