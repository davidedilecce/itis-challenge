# ****
# author: DAVIDE DI LECCE - Applica s.r.l.
# ****



# ------------------------- IMPORTAZIONE LIBRERIE --------------------------- #

#libreria utile per manipolare/acquisire informazioni sul tempo come date, ore, etc...
#         la utilizzeremo per calcolare quanto tempo è richiesto per ottenere una pagina html
import datetime

#libreria utile per effettuare chiamate HTTP (protocollo stateless che permette ad un client
#         in questo caso il nostro script di effettuare chiamate al server che restituisce una risposta)
#         nel nostro caso faremo chiamate http per poter acquisire l'html delle pagine contenenti le
#         offerte di lavoro su indeed
import requests

#libreria utile per poter effettuare il parse della stringa html grezza che ci arriverà dalla request
#         questo per poter estrarre dati dall'html come il testo all'interno di div con una determinata classe
from bs4 import BeautifulSoup

#libreria utile per l'apprendimento automatico che permette attraverso algoritmi di classificazione di effettuare
#         operazioni complesse con poche righe di codice
from sklearn.feature_extraction import text

#lista di parole non utili per l'apprendimento automatico come le preposizioni, gli articoli, etc...
from italians_stop_words import ITALIAN_STOP_WORDS
# libreria utile per manipolare/acquisire informazioni sul tempo come date, ore, etc...
#         la utilizzeremo per calcolare quanto tempo è richiesto per ottenere una pagina html
import datetime

# libreria utile per effettuare chiamate HTTP (protocollo stateless che permette ad un client
#         in questo caso il nostro script di effettuare chiamate al server che restituisce una risposta)
#         nel nostro caso faremo chiamate http per poter acquisire l'html delle pagine contenenti le
#         offerte di lavoro su indeed
import requests
# libreria utile per poter effettuare il parse della stringa html grezza che ci arriverà dalla request
#         questo per poter estrarre dati dall'html come il testo all'interno di div con una determinata classe
from bs4 import BeautifulSoup
# libreria utile per l'apprendimento automatico che permette attraverso algoritmi di classificazione di effettuare
#         operazioni complesse con poche righe di codice
from sklearn.feature_extraction import text

# lista di parole non utili per l'apprendimento automatico come le preposizioni, gli articoli, etc...
from italians_stop_words import ITALIAN_STOP_WORDS

# ------------------------- CONFIGURAZIONE ALGORMITO --------------------------- #


#lavoro che interessa ricercare (Data scientist, Developer, Magazziniere, etc...)
job_name = "Data scientist"

#area di interesse (es: Milano, Matera, Roma, etc...)
area = "Milano"

#pagine di indeed che vogliamo scansionare, più alto è il numero più il tempo l'esecuzione
#del nostro algoritmo sarà alto più il risultato sarà accurato
pages_to_scan = 100

#numero delle principali parole che vorremmo visualizzare in output
results_number = 30


# ------------------------------ INIZIO ALGORMITO ------------------------------ #


#in questa variabile salveremo tutte le offerte di lavoro
job_offers = []

formatted_job_name = job_name.replace(" ", "+")

for index in range (0, pages_to_scan * 10, 10):

  print("Index: " + str(index))

  page_url = "https://it.indeed.com/offerte-lavoro?q=" + formatted_job_name + "&l=" + area + "&start=" + str(index)

  print("Inizio caricamento pagina: " + page_url)

  before_loading_date = datetime.datetime.now()

  web_page = requests.get(page_url).content

  print("Caricamento ultimato in: " + str((datetime.datetime.now() - before_loading_date).seconds) + " secondi")

  parsed_html_web_page = BeautifulSoup(web_page, "html.parser")

  for raw_job_offer in parsed_html_web_page.find_all("div", attrs={"class":"summary"}):
      job_offers.append(raw_job_offer.text)


#qui viene creata un istanza del nostro plugin definendogli alcune regole per imparare le parole
vect = text.CountVectorizer(ngram_range=(1,2), lowercase=True, stop_words=ITALIAN_STOP_WORDS.union(text.ENGLISH_STOP_WORDS))

print("Sto imparando il vocabolario delle parole")

#qui permettiamo al nostro vocabolario di imparare tutte le parole contenute nelle nostre offerte di lavoro
matrix = vect.fit_transform(job_offers)

print("Numero di offerte di lavoro: " + str(len(job_offers)))
print("Numero di parole con maggiore frequenza: " + str(len(vect.get_feature_names())))


# ------------------------------ STAMPA DEI RISULTATI ------------------------------ #


# vect ha una prioprietà di tipo dizionario (chiave, valore) e per ogni iterazione avremo 2 variabili word e idx
# che useremo per creare una lista contenente l'associazione tra la parola e la relativa frequenza
freqs = [(word, matrix.getcol(idx).sum()) for word, idx in vect.vocabulary_.items()]


# sorted        permette di creare una nuova lista a partire da una esistente (nel nostro caso freqs)
# key           contiene la funzione che deve essere chiamata per ogni elemento della lista che ha un singolo argomento
#               e che permette di ordinare l'array in base proprio al risultato della funzione
# lambda        è una funzione anonima (cioè senza nome)
#               la sua sintassi è LAMBDA ARGOMENTO: ESPRESSIONE
# qui stiamo dicendo di prendere il secondo elemento della lista e di poter ordinare per quello
for phrase, times in sorted (freqs, key = lambda x: -x[1])[:results_number]:
  print("Parola: " +  phrase + ", frequenza: " + str(times))