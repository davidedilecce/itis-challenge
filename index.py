import datetime

import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer

job_name = "developer"
job_offers = []

for index in range (0, 100, 10):

  print("Range index: " + str(index))

  page_url = "https://it.indeed.com/offerte-lavoro?q=" + job_name + "&start=" + str(index)

  print("Inizio caricamento pagina: " + page_url)
  before_loading_date = datetime.datetime.now()

  web_page = requests.get(page_url).content

  print("Caricamento ultimato in: " + str((datetime.datetime.now() - before_loading_date).seconds))

  print("Inizio parsing pagina")
  before_parsing_date = datetime.datetime.now()

  parsed_html_web_page = BeautifulSoup(web_page, "html.parser")

  print("Parsing ultimato in: " + str((datetime.datetime.now() - before_parsing_date).seconds))

  print("Aggiunta del testo raw in corso")

  for raw_job_offer in parsed_html_web_page.find_all("div", attrs={"class":"summary"}):
    job_offers.append(raw_job_offer.text)

  print("Aggiunta del testo raw TERMINATO")

vect = CountVectorizer(ngram_range=(1,2))

print("Sto imparando il vocabolario delle parole")

matrix = vect.fit_transform(job_offers)

print("Ho terminato di imparare il vocabolario delle parole")

print("INIZIO A STAMPARE IL RISULTATO")


print("Numero di parole con maggiore frequenza: " + str(len(vect.get_feature_names())))

freqs = [(word, matrix.getcol(idx).sum()) for word, idx in vect.vocabulary_.items()]

#sort from largest to smallest
for phrase, times in sorted (freqs, key = lambda x: -x[1])[:25]:
  print("parola:" +  phrase + ", frequenza: " + str(times))