# Insiemi

## 1. (3-11) Operazioni

Dato l'insieme $Ω = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$ e $A, B, C, D ∈ {\cal P}(Ω)$

$A = \{9, 7\} \\
B = \{7, 9\} \\
C = \{4, 10, 9, 7, 6, 1\} \\
D = \{10, 4, 9, 1\}$

Le seguenti affermazioni sono vere o false?



> `TEORIA` (**regole di De Morgan**)
>
> - $(A ∪ B)^c = A^c ∩ B^c$
> - $(A ∩ B)^c = A^c ∪ B^c$



### Q1

> $$
> ((A ∪ B)^c ∩ D^c) ∩ C^c = Ω^c
> $$

$((A ∪ B)c ∩ D^c) ∩ C^c = Ω^c ⇔ (A ∪ B ∪ D ∪ C)^c = ∅$

==FALSE==



### Q2

> $$
> ((A ∩ B)^c ∪ D^c) ∪ C^c = Ω
> $$

$((A ∩ B)^c ∪ D^c) ∪ C^c = (A ∩ B ∩ D ∩ C)^c=\{9\}^c \ne Ω$

==FALSE==



### Q3

> $$
> (B ∩ C)^c ∪ A^c = (A ∩ B)^c ∪ C^c
> $$

$(B ∩ C)^c ∪ A^c = B^c\cup C^c \cup A^c = (B\cap C \cap A)^c$

$(A ∩ B)^c ∪ C^c=(A ∩ B ∩ C)^c$

$(B\cap C \cap A)^c=(A ∩ B ∩ C)^c$

==TRUE==



### Q4

> $$
> ((C^c △ D^c) ∩ B)^c = ∅
> $$

$C^c △ D^c=C △ D$

$(C^c △ D^c) ∩ B = (C △ D) ∩ B = (C ∩ B) △ (D ∩ B)$

$(\{7,9\}△\{9\})^c=\{7\}^c\ne \empty$

==FALSE==



### Q5

> $$
> (A △ C △ D) ∩ B = ∅
> $$

$(A △ C △ D) ∩ B = (A ∩ B) △ (C ∩ B) △ (D ∩ B)$

$\{7,9\}△\{7,9\}△\{9\}=\{9\}\ne \empty$

==FALSE==





## 2. (3-12) Lettere

$Ω = \{ f, i, s, g, e, r, u, n, m, k, y, o, t, j, l, p\}$ lo spazio campionario

$P(Ω) ∋ \cal A = \{∅, \{ g, p, k \}, \{ f, i, s, e, r, u, n, m, y, o, t, j, l\},\\ \{ f, i, s, g, e, r, u, n, m, k, y, o, t, j, l, p\}\}$

$A = \{ o, s, l, t, y, n, m, i, k, u, f, j\}$ un sottoinsieme di $Ω$.



### Q1

> $\cal A$ è un'algebra su $Ω$?

> `TEORIA` (**algebra**)
>
> Un insieme $\cal A$ è un'algebra di $Ω$ se
>
> - $\{\empty,Ω\} \sub \cal A$
> - $∀A ∈ {\cal A} → A^c ∈ \cal A$
> - L'unione finita di elementi di $\cal A$ continua a stare in $\cal A$
>

==TRUE==



### Q2

> Si determini la probabilità che, pescando da $A$, si estragga una vocale

$E=\{o,i,u\}$

$\Pr(E)=\dfrac{\#E}{\#A}=$==$1/4$==



### Q3

> Si determini la probabilità che, pescando da $A$, si estragga $\{s, t, a, i, c\}$

$E=\{s,t,a,i,c\}\cap A = \{s,t,i\}$

$\Pr(E)=\dfrac{\#E}{\#A}=$==$1/4$==



### Q4

> Si determini la probabilità che, pescando da $A$, si estragga una vocale che sta in $\{s, t, a, i, c\}$

$E=\{s,t,a,i,c\}\cap\{a,e,i,o,u\}\cap A = \{i\}$

$\Pr(E)=\dfrac{\#E}{\#A}=$==$1/12$==



### Q5

> Si determini la probabilità che, pescando da $A$, si estragga una vocale o $\{s, t, a, i, c\}$

$E=(\{s,t,a,i,c\}\cap A)\cup(\{a,e,i,o,u\}\cap A) = \{i,o,u,s,t\}$

$\Pr(E)=\dfrac{\#E}{\#A}=$==$5/12$==







# Probabilità

## 3. (3-13) Dadi

Durante un gioco da tavolo un giocatore deve tirare **2 dadi da 10** e tenere il **valore più alto**. Se tale valore è **almeno 8** il giocatore non subirà danni



### Q1

> Qual è la probabilitá che il giocatore non subisca danni?

> `TEORIA` (**probabilità dell'unione**)
> $$
> \Pr(A \cup B)= \Pr(A)+\Pr(B)-\Pr(A \cap B)
> $$

$\Pr(d_1\ge8 \cup d_2\ge8)= 2·\Pr(d\ge8)-\Pr(d_1\ge8 \cap d_2\ge8)=$

$=2·3/10-(3/10)^2=$==$0.51$==



### Q2

> Il **primo dado** è stato lanciato e il giocatore ha ottenuto **5**. Qual è la probabilità che il giocatore non subisca danni?

$\Pr(S)=$==$3/10$==



### Q3

> Qual è la probabilità di ottenere lo stesso valore sui due dadi?

$\Pr(S)=$==$1/10$==





## 4. (3-16) Condizionata e insiemi

Sia $Ω = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15\}$ uno spazio campionario.

L'esperimento aleatorio consiste nell'estrazione di un numero da $Ω$.

Consideriamo ogni numero equiprobabile.

$A = \{4, 6, 8, 15\}\\ B = \{2, 4, 15\}\\ C = \{11, 3, 14, 5, 7, 13\}$ 

tre sottoinsiemi dello spazio campionario.



### Q1

> Qual è la probabilità $\Pr(A|B)$?

$a\in A\ \ → \ \ \Pr(A|B)=\Pr(a\in B)=$==$2/3$==



### Q2

> Qual è la probabilità $\Pr(A ∩ B|A ∪ B)$?

$\Pr(A ∩ B|A ∪ B)=\dfrac{\Pr(A ∩ B)}{\Pr(A ∪ B)}=\dfrac{2/15}{5/15}=$==$2/5$==​



### Q3

> Qual è la probabilità di $\Pr(C|A ∪ B)$?

$\Pr(C|A ∪ B)=\dfrac{\Pr(C ∩ (A\cup B))}{\Pr(A ∪ B)}=\dfrac{0}{5/15}=$==$0$==



### Q4

> Qual è la probabilità che nessuno dei 3 si verifichi?

$\Pr((A\cup B\cup C)^c)=1-\Pr(A\cup B\cup C)=1-11/15=$==$4/15$==​





## 5. (3-17) Moneta truccata

Si consideri il lancio di una moneta, di cui **non si sa se sia equilibrata** o truccata. Ci viene detto che, lanciando la moneta due volte, la probabilità di ottenere esattamente una testa $T$ e una croce $C$ (non necessariamente in questo ordine) è 0.455



### Q1

> La moneta è equilibrata?

$2·\Pr(C)·\Pr(T)=0.455\ne0.5$

==FALSE==



### Q2

> Supponiamo che la probabilità di fare croce $\Pr(C)$ sia minore o uguale della probabilità $\Pr(T)$ di fare testa. Tiriamo la moneta ed esce $C$. Qual è la probabilità di ottenere nuovamente $C$ rilanciando la moneta?

$\Pr(C)\le\Pr(T)$

$\Pr(C)·\Pr(C)+\Pr(T)·\Pr(T)=1-0.455=0.545$

$\begin{cases}
c^2+t^2=0.545\\
c· t = 0.2275
\end{cases}$

$\begin{cases}
c = 0.2275/t\\
0.05175625/t^2+t^2=0.545
\end{cases}$

$\begin{cases}
c = 0.2275/t\\
t^4-0.545t^2+0.05175625=0
\end{cases}$

$t^2=\{0.1225,0.4225\}\ →\ c=0.35,\ t=0.65$

==$\Pr(C)=0.35$==



### Q3

> Giochiamo ancora e questa volta lanciamo la moneta tre volte. Due su tre sono $T$, qual è la probabilità che non siano tre $T$?

$\Pr(\{T,T,C\}|\{T,T\})=1-\Pr(\{T,T,T\}|\{T,T\})$

$1-\Pr(\{T,T,T\}|\{T,T\})=1-\dfrac{\Pr(T)^3}{\Pr(T)^3+3·\Pr(T)^2·\Pr(C)}=$==$0.6176471$==





## 6. (3-18) Urna con reimmissione

Un'urna contiene **28 palline**, etichettate con numeri da 1 a 28. Si estraggono **due palline con reimmissione**



### Q1

> Qual è la probabilità che almeno una delle due palline pescate sia etichettata con un numero minore o uguale a 20?

$\Pr(a\le20\cup b\le20)=1-\Pr(a>20\cap b>20)$

$1-\Pr(a>20\cap b>20)=1-(8/28)^2=$==$45/49$==



### Q2

> Qual è la probabilità che la somma dei numeri sulle due palline sia pari sapendo che almeno una delle due palline pescate sia etichettata con un numero minore o uguale a 20?

==$\Pr(S|A\cup B)=0.5$==

![image-20200606202619857](/home/zeep/Documenti/UniTN/2-Semestre/0_Note/stat-es.assets/image-20200606202619857.png)





## 7. (3-19) Bayes meteo

Le previsioni **meteo** dicono che oggi la probabilità di **pioggia** è **0.16**, la probabilità che ci sia **bel tempo** è **0.83** ma che c'è anche una remota probabilità, **0.01**, che **nevichi**

La probabilità che Mario Rossi arrivi **tardi** al lavoro in caso di **pioggia** è **0.15**, in caso di **neve 0.68**, mentre con il **bel tempo** la probabilità che lui sia in ritardo scende a **0.03**

Oggi Mario è in ritardo al lavoro



### Q1

>Qual è la probabilità che oggi stia piovendo?

$\Pr(P|R)=\dfrac{\Pr(R|P)·\Pr(P)}{\sum_X^{\{P,N,S\}} \Pr(R|X)·\Pr(X)}=$==$0.4308797$==





## 9. (3-24) Scatole palline

In questo esperimento casuale ci sono due scatole (A e B) contenenti un diverso numero di palline bianche e nere

In particolare, la scatola **A** contiene **20 bianche** e **12 nere**, mentre la scatola **B** contiene **17 bianche e 23 nere**

Si pesca da A una pallina e, senza guardarla, la si inserisce in B; poi si estrae una pallina da B



### Q1

> Qual è la probabilità che la pallina estratta da B sia bianca?

$\Pr(B_b')=\Pr(A_b)·(18/41)+\Pr(A_n)·(17/41)=$==$0.429878$==



### Q2

> Sapendo che la pallina estratta da B è bianca, qual è la probabilità che fosse bianca anche la pallina estratta da A?

$\Pr(A_b|B'_b) = \dfrac {\Pr(B'_b|A_b) · \Pr(A_b)}{\Pr(B'_b)}=\dfrac {(18/41) · \Pr(A_b)}{\Pr(B'_b)}=$==$0.6382979$==





## 13. (3-30) Gatti covid

Si calcola che il **16%** dei gatti di una regione sia **portatore** di un virus pericoloso per l'uomo. I gatti vengono sottoposti a un test che presenta un certo margine di insicurezza, nel senso che esso dà **risposta positiva** sia nel **90% dei gatti portatori** sia nel **3% dei gatti sani** (non portatori). Un gatto viene sottoposto al test.



### Q1

> Determinare la probabilità di una risposta negativa del test.

$\Pr(N_t)=1-(0.16·0.90+(1-0.16)·0.03)=$==$0.8308$==



### Q2

> Sapendo che la risposta è stata negativa, determinare la probabilità che il gatto sia, in realtà, portatore.

$\Pr(P_g|N_t)=\dfrac {\Pr(N_t|P_g) · \Pr(P_g)}{\Pr(N_t)}=\dfrac {(1-0.90) · 0.16}{0.8308}=$==$0.01925855$==





## 14. (3-31) Messaggio bambini

Due bambini giocano a trasmettersi un messaggio attraverso uno strano apparecchio. Questo può inviare sequenze di 4 caratteri composte dalle sole lettere “A”, “B”, “C”. Uno dei due bambini trasmette una delle seguenti stringhe

- “AAAA”, con probabilità 0.21
- “BBBB”, con probabilità 0.29
- “CCCC”, con probabilità 0.50

Per ogni lettera, la probabilità che essa sia trasmessa correttamente è $p = 0.52$ e distorta in ciascuna delle altre due con la stessa probabilità. Ogni lettera è trasmessa in maniera indipendente dalla ogni altra.



### Q1

> Calcolare la probabilità che sia stata trasmessa la sequenza “AAAA”, avendo ricevuto la sequenza “B, B, B, A”

$\Pr(A|BBBA)=\\
=\dfrac {\Pr(BBBA|A) · \Pr(A)}{\Pr(BBBA|A) · \Pr(A)+\Pr(BBBA|B) · \Pr(B)+\Pr(BBBA|C) · \Pr(C)}$

$n=((1-p)/2)$

$\Pr(A|BBBA)=\dfrac {n^3· p · \Pr(A)}{n^3· p · \Pr(A)+p^3 · n·  \Pr(B)+n^4 · \Pr(C)}=$==$0.116527$==



### Q2

> Date le tre lettere “A”, “B”, “C” quante sono le possibili sequenze lunghe 3 caratteri?

$D_{3,3}^r=3^3=$==$27$==







# Calcolo combinatorio

## 8. (3-23) Comitati mate-fisica

Il preside della facoltà di Scienze deve istituire un comitato formato da **8 persone** tra matematici o fisici per valutare un candidato per la cattedra di Fisica Matematica

In facoltà ci sono **22 matematici** e **15 fisici**



### Q1

> Quanti sono i possibili comitati formati da 5 matematici e 3 fisici?

$c=C_{22,5}· C_{15,3}={22 \choose 5}·{15 \choose 3}=$==$11981970$==



### Q2

> Qual è la probabilità di avere un comitato di 5 matematici e 3 fisici?

$\Pr(C)=\dfrac{c}{\#Ω}=\dfrac{c}{C_{37,8}}=$==$0.3103492$==



### Q3

> Quanti sono i possibli comitati (sempre di 8 persone) tali che
>
> 1. abbiano più matematici che fisici (>)
> 2. contengano almeno un fisico

Dobbiamo considerare i comitati formati da

- 1 fisico e 7 matematici
- 2 fisici e 6 matematici
- 3 fisici e 5 matematici

$d=C_{15,1}· C_{22,7}+C_{15,2}· C_{22,6}+C_{15,3}· C_{22,5}=$==$22374495$==





## 10. (3-25) Bandiere

Vogliamo disegnare una bandiera, formata da tre strisce verticali colorate
Vogliamo che il colore della striscia centrale sia diverso dalle altre due



### Q1

> Quante possibili bandiere diverse possiamo creare con 5 colori?

$n=5·4·4=$==$80$==



### Q2

> Consideriamo ora le possibili bandiere ottenute: qual è la probabilità di avere una bandiera con solo due colori?

$\Pr(E)=\dfrac{5·4·1}{5·4·4}=$==$1/4$==





## 12. (3-27) Combinazioni

Siano $N = 7200$ e $r = 4$.



### Q1

> Quanti sono i possibili sottoinsiemi di {1, … , 7200} con 4 elementi?

$C_{N,r}=$==$1.1188111 × 10^{14}$==



### Q2

>Quanti sono i possibili sottoinsiemi di {1, … , 7200} con 4 elementi e tali che contengano almeno un numero pari?

$C_2=C_{N,r}-C_{N/2,r}=$==$1.0489437 × 10^{14}$==



### Q3

> Qualcuno estrae casualmente 4 numeri da {1, … , 7200} e annuncia che fra i numeri estratti c'è almeno un numero divisibile per due. Qual è la probabilità che tutti e 4 i numeri estratti siano divisibili per due?

$\Pr(E)=\dfrac{C_{N/2,r}}{C_2}=$==$0.0666074$==







# Serie geometriche

> `TEORIA` (**distribuzione geometrica**)
>
> Siano $n$ eventi $E_1,...,E_n$ che possono verificarsi ciascuno con probabilità $p_1,...,p_n$, in successione e a rotazione
>
> Sia $X_i$ l'evento “si verifica $E_i$ per primo”
>
> Chiamiamo $x$ la probabilità che non si verifichi nessuno degli $n$ eventi $E$ in un certo ciclo, ovvero la ragione della serie geometrica ($x<1$)
> $$
> x=\prod_{j=0}^{n}(1-p_j)
> $$
>
> $$
> \Pr(X_i)=\sum_{k=0}^{\infin} \Bigg( \prod_{j=0}^{i-1}(1-p_j) · p_i · x^k  \Bigg) = \dfrac{\prod_{j=0}^{i-1}(1-p_j) · p_i}{1-x}
> $$



## 11a. (3-26) Canestri

Tre amici, a turno, tirano una palla verso il canestro. Il primo ha una probabilità $p_1 = 0.8$ di fare canestro, il secondo $p_2 = 0.77$ e il terzo $p_3 = 0.1$

Continuano a tirare, secondo lo stesso ordine, finchè uno di loro non segna



Consideriamo i seguenti eventi complementari

$C_i^k$ :  al tiro $k$ il giocatore $i$ fa canestro

$M_i^k$ :  al tiro $k$ il giocatore $i$ non fa canestro



### Q1

> Probabilità che il primo a fare canestro sia il primo giocatore

$\Pr(E_1)=\sum_{k=0}^\infin p_1((1-p_1)(1-p_2)(1-p_3))^k=\sum_{k=0}^\infin p_1· x^k$

$\Pr(E_1)=\dfrac{p_1}{1-x}=\dfrac{p_1}{1-(1-p_1)(1-p_2)(1-p_3)}=$==$0.8345504$==



### Q2

> Probabilità che il primo a fare canestro sia il secondo giocatore.

$\Pr(E_2)=\sum_{k=0}^\infin (1-p_1)p_2((1-p_1)(1-p_2)(1-p_3))^k=\sum_{k=0}^\infin(1-p_1)p_2· x^k$

$\Pr(E_2)=\dfrac{(1-p_1)p_2}{1-x}=\dfrac{(1-p_1)p_2}{1-(1-p_1)(1-p_2)(1-p_3)}=$==$0.1606509$==



### Q3

> Probabilità che il primo a fare canestro sia il terzo giocatore.

$\Pr(E_3)=\dfrac{(1-p_1)(1-p_2)p_3}{1-((1-p_1)(1-p_2)(1-p_3))}=$==$0.0047987$==





## 11b. (3-26) Dadi

Questo esperimento casuale consiste in una successione di prove. In ogni prova, il giocatore **A lancia 6 dadi** e il giocatore **B** contemporaneamente **ne lancia 3**. Il gioco si ferma quando almeno uno dei giocatori **ottiene un 6** su almeno un dado.



$p_A=1-(5/6)^6=0.665102$

$p_B=1-(5/6)^3=0.4212963$



### Q1

> Qual è la probabilità che il gioco si fermi a causa di A e non di B?

$P(E_1)=∑_{n=1}^∞ p_A(1−p_A)^{n−1}(1−p_B)^n =\\ = p_A(1−p_B)(∑_{n=0}^∞ ((1−p_A)(1−p_B))^n)$

Serie geometrica di ragione $(1−p_A)(1−p_B)<1(1−p_A)(1−p_B)<1$

$P(E_1)=\dfrac{p_A(1−p_B)}{1−(1−p_A)(1−p_B)}=$==$0.4774252$==



### Q2

> Qual è la probabilità che il gioco si fermi a causa di B e non di A?

$P(E_2)=\dfrac{p_B(1−p_A)}{1−(1−p_A)(1−p_B)}=$==$0.1750093$==



### Q3

> Con che probabilità il gioco si ferma perché A e B hanno ottenuto entrambi il valore giusto?

$\Pr(E_3)=1-(Pr(E_1)+Pr(E_2))=$==$0.3475656$==







# Funzioni

## 15. (4-01) Ripartizione semplice

Consideriamo lo spazio probabilizzabile $(\R, \cal B(\R))$ e sia data la seguente funzione di ripartizione
$$
F(x)=
\begin{cases}
1 − e^{−λx} & x ≥ 0 \\
0 & x <0
\end{cases}
$$
Prendiamo in particolare $λ = 2.926$



> `TEORIA` (**funzione di ripartizione**)
>
> $F (x)$ è una funzione di ripartizione, infatti soddisfa
>
> - non-decrescenza, infatti la derivata $\forall x,\ \ F'(x) = λ e^{−λx} > 0$ 
> - continua da destra e anche da sinistra (quindi in particolare limitata)
> - nulla per $x → −∞$ e tendente a uno per $x → ∞$
>
> Grazie all'identità $P ((a, b]) = F (b) − F (a)$ possiamo attribuire una probabilità agli intervalli $(a, b]$
>
> Grazie alla continuità di $F$ i punti hanno probabilità nulla, quindi tutti gli intervalli $(a, b], [a, b), [a,b], (a, b)$ sono equiprobabili



### Q1

> Qual è la probabilità dell'intervallo $[−0.228, 0.228)$?

$\Pr(I)=F(0.228)-F(-0.228)=F(0.228)=$==$0.4868197$==



### Q3

> Qual è la probabilità dell'evento $A_1 = (0.084, 0.128] ∪ (0.219, 0.52]$?

$\Pr(A_1)=F(0.128)-F(0.084)+F(0.52)-F(0.219)=$==$0.4029716$==





## 16. (4-02) Ripartizione parametri

Consideriamo lo spazio probabilizzabile $(\R, \cal B(\R))$ e la funzione
$$
F(x)=
\begin{cases}
c ⋅ (x − 1)^3 & 1 ≤ x ≤ 13.5 \\
0 & x ≤ 1 \\
1 & x ≥ 13.5
\end{cases}
$$


### Q1

> Qual è la costante $c > 0$ tale per cui $F$ è una funzione di ripartizione?

$F(13.5)=1=c ⋅ (13.5-1)^3$

$c=\big(\frac{1}{12.5}\big)^3=$==$0.000512$==



### Q3

> Qual è il numero reale $t$ tale che l'intervallo $(2, t]$ abbia probabilità $0.3$?

$F(t)-F(2)=F(t)-0.000512=0.3$

$F(t)=0.300512$

$t=(F(t)/c)^{1/3}+1=$==$9.37267$==





## 17. (4-03) Ripartizione R

Consideriamo la funzione

$F (x) = \dfrac 1 {1 + e^{1.4x}}$

definita su tutto $\R$



### Q1

> Scrivere un'implementazione in R di $F$

```R
function(x) { y <- 1 / (1 + exp(1.4*x)) }
```



### Q2

> La funzione F (x) è una funzione di ripartizione?

```R
curve(F,-10,10)
```

==FALSE==



### Q3

> Sia ora
> $$
> F_L(x) =
> \begin{cases}
> \frac 1 2e^{\frac x {1.4}} & x<0 \\
> 1-\frac 1 2e^{-\frac x {1.4}} & x\ge0 
> \end{cases}
> $$
> definita per ogni $x ∈ \R$. Essa è una funzione di ripartizione. Qual è la probabilità secondo la legge $F_L$ dell'intervallo $[0.86, 1.78]$?

$P ([0.86, 1.78]) = F_L(1.78) − F_L(0.86)=$==$0.1302982$==



### Q4

> Qual è la probabilità di {0}?

Questa probabilità è nulla, come per ogni singoletto, per la continuità di $F_L$

==$0$==





## 18. (4-06) Densità discreta

Sia $X$ una variabile aleatoria discreta con la seguente densità discreta (o funzione di massa di probabilità)
$$
p_X(x) =
\begin{cases}
0.1437 & x = 1.563 \\
0.3292 & x = 2.952 \\
0.3141 & x = 4.341 \\
0.1598 & x = 5.731 \\
0.0458 & x = 7.120 \\
0.0070 & x = 8.510 \\
0.0004 & x = 9.899
\end{cases}
$$



Determinare la funzione di ripartizione $F (x)$ della v.a. $X$
$$
F(x) =
\begin{cases}
0 & x < 1.563 \\
0.1437 & 1.563 \le x < 2.952 \\
0.4729 & 2.952 \le x < 4.341 \\
0.7870 & 4.341 \le x < 5.731 \\
0.9468 & 5.731 \le x < 7.120 \\
0.9926 & 7.120 \le x < 8.510 \\
0.9996 & 8.510 \le x < 9.899 \\
1 & 9.899 \le x
\end{cases}
$$



### Q1

> Qual è il valore della funzione di ripartizione $F (x)$ di $X$ in $x = 8.0937363$?

==$0.9926$==



### Q2

> Qual è il valore della funzione di ripartizione $F (x)$ di $X$ in $x = 5.1798821$?

==$0.787$==



### Q3

> Qual è la probabilità dell'intervallo $(2.952, 4.37]$?

$\Pr ((a, b]) = F (b) − F (a)=0.787-0.4729=$==$0.3141$==



### Q4

>Qual è la probabilità dell'intervallo $[4.341, 5.731)$?

Siccome stiamo considerando una funzione di ripartizione discontinua, non possiamo prendere il valore negli estremi dell'intervallo, ma dobbiamo guardare il limite da sinistra (o equivalentemente sottrarre il valore della densità discreta nel punto)

$\Pr ([a, b)) = \Pr (X < b) − \Pr (X < a)=0.787-0.4729=$==$0.3141$==





## 19. (4-09) Ripartizione mista

Abbiamo una funzione di ripartizione $FX(x)$ definita da
$$
F_X(x) =
\begin{cases}
0 & x < -2 \\
0.15 & -2 \le x < 1 \\
0.015x^2 + 0.035x + 0.3 & 1 \le x < 3 \\
0.13x + 0.35 & 3 < x < 5 \\
1 & 5 \le x
\end{cases}
$$



### Q1

>Quanto vale $F_X(3)$?

È una funzione di ripartizione, dunque deve essere continua a destra
$F_X(3) = \lim_{x→3^+} F_X(x) = \lim_{x→3^+}0.13x + 0.35 =$==$0.74$==



### Q2

> Qual è la probabilità di dell'intervallo $(−∞, 0)$?

$\Pr ((−∞, 0)) = \Pr (X < 0) = \lim_{x→0^−}F_X(x) =$==$0.15$==



### Q3

> Qual è la probabilità di dell'intervallo $[1, 2)$?

$\Pr([1,2))=\lim_{x→2^-}F_X(x)-\lim_{x→1^-}F_X(x)=0.43-0.15=$==$0.28$==



### Q4

> Qual è la probabilità di dell'intervallo $[1, 7)$?

$\Pr([1,7))=\lim_{x→7^-}F_X(x)-\lim_{x→1^-}F_X(x)=1-0.15=$==$0.85$==







# Distribuzioni

## 20. (4-10) Urna biglie (bin)

Un'urna contiene 16 biglie azzurre, 15 biglie bianche e 24 biglie cremisi.



### Q1

> Qual è la probabilità, effettuando una singola estrazione, di estrarre una biglia cremisi?

$\Pr(C)=$==$24/55$==



### Q2

> Supponiamo ora di fare più estrazioni con reimmissione. Qual è la probabilità di estrarre esattamente una biglia cremisi in $N = 7$ estrazioni?

$\Pr(C=1)=\text{Bin}(1,7,\Pr(C))=$`dbinom(1,7,24/55)`$=$==$0.0979356$==



### Q3

> Sempre facendo più estrazioni con reimmissione, qual è la probabilità di estrarre almeno 4 biglie azzurre in $M = 9$ estrazioni?

$\Pr(A\ge4)=1-F_X(3)=1-\sum_{k=0}^3\text{Bin}(k,9,\Pr(A))=\sum_{k=4}^9\text{Bin}(k,9,\Pr(A))$

`sum(dbinom(4:9,9,16/55)) = 1 - pbinom(3,9,16/55) = pbinom(3,9,16/55,FALSE) =` ==$0.2498292$==





## 21. (4-13) Binomiale (bin)

Abbiamo una v.a. $X$ di distribuzione binomiale di parametri $n = 12$ e $p$



### Q1

>Se abbiamo $p = 0.471$ quanto vale $\Pr(X < 5)$?

`pbinom(4,n,p) =` ==$0.2547067$==



### Q2

> Se abbiamo $p = 0.208$ quanto vale $\Pr(X ∈ [4, 6])$?

`pbinom(6,n,p) - pbinom(3,n,p) =` ==$0.2221762$==



### Q3

> Supponiamo ora invece di sapere che $\Pr(X = 0) = 0.04$. Quanto vale $p$?

$0.04=\Pr(X=0)= {n \choose 0}· p^0·(1-p)^n$

$p=1-(0.04)^{1/n}=$==$0.2352755$==





## 22. (4-14) Dado (bin, nbin)

Abbiamo un dado non equilibrato. In particolare per ogni faccia del dado, la probabilità che essa esca è

| 1    | 2    | 3    | 4    | 5    | 6    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 0.16 | 0.21 | 0.14 | 0.19 | 0.10 | 0.2  |

Vinciamo se esce 5 o 3. Se esce uno degli altri numeri perdiamo



$p=\Pr(\{3\}\cup\{5\})=0.24$



### Q1

>Consideriamo $n = 19$ lanci del dado. Qual è la probabilità che otteniamo almeno 8 successi?

`pbinom(7,n,p) =` ==$0.06289601$==



### Q2

> Lanciamo il dado finché non otteniamo un successo. Qual è la probabilità che otteniamo il primo successo esattamente al lancio numero $m= 6$?

`dnbinom(m-1,1,p) =` ==$0.06085261$==



### Q3

> Qual è la probabilità che ci occorrano più di $m = 6$ lanci per ottenere il primo successo?

`pbinom(0,m,p) =` ==$0.1926999$==





## 23. (4-15) Somma di v.a. (bin)

Abbiamo due variabili aleatorie binomiali indipendenti $X$ e $Y$, di parametri rispettivamente $(n = 7,\ p = 0.409)$ e $(n = 5,\ p = 0.409)$. Prendiamone anche la somma $S = X+ Y$



$S\sim {\cal B}(n = 5+7,\ p = 0.409)$



### Q1

> Qual è la probabilità che $S$ sia compresa nell'intervallo $[4, 5)$?

`pbinom(4,n,p) - pbinom(3,n,p) = dbinom(4,12,p) =` ==$0.2061571$==



### Q2

> Se sappiamo che $S = 8$, qual è la probabilità che $X = 4$?

$\Pr(X=4|S=8)=\dfrac{\Pr(S=8|X=4)· \Pr(X=4)}{\Pr(S=8)}=\dfrac{\Pr(Y=4)· \Pr(X=4)}{\Pr(S=8)}$

`dbinom(4,5,p) * dbinom(4,7,p) / dbinom(8,12,p) =` ==$0.3535354$==



### Q3

> Se sappiamo che $S = 7$, qual è la probabilità che $Y ∈ [1, 4]$?

$\Pr(Y∈[1,4]|S=7)=\dfrac{\Pr(S=7|Y∈[1,4])· \Pr(Y∈[1,4])}{\Pr(S=7)}$

`k <- 1:4`

`sum (dbinom(7-k,7,p) * dbinom(k,5,p)) / dbinom(7,12,p) =`
==$0.9722222$==





## 24. (4-16) Feedback prototipo (bin, nbin)

~~Prima di lanciare un nuovo prodotto, un'azienda vuole darne alcuni esemplari ad alcune persone per avere un ultimo feedback e farsi ulteriore pubblicità: infatti come condizione chiede che i riceventi pubblichino almeno un post al giorno sui loro social media in cui parlino del prodotto.~~

~~Di conseguenza hanno stimato che~~ ogni persona che verrà contattata accetterà il prototipo (e le condizioni) con probabilità $p=0.545$



### Q1

> Se in Italia vogliono distribuire $n=6$ prototipi, con che probabilità dovranno contattare esattamente 6 persone?

`dbinom(6,n,p) =` ==$0.02620469$==



### Q2

> Qual è invece la probabilità che debbano contattarne esattamente 12?

`dnbinom(12-n,n,p) =` ==$0.107421$==



### Q3

> Sapendo che comunque l'azienda non contatterà più di 13 persone, qual è la probabilità che riescano a distribuire tutti i 6 prototipi?

`pbinom(n-1,13,p,FALSE) =` ==$0.8113972$==





## 25. (4-17) Posto di blocco (pois)

Ad un posto di controllo della polizia, passano e vengono fermate in **media 5** autoveicoli all'ora. Indichiamo con $X$ la variabile aleatoria che conta il numero di autoveicoli fermati tra le 8 e le 9 del mattino



La distribuzione per modellizzare questo fenomeno è la distribuzione di Poisson. Quindi $X ∼ {\cal P}(λ)$, con $λ = 5$



### Q1

> Qual è la probabilità che la Polizia non fermi autoveicoli nell'ora indicata?

`dpois(0,l) =` ==$0.006737947$==



### Q2

> Qual è la probabilità che nell'ora indicata ne fermi esattamente 1?

`dpois(1,l) =` ==$0.03368973$==



### Q3

> Qual è la probabilità che ne fermi almeno 7 e non più di 12?

`ppois(12,l)-ppois(7-1,l) =` ==$0.2357977$==





## 26. (4-20) Calcio (bin)

In una squadra amatoriale di calcio, ogni giocatore viene confermato per la stagione successiva, indipendentemente dagli altri, con una probabilità $p=0.18$. La squadra, quest'anno, ha una rosa di 18 giocatori.



Stiamo contando il numero di successi in una sequenza di prove indipendenti e identicamente distribuite. Possiamo quindi rappresentare il numero di giocatori confermati come una variabie aleatoria binomiale $X ∼ {\cal B}(n, p)$ con $n = 18$ e $p = 0.18$



### Q1

> Qual è la probabilità che all'inizio della prossima stagione ci siano almeno 11 giocatori?

`pbinom(11-1,n,p,FALSE) =` ==$0.00005823$==



### Q2

> Con che probabilità saranno stati lasciati a casa (esattamente) 11 giocatori?

`dbinom(11,n,1-p) =` ==$0.02195911$==



### Q3

> Con che probabilità la nuova rosa non avrà lasciato a casa più di 13 giocatori?

`pbinom(13,n,1-p) =` ==$0.2116291$==





## 27. (4-21) Lampadina (nbin)

Una lampadina led ha ogni giorno, indipendentemente dagli altri giorni, probabilità $p = 0.0038$ di fulminarsi



Sia $T$ la variabile aleatoria che indica il giorno in cui la lampadina si fulmina (primo tempo di successo). Allora $T$ ha distribuzione geometrica di parametro $p = 0.0038$  ($T\sim{\cal G}(p)\sim\text{NBim(1,m,p)}$)



### Q1

> Determinare la durata media (in giorni) della lampadina

$\text E[T]=1/p=$==$263.1578947$==



### Q2

> Determinare la probabilità che la lampadina duri almeno un anno (365 giorni)

`pgeom(365-1,p,FALSE) = 1-pnbinom(364,1,p) =` ==$0.2491645$==



### Q3

> Nella città senza nome ci sono 9200 lampioni che montano tale lampadina. Determinare il numero minimo di lampadine di scorta occorrenti affinché, con probabilità del 99%, si riescano a cambiare tutte le lampadine, fra le 9200 montate, che si fulminano in un giorno.

> `TEORIA` (**quantile**)
>
> La funzione `qbinom` fornisce il più piccolo valore $q$ tale che $\Pr(X ≤ q) ≥ x$

$X\sim{\cal B}(m=9200,p)$

~~$\text E[X]=mp=34.96$~~

`qbinom(0.99,m,p) =` ==$49$==



### Q4

> È vero che è più probabile che in un giorno nella città senza nome se ne fulminino meno di 207 che più di 304?

```R
> pbinom(207-1,m,p)
[1] 1-
> pbinom(304,m,p,FALSE)
[1] 1.063509e-173
```

==TRUE==





## 31. (4-28) Somma di Poisson (pois)

Sia $X$ una variabile aleatoria Poissoniana di parametro $λ_X$. Sappiamo che $\Pr (X = 3) = \Pr (X = 4)$. Sia inoltre $Y$ un'altra variabile aleatoria Poissoniana, indipendente da $X$, di media $6$. Sia infine $Z = X + Y$ la somma delle due variabili aleatorie precedenti.



$λ_X=4,\ \ λ_Y=6,\ \ λ_Z=10$



### Q1

> Qual è il valore di $λ_X$?

$\Pr(X=k)=\dfrac{\lambda_X}{k}\Pr(X=k-1)$

$\Pr (X = k) = \Pr (X = k-1) \ \ \lrarr \ \ \frac{\lambda_X}{k}=1$

$λ_X=k=$==$4$==



### Q2

> Qual è la probabilità $\Pr (X = 9|Z = 11)$?

$\Pr (X = 9|Z = 11) = \dfrac {\Pr (X = 9)· \Pr(Y = 2)}{\Pr (Z = 11) }$

`dpois(9,4) * dpois(2,6) / dpois(11,10) =` ==$0.005190451$==



### Q3

> Qual è il valore atteso condizionato $\text E[X|Z = 11]$?

$\text E[X|Z = 11]=\sum_{i=0}^{11} i·\dfrac{\Pr(X=i)·\Pr(Y=11-i)}{\Pr(Z=11)}=11·\dfrac {λ_X}{λ_Z}$

```R
i <- 0:11
sum (i * dpois(i,4) * dpois(11-i,6)) / dpois(11,10)
```

$\text E[X|Z = 11]=$==$4.4$==





## 34. (5-04) Listelli (norm)

Nella pavimentazione di una stanza vengono adoperati listelli di legno di lunghezza media $μ=16.5$ cm. Dai macchinari per la produzione, si sa che le lunghezze di tali listelli seguono una legge normale con deviazione standard uguale a $σ = 0.12$ cm

Per ricoprire il buco lasciato dai lavori per inserire un tubo, bisogna creare una striscia larga quanto un listello e lunga $609.0912322$ cm, con un opportuno numero $n$ di listelli.



### Q1

> Qual è la probabilità che servano più di $n = 37$ listelli per coprire il buco?

$X_i ∼ {\cal N} (μ, σ^2)$

$S_n=\sum_{i=1}^n X_i ∼ {\cal N} (n ⋅ μ, n ⋅ σ^2) $

$\Pr(S_{37} < 609.0912322)=$
`pnorm (609.0912322, n*mu, sqrt(n)*sig) =` ==$0.02680342$==



### Q2

> Qual è la probabilità che servano meno di $n = 37$ listelli?

$\Pr(S_{37} > 609.0912322)=$
`1 - pnorm (609.0912322, n*mu, sqrt(n)*sig) =` ==$0.9731966$==



### Q3

> Quanto dovrebbe essere lunga la striscia affinché $37$ listelli siano sufficienti per ricoprirla con una probabilità $p$ maggiore o uguale a $0.73164$?

$L = \sqrt nσ ⋅ ϕ^{−1}(1 − p) + nμ=$
`sqrt(n)*sig * qnorm(1-0.73164) + n*mu =` ==$610.0491$==





## 35. (5-05) Minimo di esponenziali (exp)

Siano $X$ e $Y$ due variabili aleatorie indipendenti di legge esponenziale di parametri $λ_1 = 1.2$ e $λ_2 = 1.7$ rispettivamente. Sia $U := \min\{X,Y\}$



### Q1

> Qual è la distribuzione di $U$? (Determinare la funzione di ripartizione $F_U$ e implementarla in R)
>
> <u>Suggerimento</u>: fate attenzione al supporto della variabile $U$, cioè l'insieme su cui $U$ è definita

> `TEORIA` (**minimo di esponenziali**)
>
> $X$ e $Y$ sono definite su $(0, +∞)$, per cui anche il loro minimo avrà valori in $(0, +∞)$, estremi esclusi
> $$
> F_U(u)=\Pr (U ≤ u) = 1 − \Pr (U > u)
> $$
>
> $$
> \min\{X,Y\} > u\ \lrarr\ X>u\ \and\ Y>u
> $$
>
> $$
> \Pr(U>u) = \Pr(\min\{X,Y\} > u) = \Pr(X>u, Y>u) =\\
> = \Pr (X > u)\Pr (Y > u) = \exp\{−λ_1u\} \exp\{−λ_2u\} = \exp\{−(λ_1 + λ_2)u\}
> $$
>
> $$
> F_U(u)=1−\exp\{−(λ_1+λ_2)u\}\ →\ U∼{\rm Exp}(λ_1+λ_2)
> $$
>
> $$
> λ=λ_1+λ_2
> $$

```R
function(u) { ifelse (u > 0, 1 - exp(-(l1 + l2) * u), 0) }
```



### Q2

> Quanto vale $\Pr (U > 0.45|X > 0.096)$?

$\Pr(U>u|X>x)=\dfrac{\Pr(U>u,X>x)}{\Pr(X>x)}= \\=\dfrac{\Pr(\min\{X,Y\}>u,X>x)}{\Pr(X>x)}= \dfrac{\Pr(X>u,Y>u,X>x)}{\Pr(X>x)}$

$\Pr(U>u|X>x)=\dfrac{\Pr(X>\max\{u,x\},Y>u)}{\Pr(X>x)}=$

`pexp(0.45,1.2,FALSE) * pexp(0.45,1.7,FALSE) / pexp(0.096,1.2,FALSE) =` ==$0.3042821$==



### Q3

> Quanto vale $\Pr (U > 0.096|X > 0.45)$?

`pexp(0.45,1.2,FALSE) * pexp(0.096,1.7,FALSE) / pexp(0.45,1.2,FALSE) =` ==$0.8494213$==





## 36. (5-06) Caramelle (norm)

Delle caramelle artiginali hanno un peso distribuito come una normale con media $μ = 6.423$ g e deviazione standard $σ = 0.879$ g. Al controllo qualità le caramelle con un peso superiore a $8.027181$ g o inferiore a $5.1867585$ g vengono scartate



### Q1

> Qual è la probabilità che una caramella sia scartata al controllo qualità?

`pnorm(8.02718,mu,sig,FALSE)+pnorm(5.186758,mu,sig) =` ==$0.1138$==



### Q2

> Qual è la probabilità che se vengono controllate $n=55$ caramelle, queste pesino complessivamente più di $364.4122138$ g ?

$X_i \sim {\cal N}(μ,σ^2)$

$S_n=\sum_{i=1}^n X_i \sim {\cal N}(n⋅μ,n⋅σ^2)$

`pnorm(364.4122138, n*mu, sqrt(n)*sig, FALSE) =` ==$0.04363294$==



### Q3

> Qual è la probabilità che su 55 caramelle al più 7 siano da scartare?

`pbinom(7,55,0.1138) =` ==$0.7143946$==





## 37. (5-07) Traffico (exp)

È stato osservato che il tempo trascorso tra il passaggio di due veicoli successivi sotto una videocamera del traffico ha una distribuzione esponenziale di media $μ=7$ minuti.



$λ=\dfrac 1 μ=\dfrac 1 7$



### Q1

> Qual è la probabilità che il tempo trascorso tra il passaggio di due veicoli successivi sia minore di $5.9$ minuti?

`pexp (5.9, 1/7) =` ==$0.5695212$==



### Q2

> Qual è l'intervallo di tempo $t$ (in minuti) tale per cui siamo certi al $89\%$ che il tempo trascorso tra il passaggio di due veicoli sia maggiore di $t$ minuti?

`qexp (0.89, 1/7, FALSE) =` ==$0.8157367$==



### Q3

> Sapendo che sono già trascorsi $6.6$ minuti dal passaggio dell'ultimo veicolo, qual è la probabilità che si debba attendere al più altri $4$ minuti per il passaggio del veicolo successivo?

`pexp(4, 1/7) =` ==$0.4352819$==



### Q4

> Qual è la funzione di densità della variabile casuale $U = \sqrt T$?

> `TEORIA` (**trasformazione non lineare**)
> $$
> F_U(u)=\Pr(U<u)=\Pr(T<u^2)=1-e^{-λu^2}
> $$
>
> $$
> f_U(u)=d(1-e^{-λu^2})=-e^{-λu^2}·(-2λu)=2λue^{-λu^2}
> $$

```R
function(u) { ifelse (u > 0, (2*u*λ) * exp(-λ*u^2), 0) }
```





## 38. (5-08) Cinema (bin)

In un cinema multisala vengono venduti solo biglietti in prevendita online e non all'entrata. Sapendo che il 12% ($p=0.12$) delle persone che acquistano un biglietto online per un film poi non si presenta al cinema, i gestori del sito di prevendita del cinema vendono 17 biglietti per il film proiettato nella sala 1, che ha 16 posti e 22 biglietti per quello nella sala 2, da 19 posti.



### Q1

> Calcolare la probabilità che almeno una persona che ha comprato il biglietto online (per il primo film) non trovi posto nella sala 1.

`pbinom(16,17,1-p,FALSE) =` ==$0.1138166$==



### Q2

> Calcolare la probabilità che nessun acquirente del biglietto online per il secondo film abbia problemi a trovare posto nella sala 2.

`pbinom(19,22,1-p) =` ==$0.5017366$==



### Q3

> Calcolare il numero $N$ di biglietti che si potrebbero vendere per la sala 1, tale che la probabilità di scontentare una persona non sia superiore a $0.32$

Trovare il valore di $N$ per tentativi partendo da $N=17$, tale per cui

$\text{Bin}(16,N,p)\le a\ \ \and\ \ \text{Bin}(16,N+1,p)>a$

$N=$==$17$==



### Q4

> In media quante persone si presentano per il film della sala 2?

$\text E[X]=22· (1-p)=$==$19.36$==





## 41. (5-13) Moneta (bin)

Abbiamo una moneta che dà testa con probabilità $p=0.4$



### Q1

> Lanciando 17 volte la moneta, l'evento “si ottengono 8 croci” ha la stessa probabilità del suo complementare?

==FALSE==



### Q2

> Qual è il numero medio di croci in $n=17$ lanci?

$\text E[C]=n·(1-p)=$==$10.2$==



### Q3

> Qual è la probabilità di ottenere almeno $t=7$ teste?

$\Pr(T\ge t)=$ `pbinom(7-1,17,0.4,FALSE) =` ==$0.5521594$==



### Q4

> In quanti modi si possono distribuire 7 teste in una successione di 17 lanci?

$P_n^r=\dfrac{n!}{r_1!·r_2!}=\dfrac{n!}{k!·(n-k)!}=$ `choose(17,7) =` ==$19448$==





## 43. (5-15) Richieste IT (pois)

Le richieste di intervento al supporto IT di un Dipartimento sono, in media, $μ=6$ al giorno
Per fare una stima del presonale necessario a fronteggiare queste richieste, la Direzione vuole calcolare alcune probabilità



### Q1

> Qual è la probabilità che in un giorno ci siano più di 8 richieste?

`1 - ppois(8,6) =` ==$0.1527625$==



### Q2

> Qual è la probabilità che in due giorni ci siano al più 4 richieste?

`ppois(4,6*2) =` ==$0.007600391$==



### Q3

> Qual è la probabilità che tra due richieste passino almeno 4 giorni?

`ppois(0,6)^4 =` ==$3.775135e-11$==







# Variabili aleatorie

## 28. (4-22) Densità, speranza, varianza

Di una variabile aleatoria $X$ sappiamo che ha la seguente funzione di densità: $f(x) = c ⋅ t^{−8}$ per $t > 9$ e identicamente nulla altrimenti.



### Q1

> Quanto vale $c$?

$\int^∞_9 f(x)\ dt = \int^∞_9 c ⋅ t^{−8}\ dt = 1$

$c ⋅ \int^∞_9 t^{−8}\ dt = c ⋅ \big[\frac 1 {1-8} ⋅ t^{1-8}\big]_9^∞ = c ⋅ (0-(-\frac 1 {7} ⋅ 9^{-7}))=c ⋅ \frac 1 {7} ⋅ 9^{-7}$

$c = 7 ⋅ 9^7=$==$33480783$==



### Q2

> Qual è la speranza di $X$?

> `TEORIA` (**speranza**)
>
> Per definizione, la speranza di una v.a. con densità $f$ a supporto in $(a,b)$ è
> $$
> \text E[X]=\int^b_a t· f(t)\ dt
> $$

$\text E[X]=\int^∞_9 t· c ⋅ t^{−8}\ dt=\int^∞_9 c ⋅ t^{−7}\ dt = 7 ⋅ 9^7 ⋅ \frac 1 6 ⋅ 9^{-6}=\dfrac{7⋅ 9}6=$==$10.5$==



### Q3

> Qual è la varianza di $X$?

> `TEORIA` (**varianza**)
>
> Per definizione, la varianza di una variabile aleatoria è
> $$
> \text{Var}[X] = \text E[(X− \text E[X])^2] = \text E[X^2] − \text E[X]^2 =\int^b_a t^2f(t)\ dt- \text E[X]^2
> $$

$\text E[X^2]=\int^∞_9 t^2· c ⋅ t^{−8}\ dt=\int^∞_9 c ⋅ t^{−6}\ dt = 7 ⋅ 9^7 ⋅ \frac 1 5 ⋅ 9^{-5}=\dfrac{7⋅ 9^2}5=113.4$

$\text{Var}[X] = 113.4-10.5^2=$==$3.15$==





## 29. (4-24) Luna park

Un gioco al Luna Park consiste in un distributore contenente palline numerate da 1 a 7, cui corrispondono premi di valore differente. Per giocare è necessario inserire un gettone. Le palline escono con le seguenti probabilità

| 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0.03 | 0.03 | 0.10 | 0.27 | 0.21 | 0.06 | 0.30 |

Chiamiamo $X$ la variabile aleatoria che indica il numero della pallina estratta, $X ∈ \{1, … , 7\}$



```R
X <- c(1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00)
p <- c(0.03, 0.03, 0.10, 0.27, 0.21, 0.06, 0.30)
```



### Q1

> Qual è il valore atteso di $X$?

$\text E[X]=$ `sum (X * p) =` ==$4.98$==



### Q2

> Qual è il terzo momento centrato di $X$?

$\text E\big[(X-\text E[X])^3\big]=\sum_{i=1}^7 (i-\text E[X])^3·\Pr(X=i)$

`sum ((X-EX)^3 * p) =` ==$-1.179216$==



### Q3

> Qual è il terzo momento (non centrato) della variabile aleatoria $Y = 6 ⋅ X$?

$\text E\big[Y^3\big]=\text E\big[(6X)^3\big]=6^3·\text E\big[X^3\big]=6^3·\sum_{i=1}^7 i^3·\Pr(X=i)$

`6^3 * sum (X^3 * p) =` ==$35069.76$==



### Q4

> Due amici, Alessandra e Bernardo, sono al Luna Park e vorrebbero entrambi giocare a questo gioco. Tuttavia è rimasto loro solamente un gettone. Usano il gettone per tirare a sorte chi giocherà: esso ha due facce ben distinguibili ed è equilibrato. Se Alessandra sceglie la faccia del gettone con le montagne russe, qual è la probabilità che Bernardo vinca il premio associato alla pallina 5?

$\Pr(B=5)=\frac 1 2 \Pr(X=5)=$==$0.105$==





## 30. (4-27) Moneta e dado

Consideriamo una moneta non equilibrata, per cui la probabilità di avere testa è $p = 0.503$. Lanciamo un dado a 8 facce e poi la moneta, tante volte quante il valore uscito nel lancio del dado. Sia $D$ la variabile aleatoria che ci dà l'esito del dado e $N$ la variabile aleatoria che conta il numero di teste uscite.



### Q1

> Qual è il valore atteso di $N$?

$\text E[N]=\text E[D]· p=$==$2.2635$==



### Q2

> Qual è la media di $N$ sapendo che $D = 2$?

$\text E[N|D=2]=\text 2· p=$==$1.006$==



### Q3

> Sapendo che alla fine dell'esperimento abbiamo avuto 3 teste, qual è la media del risultato del lancio del dado?

$\text E[D|N=3]=\sum_{d=1}^8d·\Pr(D=d|N=3) = \\ \sum_{d=1}^8d· \dfrac {\Pr(D=d,N=3)}{\Pr(N=3)} =  \sum_{d=1}^8d· \dfrac {\text{Bin}(3,d,p)·\frac 1 8}{\sum_{e=1}^8\text{Bin}(3,e,p)·\frac 1 8}$

```R
d <- 1:8
PN <- sum (dbinom(3,d,p) * 1/8)
sum (d * (dbinom(3,d,p) * 1/8) / PN)
```

==$5.666776$==





## 33. (4-30) Disuguaglianze

Abbiamo quattro variabili aleatorie: $X, Y , W, Z$
Le prime due, $X$ e $Y$, sono indipendenti tra loro e hanno entrambe distribuzione poissoniana, di parametri $λ_X = 12$ e $λ_Y = 6$ rispettivamente
La variabile $Z$ è una normale standard, mentre $W = 1.5 ⋅ Z$



### Q1

> Dare una stima dall'alto della probabilità che la somma $X+ Y$ sia maggiore o uguale a $28$, usando la disuguaglianza di Markov

> `TEORIA` (**disuguaglianza di Markov**)
>
> Disuguaglianza di Markov per una variabile aleatoria non negativa $T$
> $$
> \Pr(T\ge a)\le\dfrac{\text E[T]}a
> $$

$\text E[X+Y]=\text E[X]+\text E[Y]=λ_X+λ_Y=18$

$\Pr(X+Y\ge 28)\le\dfrac{18}{28}=$==$9/14$==



### Q2

> Dare una stima dall'alto della probabilità $\Pr(X ≥ 27|X+ Y = 28)$, usando la disuguaglianza di Markov

> `TEORIA` (**poissoniana condizionata**)
>
> La distribuzione di una poissoniana $X$ data la somma di due poissoniane $X+ Y = n$ è una binomiale di parametri $n$ e $p = \dfrac{λ_X} {λ_X+λ_Y}$

$\Pr(X ≥ 27|X+ Y = 28)=\dfrac{\text E[X|X+Y]}{a}=\dfrac{np}{a}=\dfrac{28·\frac23}{27}=$==$0.691358$==



### Q3

> Dare una stima dal basso della probabilità $\Pr(|W| < 3.4)$, usando la disuguaglianza di Chebychev

> `TEORIA` (**disuguaglianza di Chebychev**)
>
> Disuguaglianza di Chebychev per una variabile aleatoria non negativa $T$
> $$
> \Pr(|T-μ|\ge a)\le\dfrac{σ^2}{a^2}
> $$

$Z ∼ {\cal N} (0, 1),\ \ \ W ∼ {\cal N} (0, 1.5^2)$

$p_c=\Pr(|W| < 3.4)=1-\Pr(|W| \ge 3.4)=1-\dfrac{2.25}{11.56}=$==$0.8053633$==



### Q4

> Qual è l'errore assoluto (rispetto al valore vero di $\Pr(|W| < 3.4)$) fatto nella stima precedente?

$p_n=\Pr(W < 3.4)-\Pr(W < -3.4)=$
`= pnorm(3.4,0,1.5)-pnorm(-3.4,0,1.5)`

$ε_A=|p_n-p_c|=$==$0.1712261$==





## 39. (5-11) Viaggiatore / fattorizzazione

Un viaggiatore che ha perso la mappa si trova a un bivio con tre strade

- la prima strada riporta al punto in cui si trova ora, dopo un'ora
- la seconda riporta al punto in cui il viaggiatore si trova ora, dopo 6 ore
-  la terza strada porta alla città successiva, dopo 4 ore di cammino

Ogni volta che il viaggiatore si trova al bivio sceglie una strada con la stessa probabilità (il viaggiatore non ha memoria)

Sia $T$ il tempo necessario per raggiungere la città e $S$ la variabile aleatoria che ci dice quale strada ha preso il viaggiatore, dunque $R_S = \{1, 2, 3\}$



### Q1

> Determinare il tempo medio che il viaggiatore impiega per raggiungere la città. (Suggerimento: usare la speranza condizionata e il suo valore atteso.)

> `TEORIA` (**legge della speranza totale**)
> $$
> \text E[T]=\text E_S[\text E[T|S]]=\sum_{i=1}^n \text E[T|S=i]·\Pr(S=i)
> $$

$\text E[T|S=1]=\text E[T]+1\\
\text E[T |S = 2] = \text E[T ] + 6\\
\text E[T |S = 3] = 4$

$\text E[T]=\sum_{i=1}^3 \text E[T|S=i]·\frac13=\frac13(2·\text E[T]+11)=\frac23\text E[T]+\frac{11}3$

$\frac13\text E[T]=\frac{11}3\ →\ \text E[T]=$==$11$==



----


Sia $Y$ una variabile aleatoria discreta che prende i valori $\{1, 2, 3\}$ con le seguenti probabilità $0.34, 0.18, 0.48$

Sono date inoltre le probabilità condizionate $p_{X|Y}(x|y)$ (indicate come righe nella seguente tabella), con $X$ altra variabile aleatoria discreta

|       | $p(Y)$ | -6.5 | -4   | 4.5  | 8    |
| ----- | ------ | ---- | ---- | ---- | ---- |
| **1** | 0.34   | 0.31 | 0.16 | 0.22 | 0.31 |
| **2** | 0.18   | 0.18 | 0.32 | 0.23 | 0.27 |
| **3** | 0.48   | 0.22 | 0.23 | 0.27 | 0.28 |

```R
Y  <- c(1, 2, 3)
pY <- c(0.34, 0.18, 0.48)
X  <- c(-6.5, -4, 4.5, 8)
pX <- matrix(
        c(0.31, 0.16, 0.22, 0.31,
          0.18, 0.32, 0.23, 0.27,
          0.22, 0.23, 0.27, 0.28),
        3,4,TRUE)
```



### Q2

> Qual è il valore atteso $\text E[X]$ di $X$?

$\text E[X]=\text E_Y[\text E[X|Y]]=
\sum_{y=1}^3 \text E[X|Y=y]·\Pr(Y=y)=\\
=\sum_{y=1}^3\big(\sum_{x=1}^4 X_x·p_{X|Y}(x|y)\big)·p_Y(y)$

```R
EXcY <- c()
for (y in Y) {
    EXcY[y] <- sum (X * pX[y,])
}
EX <- sum (EXcY * pY)
```

==$0.9416$==



### Q3

> Nello stesso caso del quesito 2, qual è la varianza di $X$?

> `TEORIA` (**legge della varianza totale**)
> $$
> \text{Var}(X) = \text E_Y (\text{Var}(X|Y )) + \text{Var}_Y (\text E(X|Y ))
> $$

```R
VarXcY <- c()
for (y in Y) {
    VarXcY[y] <- sum ((X - EXcY[y])^2 * pX[y,])
}
EY <- sum (VarXcY * pY)
VarY <- sum ((EXcY - EX)^2 * pY)
VarX <- EY + VarY
```

==$36.39049$==





## 40. (5-12) Pallacanestro / approssimazioni

Un giocatore di pallacanestro ha una probabilità del 55% di fare canestro con un tiro da 2 punti.



### Q1

> Determinare la probabilità che il giocatore non faccia più di 62 punti in 50 tiri tutti da 2 punti, utilizzando l'approssimazione normale (con TLC) e la correzione di continuità

> `TEORIA` (**approssimazione normale con TLC**)
>
> Approssimazione normale con teorema del limite centrale e correzione di continuità
> $$
> \text P(X<a)=\Pr\bigg(\dfrac{X-\text E[X]}σ \le \dfrac{(a+\frac12)-\text E[X]}σ\bigg)≈ Φ\bigg(\dfrac{(a+\frac12)-\text E[X]}σ\bigg)
> $$
> 

$X_{50} ∼ {\cal B}(n = 50,\ p = 0.55)$

$\text E[X_{50}] = n ⋅ p = 27.5$

$\text {Var}(X_{50}) = np(1 − p) = 12.375$

`pnorm ((31 + 1/2 - 27.5) / sqrt (12.375)) =` ==$0.8722456$==



### Q2

> Qual è l'errore assoluto tra la probabilità ottenuta con l'approssimazione calcolata al quesito 1 e il valore esatto?

`pbinom (31,50,p) =` $0.8726549$

$ε_A=|0.8726549-0.8722456|=$==$0.0004093$==



### Q3

> Determinare il numero minimo di tiri che il giocatore deve effettuare affinché la probabilità di segnare almeno 90 punti sia non inferiore a 0.83, utilizzando l'approssimazione normale e la correzione di continuità.

$X_n ∼ {\cal B}(n,\ p = 0.55)$

$\Pr(X_n\ge45)=\Pr(X_n>45-0.5)=1-\Pr(X_n<45-0.5)≈$

$≈1-Φ\bigg(\dfrac{45.5-np}{\sqrt{np(1-p)}}\bigg)=1-Φ\bigg(\dfrac{45.5-0.55·n}{\sqrt{0.2475·n}}\bigg)\ge0.83$

$Φ\bigg(\dfrac{45.5-0.55·n}{\sqrt{0.2475·n}}\bigg)\le0.17 \iff \dfrac{45.5-0.55·n}{\sqrt{0.2475·n}}\leΦ^{-1}(0.17)$

$n ≥ 89.0537835 \ → \ n=$==$90$==







# V.C. congiunte

## 32. (4-29) Continue

Consideriamo la seguente funzione, $f(x, y) = k ⋅ (7x + 3y)$ per $(x, y) ∈ [0, 1] × [0, 1]$ e nulla altrove



### Q1

> Per quale valore di $k$, $f(x, y)$ è una densità di probabilità?

> `TEORIA` (**densità di probabilità congiunta**)
>
> Affinchè $f(x, y)$ sia una densità di probabilità, deve valere $f(x, y) ≥ 0$ per ogni $x, y ∈ \R^2$ e il suo integrale su $\R^2$ deve essere uguale a $1$
> $$
> \int\int_{\R^2} f(x,y)\ dx\ dy = 1
> $$

$\int_0^1\int_0^1 k ⋅ (7x + 3y)\ dx\ dy = 
k ⋅ \int_0^1(3y+\int_0^1 7x \ dx)\ dy = \\
= k ⋅ \int_0^1(3y+[\frac 7 2 x^2]_0^1)\ dy = 
k ⋅ (\frac 7 2 + \int_0^1 3y\ dy) = k ⋅ \dfrac {7+3} 2$

$k=$==$1/5$==



### Q2

> Le variabili aleatorie $X$ e $Y$ sono indipendenti?

> `TEORIA` (**v.a. indipendenti congiunte**)
>
> Per determinare se $X$ e $Y$ sono indipendenti calcoliamo le rispettive densità marginali $f_X$ e $f_Y$ e vediamo se il loro prodotto è uguale alla densità congiunta. Ricordiamo infatti che $X$ e $Y$ sono variabili aleatorie indipendenti se e solo se $f_{X,Y} (x, y) = f_X(x) ⋅ f_Y (y)$
> $$
> x,y\in\R \ \ \ \ \ \ \ \ \ \ \
> f_X(x)=\int_\R f_{X,Y}(x,y)\ dy \ \ \ \ \ \ \ f_Y(y)=\int_\R f_{X,Y}(x,y)\ dx
> $$

$f_X(x)=k·\int_0^1 (7x+3y) \ dy=\frac 1 5(7x+\frac 3 2)$

$f_Y(y)=k·\int_0^1 (7x+3y) \ dx=\frac 1 5(3y+\frac 7 2)$

e nulle altrove

Si vede quindi che $f_{X,Y} ≠ f_X ⋅ f_Y$, per cui $X$ e $Y$ non sono indipendenti

==FALSE==



### Q3

> Quanto vale la differenza tra la media di $X$ e quella di $Y$?

> `TEORIA` (**media di densità marginali**)
>
> Le medie equivalgono agli integrali di $x ⋅ f_X(x)$ e $y ⋅ f_Y (y)$
> $$
> \text E[X]=\int_\R x· f_X(x)\ dx
> $$

$\text E[X]=k·\int_0^1 (7x^2+\frac 3 2 x)\ dx=\frac 1 5 · (\frac 7 3 +\frac 3 4)$

$\text E[Y]=k·\int_0^1 (3y^2+\frac 7 2 y)\ dy=\frac 1 5 · (\frac 3 3 +\frac 7 4)$

$\text E[X]-\text E[Y]=$==$1/15$==



### Q4

> Qual è il valore atteso di $0.334 − XY$?

> `TEORIA` (**valore atteso**)
>
> Per linearità $\text E[0.334 − XY ] = 0.334 − \text E[XY ]$
>
> Si ha il vettore aleatorio $(X, Y )$ e $Z = g(X, Y ) = XY$, il valore atteso è
> $$
> \text E[Z] = \int\int_{\R^2} g(x,y)· f_{X,Y}(x,y) \ dx\ dy
> $$

$\text E[Z] = k·\int_0^1\int_0^1 xy· (7x+3y) \ dx\ dy =
k·\int_0^1 y·\int_0^1 (7x^2+3xy) \ dx\ dy = \\
= k·\int_0^1 y· (\frac 7 3+\frac 3 2 y)\ dy =
\frac 1 5 · (\frac 7 6 + \frac 3 6)=\dfrac 1 3$

$\text E[0.334 − XY ] = 0.334 − \text E[Z]=$==$0.0006667$==





## 42. (5-14) Discrete

Consideriamo la seguente tabella dove sulla prima colonna abbiamo i valori che può assumere la v.a. discreta $X$ e sulla prima riga i valori che può assumere la v.a. discreta $Y$

| $X\backslash Y$ | -0.7 | -0.41 | 0    | 4.49 |
| --------------- | ---- | ----- | ---- | ---- |
| **-3.26**       | 2 k  | 6 k   | 7 k  | 11 k |
| **0.53**        | 9 k  | 12 k  | 1 k  | 3 k  |
| **5.51**        | 10 k | 5 k   | 8 k  | 4 k  |



```R
Y <- c(-0.7, -0.41, 0, 4.49)
X <- c(-3.26, 0.53, 5.51)
p <- matrix( c(2 , 6 , 7, 11,
               9 , 12, 1, 3 ,
               10, 5 , 8, 4 ),
             3,4,TRUE)
```



### Q1

> Calcolare la costante $k$ che deve essere utilizzata affinché la tabella riporti i valori della densità discreta congiunta di $X$ e $Y$

$\sum_{(x,y)\in R_x\times R_y}p_{X,Y}(x,y)=78k=1$

$k=$ `1/sum(p) =` ==$1/78$==



### Q2

> Determinare $\Pr(X ≤ −3.26)$

$\sum_{(x,y)\in (-\infin,3.26]\times R_y}p_{X,Y}(x,y)=$ `sum(p[1,])*k =` ==$0.333333$==



### Q3

> Determinare $\Pr(Y > 0)$

$\sum_{(x,y)\in R_x\times (0,+\infin)}p_{X,Y}(x,y)=$ `sum(p[,4])*k =` ==$0.2307692$==



### Q4

> Calcolare il valore atteso condizionato $\text E [X|Y = −0.7]$

$\Pr(Y = -0.7)=\sum_{x\in R_x}p_{X,Y}(x,-0.7)=$ `sum(p[,1])*k =` $0.2692308$

$\text E [X|Y = −0.7]=\dfrac{\sum_{x\in R_x}x·p_{X,Y}(x,-0.7)}{\Pr(Y = -0.7)}$
`= (sum(X*p[,1])*k) / (sum(p[,1])*k) =` ==$2.540476$==



### Q5

> Determinare la varianza condizionata $\text {Var} [Y |X = −3.26]$

$\Pr(X = -3.26)=\sum_{y\in R_y}p_{X,Y}(-3.26,y)=$ `sum(p[1,])*k =` $0.3333333$

$\text E [Y|X = −3.26]=\dfrac{\sum_{y\in R_y}y·p_{X,Y}(-3.26,y)}{\Pr(X = -3.26)}=$
`= sum(Y*p[1,])*k / (sum(p[1,])*k) =` $1.751154$

$\text {Var} [Y|X = −3.26]=\dfrac{\sum_{y\in R_y}(y-\text E [Y|X = −3.26])^2·p_{X,Y}(-3.26,y)}{\Pr(X = -3.26)}=$
`= sum((Y-EYX)^2*p[1,])*k / PX =` $5.539218$







# Statistica

## 44. (5-18) Parametro toracico

Durante uno studio medico si misura il parametro toracico di $n = 11$ persone, ottenendo i valori riportati nella seguente tabella

81.20 | 87.90 | 88.60 | 86.60 | 95.00 | 91.40 | 93.90 | 85.70 | 84.80 | 89.90 | 89.80

Vogliamo una stima di media e varianza, $μ$, $σ^2$, del parametro toracico della popolazione, a partire dai dati osservati



```R
T <- c(81.20, 87.90, 88.60, 86.60, 95.00, 91.40, 93.90, 85.70, 84.80, 89.90, 89.80)
```



### Q1

> Dare una stima della media del parametro toracico

$\bar T =$ `mean(T) = sum(T) / length(T) =` ==$88.61818$==



### Q2

> Dare una stima (usando uno stimatore non distorto) della varianza del parametro toracico

> `TEORIA` (**stimatore non distorto di Var**)
>
> - **Con μ non noto**
>
>   Non conoscendo la media teorica della distribuzione, occorre uno stimatore non distorto della varianza che usi solamente i dati osservati
>
> $$
> S^2=\dfrac n {n-1}\bar S^2=\dfrac 1 {n-1}\sum_{i=1}^n (X_i-\bar X)^2
> $$
> - **Con μ noto**
>
>   Conoscendo la media teorica della distribuzione si può utilizzare
>
> $$
> S_*^2=\dfrac 1 n\sum_{i=1}^n (X_i-μ)^2
> $$
>
> Dove $\bar S^2$ è uno stimatore distorto

`var(T) = 1 / (length(T)-1) * sum((T - T_)^2)` ==$88.61818$==



### Q3

> Sapendo che la media del parametro toracico è $μ=89$, dare un'ulteriore stima della varianza, usando uno stimatore non distorto.

`1 / (length(T)) * sum((T - 89)^2) =` ==$14.88364$==





## 45. (5-19) Campione popolazione

Un campione estratto da una popolazione di distribuzione ignota è composto dai seguenti valori
$$
2, 2, 3, 4, 3, 6, 3, 2, 6, 2, 8
$$
Vogliamo calcolare le stime di alcuni indicatori per questo campione.



```R
X <- c(2, 2, 3, 4, 3, 6, 3, 2, 6, 2, 8)
```



### Q1

> Qual è la media campionaria?

`X_ = mean(X) = sum(X) / length(X) =` ==$3.727273$==



### Q2

> Qual è la varianza campionaria (ottenuta con uno stimatore non distorto)?

`var(X) = 1 / (length(X)-1) * sum((X-X_)^2) =` ==$4.218182$==



### Q3

> Qual è la moda del campione?

```R
moda <- function(X) {
    srt <- sort(X)
    count <- c(1)
    x <- c(srt[1])
    j <- 1

    for (i in 2:length(X)) {
        if (srt[i] == srt[i-1]) {
            count[j] <- count[j] + 1
        } else {
            j <- j+1
            count[j] = 1
            x[j] <- c(srt[i])
        }
    }

    Mi <- which(count %in%  max(count))
    M  <- x[Mi]

 #  print(x)
 #  print(count)
    
    M
}
```

`moda(X) =` ==$2$==



### Q4

> Qual è la mediana del campione?

> `TEORIA` (**mediana**)
>
> La mediana di una v.a. è il valore $m_X$ per cui
> $$
> \Pr (X ≤ m_X) = \Pr (X ≥ m_X) = 0.5
> $$

`median(X) =` ==$3$==





## 46. (5-20) Stimatori (espon)

Sia $\{X1, X2, X3, X4\}$ un campione casuale estratto da una distribuzione esponenziale di parametro $λ$. Si considerino i seguenti stimatori della media

- $\hatψ_1(λ) = X_3$
- $\hatψ_2(λ) = \dfrac{X_1+2X_2}3$
- $\hatψ_3(λ) = \dfrac{X_1+X_2+X_3}6+\dfrac{X_3+X_4}4$



$X_i ∼ \text{Exp}(λ)\ \ \ \ \ \ \ \ f_{X_i}(x) = λ e^{−λx}\ \ \ \ \ \ \ \ \text E[X_i] = \dfrac1λ\ \ \ \ \ \ \ \ \text {Var}[X_i] = \dfrac1{λ^2}$



### Q1

> Quali tra i precedenti stimatori sono corretti (ossia non distorti)?
>
> - ~~0, se nessuno è corretto~~
> - ~~1-3, il numero corrispondente allo stimatore non distorto se unico~~
> - ~~4, se entrambi gli stimatori 1 e 2 sono corretti~~
> - ~~5, se entrambi gli stimatori 1 e 3 sono corretti~~
> - ~~6, se entrambi gli stimatori 2 e 3 sono corretti~~
> - ~~7, se sono tutti non distorti~~

> `TEORIA` (**stimatore non distorto**)
>
> Uno stimatore $\hatθ$ di un parametro $θ$ si dice corretto o non distorto se
> $$
> \text E[\hatθ] = θ
> $$

$\text E[\hatψ_1(λ)] = \text E[X_3] = \dfrac 1 λ$

$\text E[\hatψ_2(λ)] = \dfrac13 \text E[X_1+2X_2] = \dfrac13 (\text E[X_1]+2\text E[X_2]) = \dfrac 1 λ$

$\text E[\hatψ_3(λ)] = \dfrac16 \text E[X_1+X_2+X_3]+\dfrac14 \text E[X_3+X_4] = \dfrac 1 λ$

==$7$==



### Q2

> Quale tra gli stimatori minimizza l'errore quadratico medio?

> `TEORIA` (**errore quadratico medio di uno stimatore**)
>
> L'errore quadratico medio di uno stimatore $\hatθ$ di $θ$ è
> $$
> \text {EQM}(\hatθ) = \text E\big[(\hatθ-θ)^2\big] = \text {Var}[\hatθ]+\text{bias}^2
> $$

$\forall i,\ \text E[\hatψ_i] = ψ_i\ →\ \text{bias}_i=0$

$\min\{\text {EQM}(\hatψ_i)\} = \min\{\text {Var}[\hatψ_i]\}$

$\text {Var}[\hatψ_1(λ)] = \text {Var}[X_3] = λ^{-2}$

$\text {Var}[\hatψ_2(λ)] = \text{Var}\bigg[\dfrac{X_1+2X_2}3\bigg] = \dfrac19 (\text{Var}[X_1]+4\text{Var}[X_2]) =\dfrac 5 9λ^{-2}$

$\text{Var}[\hatψ_3(λ)] = \text {Var}\bigg[\dfrac{X_1+X_2+X_3}6+\dfrac{X_3+X_4}4\bigg] =\\=\dfrac1{12^2}\text {Var}[2X_1+2X_2+5X_3+3X_4]=\dfrac7{24}λ^{-2}$

$\min\{\text {Var}[\hatψ_i]\}=\text {Var}[\hatψ_3]\ \Rightarrow$  ==$3$==



### Q3

> Dopo aver determinato lo stimatore di massima verosimiglianza $\hatλ_{MLE}$ per $λ$, calcolarne la stima per il seguente campione casuale
> $$
> 1.80, 0.90, 0.20, 0.40, 0.80, 0.10, 0.40, 0.40, 0.10, 0.10
> $$

> `TEORIA` (**stimatore di massima verosimiglianza**)
>
> - **Funzione di verosimiglianza**
>
>   Per l'indipendenza delle $X_i$, la funzione di verosimiglianza è data dal prodotto delle densità $f_{X_i}$
>
> $$
> L (λ|x_1, … , x_n)=\prod_{i=1}^nf_X(x_i)
> $$
>
> - **log-verosimiglianza**
>
>   Logaritmo naturale della funzione di verosimiglianza
>
> $$
> l(λ|x_1, … , x_n)=\ln(L(λ))
> $$
>
> - **Score function**
>
>   Derivata prima della log-verosimiglianza rispetto al parametro
>
> $$
> S(λ)=\dfrac {dl(λ)}{dλ}
> $$
>
> - **Stimatore di massima verosimiglianza**
>
>   Lo stimatore si ottiene ponendo la $S(λ)=0$ e ricavando $λ$
>
> $$
> \hatλ_{MLE}=S^{-1}(0)
> $$

$L (λ|x_1, … , x_n)=λ^ne^{-λ·\sum x_i}$

$l(λ|x_1, … , x_n)=n\ln(λ)-λ·\sum_{i=1}^n x_i$

$S(λ)=\dfrac n λ-\sum_{i=1}^n x_i$

$\dfrac n λ-\sum_{i=1}^n x_i=0\ →\ λ=\dfrac n {\sum_{i=1}^n x_i}$

$\hatλ_n=\dfrac n {\sum_{i=1}^n x_i}=$==$1.923077$==





## 47. (5-21) Reddito / intervalli di confidenza

In uno studio sul reddito medio annuo in una cittadina europea, sono stati raccolti i seguenti dati, che rappresentano il reddito annuo in migliaia di euro
$$
39.6, 40.8, 41.4, 38.1, 43.9, 39.4, 38.9, 47.2, 40, 41.6, 40.6,\\ 42.2, 35.3, 36.4, 44.4, 42.1, 38, 39.7, 46.8, 42.2, 41.6
$$

Supponiamo che la popolazione abbia una distribuzione gaussiana



```R
X <- c(39.6, 40.8, 41.4, 38.1, 43.9, 39.4, 38.9,
       47.2, 40.0, 41.6, 40.6, 42.2, 35.3, 36.4,
       44.4, 42.1, 38.0, 39.7, 46.8, 42.2, 41.6)
n <- length(X)
a <- 1 - 0.95
```



### Q1

> Vogliamo come prima cosa calcolare un intervallo di confidenza di livello 95% per il reddito medio. Qual è il margine di errore (metà dell'ampiezza)?

`qt(1-a/2, n-1) * sqrt(var(X) / n) =` ==$1.365089$==



### Q2

> Se invece fossimo interessati ad un intervallo di confidenza unilaterale sinistro, allo stesso livello 95%, qual è l'estremo non banale?

`mean(X) + qt(1-a, n-1) * sqrt(var(X) / n) =` ==$42.09059$==



### Q3

> Supponiamo ora di sapere che la varianza della popolazione è $σ^2=12$
> Qual è il margine di errore per un intervallo (bilaterale) di confidenza al 95% in questo caso?

`qnorm(1-a/2) * sqrt(sig2 / n) =` ==$1.481594$==



### Q4

> Rimaniamo nel caso del quesito 3. Quante altre osservazioni dovremmo aggiungere al campione per avere un intervallo allo stesso livello di confidenza di ampiezza al più $2.7$?

$2·Φ^{-1}(1-\frac α2) · \sqrt{\dfrac{σ^2} {n+k}} \le 2.7$

$\dfrac{σ^2} {n+k} \le \bigg(\dfrac{2.7}{2·Φ^{-1}(1-\frac α2)}\bigg)^2$

$k \ge {σ^2}·\bigg(\dfrac{2·Φ^{-1}(1-\frac α2)}{2.7}\bigg)^2 -n=$
`= ceiling (sig2 * (2 * qnorm(1-a/2) / 2.7)^2 - n) =` ==$5$==





## 48. (5-22) Cioccolatini

In un'azienda dolciaria vengono prodotti cioccolatini. Si selezionano $n = 113$ cioccolatini, il cui peso medio è pari a $μ=13.1$g. La deviazione standard del peso di ogni singolo cioccolatino prodotto dall'azienda è uguale a $σ=1.5 $g.



```R
n   <- 113
a   <- 1 - 0.99
mu  <- 13.1
sig <- 1.5
```



### Q1

> Si trovi l’intervallo di confidenza bilaterale per il peso medio $μ$ di ogni singolo cioccolatino prodotto a livello di confidenza del 99%. Qual è il valore dell'estremo superiore?

`mu + qnorm(1-a/2) * sqrt(sig^2 / n) =` ==$13.46347$==



### Q2

> Qual è il valore dell'estremo inferiore?

`mu - qnorm(1-a/2) * sqrt(sig^2 / n) =` ==$12.73653$==



### Q3

> Di quanto deve aumentare la dimensione del campione se si vuole che l’ampiezza dell’intervallo si dimezzi?

`l = qnorm(1-a/2) * sqrt(sig^2 / n) =` $0.3634705$

`ceiling (sig^2 * (2 * qnorm(1-a/2) / l)^2 - n) =` ==$339$==



### Q4

> Qual è il numero minimo di cioccolatini $k$ che occorre prelevare se si vuole che lo stimatore del peso medio si discosti dal vero peso medio $μ$ per meno di $0.5$g con probabilità almeno $p=0.96$

`a1 = 1 - 0.96`

`ceiling (sig^2 * (qnorm(1-a1/2) / 0.5)^2) =` ==$38$==







## 49. (5-25) Differenza medie

Sono stati raccolti i seguenti campioni da due popolazioni gaussiane omoschedastiche di varianza ignota



```R
X <- c(8.21,2.54,4.44,5.25,9.65,9.41,-4.09,-1.16,-1.73,4.09,
       10.31,2.49,6.66,4.17,2.36,4.86,8.98,6.11,-1.39)
Y <- c(3.86,7.06,-0.28,2.3,-0.53,-1.07,9.45,2.52,-1.91,
       0.49,3.17,8.09,6.04,9.96,-5.53,9.59,11.8)

mX <- mean(X)
mY <- mean(Y)
lX <- lenght(X)
lY <- lenght(Y)
```



### Q1

> Qual è una stima puntuale per la differenza tra le medie della prima e della seconda popolazione?

`mD = mX - mY =` ==$0.4474613$==



### Q2

> Qual è l'ampiezza dell'intervallo di confidenza al 90% per la stima fatta?

> `TEORIA` (**intervalli di confidenza per differenza di medie**)
> $$
> Z=\overline X - \overline Y
> $$
>
> $$
> \text E[X-Y]=\text E[X]-\text E[Y]
> $$
>
> - **Varianze note**
>
> $$
> \text {Var}[X-Y]=\text {Var}[X]+\text {Var}[Y]=σ_X^2+σ_Y^2
> $$
>
> $$
> \overline X \sim {\cal N}\bigg(μ_X,\frac{σ_X^2}{n_X}\bigg)
> \ \ \ \ \ \ \ \ \ \ \ 
> \overline Y \sim {\cal N}\bigg(μ_Y,\frac{σ_Y^2}{n_Y}\bigg)
> $$
>
> $$
> Z = \frac{(\overline X - \overline Y)-(μ_X-μ_Y)}{\sqrt{\frac{σ_X^2}{n_X}+\frac{σ_Y^2}{n_Y}}}
> $$
>
> $$
> \Bigg[(\overline X - \overline Y) -F_{t(n-2)}^{-1}\Big(1-\fracα2\Big)·\sqrt{\frac{σ_X^2}{n_X}+\frac{σ_Y^2}{n_Y}}\ ,\\ \ \ \ \
> (\overline X - \overline Y) +F_{t(n-2)}^{-1}\Big(1-\fracα2\Big)·\sqrt{\frac{σ_X^2}{n_X}+\frac{σ_Y^2}{n_Y}} \ \Bigg]
> $$
>
> - **Varianze ignote**
>
> $$
> S^2=\frac{(n_X-1)S_X^2+(n_Y-1)S_Y^2}{n_X-n_Y-2}
> $$
>
> $$
> Z = \frac{(\overline X - \overline Y)-(μ_X-μ_Y)}{\sqrt{S^2\big(\frac{1}{n_X}+\frac{1}{n_Y}\big)}}
> $$
>
> $$
> \Bigg[(\overline X - \overline Y) -F_{t(n-2)}^{-1}\Big(1-\fracα2\Big)·\sqrt{S^2\bigg(\frac{1}{n_X}+\frac{1}{n_Y}\bigg)}\ ,\\ \ \ \ \
> (\overline X - \overline Y) +F_{t(n-2)}^{-1}\Big(1-\fracα2\Big)·\sqrt{S^2\bigg(\frac{1}{n_X}+\frac{1}{n_Y}\bigg)} \ \Bigg]
> $$

`S2 = ((nX-1) * var(X) + (nY-1) * var(Y)) / (nX + nY - 2)`

`L = 2 * qt(1-a/2, nX+nY-2) * sqrt(S2 * (1/nX + 1/nY)) =` ==$5.169108$==



### Q3

> Qual è l'estremo superiore dell'intervallo di confidenza?

`(mX - mY) + L/2 =` ==$3.032016$==



### Q4

> Quanto vale la stima della varianza

$S^2=$==$20.96153$==





## 50. (5-26) Sorveglianza esami

L'11% degli studenti ha tentato di copiare agli esami nell'AA 2018-19



### Q1

> Se al primo appello (AA 2018-19) hanno preso parte 111 studenti, qual è la probabilità che abbiano copiato fra i 9 e i 14 studenti (estremi inclusi)?

`pbinom(14,n1,p) - pbinom(9-1,n1,p) =` ==$0.6357157$==



### Q2

> L'anno successivo (AA 2019-20) vengono implementate tecniche di sorveglianza. Al primo appello partecipano 110 studenti. Il sistema di proctoring rileva che a copiare sono stati 6 studenti. Qual è l'estremo inferiore dell'intervallo di confidenza al 95% della popolazione di studenti del corso che copiano?

`S2 = n2*p * (1-p)`

`inf = 6 - qt(1-a/2, n2-1) * sqrt(S2 / n2) =` ==$5.379863$==



### Q3

> Qual è l'estremo superiore?

`sup = 6 + qt(1-a/2, n2-1) * sqrt(S2 / n2) =` ==$6.620137$==



### Q5

> Qual è il p-dei-dati del test?

> `TEORIA` (**p-value**)
>
> Il p-dei-dati è la probabilità di ottenere risultati uguali o meno probabili di quello osservato durante il test, supposta vera l'ipotesi nulla
> $$
> \text{p-value}=2·\min\big(\Pr(X\le z|H),\ \Pr(X\ge z|H) \big)
> $$

`pv = 2 * min(pbinom(6,n2,p), 1-pbinom(6,n2,p)) =` ==$0.07058807$==



### Q4

> L'università vuole valutare se quest'anno ci sia stato un cambiamento della percentuale degli studenti che copiano. I dati supportano questa tesi (con significatività 5%)?

> `TEORIA` (**regione di accettazione**)
>
> I dati possono
>
> - non contraddire l'ipotesi nulla $H_0$
> - sostenere l'ipotesi alternativa $H_1$
>
> Le regioni di accettazione per per le ipotesi sono date dagli intervalli
>
> - $\text{p-value}\ge α\ →\ H_0$
> - $\text{p-value}< α\ →\ H_1$

==FALSE==





## 51. (5-27) Richieste assistenza

Ad un centro assistenza arrivano 45 richieste in un dato giorno (12 ore lavorative) e il numero di richieste di ciascuna ora è riportato di seguito

```R
X <- c(2, 4, 5, 0, 5, 6, 4, 4, 4, 5, 2, 4)
```

Il numero di richieste, indipendenti fra loro, segue una distribuzione di Poisson con parametro λ



### Q1

> Qual è la stima (metodo dei momenti) del parametro λ?

> `TEORIA` (**metodo dei momenti**)
>
> Sia $\hat μ_k$ il $k$-esimo momento campionario, cioè la v.a.
> $$
> \hat μ_k:=\frac1n \sum_{i=1}^n X_i^k=\overline X
> $$
> Sia $μ_k$ il $k$-esimo momento della popolazione, cioè il numero
> $$
> μ_k(θ)=μ_k:= \text E[X_1^k]=\int_\R x^k·f(x|θ)dx
> $$
> La statistica $\hat μ_k$ è uno stimatore corretto di $μ_k$

> `TEORIA` (**stimatore con metodo dei momenti**)
>
> Si dice stimatore con metodo dei momenti del parametro $θ$ la soluzione (se esiste) $\hat θ_{mom}$ dell'equazione
> $$
> \hat θ_{mom}=μ_1(\hat θ_{mom})=\hat μ_1
> $$

`l = mean(X) =` ==$3.75$==



### Q2

> Dato $α=0.01$ costruire un intervallo di confidenza bilaterale di livello $1-α$. Qual è l'estremo superiore?

`l + qt(1-a/2, n-1) * sqrt(var(X) / n) =` ==$5.236792$==



### Q3

> Il capo del personale pensava che il numero di richieste fosse al più $λ_0=3$ e ora vuole sapere se i suoi dati supportino la sua ipotesi. Qual è il valore della statistica test per il campione osservato? (Con approssimazione TLC)

> `TEORIA` (**funzione ancillare con TLC**)
> $$
> \frac{\overline X_n-λ}{\sqrt{\fracλn}}\sim{\cal N}(0,1)
> $$

$Z_0=\dfrac{\overline X_n-λ_0}{\sqrt{\fracλn}}=$==$1.341641$==



### Q4

> Qual è il p-value?

`pv = 2 * min(ppois(3,l), ppois(3,l,FALSE)) =` ==$0.9675348$==



### Q5

> Accettiamo (con significatività 1%) l'ipotesi nulla del capo del personale?

==TRUE==







# Regressione lineare

## 52. (5-28) Modello lineare

Delle misurazioni hanno raccolto le seguenti coppie di dati

|      | 1     | 2      | 3      | 4     | 5      | 6      | 7     | 8      | 9      | 10     | 11     | 12    |
| ---- | ----- | ------ | ------ | ----- | ------ | ------ | ----- | ------ | ------ | ------ | ------ | ----- |
| $x$  | -8.00 | 21.00  | 16.00  | -2.00 | 29.00  | 17.00  | 1.00  | 3.00   | 12.00  | 4.00   | 5.00   | -5.00 |
| $y$  | 11.30 | -49.50 | -35.40 | -1.70 | -61.50 | -38.90 | -4.30 | -11.20 | -29.50 | -13.00 | -10.10 | 5.50  |

Se ne vuole ricavare un modello lineare, con $y$ in funzione di $x$



```R
x <- c(-8.00, 21.00, 16.00, -2.00, 29.00, 17.00,
        1.00,  3.00, 12.00,  4.00, 5.00,  -5.00)
y <- c(11.30, -49.50, -35.40,  -1.70, -61.50, -38.90,
       -4.30, -11.20, -29.50, -13.00, -10.10,   5.50)

mx <- mean(x)
my <- mean(y)
n  <- length(x)
```



> `TEORIA` (**modello lineare**)
>
> - Coefficiente di grado 1
>
> $$
> \hatα_1=\dfrac{(\sum_ix_iy_i)-n\bar x\bar y}{(\sum_ix_i^2)-n\bar x^2}
> $$
>
> - Termine noto
>
> $$
> \hatα_0=\bar y-\hatα_1\bar x
> $$
>
> - Modello lineare
>
> $$
> y=\hatα_1·x+\hatα_0
> $$



### Q1

> Qual è la stima del coefficiente di grado 1?

`a1 = (sum(x*y) - n*mx*my) / (sum(x^2) - n*mx^2) =` ==$-2.017411$==



### Q2

> Qual è la stima del termine noto (coefficiente di grado 0)?

`a0 = my - a1 * mx =` ==$-4.2234$==



### Q3

> Che previsione dà il modello per la nuova osservazione $x = −2$?

`-2 * a1 + a0 =` ==$-0.1885781$==



### Q4

> Che previsione dà il modello per la nuova osservazione $x = 1.6$?

`1.6 * a1 + a0 =` ==$-7.451257$==





## 53. (5-29) Regressione lineare

Abbiamo i dati degli anni di anzianità di servizio e dello stipendio mensile di alcuni dipendenti di un'azienda

|      | 1       | 2       | 3       | 4       | 5       | 6       | 7       | 8       | 9       | 10      |
| ---- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| $x$  | 2.00    | 8.00    | 4.00    | 4.00    | 7.00    | 9.00    | 4.00    | 7.00    | 7.00    | 9.00    |
| $y$  | 1403.40 | 1438.50 | 1412.90 | 1415.10 | 1431.40 | 1446.30 | 1416.20 | 1430.60 | 1432.10 | 1442.80 |

Ipotizziamo una relazione lineare



```R
x <- c(2.00, 8.00, 4.00, 4.00, 7.00, 9.00,
       4.00, 7.00, 7.00, 9.00, 9.00)
y <- c(1403.40, 1438.50, 1412.90, 1415.10, 1431.40, 1446.30, 		1416.20, 1430.60, 1432.10, 1442.80, 1442.30)

mx <- mean(x)
my <- mean(y)
n  <- length(x)

a1 <- (sum(x*y) - n*mx*my) / (sum(x^2) - n*mx^2)
a0 <- my - a1 * mx
```



### Q1

> Che stipendio mensile ci aspettiamo per un dipendente con 12 anni di servizio?

`12 * a1 + a0 =` ==$1460.909$==



### Q2

> Qual è l'estremo superiore di un intervallo unilaterale sinistro di confidenza al 99.5% per il coefficiente di primo grado?

> `TEORIA` (**Root Sum Squared**)
> $$
> \text{RSS} = \sum_i(y_i − \hatα_0 − \hatα_1 · x_i)^2
> $$

> `TEORIA` (**funzione ancillare**)
> $$
> (\hatα_1-α_1)\sqrt{\dfrac{(n-2)\sum_i(x_i^2-\bar x^2)}{\text{RSS}}}\sim t(n-2)
> $$

> `TEORIA` (**intervalli di confidenza**)
>
> Bilaterale
> $$
> \Bigg[\hatα_1-F_{t(n-2)}^{-1}\Big(1-\fracα2\Big)·\sqrt{\dfrac{\text{RSS}}{(n-2)\sum_i(x_i^2-\bar x^2)}},\\ \ \ \ \
> \hatα_1+F_{t(n-2)}^{-1}\Big(1-\fracα2\Big)·\sqrt{\dfrac{\text{RSS}}{(n-2)\sum_i(x_i^2-\bar x^2)}} \Bigg]
> $$
> Unilaterale sinistro
> $$
> \Bigg(-\infin,\ \ \
> \hatα_1+F_{t(n-2)}^{-1}(1-α)·\sqrt{\dfrac{\text{RSS}}{(n-2)\sum_i(x_i^2-\bar x^2)}} \Bigg]
> $$

`RSS <- sum ((y - a0 - a1 * x)^2)`

`a1 + qt(1-a, n-2) * sqrt(RSS / ((n-2) * sum(x^2-mx^2))) =` ==$6.375761$==



### Q3

> Vogliamo ora verificare se i dati sostengono che il coefficiente di primo grado sia maggiore di 5. Qual è il p-dei-dati?

> `TEORIA` (**test statistico su $α_1$**)
>
> Dire che “i dati sostengono” significa fare un test positivo (maggiore, $H_1$)
> $$
> H_0:α_1\le z \ \ \ \ \ \ \ H_1:α_1>z
> $$
> La statistica test è
> $$
> S_t=(\hatα_1-z)\sqrt{\dfrac{(n-2)\sum_i(x_i^2-\bar x^2)}{\text{RSS}}}
> $$

> `TEORIA` (**p-value per $α_1$**)
>
> Probabilità che una $t$ a $n − 2$ gradi di libertà sia maggiore del valore $z$ della statistica test, cosa si può calcolare con
>
> ```R
> pt (St, n-2, lower = FALSE)
> ```

`St <- (a1 - 5) * sqrt(((n-2) * sum(x^2 - mx^2)) / RSS)`

`pt (St, n-2, FALSE) =` ==$0.001051232$==



### Q4

> Per il test del quesito 3, con significatività $α=0.01$ è vero che i dati non contraddicono l'ipotesi nulla?

==FALSE==

