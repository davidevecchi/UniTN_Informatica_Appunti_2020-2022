# ASD – Analisi di algoritmi

|      |           |                                                              |
| ---- | :-------: | -----------------------------------------------------------: |
| ASD  | Analisi di algoritmi | [🗀][root] [🗍](http://cricca.disi.unitn.it/montresor/teaching/asd/materiale/lucidi/) [🖭](http://cricca.disi.unitn.it/montresor/teaching/asd/materiale/video/) |

[TOC]



# 1. Introduzione

## Concetti di base

### Definizioni

> ­[^1] **Problema computazionale**
> ­[^2] **Algoritmo**
## Valutare un algoritmo

### Efficienza

> ­[^3] **Complessità**
> ­[^4] **Risorse**
> ­[^5] **Tempo**
### Correttezza

> ­[^6] **Invariante**
> ­[^7] **Invariante di ciclo**
> ­[^8] **Invariante di classe**
### Complessità

#### Dimensione dell’input

> ­[^9] **Taglia dell’input**
#### Tempo

> ­[^10] **Tempo**



# 2. Analisi di algoritmi

## Modelli di calcolo

### Definizioni

> ­[^11] **Modello di calcolo**
#### Macchina di Turing

> ­[^12] **Macchina di Turing**
#### Random Access Machine

> ­[^13] **Random Access Machine**
### Classi di complessità

> ­[^14] **Classi di complessità**
## Notazione asintotica

### Definizioni

> ­[^15] **Notazione $O\,$**
> ­[^16] **Notazione $Ω\,$**
> ­[^17] **Notazione $Θ\,$**
## Complessità di problemi e algoritmi

### Algoritmi e problemi

#### Limiti alla complessità di un problema

> ­[^18] **Limiti superiore e inferiore di un problema**



# 3. Funzioni di costo

## Notazione asintotica

### Espressioni polinomiali

> ­[^19] **Espressione polinomiale**
### Notazioni $o$, $ω$

> ­[^20] **Notazione $o$**
> ­[^21] **Notazione $ω$**
## Ricorrenze

### Definizioni

> ­[^22] **Equazione di ricorrenza**
> ­[^23] **Formula chiusa**
### Metodo dell’esperto

> ­[^24] **Ricorrenze comuni**



# 4. Analisi ammortizzata

## Introduzione

### Definizione

> ­[^25] **Analisi ammortizzata**
### Metodi per l’analisi

#### Aggregazione

> ­[^26] **Aggregazione**
#### Potenziale

> ­[^27] **Funzione di potenziale**
> ­[^28] **Costo ammortizzato - Potenziale**







---




# Termini
- Problema computazionale[^1]
- Algoritmo[^2]
- Complessità[^3]
- Risorse[^4]
- Tempo[^5]
- Invariante[^6]
- Invariante di ciclo[^7]
- Invariante di classe[^8]
- Taglia dell’input[^9]
- Tempo[^10]
- Modello di calcolo[^11]
- Macchina di Turing[^12]
- Random Access Machine[^13]
- Classi di complessità[^14]
- Notazione $O\,$[^15]
- Notazione $Ω\,$[^16]
- Notazione $Θ\,$[^17]
- Limiti superiore e inferiore di un problema[^18]
- Espressione polinomiale[^19]
- Notazione $o$[^20]
- Notazione $ω$[^21]
- Equazione di ricorrenza[^22]
- Formula chiusa[^23]
- Ricorrenze comuni[^24]
- Analisi ammortizzata[^25]
- Aggregazione[^26]
- Funzione di potenziale[^27]
- Costo ammortizzato - Potenziale[^28]







---
[^1]: **Problema computazionale**: *relazione matematica che associa un elemento del dominio di output ad ogni elemento del dominio di input*
---
[^2]: **Algoritmo**: *procedimento effettivo, espresso tramite un insieme di passi elementari ben specificati in un sistema formale di calcolo, che risolve il problema in tempo finito*
---
[^3]: **Complessità**: *analisi delle risorse impiegate da un algoritmo per risolvere un problema, in funzione della dimensione e dalla tipologia dell’input*
---
[^4]: <u>Definizione</u>  (**Risorse**)<br>- **Tempo**: tempo impiegato per completare l’algoritmo<br>- **Spazio**: quantità di memoria utilizzata<br>- **Banda**: quantità di bit spediti (algoritmi distribuiti)
---
[^5]: <u>Definizione</u>  (**Tempo**)<br>- **Wall-clock time**: tempo effettivamente impiegato per eseguire un algoritmo<br>- **Numero di operazioni rilevanti**: che caratterizzano lo scopo dell’algoritmo<br>- **Numero di operazioni elementari**: eseguibili in tempo costante dalla CPU
---
[^6]: **Invariante**: *condizione sempre vera in un certo punto del programma*
---
[^7]: **Invariante di ciclo**: *condizione sempre vera all’inizio dell’iterazione di ciclo*
---
[^8]: **Invariante di classe**: *condizione sempre vera al termine dell’esecuzione di un metodo della classe*
---
[^9]: <u>Definizione</u>  (**Taglia dell’input**)<br>Numero di<br>- **Bit** necessari per rappresentarlo (**criterio di costo logaritmico**)<br>- **Elementi** di cui è costituito (**criterio di costo uniforme**)
---
[^10]: **Tempo**: *numero di istruzioni elementari eseguibili in tempo costante*
---
[^11]: **Modello di calcolo**: *rappresentazione astratta di un calcolatore*
---
[^12]: <u>Definizione</u>  (**Macchina di Turing**)<br>Macchina ideale che manipola i dati contenuti su un nastro di lunghezza infinita secondo un insieme prefissato di regole
---
[^13]: <u>Definizione</u>  (**Random Access Machine**)<br>- **Memoria**<br>  - Quantità infinita di celle di dimensione finita<br>  - Accesso in tempo costante<br>    - Indipendente dalla posizione<br>- **Processore**<br>  - Uno solo<br>  - Set di istruzioni elementari simile a quelle reali<br>    - Operazioni aritmetiche e logiche<br>    - Istruzioni di controllo<br>- **Costo delle istruzioni elementari**<br>  - Uniforme<br>  - Ininfluente ai fini della valutazione
---
[^14]: <u>Definizione</u>  (**Classi di complessità**)<br>$$\begin{array}{c}& f(n) && \rm Tipo & \\ \hline& \log n && \rm logaritmico \\& \sqrt n && \rm sublineare \\& n && \rm lineare \\& n\log n && \rm loglineare \\& n^k && \rm polinomiale \\& k^n && \rm esponenziale\end{array}$$
---
[^15]: <u>Definizione</u>  (**Notazione $O\,$**)<br>Sia $g(n)$ una funzione di costo<br>Si indica con $O(g(n))$ l'insieme delle funzioni $f(n)$ tali per cui<br>$$f(n)=O(g(n))\iff \exist\, c > 0,\ \exist\,m\ge 0\ : \ f(n)\le cg(n),\ \ \forall\, n\ge m$$
---
[^16]: <u>Definizione</u>  (**Notazione $Ω\,$**)<br>Sia $g(n)$ una funzione di costo<br>Si indica con $Ω(g(n))$ l'insieme delle funzioni $f(n)$ tali per cui<br>$$f(n)=Ω(g(n))\iff \exist\, c > 0,\ \exist\,m\ge 0\ : \ f(n)\ge cg(n),\ \ \forall\, n\ge m$$
---
[^17]: <u>Definizione</u>  (**Notazione $Θ\,$**)<br>Sia $g(n)$ una funzione di costo<br>Si indica con $Θ(g(n))$ l'insieme delle funzioni $f(n)$ tali per cui<br>$$f(n)=Θ(g(n))\iff\\ \exist\, c_1, c_2 > 0,\ \exist\,m\ge 0\ : \ c_1g(n)\le f(n)\le c_1g(n),\ \ \forall\, n\ge m$$
---
[^18]: <u>Definizione</u>  (**Limiti superiore e inferiore di un problema**)<br>Un problema ha complessità $\lang O,Ω\rang (f (n))$ se esiste almeno un algoritmo avente complessità $\lang O,Ω\rang (f (n))$ che lo risolve
---
[^19]: <u>Definizione</u>  (**Espressione polinomiale**)<br>$$f(n) = \sum_{i=0}^k a_in^i,\ \ a_k\ne0 \ \ \Rarr\ \ f(n)=Θ(n^k)$$
---
[^20]: <u>Definizione</u>  (**Notazione $o$**)<br>Sia $g(n)$ una funzione di costo<br>Si indica con $o(g(n))$ l’insieme delle funzioni $f (n)$ tali per cui<br>$$f(n) = o(g(n)) \iff ∀\,c,\ ∃\,m\ :\ f (n) < cg(n),\ ∀\,n ≥ m$$
---
[^21]: <u>Definizione</u>  (**Notazione $ω$**)<br>Sia $g(n)$ una funzione di costo<br>Si indica con $ω(g(n))$ l’insieme delle funzioni $f (n)$ tali per cui<br>$$f(n) = ω(g(n)) \iff ∀\,c,\ ∃\,m\ :\ f (n) > cg(n),\ ∀\,n ≥ m.$$
---
[^22]: **Equazione di ricorrenza**: *formula matematica definita in maniera ricorsiva che esprime la complessità di un algoritmo ricorsivo*
---
[^23]: **Formula chiusa**: *rappresenta la classe di complessità della funzione*
---
[^24]: **Ricorrenze comuni**: *ricorrenze facilmente risolubili ricorrendo a teoremi specifici per ogni classe particolare di equazioni di ricorrenza*
---
[^25]: <u>Definizione</u>  (**Analisi ammortizzata**)<br>Tecnica di analisi di complessità che valuta il **tempo richiesto** per eseguire, nel caso pessimo, una sequenza di operazioni su una **struttura dati**
---
[^26]: <u>Definizioni</u>  (**Aggregazione**)<br>- **Sequenza**: evoluzione della struttura data una sequenza di operazioni<br>- **Caso pessimo**: peggior sequenza di operazioni<br>- **Aggregazione**: sommatoria delle complessità individuali
---
[^27]: <u>Definizione</u>  (**Funzione di potenziale**)<br>Una funzione di potenziale $Φ$ associa ad uno **stato** $S$ della struttura dati la "**quantità di lavoro**" $Φ(S)$ che è stato contabilizzato nell’analisi ammortizzata, ma non ancora eseguito
---
[^28]: <u>Definizione</u>  (**Costo ammortizzato - Potenziale**)
---
