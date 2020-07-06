# SCHEMA

- Pre-processing (esplorazione e individuazione delle feature)
- Clustering - HDBSCAN e Manifold Learning per validazione
- Viz (da finire)
- Prodotti
- App

# COME POTREMMO DISTINGUERE TRA I CLUSTERING

Il nostro obiettivo è quello di presentare un clustering che sia al contempo interessante e significativo. Per fare questo, si deve trovare un modo intelligente per poter andare a confrontare tra i diversi algoritmi che andiamo a proporre (oltre che un metodo per determinare il corretto numero di cluster). 
Ci sono due strade:
- Metodi parametrici; in questo caso, si calcolano degli indici, e.g. *silhouette* per la bontà del clustering e qualche misura relativa per determinare il numero di cluster. Sono tecniche molto buone, ma permettono di distungere solamente tra cluster della stessa famiglia: quando si ha a che fare con metodi differenti, alcune misure possono risultare non idonee, e.g. Silhouette per *density based clustering*.
- Metodi visivi: in questo caso, spetta a noi andare a vedere a occhio, tramite rappresentazioni grafiche, quanto siano buoni i cluster e se abbiamo azzeccato il loro numero corretto. In questa istanza, oltre a delle rappresentazioni 2D attributo-attributo, molto utili se si usano solamente 2 dimensioni per creare il modello ma di utilità limitata in più dimensioni, si potrebbero usare delle tecniche di **riduzione dimensionale**. In particolare, oltre a tecniche analitiche come PCA, si può sicuramente usare il campo del **manifold learning**. Queste tecniche potrebbero permetterci di portare i dati in un numero minore di dimensioni, prendendo però in considerazioni la disposizione interna degli stessi.

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



