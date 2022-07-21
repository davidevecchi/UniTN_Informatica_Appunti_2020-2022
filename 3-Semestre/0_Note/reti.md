# Reti

|      |           |                                                              |
| ---- | :-------: | -----------------------------------------------------------: |
| Reti |  | [🗀][root] [🗍](http://cricca.disi.unitn.it/montresor/teaching/asd/materiale/lucidi/) [🖭](http://cricca.disi.unitn.it/montresor/teaching/asd/materiale/video/) |

[TOC]



# [1.][pdf-1] Introduzione

## Cos'è Internet

### Definizioni

> **End system / Host**: *sistema terminale (dispositivo)*

> **Ampiezza di banda**: *frequenza di trasmissione (bit/s)*

> **Router**: *instrada i pacchetti verso la loro destinazione finale*

**Standard Internet**

- **RFC**: request For Comments
- **IETF**: Internet Engeneering Task Force



### Internet

> **Internet**: *infrastruttura di comunicazione per applicazioni distribuite*

“Rete delle reti”

- Struttura gerarchica
- Internet pubblica e intranet private

**Servizi** forniti alle applicazioni

- Servizio affidabile dalla sorgente alla destinazione
- Servizio best effort senza connessione
  - Non affidabile



### Protocollo

Definisce

- **Formato e ordine dei messaggi** scambiati tra entità in comunicazione
- **Azioni** intraprese in fase di trasmissione e/o ricezione di messaggi o eventi

Tipologie

- **Protocolli umani**
  - Invio di specifici messaggi
  - Quando il messaggio e ricevuto, vengono intraprese specifiche azioni, o si verificano altri eventi
- **Protocolli di rete**
  - Dispositivi hardware e software, non umani
  - Governano tutta l'attività di comunicazione in Internet





## Ai confini detta rete

### Struttura di rete

- **Confini** della rete
  - Applicazioni
  - Sistemi terminali
- **Reti**, dispositivi fisici
  - collegamenti cablati e wireless
- **Centro** della rete
  - Router interconnessi
  - La rete delle reti



### ==Reti condivise e dedicate==



### Architetture ai confini

- **Sistemi terminali** (**host**)
  - Fanno girare programmi applicativi
  - Situati all'estremità di Internet
  - ~~es: Web, email~~
- **Architettura client/server**
  - L'host client richiede e riceve un servizio da un programma server in esecuzione su un altro terminale
  - ~~es: browser/server Web, client/server email~~
- **Architettura peer to peer**
  - Uso limitato (o inesistente) di server dedicati
  - ~~es: Skype, Bit Torrent~~



### Reti d'accesso

> **Rete d'accesso**: *collegamenti fra sistemi terminali e router esterni*

Tipi di reti di accesso

- **Residenziale**: punto-punto
- **Aziendale**: reti locali (LAN)
- **Mobile**: wireless



#### Accesso residenziale

- **Modern dial-up**
  - Fino a 56 kbit/s ~~(spesso inferiore)~~
  - Non e possibile navigare e telefonare nello stesso momento
- **DSL** (Digitat Subsoriber Line)
  - Installato generalmente da società telefoniche
  - Fino a 1-5 Mbit/s in upstream
  - Fino a 10-50 Mbit/s in downstream
  - Linea dedicata
- ==**FTTH**  (Fiber To The Home)==



#### Accesso aziendale

**LAN** che collega sistemi terminati di aziende e università all'edge router

- **Ethernet**
  - 10 Mbit/s, 100 Mbit/s, 1 Gbit/s, 10 Gbit/s
  - Moderna configurazione: sistemi terminali collegati con uno switch Ethernet



#### Accesso ==mobile / wireless==

**Rete condivisa d'accesso wireless** che collega i sistemi terminali al router attraverso la stazione base, detta **access point**

- **LAN wireless**
  - 802.11a/b/g/n/ac (WiFi): 11, 54, 100+ Mbit/s
- **Rrete d'accesso wireless geografica**
  - Gestita da un provider di telecomunicazioni
  - Da qualche Mbit/s per sistemi cettutari 3G (UMTS, HSDPA) ad 1 Gbit/s
  - Oggi 4G/5G



#### Reti domestiche

Componenti di una tipica rete da abitazione

- DSL o modem via cavo
- Router / firewall / NAT
- Ethernet
- Punto d'accesso wireless



### Mezzi trasmissivi

- **Bit**
  - Viaggia da un sistema terminate a un altro
  - Passando per una serie di coppie trasmittente-ricevente
- **Mezzo fisico**
  - Ciò che sta fra il trasmittente e il ricevente
- **Mezzi guidati**
  - I segnali si propagano in un mezzo fisico
    - Fibra ottica, filo di rame, cavo coassiale
- **Mezzi a onda libera**
  - I segnali si propagano nell'atmosfera e nello spazio esterno



#### Doppino intrecciato (TP)

- **Due fili** di rame avvolti
  - Tipico cavo usato per lo standard Ethernet
- Diversi tipi di **schermatura**
  - Nessuna (unshielded)
  - Schermatura per doppino (shielded)
  - Lamina o maglia che avvolge l'ntero cavo (foiled)
  - Entrambe (screened)



#### Denominazione sintetica dei cavi

- **X / Y TP**
  - X è la schermatura dell'intero cavo
    - U: unshielded
    - F: foiled (di solito una lamina di alluminio)
    - S: maglia metallica intrecciata (di solito rame placcato alluminio)
    - SF: entrambe
  - Y è la schermatura di ogni doppino
    - U: unshielded
    - F: shielded

[Esempi e immagini (slide 21-27)][pdf-1]



#### Cavo coassiale e fibra ottica

- **Cavo coassiale**
  - Due conduttori in rame concentrici
  - **Bidirezionale**
  - **Banda base**
    - Singolo canale sul cavo
    - Legacy Ethernet
  - **Banda larga**
    - Più canali sul cavo
    - HFC
- **Fibra ottica**
  - Mezzo sottile e flessibile che conduce impulsi di luce
    - Ciascun impulso rappresenta un bit
  - **Alta frequenza trasmissiva**
    - Elevata velocità di trasmissione punto-punto (da 10 a 100 Gbit/s)
  - Notevoli vantaggi
    - Basso tasso di errore
    - Ripetitori distanziati
    - Immune all'interferenza elettromagnetica
  - Mezzo preferito per **collegamenti long-haul**



#### Canali radio

- Trasportano segnali nello **spettro elettromagnetico**
- **Non** richiedono l'installazione fisica di **cavi**
- **Bidirezionali**
- Effetti dell'**ambiente** di propagazione
  - Riflessione
  - Ostruzione da parte di ostacoli
  - Interferenza



#### Tipi di canali radio

- **Microonde terrestri**
  - Canali fino a 45 Mbit/s
- **LAN** (es: WiFi)
  - 11Mbit/s, 54 Mbit/s, 100+ Mbit/s
- **Wide-area** (es: cellulari)
  - 3G: ~1 Mbit/s
  - HSDPA: ~14.4 Mbit/s
  - LTE: 100 Mbit/s
  - 5G: ?
- **Satellitari**
  - Canali fino a 45 Mbit/s (o sottomultipli)
  - Ritardo punto-punto di ~280 ms
  - Geostazionari (GEO) a 36.000 km
  - Low-Earth Orbit (LEO) a bassa quota





## Il nucleo della rete

### Trasferimento di dati

> **Nucleo della rete**: *rete magliata di router che interconnettono sistemi terminali*

Il **trasferimento di dati** attraverso la rete avviene tramite **commutazione di**

- **Circuito**: circuito dedicato per l'intera durata della sessione 
  - Rete telefonica
- **Pacchetto**: i messaggi di una sessione utilizzano le risorse su richiesta
  - Di conseguenza potrebbero dover attendere per accedere a un collegamento



### Commutazione di circuito

**Risorse di rete** (es. ampiezza di banda, bandwidth) suddivise in '**porzioni**'

- Ripartizione della bit rate
- Divisione di frequenza
- Divisione di tempo

==Proprietà==

- Ciascuna 'porzione' viene **allocata** ai vari collegamenti
- Le risorse rimangono **inattive** se non utilizzate
  - Non c'è condivisione

[Esempi (slide 34-35)][pdf-1]



### Commutazione di pacchetto

**Flusso di dati** punto-punto suddiviso in **pacchetti**

- I pacchetti degli utenti **condividono** le risorse di rete
- Ciascun pacchetto utilizza **completamente** il canale
- Le risorse vengono usate a seconda delle necessità (**on demand**)

**Contesa per le risorse**

- La richiesta di risorse può **eccedere** il quantitativo disponibile
- **Congestione**: accodamento dei pacchetti, attesa per l'utilizzo del collegamento
- **Store and forward**: il commutatore deve ricevere l'intero pacchetto prima di poter cominciare a trasmettere sul collegamento in uscita

<p></p>

#### Multiplexing statistico

- La sequenza dei pacchetti A e B **non** segue uno **schema prefissato**
  - Condivisione di risorse **su richiesta** → **multiplexing statistico**
- **TDM**: ciascun host ottiene uno **slot di tempo**
  - Dedicato unicamente a quella trasmissione

<p></p>

#### Store and forward

- Occorrono $L/R$ secondi per **trasmettere** (push out) un pacchetto di $L\ \rm bit$ su un collegamento in uscita da $R\  \rm bit/s$
- **Store and forward**: l'intero pacchetto deve arrivare al router prima che questo lo trasmetta sul link successivo
- **Tempo di trasmissione** totale:  $3\,L/R$
  - Supponendo che il ritardo di propagazione sia zero



### Confronto fra commutazioni

<u>Dati</u>

- 1 collegamento da 1 Mbit/s
- Ciascun utente
  - 1 kbit/s quando attivo
  - Attivo per il 10% del tempo

- <u>Commutazione di circuito</u>
  - **10 utenti**
- <u>Commutazione di pacchetto</u>
  - Consente a **più utenti** di usare la rete
  - **Fino a 10 utenti attivi**: tutti possono trasmettere contemporaneamente
  - **Più di 10 utenti attivi**: i pacchetti si accumulano finché gli utenti attivi non diminuiscono
  - **Con 35 utenti**: la probabilità di averne più di 10 attivi è inferiore a 0,0004

<p></p>

#### Commutazione di pacchetto

- Ottima per i **dati a raffica**
  - **Condivisione** delle risorse
  - **Più semplice**
    - Non necessita l'impostazione della chiamata
- **Eccessiva congestione**: ritardo e perdita di pacchetti
  - Sono necessari **protocolli** per
    - **Trasferimento** affidabile dei dati
    - **Controllo** della congestione
- Comportamento **circuit-like**
  - Necessario fornire garanzie di **larghezza di banda** per le applicazioni audio/video
  - Ancora un problema irrisolto



### Struttura di Internet









---

###### -





# 🗍

[root]: ../Reti
[pdf-0]: ../Reti/0.Intro.pdf
[pdf-1]: ../Reti/1.Introduzione.pdf
[pdf-2]: ../Reti/2.Livello.applicazione.pdf
[pdf-3]: ../Reti/3.Livello.trasporto.pdf
[pdf-4]: ../Reti/4.Livello.rete.pdf
[pdf-5]: ../Reti/5.BGP.pdf
[pdf-6]: ../Reti/6.Livello.data.link.pdf