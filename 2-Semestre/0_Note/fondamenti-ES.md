# <span style='color: darkgreen'><u>Teoria per l'esame di FMI</u></span>



# Esercizi

## 1.  Principio di induzione

> ### <span style='color: blue'>Consegna</span>
>
> Si dimostri per induzione su $n\in\N$ che, per ogni intero $n\ge n_0$, vale
> $$
> \sum_{k=n_0}^n P(k)=Q(n)
> $$
>
> ### <span style='color: blue'>Svolgimento</span>
>
> Si proceda per induzione su $n\ge n_0$
>
> 1. <u>Base induttiva</u>:   $n=n_0$
>
>    Si verifichi che
>    $$
>    \sum_{k=n_0}^{n_0} P(k)=Q(n_0)
>    $$
>    Vale
>    $$
>    \sum_{k=n_0}^{n_0} P(k)=P(n_0)=c\,,\ \ \ \ Q(n_0)=c'\ \ \ \Rarr\ \ \ c=c'
>    $$
>    Dunque si è verificata la base induttiva
>
> 2. <u>Passo induttivo</u>:   $n\ge n_0\,,\ \ n\mapsto n+1$
>
>    <u>Ipotesi induttiva</u>:  si assuma vera $(*)$ per qualche $n\ge n_0$, ovvero
>    $$
> \exist\ n\ge n_0\ \ |\ \ \sum_{k=n_0}^n P(k)=Q(n)
>    $$
>    Si dimostri che
>    $$
>    \sum_{k=n_0}^{n+1} P(k)=Q(n+1)\ \ \ \ (**)
>    $$
>    Vale
>    $$
>    \sum_{k=n_0}^{n+1} P(k)=\bigg(\sum_{k=n_0}^{n} P(k)\bigg)+P(n+1) \stackrel{\rm (ip\ ind)}{=}
> $$
> 
> $$
>    =Q(n)+P(n+1) = \dots = Q(n+1)
> $$
> 
>    Il passo induttivo è stato fatto, ovvero $(**)$ è verificata
>
> Grazie al p.d.i., l'uguaglianza $(*)$ è vera per ogni $n\ge n_0$



> ### <span style='color: green'>Teorema</span>  (principio di induzione)
>
> Sia $P(n)$ una famiglia di proposizioni indicizzate su $\N$ e si supponga che
>
> 1. $P(0)\ \rm vera$
> 2. $\forall n>0,\ (\forall k<n,\ P(k)\ {\rm vera})\ \Rarr\ P(n)$
>
> Allora $\forall n\in\N,\ P(n)\ \rm vera$





## 2.  Teorema cinese del resto

> ### <span style='color: blue'>Consegna</span>
>
> 1. Si determinino tutte le soluzioni del seguente sistema di congruenze
>
> $$
> \begin{cases}
> x \equiv a &({\rm mod}\ \ n)\\
> x \equiv b &({\rm mod}\ \ m)
> \end{cases}
> $$
>
> 2. Si dica inoltre se esistono soluzioni che divise per $d$ abbiano resto uguale a $r$
>
> ### <span style='color: blue'>Svolgimento 1</span>
>
> Si calcoli l'insieme delle soluzioni del sistema
>
> 1. <u>Compatibilità</u>:  $S\ne Ø\iff (n,m)\mid a-b$
>
>    Si calcoli il MCD fra $n$ e $m$ con l'algoritmo di Euclide
>
>    Si verifichi che $(n,m)\mid a-b\,$; se vero allora il t.c.r. implica che $S\ne Ø$
>    
>
> Si osservi che
> $$
>    a-b=c\,(n,m)\ \ \ \ (1)
> $$
>
> 2. <u>Calcolo di una soluzione</u>
>
>   Si applichi la scomposizione a ritroso (alg. di Euclide) per ottenere
> $$
>    (n,m)=kn-hm\ \ \ \ (2)
> $$
> Da $(1)$ e $(2)$ segue che 
> $$
>    a-b=ckn-chm
> $$
>    Dunque si definisca
> $$
>    s\ :=\ a-ckn\ =\ b-chm
> $$
>    È evidente che
> $$
>    s \equiv a\ ({\rm mod}\ \ n)\ \ \and\ \
>    s \equiv b\ ({\rm mod}\ \ m)\ \ \Rarr\ \ s\in S
> $$
>
> 3. <u>Calcolo dell'insieme delle soluzioni</u>
>
>    Si calcoli il mcm fra $n$ e $m$
> $$
>    t=[n,m]=\dfrac{n·m}{(n,m)}
> $$
> Dunque grazie al t.c.r. vale
> $$
>   S=[s]_t=\{s+kt\in\Z\ |\ k\in\Z \}
> $$
>
> ### <span style='color: blue'>Svolgimento 2</span>
>
> Si osservi che esiste una soluzione $x$ del sistema ($x\in\Z\ |\ x\equiv s\ ({\rm mod}\ t)$) che divisa per $d$ abbia resto $r$ se e solo se il seguente sistema è compatibile
> $$
> \begin{cases}
> x \equiv s &({\rm mod}\ \ t)\\
> x \equiv r &({\rm mod}\ \ d)
> \end{cases}
> $$
> Dal t.c.r. segue che il sistema è compatibile se e solo se
> $$
> (t,d)\mid s-r
> $$
> Se questa proposizione è falsa segue che il sistema sopra è incompatibile, dunque non esiste alcuna soluzione $x\in S$ che divisa per $d$ abbia resto $r$
> $$
> \forall h\in\Z\,,\ r<d\ \ \Rarr\ \ \nexists\ x\in S\ \ |\ \ x=hd+r
> $$



> ### <span style='color: green'>Teorema</span>  (teorema cinese del resto)
>
> Il sistema di congruenze
> $$
> \begin{cases}
> x \equiv a &({\rm mod}\ \ n)\\
> x \equiv b &({\rm mod}\ \ m)
> \end{cases}
> $$
> Ha soluzione se e solo se $(n,m)\mid a-b$
>
> Se $c$ è una soluzione del sistema allora gli elementi di $[c]_{[n,m]}$ sono tutte e sole le soluzioni del sistema
> $$
> S=\{s,k\in\Z\ |\ s=c+k[n,m]\}
> $$
>

> ### <span style='color: green'>Algoritmo</span>  (divisione euclidea)
>
> <u>Input</u>:  $(n,m)\in\N\times\N,\ m>0$
>
> - $n<m\ \Rarr$  <u>output</u>:  $(0,n)$
> - $n\ge m\ \Rarr$
>   - applica l'algoritmo a $(n-m,m)$
>   - aggiunge $1$ al quoziente
>
> ```c
> DIVE (n,m) {
>   IF n < m THEN [0,n]
>   ELSE [1,0] + DIVE(n-m,m)
>   END IF
> }
> ```

> ### <span style='color: green'>Algoritmo</span>  (di Euclide per il MCD)
>
> <u>Input</u>:  $(n,m)\in\Z\times\Z$
>
> - $n\ =0 \Rarr$  <u>output</u>:  $m$
> - $m=0 \Rarr$  <u>output</u>:  $n$
> - $n\ne0\ \and\ m\ne0\ \Rarr$
>   - calcola la divisione euclidea $n=mq+r$
>   - applica l'algoritmo a $(m,r)$
>
> ```c
> MCD (n,m) {
>   IF m = 0 THEN n
>   ELSE [q,r] = DIVE(n,m)
>        MCD(m,r)
>   END IF
> }
> ```





## 3.  Crittografia RSA

> ### <span style='color: blue'>Consegna</span>
>
> Si determinino tutte le soluzioni della seguente congruenza
> $$
> x^c \equiv d\ \ ({\rm mod}\ n)
> $$
>
> ### <span style='color: blue'>Svolgimento</span>
>
> Sia $S$ l'insieme delle soluzioni
>
> 1. <u>Applicabilità del metodo RSA</u>
>
>    - Si calcoli il valore della funzione di Eulero $Φ(n)$, ovvero il numero di naturali minori o uguali a $n$ e coprimi con $n$
>      - Si scomponga $n$ in fattori primi
>
>      $$
>      n=p_1^{k_1}\, p_2^{k_2}\, ···\, p_r^{k_r}
>      $$
>
>      - Si calcoli $Φ(n)$
>
>      $$
>      Φ(n)=n·\bigg(1-\dfrac 1 {p_1} \bigg)·\bigg(1-\dfrac 1 {p_2} \bigg)···\bigg(1-\dfrac 1 {p_r} \bigg) =\\ \ \\
>      =\big((p_1-1)·p_1^{k_1-1}\big)·\big((p_2-1)·p_2^{k_2-1}\big)···\big((p_r-1)·p_r^{k_r-1}\big)\\
>      $$
>
>    - Si verifichi che valgono le seguenti condizioni (i seguenti numeri devono essere coprimi)
>
>      - $(d,n)=1$
>      - $(c,Φ(n))=1$
>
>    - Si applichi il metodo RSA, ottenendo
>      $$
>      S=[d^e]_n \subset\Z\ \ |\ \ e>0\ \and\ e\in[c]^{-1}_{Φ(n)}\ \ \ \ \ (1)
>      $$
>
> 2. <u>Calcolo di $S$</u>
>
>    - Si applichi l'algoritmo di Euclide a $c$ e $Φ(n)$ per ottenere
>      $$
>      (c,Φ(n))=1=k·c+h·Φ(n)
>      $$
>      Passando al quoziente modulo $Φ(n)$ si ottiene
>      $$
>      [1]_{Φ(n)}=[k]_{Φ(n)}·[c]_{Φ(n)}
>      $$
>      Dunque
>      $$
>      [c]_{Φ(n)}^{-1}=[k]_{Φ(n)}\ \ \ \ \ (2)
>      $$
>      
>    - Da $(1)$ e $(2)$ segue che
>      $$
>      e:=k\ \ \ \Rarr\ \ \ S=[d^k]_n\subset\Z
>      $$
>    
>      Si calcolino alcuni rappresentanti di $[d^i]_n$
>      |  $i$  | $\ \ \ \ [d^i]_n$                 |
>      | :---: | :-------------------------------- |
>      |  $1$  | $d^1\equiv d\ \ \ ({\rm mod}\ n)$ |
>      |  $2$  | $d^2\equiv d_2\ \ ({\rm mod}\ n)$ |
>      | $···$ | $\ \ \ \ {···}$                   |
>      |  $j$  | $d^j\equiv 1\ \ ({\rm mod}\ n)$   |
>      
>      Se esiste un tale $j$ segue che
>      $$
>      [d^j]_n=[1]_n
>      $$
>      Dunque
>      $$
>      S=[d^k]_n=[d^j]_n·[d^{k-j}]_n=[1]_n·[d^{k-j}]_n=[d^{k-j}]_n
>      $$
>    
>    Ciò dimostra che
>    $$
>    S=[d^{k}]_n=[d^{k-j}]_n=\{d^{k-j}+hn\in\Z\ |\ h\in\Z \}
>    $$
>



> ### <span style='color: green'>Definizione</span>  (funzione $Φ$ di Eulero)
>
> Dato un numero naturale $n$ si indica con $Φ(n)$ il numero di naturali minori o uguali a $n$ e coprimi con $n$
>
> Sia $n=p_1^{k_1}\, p_2^{k_2}\, ···\, p_r^{k_r}$ la scomposizione in fattori primi di $n$, allora
> $$
> \begin{align}
> Φ(n)\ &=\ \big((p_1-1)·p_1^{k_1-1}\big)·\big((p_2-1)·p_2^{k_2-1}\big)···\big((p_r-1)·p_r^{k_r-1}\big) =\\ \\
> &=\ n·\bigg(1-\dfrac 1 {p_1} \bigg)·\bigg(1-\dfrac 1 {p_2} \bigg)···\bigg(1-\dfrac 1 {p_r} \bigg)
> \end{align}\\
> $$

> ### <span style='color: green'>Proposizione</span>  (crittografia RSA)
>
> Sia $c$ coprimo con $Φ(n)$, allora l'applicazione $C:\Z/n\Z^*→\Z/n\Z^*$ definita da $x\mapsto x^c$ è invertibile e la sua inversa è data da $D(x)=x^d$ essendo $cd\equiv1\ \ ({\rm mod}\ Φ(n))$





## 4.  Score di un grafo

> ### <span style='color: blue'>Consegna</span>
>
> 1. Si dica se il seguente vettore è lo score di un grafo e, in caso lo sia, si costruisca un tale grafo utilizzando il teorema dello score
>    $$
>    d=(d_1,d_2,...,d_n)
>    $$
>
> 2. Si dica inoltre se esiste un tale grafo che sia
>    - sconnesso
>    - connesso
>    - 2-connesso
>    - un albero
>    - una foresta
>    - hamiltoniano
>
> ### <span style='color: blue'>Svolgimento 1</span>
>
> 1. <u>Verifica delle ostruzioni</u>
>
>    Un vettore $d$ con $n$ componenti intere è lo score di un grafo se e solo se
>    - Soddisfa il lemma dei cassetti: se il numero di componenti di grado dispari non è pari, allora $d$ non può essere lo score di un grafo
>
>    - Il grafo con score $d$ non presenta ostruzioni
>
>       Le ipotesi per cui $d$ possa presentare ostruzioni sono
>       $$
>       \exist\ d_i\in d\ \ |\ \ d_i\ge n-1\ \ \or\ \ \forall\ d_i\in d\,,\ 0\le d_i\le 2
>       $$
>       Se le ipotesi non sono soddisfatte allora $d$ non presenta ostruzioni
>
>       Altrimenti si proceda a verificare le ostruzioni di cui sono soddisfatte le ipotesi
>
> 2. <u>Applicazione del teorema dello score</u>
>
>    Non avendo trovato ostruzioni all'esistenza di un grafo con score $d$ (in particolare $\forall i,\ d_i\le n-1$) si proceda all'applicazione del teorema a $d$
>
>    1. Si elimini $d_n$ da $d$ e si sottragga $1$ ai $d_n$ componenti precedenti a $d_n$
>    2. Si ordini il vettore $d^{(i)}$ così ottenuto ($i=1,...,j$)
>    3. Si ripeta da (1) finché il grado massimo non sia minore o uguale a $2$
>    
>    Poiché l'ultimo vettore ottenuto $d^{(j)}$ è lo score del grafo $G^{(j)}$, grazie al teorema dello score anche $d$ è lo score di un grafo
>
> 3. <u>Si costruisca $G$ con score $d$ utilizzando il teorema dello score</u>
>    1. Si disegni il grafo avente come score $d^{(j)}$, l'ultimo vettore ottenuto
>    2. Si proceda aggiungendo i vertici e i lati rimossi per ottenere progressivamente grafi con score $d^{(i)}$ ($i=j-1,...,1$)
>
> ### <span style='color: blue'>Svolgimento 2</span>
>
> Un grafo è
>
> - <u>connesso/sconnesso</u> se
>   
>   - $|E(G)|<|V(G)|-1\ \ \, \ \Rarr$   necessariamente sconnesso
>   - $d_1\ge |V(G)|-d_n-1\ \ \Rarr$   necessariamente connesso
>   - altrimenti può essere sia connesso che sconnesso
>   
> - <u>2-connesso</u> se non ha foglie, ovvero $\forall i,\ d_i>1$
>
> - <u>un albero</u> se è connesso e senza cicli, ovvero se il numero dei lati è uguale al numero dei vertici meno $1$
>   $$
>   |E(G)|=|V(G)|-1
>   $$
>   Dato lo score, è sufficiente verificare che soddisfi la formula di Eulero
>   $$
>   \dfrac12\sum_{i=1}^n d_i=n-1
>   $$
>
> - <u>una foresta</u> se è un grafo senza cicli
>
> - <u>hamiltoniano</u> se contiene almeno un ciclo hamiltoniano, ovvero una passeggiata chiusa che tocca tutti i vertici di $G$ una ed una sola volta
>
>    - Condizione necessaria: $G$ deve essere connesso, con almeno $3$ vertici tutti di grado maggiore o uguale a $2$
>     - Condizione sufficiente: il grado di ogni vertice deve essere maggiore o uguale a $\frac{|V(G)|}{2}$ (teorema di Dirac)
>
>   $$
>   \forall d_i\,, \ \ d_i\ge\dfrac{|V(G)|}{2}\ \ \Rarr\ \ {\rm hamiltoniano}\ \iff\ d_i\ge 2
>   $$
>



> ### <span style='color: green'>Definizione</span>  (grado di un vertice)
>
> Sia $G$ un grafo finito e sia $v\in V(G)$, il grado di $v$ è il numero (cardinale)
> $$
> {\rm deg}(v)=|\{e\in E(G)\ |\ v\in e\}|
> $$

> ### <span style='color: green'>Proposizione</span>  (relazione fondamentale)
>
> Se $G(V,E)$ è un grafo finito allora
> $$
> \sum_{v\in V} \deg(v)=2|E|
> $$

> ### <span style='color: green'>Definizione</span>  (score di un grafo)
>
> Sia $G$ un grafo finito e sia $V(G)=\{v_1,...,v_n\}$, lo score di $G$ è la successione finita $n$-pla dei gradi dei suoi vertici, ovvero
> $$
> {\rm score}(G)=\{deg(v_1),...,deg(v_n)\}
> $$

> ### **<span style='color: green'>Lemma</span> (delle strette di mano)**
>
> Se $G$ è un grafo finito, allora il numero di vertici di grado dispari è pari

> ### <span style='color: green'>Proposizioni</span>  (ostruzioni sui grafi)
>
> 1. Se $G$ è un grafo finito con $n$ vertici allora $\forall v\in V,\ \deg(v)\le n-1$
>    
>
>    
>    ---
>    
>    
>    
> 3. Se in un vettore $d$ con $n$ componenti, scritto in forma canonica,
>    $$
>    d=(d_1,...,d_n)
>    $$
>    ci sono $m$ componenti uguali a $n-1$
>    $$
>    |\{d_i\in d\ |\ d_i=n-1 \}|=m
>    $$
>    allora, affinché $d$ sia lo score di un grafo, necessariamente dovrà essere
>    $$
>    \forall d_i\in d\,,\ \ d_i\ge m
>    $$
>
>     
>
>    ------
>
>    
>
> 4. Se $G=(V,E)$ è un grafo finito con $n$ vertici e $u$ e $v$ sono due vertici di grado massimo, ovvero
>    $$
>    \begin {align}
>    \forall w\in V, \ \ &\deg(w)\le\deg(u) \\
>    &\deg(w)\le\deg(v)
>    \end{align}
>    $$
>    allora il numero di vertici di $G$, diversi da $u$ e da $v$, con grado almeno $2$, è almeno $\deg(u)+\deg(v)-n$
>    $$
>    |\{w\in V\setminus\{u,v\}\ |\ \deg(w)\ge2 \}|\ \ge\ \deg(u)+\deg(v)-n
>    $$
>
>    
>    
>    ---
>    
>    
>
> 4. Sia $d=(d_1,...,d_n)$ un vettore a componenti intere tali che
>    $$
>    0\le d_1\le\, ...\le d_n\le 2
>    $$
>    e tali che soddisfino il lemma delle strette di mano, ovvero c'è un numero pari ($0$ compreso) di componenti uguali a $1$, allora si possono presentare tre casi
>    
>       1. Tra le componenti del vettore $d$
>    
>          - NON compaiono componenti uguali a $1$
>          - Esistono UNA o DUE componenti uguali a $2$
>    
>          $$
>          d=(0,...,0,2)\ \ \ \or \ \ \ d=(0,...,0,2,2)
>          $$
>    
>           In questo caso NON esiste un grafo avente $d$ come score
>    
>    2. Tra le componenti del vettore $d$
>    
>       - NON compaiono componenti uguali a $1$
>       - Esistono ZERO o più di TRE comp. uguali a $2$ ($m=0\or m\ge3$)
>    
>       $$
>       d=(0,...,0)\ \ \ \or \ \ \ d=(0,...,0,2,...,2)
>       $$
>    
>       In in entrambi i casi ESISTE un grafo di score $d$, formato da
>    
>       - $m=0$:  $n$ vertici di grado $0$
>       - $m\ge3$:  $n-m$ vertici di grado $0$ e un ciclo $C_m$ di lunghezza $m$
>    
>    3. Tra le componenti del vettore $d$ compaiono
>    
>       - $n$ componenti uguali a $0$  ($n\ge0$)
>       - $2k+2$ componenti uguali a $1$  ($2k+2\ge2$)
>       - $m$ componenti uguali a $2$  ($m\ge0$)
>    
>       $$
>       d=(0,...,0,1,...,1,2,...,2)
>       $$
>    
>       In questo caso ESISTE un grafo avente $d$ come score, formato dall'unione di
>    
>       - $n$ vertici di grado $0$
>       - un cammino formato dagli eventuali vertici di grado $2$ con agli estremi due vertici di grado $1$
>       - $k$ eventuali cammini di lunghezza $1$ costituiti dai restanti vertici di grado $1$
>





## 5.  Isomorfismi di grafi

> ### <span style='color: blue'>Consegna</span>
>
> Si dica se i seguenti grafi sono isomorfi
>
> ### <span style='color: blue'>Svolgimento</span>
>
> Si proceda verificando le seguenti condizioni e escludendo i grafi che non le soddisfano
>
> 1. <u>Confronto degli score</u>
>
>    Se due grafi sono isomorfi allora hanno lo stesso score
>
>    Equivalentemente, due grafi con score diverso non sono isomorfi
>
> 2. <u>Confronto dei $k$-cicli</u>
>
>    Se due grafi sono isomorfi allora hanno lo stesso numero di $k$-cicli
>
>    Eq., due grafi con numero di $k$-cicli diverso non sono isomorfi
>
> 3. <u>Confronto dei gradi dei vertici adiacenti</u>
>
>       Se due grafi sono isomorfi allora vertici con lo stesso grado sono adiacenti a vertici con lo stesso grado
>
> <u>Costruzione di un isomorfismo</u>
>
> - Si scriva una funzione che associ i vertici di $G_1$ a quelli di $G_2$, tale che i vertici di ogni coppia $(v_1,v_2)\in f$ abbiano lo stesso grado
>    	$$
>    f=\{(v_1,v_2)\in V_1\times V_2\ |\ \deg(v_1)=\deg(v_2) \} \\ \ \\
>    f:V_1→V_2 \\
> a_1\mapsto b_1 \\
>    a_2\mapsto b_2 \\
>    ... \\
>    a_n\mapsto b_n
>    $$
>    
>    $f$ deve essere bigettiva: in $f(V_1)$ devono comparire tutti i vertici di $G_2$ senza ripetizioni
>    
> - Per essere un morfismo, $f$ deve indurre i lati di $G_1$ in quelli di $G_2$
>     $$
>     f:E_1→{V_2 \choose 2}\\
>     \{a_1,a_2\}\mapsto \{b_1,b_2\}\in E_2 \\
>     ... \\
>     \{a_n,a_m\}\mapsto \{b_j,b_k\}\in E_2
>     $$
>     Ovvero deve verificarsi
>     $$
>     f(E_1)\subseteq E_2
>     $$
>     $f$ deve essere bigettiva: in $f(E_1)$ devono comparire tutti i lati di $G_2$ senza ripetizioni
>
> Se la funzione $f$ che manda vertici e lati da $G_1$ a $G_2$ è un morfismo ed è bigettiva, allora $f$ è un isomorfismo tra $G_1$ e $G_2$, quindi $G_1 ≅G_2$







# Teoremi e dimostrazioni

#### 1.  L'ordinamento dei numeri naturali è un buon ordinamento

> ### <span style='color: green'>Definizione</span>  (buon ordinamento)
>
> Sia $(X,\le)$ un insieme parzialmente ordinato. $(X,\le)$ è ben ordinato se ogni sottoinsieme non vuoto $A\subseteq X$ ammette minimo, ovvero
> $$
> \forall\ A\subseteq X,\ \ \exist\ a\in A\ \ |\ \ \forall\ b\in A,\ a\le b
> $$
>
> ### <span style='color: red'>Teorema 7.4</span>  (ordinamento dei naturali)
>
> L'ordinamento dei numeri naturali $(\N,\le)$ è un buon ordinamento
>
> ### <span style='color: red'>Dimostrazione</span>
>
> Supposto che $A\subseteq\N$ non ammetta minimo, si provi che $A=Ø$
>
> Si definisca $B:=\N-A$ il suo complementare
>
> Si proceda **per induzione** su $n\in\N$
>
> 1. <u>Base induttiva</u>:   $n=0\ \ \Rarr\ \ \{0\}\subseteq B$
>
>    $0\notin A$, altrimenti sarebbe il suo minimo, quindi $0\in B$  e  $\{0\}\subseteq B$
>
> 2. <u>Passo induttivo</u>:  $n>0,\ \ \ n\mapsto n+1$
>
>    Supposto che $\{0,...,n\}\subseteq B\ \Rarr\ 0,...,n\notin A\ \Rarr\ n+1\notin A$ altrimenti $n+1$ sarebbe il minimo di $A$
>
>    Allora $n+1\in B$ e $\{0,...,n,n+1\}\subseteq B$
>
> Da ciò segue che $B=\N$ e quindi $A=Ø$

#### 1.  Seconda forma del principio di induzione

> ### <span style='color: red'>Teorema 7.5</span>  (principio di induzione - II forma)
>
> Sia $P(n)$ una famiglia di proposizioni indicizzate su $\N$ e si supponga che
>
> 1. $P(0)\ \rm vera$
> 2. $\forall n>0,\ (\forall k<n,\ P(k)\ {\rm vera})\ \Rarr\ P(n)\ \rm vera$
>
> Allora $\forall n\in\N,\ P(n)\ \rm vera$
>
> ### <span style='color: red'>Dimostrazione</span>
>
> Sia $A=\{n\in\N\ |\ P(n)\ \rm falsa \}$ e **per assurdo** $A\neØ$, allora per la ==proprietà di buon ordinamento== $A$ ha minimo $n$
>
> Dal teorema segue che
>
> 1. $n\ne 0$ in quanto $P(0)\ \rm vera$
> 2. $\forall k<n,\ k\notin A$ in quanto $n=\min A$
>
> Ma dalla (2) segue che $P(n)\ \rm vera$, quindi $n\notin A$, contraddicendo $n\in A$



#### 2.  Esistenza e unicità di quoziente e resto (divisione euclidea)

> ### <span style='color: red'>Teorema 7.7</span>  ($\boldsymbol \exist!$ quoziente e resto)
>
> $$
> n,m\in\Z\ \and\ m\ne0\ \Rarr\ \exist!\ q,r\in\Z\ \ {\rm t.c.}
> $$
>
> $$
> \begin {cases}
> n=mq+r\ \\
> 0\le r<|m|
> \end {cases}
> $$
>
> ### <span style='color: red'>Dimostrazione</span>
>
> ##### <u>Esistenza</u>
>
> Si proceda **per induzione** su $n,m\in\Z$
>
> - <u>Base induttiva</u>:   $n=0\ \ \Rarr\ \ q=0\ \and\ r=0$
>
> - $0<n<m\ \and\ \forall k<n,\ \text{tesi vera}\ \ \Rarr\ \ q=0\ \and\ r=n$
>
> - $n\ge m>0\ \and\ \forall k<n,\ \text{tesi vera}$
>
>   Sia $k:=n-m$, dato che $m\ne 0$ allora $0\le k<n$
>
>   Per le ipotesi di induzione
>   $$
>   \exist\ q,r\in\N\ \ |\ \ k=mq+r \ \and\ 0\le r< m\ \Rarr
>   $$
>
>   $$
>   \Rarr\ n=m+k=m+(mq+r)=m(q+1)+r
>   $$
>
> - $n<0\ \and\ m>0\ \ \Rarr\ -n>0$
>   
>   Si applichi il caso precedente a $m$
>   $$
> \exist\ q,r\in\Z\ \ |\ -n=mq+r \ \and\ 0\le r< m=|m|
>   $$
>   
>   - $r=0\ \ \Rarr\ \ n=m(-q)-r$
>   
>   - $0<r<m\ \Rarr\ 0<m-r<m=|m|\ \ \Rarr$
>     $$
>     \Rarr\ \ n=m(-q)-r=m(-q)-m+m-r=m(-1-q)+(m-r)
>     $$
>   
> - $m<0\ \ \Rarr\ -m>0$
>   
>   Si applichino i casi precedenti a $-m$
>   $$
>   \exist\ q,r\in\Z\ \ |\ \ n=(-m)q+r \ \and\ 0\le r< -m=|m| \ \ \Rarr
>   $$
>   
>   $$
>   \Rarr\ \ n=m(-q)+r
>   $$
>
> ##### <u>Unicità</u>
>
> Si supponga che $n=mq+r=mq'+r'$ con $0\le r,r'<|m|$
>
> Supposto $r'\ge r$ si ha che
> $$
> \begin{align}
> &m(q-q')=r'-r\ \Rarr\\ &\Rarr\ |m||q-q'|=|r'-r|=r'-r<|m|\ \Rarr\\ &\Rarr\ 0\le |q-q'|<1 \Rarr\\ &\Rarr\ |q-q'|=0\ \Rarr\ q=q'\ \Rarr\\ &\Rarr\ mq+r=mq'+r'\ \Rarr\ r=r'
> \end{align}
> $$



#### 3.  Rappresentazione dei naturali in una base arbitraria

> ### <span style='color: red'>Teorema 8.4</span>  (rappresentazione base arbitraria)
>
> Sia $b\in\N,\ b\ge 2$, allora ogni numero naturale $n\in\N$ è rappresentabile in modo unico in base $b$ come una successione definitivamente nulla $\{ε_i\}_{i\in\N}$ 
> $$
> b\in\N\ \and\ b\ge 2\ \ \Rarr\ \ \forall n\in\N,\ \exist!\ \{ε_i\}_{i\in\N}\ \ |\ \ n=\sum_{i=0}^\infin ε_ib^i\ \ \and\ \ 0\le ε_i<b
> $$
> Ossia esiste una tale successione $\{ε_i\}$ e se $\{ε_i'\}$ è un'altra tale successione, allora $\forall i\in\N,\ ε_i=ε_i'$
>
> ### <span style='color: red'>Dimostrazione</span>
>
> ##### <u>Esistenza</u>
>
> Si proceda per induzione su $n$
>
> 1. <u>Base induttiva</u>:    $n=0\ \ \Rarr\ \ \forall i\in\N,\ ε_i=0\ \ \Rarr\ \ n=\sum_{i=0}^\infin 0·b^i=0$
>
> 2. <u>Passo induttivo</u>:  $n>0\ \and\ \forall k<n, \text{tesi vera}$
>
>    Siano $q$ e $r$ tali che $n=bq+r$ con $0\le r < b$  (==divisione eucliea==)
>
>    $b\ge 2\ \Rarr\ 0\le q< bq\le bq+r=n$
>
>    Per ipotesi di induzione esiste una successione $\{δ_i\}$ definitivamente nulla, tale che
>    $$
>    \forall i\in\N,\ δ_i\in\N\ \and\ 0\le δ_i<b\ \ |\ \ q=\sum_{i=0}^\infin δ_ib^i
>    $$
>
>    $$
>    n = b\sum_{i=0}^\infin δ_ib^i+r
>      = \sum_{i=0}^\infin δ_ib^{i+1}+r
>      = \sum_{i=1}^\infin δ_{i-1}b^i+r
>      = \sum_{i=0}^\infin ε_ib^i
>    $$
>
>    $$
>    {\rm dove}\ \ \ ε_0=r,\ \ ε_i=δ_{i-1}\ \ \forall i>0
>    $$
>
>    $\{ε_i\}$ è definitivamente nulla perché lo è $\{δ_i\}$ e
>    $$
>    \forall i>0,\ 0\le ε_i=δ_{i-1}<b\ \and\ 0\le ε_0=r<b
>    $$
>
> ##### <u>Unicità</u>
>
> Si proceda **per induzione** su $n$
>
> 1. $n=0,\ n=\sum_{i=0}^\infin ε_ib^i\ \and\ \forall i\in\N,\ 0\le ε_i<b\ \Rarr\ \forall i,\ ε_i=0$
>
> 2. $n>0,\ n=\sum_{i=0}^\infin ε_ib^i=\sum_{i=0}^\infin ε'_ib^i\ \ \Rarr$
>    $$
>    \Rarr\ \ n=b\sum_{i=1}^\infin ε_ib^{i-1}+ε_0=b\sum_{i=1}^\infin ε'_ib^{i-1}+ε_0'
>    $$
>    Per l'unicità della ==divisione euclidea== si ha che
>    $$
>    ε_0=ε'_0\ \ \ \and\ \ \ q=\sum_{i=1}^\infin ε_ib^{i-1}=\sum_{i=1}^\infin ε'_ib^{i-1}
>    $$
>    $q<n$ e quindi per ipotesi di induzione anche $\forall i\in\N,\ ε_i=ε_i'$



#### 4.  Esistenza e unicità di MCD e mcm di due numeri interi

> ### <span style='color: red'>Proposizione 9.6</span>  (esistenza e unicità del MCD)
>
> Siano $n,m\in\Z$ non entrambi nulli, allora esiste ed è unico il massimo comun divisore fra $n$ e $m$
>
> - <u>Esistenza</u>:   $n,m\in\Z,\ m\ne0\ \Rarr\ \exist\ (n,m)$
> - <u>Unicità</u>:       $d,d'\in{\rm MCD}(n,m)\ \Rarr\ d'=\pm d$
>
> ### <span style='color: red'>Dimostrazione</span>
>
> ##### <u>Esistenza</u>
>
> $$
> S=\{s\in\Z\ |\ s>0,\ \exist\ x,y\in\Z:s=nx+my \}\\
> nn+mm>0\ \Rarr\ S\neØ
> $$
>
> $$
> d:=\min S=nx+my
> $$
>
> <u>Si dimostri che $d$ è il massimo dei divisori comuni</u>
>
> Sia $c\in\Z$ tale che
> $$
> c\mid n\ \and\ c\mid m\ \Rarr\ n=ck\ \and\ m=ch\ \Rarr\\
> \Rarr\ d=nx+my=ckx+chy=c(hx+ky)\ \Rarr\ c\mid d
> $$
> Ciò dimostra che $d$ è multiplo di tutti i divisori comuni di $n$ e $m$
>
> <u>Si dimostri che $d\mid n$</u>
>
> Si esegua la ==divisione euclidea== fra $n$ e $d$
> $$
> n=dq+r\,,\ 0\le r<d
> $$
>
> $$
> r>0\ \Rarr\ r=n-dq=n-(nx+my)q=n(1-qx)+m(-y)q\ \Rarr\\
> \Rarr\ r\in S
> $$
>
> Ciò è assurdo perché $r<d=\min S$, quindi $r=0\ \Rarr\ d\mid n$
>
> Analogamente $d\mid m$
>
> ##### <u>Unicità</u>
>
> $$
> d\ \mid n\ \and\ d\ \mid m\ \and\ d'\in{\rm MCD}(n,m) \ \Rarr\ d\ \mid d'\\
> d'\mid n\ \and\ d'\mid m\ \and\ d\ \in{\rm MCD}(n,m) \ \Rarr\ d'\mid d\
> $$
>
> $$
> d\mid d'\ \and\ d'\mid d\ \Rarr\ d'=\pm d
> $$

> ### <span style='color: red'>Teorema 10.4</span>  (esistenza e unicità del mcm)
>
> Siano $n,m\in\Z$ non entrambi nulli, allora esiste ed è unico il minimo comune multiplo fra $n$ e $m$
>
> ### <span style='color: red'>Dimostrazione</span>
>
> Si osservi che
> $$
> (n,m)\mid n\ \ \Rarr\ \exist\ n'\ \in\Z\ \ |\ \ n\ =n'\ (n,m) \\
> (n,m)\mid m\ \Rarr\ \exist\ m'\in\Z\ \ |\ \ m=m'(n,m)
> $$
> Posti $n=n'(n,m)$ e $m=m'(n,m)$, si definisca
> $$
> M:=\dfrac{n·m}{(n,m)}=n'm'(n,m)
> $$
>
> $$
> M=nm'=n'm\ \ \Rarr\ \ n\mid M\ \and\ m\mid M
> $$
> <u>Si dimostri che $M$ è il minimo dei comuni multipli</u>
>
> Sia $c\in\Z$ tale che
> $$
> n\mid c\ \and\  m\mid c\ \ \Rarr\ \ (n,m)\mid c \ \ \Rarr\ \ \exist\ c'\ |\ c=c'(n,m)
> $$
> Da ciò segue che
> $$
> n'(n,m)\mid c'(n,m)\ \ \and\ \ m'(n,m)\mid c'(n,m)
> $$
> Dato che $(n',m')=\big(\frac{n}{(n,m)},\frac{m}{(n,m)} \big)=1$, allora
> $$
> n'm'(n,m)\mid c'(n,m)\ \ \Rarr\ \ M\mid c
> $$



#### 5.  Teorema fondamentale dell’Aritmetica

> ### <span style='color: red'>Teorema 10.5</span>  (fondamentale dell'aritmetica)
>
> $$
> \forall n\in\Z,\ n\ge2\ \ \Rarr\ \ \exist\ p_1,p_2,...,p_k\ {\rm primi}>0\ \ |\ \ n=p_1p_2···p_k
> $$
>
> Ovvero ogni intero maggiore di $1$ si scrive in modo unico, a meno dell'ordine, come prodotto di numeri primi positivi
> $$
> q_1,q_2,...,q_h\ {\rm primi}\ \ |\ \ n=q_1q_2···q_h\ \ \Rarr
> $$
>
> $$
> \Rarr\ \ \exist\ {\rm bigezione}\ σ:\{1,2,...,k\}→\{1,2,...,h\}\ \ |\ \ q_i=p_{σ(i)}
> $$
>
> ### <span style='color: red'>Dimostrazione</span>
>
> Si proceda per induzione su $n$
>
> 1. <u>Base induttiva</u>:    $n=2\ \ \Rarr\ \ 2\ \rm primo$ non necessita di dimostrazione
>
> 2. <u>Passo induttivo</u>:  $n>2\ \and\ \forall k<n,\ \text{tesi vera}$
>
>    - $n\ {\rm primo}\ \ \Rarr$  non necessita di dimostrazione
>
>    - $n\ !{\rm primo}\ \Rarr\ \exist\ d_1,d_2: 1<d_1,d_2<n\ \ |\ \ n=d_1d_2$
>
>      <u>Ipotesi induttiva</u>:
>      $$
>      \exist\ p_i,q_j\ {\rm primi}>0\ \ |\ \ d_1=p_1p_2···p_k\ \and\ d_2=q_1q_2···q_h
>      $$
>      Allora $n=p_1···p_kq_1···q_h$ è prodotto di numeri primi
>##### <u>Unicità</u>
> 
>Sia $n=p_1p_2···p_k=q_1q_2···q_h$ con $p_i,q_j\ {\rm primi}>0$ e $k\le h$
> 
>Si proceda per induzione su $k$
> 
>1. <u>Base induttiva</u>:   $k=1\ \ \Rarr\ \ n=p_1=q_1···q_h$
>    $$
>    \begin{align}
>    &\forall\ j,\ \ q_j\mid p_1 &\Rarr& &q_j=1\ \ \ \or\  \ \ q_j=p_1 \\
>    &\forall\ j,\ \ q_j\ {\rm primo} &\Rarr& &q_j>1\ \ \Rarr\ \ q_j=p_1
>    \end{align}
>    $$
>    
>    $$
>    h>1\ \ \Rarr\ \ n=q_1···q_h\ge q_1q_2=p_1^2>p_1=n
>    $$
>    
>    Si è giunti a un assurdo, perciò
>    $$
>    h=1\ \and\ q_1=p_1\ \ \Rarr\ \ n=p_1=q_1
>    $$
> 
>2. <u>Passo induttivo</u>:  $k>1\ \ \Rarr\ \ p_k\mid n=q_1···q_h\ \ \Rarr\ \ \exist\ j\ :\ p_k\mid q_j$
>    $$
>    p_k,q_j\ {\rm primi}>0\ \ \Rarr\ \ p_k=q_j\ \ \Rarr\ \ p_1···p_{k-1}=q_1···q_{j-1}q_{j+1}···q_h
>    $$
>    Per ipotesi di induzione le due fattorizzazioni hanno lo stesso numero di elementi, ossia $k-1=h-1$, e esiste una bigezione
>    $$
>    δ:\{1,...,j-1,j+1,...,h\}→\{1,...,k-1\}\ \ |\ \ \forall i,\ q_i=p_{δ(i)}
>    $$
>    Definendo $σ:\{1,2,...,n\}→\{1,2,...,n\}$
>    $$
>    σ(i)=
>          \begin {cases}
>          k & i=j\\
>          δ(i) & i\ne j
>          \end {cases}
>    $$
>    si ottiene una bigezione tale che $\forall i,\ q_i=p_{σ(i)}$
> 



#### 6.  Teorema cinese del resto

> ### <span style='color: red'>Teorema 12.1</span>  (cinese del resto)
>
> Il sistema di congruenze
> $$
> \begin{cases}
> x \equiv a &({\rm mod}\ \ n)\\
> x \equiv b &({\rm mod}\ \ m)
> \end{cases}
> $$
> ammette soluzione se e solo se $(n,m)\mid a-b$
>
> Se $c$ è una soluzione del sistema allora gli elementi di $[c]_{[n,m]}$ sono tutte e sole le soluzioni del sistema, ovvero
> $$
> S=\{s,k\in\Z\ |\ s=c+k[n,m]\}
> $$
>
> ### <span style='color: red'>Dimostrazione</span>
>
> Sia $c$ una soluzione del sistema allora
> $$
> \exist\ h,k\in\Z\ \ |\ \ c=a+hn=b+km\ \ \Rarr\ \ a-b=km-hn
> $$
>
> $$
> (n,m)\mid n\ \and\ (n,m)\mid m\ \ \Rarr\ \ (n,m)\mid a-b
> $$
>
> Si supponga ora il contrario, ovvero
> $$
> (n,m)\mid a-b\ \ \Rarr\ \ \exist\ h,k\in\Z\ \ |\ \ a-b=km-hn\ \ \Rarr\ \ a+hn=b+km
> $$
>
> $$
> c=a+hn=b+km\ \ \Rarr\ \ c\ \text{ risolve entrambe le congruenze}
> $$
>
> Sia $S=\{x\in\Z\ |\ x\text{ risolve il sistema}\}$, si provi che
> $$
> c\in S\ \ \Rarr\ \ S=[c]_{[n,m]}
> $$
>
> - $S\subseteq[c]_{[n,m]}$
>
>   Sia $c'$ un'altra soluzione, allora
>   $$
>   c=a+hn=b+km\ \ \ \and\ \ \ c'=a+h'n=b+k'm
>   $$
>   Quindi si ha
>   $$
>   \begin{align}
>   c-c'&=a+hn-a'-h'n\ =(h-h')n\, \ \Rarr\ n\ \mid c-c'\\
>   c-c'&=b+km-b'-k'm=(k-k')m\ \Rarr\ m\mid c-c'
>   \end{align}
>   $$
>   $$
>   [n,m]\mid c-c'\ \ \Rarr\ \ c'\equiv_{[n,m]}c\ \ \Rarr\ \ c'\in[c]_{[n,m]}
>   $$
>
> - $[c]_{[n,m]}\subseteq S$
>
>   Sia $c'\in[c]_{[n,m]}$ ovvero $c'=c+h[n,m]$
>   
>   Per ipotesi
>   $$
>   c\equiv_na\ \and\ h[n,m]\equiv_n0
>   $$
>   Allora segue che
>   $$
>   c'=c+h[n,m]\equiv_na
>   $$
>   Analogamente $c'\equiv_mb$ e quindi $c'\in S$



#### 7.  Teorema di Fermat-Eulero

> ### <span style='color: green'>Definizione</span>  (funzione $Φ$ di Eulero)
>
> Dato un numero naturale $n$ si indica con $Φ(n)$ il numero di naturali minori o uguali a $n$ e coprimi con $n$
>
> ### <span style='color: red'>Teorema 13.9</span>  (di Fermat-Eulero)
>
> Elevando ogni classe invertibile modulo $n$ alla $Φ(n)$ si ottiene la classe $[1]_n$
> $$
> u\in\Z/n\Z^*\ \ \Rarr\ \ u^{Φ(n)}\equiv1\ \ ({\rm mod}\ n)
> $$
>
> ### <span style='color: red'>Dimostrazione</span>
>
> Sia $k:=Φ(n)$ e siano $x_1,...,x_k$ tutti gli elementi di $\Z/n\Z^*$
> (<span style='color: green'>proposizione 1</span>:  $\forall n>0,\ |\Z/n\Z^*|=Φ(n)$)
>
> Si definisca la funzione $L_u:\Z/n\Z^*→\Z/n\Z^*$ ponendo $L_u(v)=uv$ (<span style='color: green'>proposizione 2</span>:  $u,v\in\Z/n\Z^*\ \Rarr\ uv\in\Z/n\Z^*$)
>
> - Tale funzione è iniettiva, infatti poichè $u$ è invertibile
>   $$
>   L_u(v_1)=L_u(v_2)\ \Rarr\ uv_1=uv_2\ \Rarr\ v_1=v_2\ \ \ \ ({\rm in}\ \Z/n\Z^*)
>   $$
>   (<span style='color: green'>osservazione 3</span>:  $ac=ad\ \Rarr\ c= d\ \ \ ({\rm in}\ \Z/n\Z^*)$)
>
> - Dato che l'insieme $\Z/n\Z^*$ è finito, $L_u$ è bigiettiva
>
> Dato che $L_u$ è bigettiva, allora $L_u(x_1),...,L_u(x_k)$ sono elementi di $\Z/n\Z^*$
>
> Allora per la ==commutatività del prodotto==
> $$
> x_1x_2···x_k=L_u(x_1)L_u(x_2)···L_u(x_k)=\\
> =ux_1ux_2···ux_k=u^kx_1x_2···x_k
> $$
> Da questa uguaglianza si osserva che $x_1x_2···x_k$ è invertibile ==(2)== da cui segue ==(3)== che $u^k=1$

#### 7.  Crittografia RSA

> ### <span style='color: red'>Proposizione 13.11</span>  (crittografia RSA)
>
> Sia $c$ un intero positivo coprimo con $Φ(n)$ e sia $d$ un intero positivo diverso da $c$ modulo $Φ(n)$ e inverso di $c$ modulo $Φ(n)$, ovvero
> $$
> \begin{align}
> c \in\Z\ \ &|\ \ c\ge0\ \and\ (c,Φ(n))=1 \\
> d\in\Z\ \ &|\ \ d>0\ \and\ d\in[c]^{-1}_{Φ(n)}
> \end{align}
> $$
> Allora l'applicazione $C:\Z/n\Z^*→\Z/n\Z^*$ definita da $x\mapsto x^c$ è invertibile e la sua inversa è data da $D(x)=x^d$ essendo $cd\equiv1\ ({\rm mod}\ Φ(n))$
>
> ### <span style='color: red'>Dimostrazione</span>
>
> Se $c$ è coprimo con $Φ(n)$ allora esiste un $d$ tale che $cd\equiv1\ ({\rm mod}\ Φ(n))$
>
> Allora $cd= k·Φ(n)+1$ e quindi per il ==teorema di Fermat==, $\forall x\in\Z/n\Z^*$
> $$
> D(C(x))=(x^c)^d=x^{kΦ(n)+1}=x(x^{Φ(n)})^k=x·1^k=x
> $$
> Del tutto analoga è la prova che $\forall x,\ C(D(x))=x$, da cui la tesi



#### 8.  Equivalenza fra congiungibilità con cammini e passeggiate

> ### <span style='color: red'>Proposizione 15.8</span>  (congiungibilità con cammino)
>
> Due vertici sono congiungbili mediante un cammino se e solo se lo sono mediante una passeggiata, ovvero
> $$
> u,v\in V(G)\ \ \Rarr
> $$
>
> $$
> \begin{align}
> \Rarr\ \ &\exist\ (v_0,...,v_n)\ \ |\ \ v_0=u\ \and\ v_n=v\ \and\ \forall\ i\ne j\,,\ v_i\ne v_j\iff \\
> \iff &\exist\ (v_0,...,v_n)\ \ |\ \ v_0=u\ \and\ v_n=v
> \end{align}
> $$
>
> ### <span style='color: red'>Dimostrazione</span>
>
> Dato che un cammino è una passeggiata, se due vertici sono congiungibili mediante un cammino lo sono anche mediante una passeggiata
>
> Viceversa si supponga che tra due vertici $u$ e $v$ esista una passeggiata
>
> Siano  ${\cal P} =\{P\ |\ P\, \text{ passeggiata tra } u,v \}$  e  $A=\{\ell(P)\in\N\ |\ P\in\cal P \}$
>
> Dato che $u$ e $v$ sono congiungibili da una passeggiata,  ${\cal P}\neØ\ \Rarr\ A\neØ$
>
> Allora per il teorema di ==buon ordinamento== dei numeri naturali, $A$ ha minimo, ovvero esiste una passeggiata $P_0$ da $u$ a $v$ che ha lunghezza minima, cioè
> $$
> \forall P\in{\cal P},\ \ \ell(P_0)\le\ell(P)
> $$
> <u>Si provi che $P_0$ è un cammino</u>
>
> Sia $P_0=(v_0,...,v_m)$, se per assurdo $P_0$ non fosse un cammino allora
> $$
> \exist\ i<j\ \ |\ \ v_i=v_j
> $$
> Si consideri $P_1=(v_0,...,v_i,v_{j+1},...,v_m)$
>
> $P_1$ è una passeggiata, infatti, dato che $P_0$ è una passeggiata,
> $$
> \forall\ 0\le h<m,\ \ \{v_h,v_{h+1}\}\in E(G)
> $$
> E dato che $v_i=v_j$
> $$
> \{v_i,v_{j+1}\}=\{v_i,v_{i+1}\}\in E(G)
> $$
> $P_1$ congiunge $u$ a $v$, dato che $v_0=u$ e $v_m=v$ e quindi $P_1\in\cal P$
>
> Ma poiché $\ell(P_1)=m-(j-i)<m$, ciò contraddice la minimità di $P_0$ e dimostra dunque che $P_0$ è un cammino

#### 8.  La congiungibilità è una relazione di equivalenza

> ### <span style='color: red'>Proposizione 15.9</span>  (congiungibilità - equivalenza)
>
> La relazione di congiungibilità è una realazione di equivalenza
>
> ### <span style='color: red'>Dimostrazione</span>
>
> Si indichi con $\sim$ la relazione di congiungibilità
>
> Si provi che la relazione $\sim$ è riflessiva, simmetrica e transitiva
>
> - <u>Riflessiva</u>:  $\forall\ v\in V(G),\ (v)$ è un cammino che congiunge $v$ a $v$, dunque
>   $$
>   \forall\ v\in V(G),\ \ v\sim v
>   $$
>
> - <u>Simmetrica</u>:  se $u\sim v$ allora esiste una passeggiata
>   $$
>   P=(v_0,...,v_n)\ \ |\ \ v_0=u\ \and\ v_n=v
>   $$
>   Ma allora $P'=(v_n,v_{n-1},...,v_0)$ è una passeggiata (due vertici consecutivi in $P'$ sono adiacenti, dato che sono consecutivi anche in $P$) il cui primo vertice è $v$ e l'ultimo è $u$, ovvero
>   $$
>   \forall\ u,v\in V(G),\ \ u\sim v\ \ \Rarr\ \ v\sim u
>   $$
>
> - <u>Transitiva</u>:  se $u\sim v$ e $v\sim w$ allora esistono passeggiate
>   $$
>   P_1=(u_0,...,u_n)\,, \ P_2=(v_0,...,v_m)\ \ |\ \ u=u_0,\ v=u_n=v_0,\ w=v_m
>   $$
>   Sia $Q=(u_0,...,u_n=v_0,v_1,...,v_m)$; $Q$ è una passeggiata dato che vertici consecutivi in $Q$ sono consecutivi in $P_1$ o in $P_2$
>
>   Poiché il primo e ultimo vertice di $Q$ sono $u$ e $v$, segue che
>   $$
>   \forall\ u,v,w\in V(G),\ \ u\sim v\ \and\ v\sim w\ \ \Rarr\ \ u\sim w
>   $$
>
> Per la ==definizione di relazione di equivalenza==, si è dimostrato che la relazione di congiungibilità $\sim$ è una realazione di equivalenza



#### 9.  Relazione fondamentale dei grafi finiti

> ### <span style='color: red'>Proposizione 17.2</span>  (relazione fondamentale)
>
> Se $G(V,E)$ è un grafo finito allora
> $$
> \sum_{v\in V} \deg(v)=2|E|
> $$
>
> ### <span style='color: red'>Dimostrazione</span>
>
> Siano $v_1,...,v_n$i vertici di $G$ e $e_1,...,e_k$ i suoi lati
>
> Si consideri il numero $m_{i,j}$ tale che
> $$
> \forall\ i=1,...,n\ \and \ j=i,...,k\ \ \ \ \ m_{i,j}=
> \begin {cases} 
> 1\ &{\rm se}\ \ v_i\in e_j \\
> 0\ &{\rm se}\ \ v_i\notin e_j
> \end {cases}
> $$
> Dalle ==proprietà associativa e commutativa della somma== si ha che
> $$
> \sum_{i=1}^n\bigg(\sum_{j=1}^k m_{i,j}\bigg) = \sum_{j=1}^k\bigg(\sum_{i=1}^n m_{i,j}\bigg)\ \ \ \ \ \ (*)
> $$
>
> - <u>Fissato $i$</u>, il numero $\sum_{j=1}^k m_{i,j}$ è uguale alla cardinalità dell'insieme
>   $$
>   \sum_{j=1}^k m_{i,j}=|\{j\ |\ m_{i,j}=1 \}|=|\{j\ |\ v_i\in e_j\}|
>   $$
>   Che è uguale al numero dei lati che contengono $v_i$, ossia
>   $$
>   \sum_{j=1}^k m_{i,j} = \deg(v_i)
>   $$
>   Pertando il primo membro dell'uguaglianza $(*)$ è pari a
>   $$
>   \sum_{i=1}^n\bigg(\sum_{j=1}^k m_{i,j}\bigg) = \sum_{i=1}^n \deg(v_i)=\sum_{v\in V} \deg(v)
>   $$
>
> - <u>Fissato $j$</u>, il numero $\sum_{i=1}^n m_{i,j}$ è pari alla cardinalità dell'insieme
>   $$
>   \sum_{i=1}^n m_{i,j}=|\{i\ |\ v_i\in e_j\}|=2
>   $$
>   dato che ogni lato contiene esattamente due vertici
>
>   Pertando il secondo membro dell'uguaglianza $(*)$ è pari a
>   $$
>   \sum_{j=i}^k\bigg(\sum_{i=1}^n m_{i,j}\bigg)=\sum_{j=i}^k2=2k=2|E|
>   $$
>
> Riscrivendo l'uguaglianza $(*)$ si ottiene
> $$
> \sum_{v\in V} \deg(v)=2|E|
> $$

#### 9.  Lemma delle strette di mano

> ### **<span style='color: red'>Lemma 17.3</span> (delle strette di mano)**
>
> Se $G$ è un grafo finito, allora il numero di vertici di grado dispari è pari
>
> ### <span style='color: red'>Dimostrazione</span>
>
> Dalla ==relazione fondamentale== dei grafi finiti segue che la somma dei gradi dei vertici di $G$ è un numero pari, infatti
> $$
> \sum_{v\in V} \deg(v)=2|E|
> $$
> Si definiscano
> $$
> \begin{align}
> &p\ :=\ \sum_{v\in V | \deg(v)\ \rm pari\ \ \ } \deg(v)\\ \\
> &d\ :=\ \sum_{v\in V | \deg(v)\ \rm dispari}\deg(v)
> \end{align}
> $$
> È evidente che
> $$
> \sum_{v\in V} \deg(v)=p+d=2|E|
> $$
> Da cui segue che
> $$
> 2|E|-p=d
> $$
> Poiché a primo membro vi sono soltanto somme e differenze di numeri pari, che portano a un risultato pari, segue che entrambi i membri sono pari, ovvero
> $$
> 2|E|-p\ \ {\rm è\ pari}\ \ \Rarr\ \ d\ \ {\rm è\ pari}
> $$
> Poiché la sommatoria dei gradi dispari è pari, è necessario che il numero di vertici di grado dispari sia pari



#### 10.  Caratterizzazione degli alberi finiti

> ### <span style='color: red'>Teorema 20.6</span>  (caratterizzazione degli alberi)
>
> Sia $T=(V,E)$ un grafo finito. Le seguenti affermazioni sono equivalenti
>
> 1. $T$ è un albero
> 2. $T$ è connesso e $|V|-1=|E|$
>
> ### <span style='color: red'>Dimostrazione</span>
>
> - $(1)\Rarr(2)$
>
>   Si proceda per induzione su $|V(T)|$
>
>   1. <u>Base induttiva</u>:   $|V(T)|=1\ \Rarr\ |E(T)|=0\ \Rarr\ \rm tesi\ vera$
>
>   2. <u>Passo induttivo</u>: $|V(T)|>1$ ,  $v\in V(T)$ una foglia e $T-v$ un albero
>
>      Per ipotesi di induzione si ha che
>      $$
>      |V(T-v)|-1=|E(T-v)|
>      $$
>      
>      $$
>      |V(T-v)|=|V(T)|-1\\ \deg(v)=1\ \Rarr\ |E(T-v)|=|E(T)|-1
>      $$
>      
>      $$
>      |V(T)|-1-1=|E(T)|-1
>      $$
>      
>      Da cui la tesi
>      $$
>      |V(T)|-1=|E(T)|
>      $$
> - $(2)\Rarr(1)$
>
>   Si provi che $T$ non abbia cicli
>
>   Si proceda per induzione su $|V(T)|$
>
>   1. <u>Base induttiva</u>:    $|V(T)|=1\ \Rarr\ \rm tesi\ vera$
>
>   2. <u>Passo induttivo</u>:  $|V(T)|>1$
>
>      Si provi che $T$ abbia una foglia
>
>      Per ipotesi di induzione e dalla ==relazione fondamentale== dei grafi finiti si ottiene, tramite la ==formula di Eulero==,
>      $$
>      2|V(T)|-2=2|E(T)|=\sum_{v\in V(T)}\deg(v)
>      $$
>      Se non esistesseo foglie, ovvero
>      $$
>      \forall\ v\in V(T)\,, \ \deg(v)\ge2
>      $$
>      (non possono esistere vertici di grado $0$ perché $T$ è connesso)
>
>      si giungerebbe ad un assurdo perché
>      $$
>      2|V(T)|-2 \ge 2|V(T)|
>      $$
>      Pertanto almeno un vertice deve avere grado $1$
>
>      Sia quindi $v$ una foglia e si consideri il grafo $T-v$
>
>      Dato che $T$ è connesso e $\deg(v)=1$, anche $T-v$ è connesso
>      $$
>      |V(T-v)|=|V(T)|-1\ \ \and\ \ |E(T-v)|=|E(T)|-1\ \Rarr
>      $$
>
>      $$
>      \Rarr\ |V(T-v)|-1=|E(T-v)|
>      $$
>
>      Per ipotesi di induzione allora $T-v$ è un albero
>
>      Poiché i vertici di un ciclo hanno tutti grado almeno $2$, allora un ciclo in $T$ non potrebbe passare per $v$, ossia sarebbe contenuto in $T-v$, contraddicendo il fatto che $T-v$ è un albero
>
>   Si è dimostrato così che $T$ non ha cicli e quindi è un albero
>



#### 11.  Esistenza dell'albero di copertura per i grafi connessi finiti

> ### <span style='color: red'>Teorema 21.3</span>  (albero di copertura)
>
> Sia $G$ un grafo connesso finito, allora $G$ ha un albero di copertura $T$, ossia un sottografo di $G$ tale che
>
> 1. $T$ è un albero
> 2. $V(T)=V(G)$
>
> ### <span style='color: red'>Dimostrazione</span>
>
> Si consideri l'insieme
> $$
> {\cal C}=\{C\ |\ C\ \text{sottografo connesso di } G\ \and\ V(C)=V(G) \}
> $$
>
> $$
> G\in C\ \ \Rarr\ \ \cal C\neØ
> $$
>
> Data la finitezza di $G$ esiste un grafo $\overline C\in\cal C$ con il minor numero di lati, cioè
> $$
> \forall\ C\in{\cal C},\ \ |E(\overline C)|\le|E(C)|
> $$
> <u>Si provi che $\overline C$ è un albero</u>
>
> Se per assurdo $\overline C$ non fosse un albero, allora per la ==proprietà del teorema di caratterizzazione degli alberi==, esisterebbe un lato $e\in E(\overline C)$ tale che $C:=\overline C-e$ sia connesso, ma
> $$
> V(C)=V(\overline C-e)=V(G)\ \ \Rarr\ \ C\in{\cal C}
> $$
>
> $$
> |E(C)|=|E(\overline C-e)|=|E(\overline C)|-1
> $$
>
> Ciò contraddice la minimalità di $\overline C$ e dimostra che $\overline C$ è un albero

