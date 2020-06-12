# Utile segnarsi alcune cose per i dati
* Abbiamo diviso i dati in due gruppi, uno che si riferisce a come il cliente è e uno che si riferisce al tipo di investimenti fatti dal cliente.
* Abbiamo guardato la correlazione fra le varie variabili: quello di interessante che abbiamo trovato è stato:
	- Age e riskpropension sono molto correlate, interessante.
	- Anche risk propension e age sono molto correlate. 
	- In generale age e altre misure sono molto correlate.
	- Inheritance index anche è piuttosto correlata con tutto, è comunque una variabile interessante
* Abbiamo trovato un gruppo di variabili molto correlate fra loro 
* Protection need ha distribuzioni strane e __divise in due__ per ogni altra variabile
* Per quanto riguarda gli investimenti, e il dataframe associato, non si notano comportamenti e correlazioni particolari. Al massimo un 0.67 tra cash e bond. e 0.60 tra portfolio horizon e equity investments.
* Orizzonte temporale: legato al rischio. 

# Prossimi step da fare
* Eliminare features
* Raggruppare le variabili con la feature extraction. Soprattutto quelle che abbiamo visto essere molto incorrelate fra di loro.
* Tentare vari algoritmi
* Capire le misure di valutazione più efficaci.

# Obiettivi
* Interpretabile
* Comunicabile
* Utile
* Dare informazioni utili riguardanti i clienti. Come investono rispetto alla loro condizione generica.


# 12/06: Obbiettivi da completare
* Individuare una classe di algoritmi che funzioni abbastanza bene. 
  - Per ora i migliori sono `__Agglomerativo__ con L2(distanza euclidea) ed K-Means`.
* Determinare gli attributi, i.e. capire come fare feature selection in problemi di clustering.
* Cercare una buona interpretabilità.
* Capire il confronto con portafoglio attuale.  
* Chiedere all'azienda come viene calcolato `Portofolio Risk`. 

