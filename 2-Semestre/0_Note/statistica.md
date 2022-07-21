# [↓](#↑)

[TOC]



# <u>1. Probabilità</u>

# 1.1. Probabilità

## Definizioni

> **Esperimento aleatorio / casuale**: *Una qualunque azione il cui risultato non è certo*

> **Evento elementare / Esito**: *Il risultato più semplice di un esperimento casuale, incompatibile a due a due*

> **Spazio campionario / Spazio degli esiti / Universo / Popolazione**: *l'insieme di tutti i possibili esiti, indicato con $\cal S$ o $\Omega$*

> **Evento**: *un insieme di eventi elementari, cioè un qualunque sottoinsieme dello spazio campionario*

>  **Catalogo di sottoinsiemi di $\cal S$ / Lista / Agebra**: *insieme indicato con $\cal F$, i cui elementi sono sottoinsiemi di $\cal S$, tale che:*
>
> 1. $A \in {\cal F} → A^{\cal c} \in {\cal F}$
>
> 2. $\empty \in \cal F$  e  $\cal S \in F$
>
> 3. $\bigcup_{i=1}^n A_i \in \cal F$



## Probabilità

> **Probabilità**: *una funzione che assegna ad ogni elemento di $\cal F$ un numero reale appartenente all'intervallo chiuso $[0,1]$*

$$
\begin {align*}
P \ : \ & {\cal F} → [0,1] \\
        & A → \Pr(A) \\
        & {\cal D = F, \ \ C } = [0,1]
\end {align*}
$$



- **Approccio classico**: il numero di elementi di $\cal S$ è finito o è un'infinità numerabile

$$
\Pr(A) = \frac {\# \text{di eventi elementari che portano alla realizzazione di }A}{\# \text{totale di eventi elementari}}
$$

- **Approccio frequentista**: si assume di ripetere l'esperimento un numero infinito di volte

$$
\Pr(A) = \frac {\# \text{di esperimenti in cui }A \text{ si è verificato}}{\# \text{totale degli esperimenti svolti}}
$$

- **Approccio soggettivista**: la valutazione che il singolo individuo può coerentemente formulare, in base alle proprie conoscenze, del grado di avverabilità dell’evento



### Assiomi della probabilità di Kolmogorov

> **Assiomi**:
>
> 1. $\Pr(A) \geq 0$
> 2. $\Pr({\cal S}) = 1$
> 3. $A \cap B = \empty \ → \ \Pr(A \cup B) = \Pr(A) + \Pr(B)$

Conseguenze:

1. $\Pr(\empty) = 0$
2. $\Pr(A) \leq 1$
3. $\Pr(A^{\cal c}) = 1 - \Pr(A)$
4. $A \subseteq B \ → \ \Pr(A) \leq \Pr(B)$
5. $\Pr(A \cup B) = \Pr(A) + \Pr(B) - \Pr(A \cap B)$



### Probabilità condizionata

> **Probabilità condizionata**: *probabilità di un evento $A$ sapendo che si è già realizzato un altro evento $B$*

Si ha un nuovo spazio campionario ${\cal S^*} = B$ e occorre considerare gli eventi comuni ad $A$ e $B$

$$
\Pr(A|B) = \frac{\Pr(A \cap B)}{\Pr(B)} \ \ \ \ \text{ se } \Pr(B) \neq 0
$$

#### Teorema delle probabilità composte

$$
\Pr(A \cap B) = \Pr(A|B) \cdot \Pr(B) = \Pr(B|A) \cdot \Pr(A) \\
$$

#### Legge delle probabilità totali

$$
\bigcup_{i=1}^n A_i = {\cal S} \and A_i \cap A_j = \empty \ → \ \Pr(B) = \sum_{i=1}^n \Pr(B|A_i) \cdot \Pr(A_i)
$$

#### Formule di Bayes

$$
\Pr(A|B) = \frac {\Pr(B|A) \cdot \Pr(A)}{\Pr(B)}
$$

$$
\Pr(B|A) = \frac {\Pr(A|B) \cdot \Pr(B)}{\Pr(A)}
$$

#### Teorema di Bayes

> **Proposizione**:
> $$
> B \in {\cal F} \and \bigcup_{i=1}^n A_i = {\cal F} \and A_i \cap A_j = \empty \ → \\
> → \ \Pr(A_i|B) = \frac {\Pr(B|A_i) \cdot \Pr(A_i)}{\sum_{j=1}^n \Pr(B|A_j) \cdot \Pr(A_j)}
> $$

#### Indipendenza stocastica

> Due eventi sono **stocasticamente indipendenti** se e solo se il conosce uno non altera la probabilità dell'altro
> $$
> \Pr(A \cap B) = \Pr(A) \cdot \Pr(B) \ → \ \Pr(A|B) = \Pr(A) \ \and \ \Pr(B|A) = \Pr(B)
> $$



## Calcolo combinatorio

| $n = \text{numero di oggetti}\\ k = \text{numero di posti}$ |          Senza ripetizione di oggetti           |     Con ripetizione $r$ di oggetti      |
| :---------------------------------------------------------- | :---------------------------------------------: | :-------------------------------------: |
| **Permutazioni**<br>conta l'ordine<br>$n = k$               |                   $P_n = n!$                    |  $P_n^r = \frac {n!}{r_1!r_2!...r_k!}$  |
| **Disposizioni**<br>conta l'ordine<br>$n \ne k$             |          $D_{n,k} = \frac{n!}{(n-k)!}$          |            $D_{n,k}^r = n^k$            |
| **Combinazioni**<br>non conta l'ordine<br>$n \ne k$         | $C_{n,k} = \frac{n!}{k!(n-k)!} = {n \choose k}$ | $C_{n,k}^r = \frac{(n+k-1)!}{k!(n-1)!}$ |



# 1.2. Variabili casuali

Definire una variabile $Y$ che associ evento $s \in \cal S$, quando lo spazio campionario non è un insieme di numeri

> **Variabile casuale**: *una v.c. $Y$ in uno spazio campionario $\cal S$ è una qualunque funzione definita in $\cal S$ e con valori nell'insieme dei numeri reali;* $Y$ associa dunque ogni evento $s \in \cal S$ a un numero reale
> $$
> Y \ : \ {\cal S} → \R
> $$

A diversi elementi di $\cal S$ può corrispondere lo stesso numero $a$, per cui la probabilità che $Y$ sia uguale ad $a$ è definita come la probabilità dell'unione di tutti gli eventi elementari che la funzione $Y$ associa al valore $a$ :
$$
\Pr(Y=a) = \Pr(\{s \in {\cal S} : Y(s) = a\})
$$

$$
a < b \ → \ \Pr(a<Y \leq b) = \Pr(\{s \in {\cal S} : a < Y(s) \leq b\})
$$



## Variabili casuali discrete

> **Supporto**: *l'insieme dei valori (finito o infinito numerabile) che $Y$ può assumere*
> $$
> Y({\cal S}) = \{y_1,y_2,...,y_k\}
> $$

> **Funzione di probabilità**: *funzione $p(\cdot)$ in $Y({\cal S})$ che associa ad ogni evento $y_i$ la sua probabilità $p(y_i)$*
> $$
> p(y_i) := \Pr(Y=y_i) = \Pr(\{s \in {\cal S} : Y(s) = y_i\}) \\
> p \ : \ Y → [0,1]
> $$
>

La funzione di probabilità ha le seguenti proprietà:
 1. $0 \leq p(y_i) \leq 1$
 2. $\sum_{i=1}^k p(y_i) = 1$



### Funzione di ripartizione

> **Funzione di ripartizione**:
> $$
> F(y) = \Pr(Y \le y) = \sum_{y_i \le y} p(y_i)
> $$
> Tale che
>
> 1. $a \le b \ → \ F(a) \le F(b)$
> 2. $y < \text{min}(y_i) \ → \ F(y)=0$  e  $y \ge \text{max}(y_i) \ → \ F(y)=1$
> 3. $\lim\limits_{y → y_0^+} F(y) = F(y_0)$

$$
\Pr(a < Y \le b) = F(b) - F(a)
$$

Se la v.c. è **discreta** la CDF presenta delle discontinuità nei punti $y : \Pr(Y=y) > 0$
$$
p(y_0) = \Pr(Y = y_0) = \Pr(y_0 \le Y \le y_0) = F(y_0) - F(y_0^-)
$$



### Valore atteso e varianza

> **Valore atteso**: *media pesata dei valori di $Y(\cal S)$ con pesi $p(y_i)$*
> $$
> \mu = \mathbb{E}(Y) = \sum_{i=1}^k y_i p(y_i)
> $$
> In generale
> $$
> \mathbb{E}(h(Y)) = \sum_{i=1}^k h(y_i) p(y_i)
> $$

$$
\mathbb{E}(a + bY) = a + b\mathbb{E}(Y) \\
\text{dove } a \text{ e } b \text{ sono due costanti}
$$

> **Momento di ordine $r$**:			$\mu_r=\mathbb E(X^r)=\sum_{i=1}^m x_i^rp_i$
>
> **M. centrato di ordine $r$**:		$m_r=\mathbb E((X-\mathbb E(X))^r)=\sum_{i=1}^m (x_i-\mu)^rp_i$

> **Varianza**:
> $$
> \sigma^2 = \text{Var}(Y) = \sum_{i=1}^k (y_i - \mu)^2 p(y_i) = \mathbb{E}((Y - \mu)^2)
> $$

$$
\text{Var}(Y) = \mathbb{E}(Y^2) - (\mathbb{E}(Y))^2
$$

$$
\text{Var}(a + bY) = b^2 \text{Var}(Y)
$$

#### Trasformazione di una v.c.

$X = h(Y)$  è a sua volta una v.c.
$$
\omega \xrightarrow{\ \ Y \ \ } Y(\omega) \xrightarrow{\ \ h \ \ } h(Y(\omega))
$$

$$
\omega \xrightarrow{\ \ X = h \circ Y \ \ } X(\omega)
$$

$$
p_X(x) = \Pr(X = x) = \Pr(Y \in \{y : h(y) = x\})
$$



## Distribuzioni di probabilità

### Distribuzione binomiale

> Un esperimento elementare con **due possibili risultati**, detti successo $s$ e insuccesso (fallimento) $f$ viene **ripetuto indipendentemente $m$ volte** e ci chiediamo qual è la **probabilità di ottenere $k$ successi** sapendo che  ogni prova ha **probabilità di successo $p$**

Lo **spazio campionario** $\cal S$ è l'insieme delle $2^m$ sequenze $q \in \cal S$ di $f$ e $s$ di lunghezza $n$

Una **variabile casuale** $B$ è definita come:
$$
B(q) = \#\text{di } s \text{ nella sequenza}
$$

$$
B({\cal S}) = \{0,1,...,m\}
$$

Definiamo l'**evento** $A \sub \cal S$ costituito da tutte le sequenze con $k$ lettere $s$ e $m-k$ lettere $f$:
$$
\#A = {m \choose k} = \frac{m!}{k!(m-k)!}
$$

$$
\Pr(A) = p^k (1-p)^{m-k}
$$

La **probabilità** cercata è dunque:

> $$
> \text{Bin}(k;m,p) := \Pr(B = k) = {m \choose k} p^k (1-p)^{m-k}
> $$
>
> ​														 `dbinom(k,m,p)`

Se $B$ si **distribuisce in accordo** alla distribuzione binomiale, allora
$$
B \sim {\cal B}(m,p)
$$

$$
\mathbb{E}(B) = mp, \ \ \ \text{Var}(B) = mp(1-p)
$$



### Distribuzione di Pascal

> **Binomiale negativa**: probabilità di avere $k$ successi con probabilità $p$ in $m$ prove, tali che il $k$-esimo successo si verifichi **esattamente alla posizione $m$**
> $$
> \text{NBin}(k;m,p) := {m-1 \choose k-1} p^k (1-p)^{m-k}
> $$
>
> ​												 		`dnbinom(m-k,k,p)`

$$
\mathbb{E}(B) = \frac kp, \ \ \ \text{Var}(B) = \frac {k(1-p)}{p^2}
$$



### Distribuzione di Bernoulli

> Caso particolare di distribuzione binomiale in cui $\boldsymbol {m=1}$, perciò la v.c. bernoulliana può assumere **solo due valori** $0$ e $1$ con probailità $p$ e $1-p$

$$
B \sim {\rm Ber}(p) = {\cal B}(1,p)
$$

$$
\mathbb{E}(B) = p, \ \ \ \text{Var}(B) = p(1-p)
$$

La somma di $m$ v.c. indipendenti $B_i \sim {\rm Ber}(p)$ è una v.c. binomiale
$$
B = \sum_{i=1}^m B_i \sim \cal B(m,p)
$$



### Distribuzione di Poisson

> Descrive la distribuzione di una v.c. $P$, la cui probabilità $\theta_m$ decresce in modo che il prodotto $m\theta_m$ **tenda ad una costante** $\lambda$ quando il numero di prove $m$ **tende all'infinito**, cioè  $\lim_{m\to \infin} \theta_m = \lim_{m\to \infin} \lambda/m$
> $$
> {\rm Pois}(k;\lambda) := \Pr(P=k) = \frac{\lambda^k e^{-\lambda}}{k!}
> $$
> ​	  											 		`dpois(k,lamda)`

Il parametro $\lambda$ determina i **momenti ** della distribuzione
$$
B\sim {\cal P}(\lambda)
$$

$$
\mathbb{E}(B) = \lambda, \ \ \ \text{Var}(B) = \lambda
$$

La funzione può essere calcolata **ricorsivamente**
$$
\Pr(P=k)=\frac{\lambda}{k}\Pr(P=k-1)
$$

**Somma** di poissoniane
$$
Z=X+Y \ \ → \ \ Z\sim{\cal P}(λ_X+λ_Y)
$$



## Variabili casuali continue

Consideriamo uno spazio campionario $\cal S$ **infinito** e $Y(\cal S)$ un **continuo di numeri** (un insieme non numerabile)

Essendo un continuo è quasi certi che

- Non si avranno due dati uguali
- Prendendo un qualsiasi numero nell'intervallo, questo numero
  - non corrisponde a un dato
  - è vicino a un dato

Dunque si può affermare che ogni numero di questo intervallo è un **dato**, cioè corrisponde a un campione

$Y(\cal S)$ è dunque una **variabile casuale continua**

Nella pratica potremmo avere un numero **limitato** di dati fra gli infiniti dati possibili



### Funzione di densità

> **Funzione di densità**: *funzione $f(y)$ che associa ad ogni classe (in un numero tendente a infinito) la sua sua frequenza relativa*

La $f(y)$ ha le seguenti **proprietà**:

- $0 \le f(y) \le 1,\ \ \forall y \in \R$
- $\int_{-\infin}^{+\infin}f(t)dt=1$

Permette di rendere l'intervallo $Y(\cal S)$ uno **spazio di probabilità** tale che:

- $\Pr(Y=y_0)=0, \ \ \forall a \in \R$
- $\Pr(a<Y\le b) = \int_a^bf(t)dt$



### Funzione di ripartizione

> **Funzione di ripartizione** per una v.c. continua
> $$
> F(y)=\Pr(Y\le y)=\int_{-\infin}^y f(t)dt
> $$

$$
\Pr(a<Y\le b)=F(b)-F(a)=\int_{-\infin}^b f(t)dt - \int_{-\infin}^a f(t)dt = \int_a^b f(t)dt
$$

$$
\Pr(Y=y_0)=0, \ \ \forall y_0 \in \R \ → \\
\Pr(a < Y \le b) = \ \Pr(a \le Y < b) = \ \Pr(a < Y < b) = \ \Pr(a \le Y \le b)
$$

Se la CDF è derivabile, la **funzione di densità** può essere calcolata derivandola
$$
f(y)=\frac{dF(y)}{dy}
$$


#### Uniforme

$$
f(n) =
\begin{cases}
  1,  & 0<y<1 \\
  0,  & \text{altrimenti}
\end{cases}
$$


$$
F(y)=\int_{-\infin}^yf(t)dt=
\begin{cases}
  0, & y \le 0 \\
  y, & 0<y<1 \\
  1, & y\ge1
\end{cases}
$$

#### Lineare
$$
f(n) =
\begin{cases}
  y/2,  & 0<y<2 \\
  0,  & \text{altrimenti}
\end{cases}
$$

$$
F(y)=\int_{-\infin}^yf(t)dt=
\begin{cases}
  0, & y \le 0 \\
  y^2/4, & 0<y<2 \\
  1, & y\ge2
\end{cases}
$$

#### Esponenziale

$$
f(n) =
\begin{cases}
  e^{-y},  & y>0 \\
  0,  & \text{altrimenti}
\end{cases}
$$

$$
F(y)=\int_{-\infin}^yf(t)dt=
\begin{cases}
  0, & y \le 0 \\
  1-e^{-y}, & y>0
\end{cases}
$$



### Valore atteso e varianza

Analoghi al caso discreto ma con gli integrali, ammesso che esistano
$$
\mu = \mathbb{E}(Y) = \int_{-\infin}^{+\infin} yf(y)dy \\
\mathbb{E}(h(Y)) = \int_{-\infin}^{+\infin} h(y)f(y)dy
$$

$$
\begin{align}
\sigma^2 = {\rm Var}(Y)
  & = \int_{-\infin}^{+\infin} (y-\mu^2)f(y)dy \\
  & = \mathbb{E}(Y^2) - \mathbb{E}(Y)^2 \\
  & = \int_{-\infin}^{+\infin} y^2f(y)dy-\mu^2
\end{align}
$$



### Distribuzione normale o gaussiana

> **Variabile casuale normale** di valore atteso $\mu$ e varianza $\sigma^2$
> $$
> Y \sim {\cal N}(\mu,\sigma^2)
> $$
>
> $$
> f(y;\mu,\sigma^2) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac12(\frac{y-\mu}{\sigma})^2}
> $$
>
> `dnorm(y,mu,sigma)`!?!?!?!?

**Osservazioni**

- La funzione di densità è **simmetrica** rispetto alla media
- media, moda e mediana **coincidono**

> **Distribuzione normale standard** di valore atteso $0$ e varianza $1$
> $$
> Z \sim {\cal N}(0,1)
> $$
>
> $$
> f(z) = \frac{1}{\sqrt{2\pi}}e^{-\frac12 z^2}
> $$

La **probabilità** della distribuzione standard si calcola mediante tavole che raccolgono le probabilità degli intervalli $-\infin<Z\le z$

I valori $z_p$ relativi alle probabilità $p$ delle tavole sono i **quantili** di ordine $p$ della variabile casuale $Z$
$$
\Pr(Z\le z_p)=p
$$

> **Standardizzazione**: *trasformazione lineare che porta una qualunque v.c. $Y$ alla variabile normale standard*
> $$
> Z= \frac{Y-\mu}{\sigma}
> $$

$$
z_0=\frac{y_0-\mu}{\sigma} \ \ \ \ \ \ \ \ \ \ \Pr(Y\le y_0)=\Pr(Z\le z_0)
$$



### Distribuzione esponenziale o di Laplace

> Descrive la **durata di vita** di un fenomeno che non invecchia, ossia la distribuzione è **priva di memoria**
> $$
> f(y;\lambda) = \lambda e^{-\lambda y} \ \ \ \ \ \ y,\lambda\ge0
> $$
> ​					   									`dexp(x,lambda)`

$$
Y \sim {\cal E}(\lambda)
$$

$$
\mathbb E (Y) = \frac 1\lambda, \ \ \ \text{Var}(Y) = \frac 1{\lambda^2}
$$

$$
F(Y)=1-e^{-\lambda y}
$$

**Minimo** di v.a. esponenziali indipendenti
$$
Z=\min\{Y_1,...,Y_n\} \ → \ \lambda_Z=\lambda_1+...+\lambda_n
$$



# 1.3 Normal Probability Plot

## QQ-plot

> **Statistica ordinata**: *permutazione $y_{(1)},\dots,y_{(n)}$ di $n$ osservazioni $y_1,\dots,y_n$ su di una variabile numerica, tale che*
> $$
> y_{(1)} \le y_{(2)} \le \dots \le y_{(n-1)} \le y_{(n)}
> $$

È l'**insieme dei valori** osservati **ordinati** dal più piccolo al più grande

$y_{(j)}$ è la **stima** del ${\rm quantile-}(j/n)$ della distribuzione che ha generato i dati (nei casi in cui i valori distinti fra le osservazioni non siano troppo pochi)

- Se **solo un'osservazione** è uguale a $y_{(j)}$ allora la percentuale di osservazioni minore o uguale a $y_{(j)}$ è esattamente $100(j/n)$
- Se **poche osservazioni** sono uguali a $y_{(j)}$ allora la percentuale di osservazioni minore o uguale a $y_{(j)}$ non sarà molto differente da $100(j/n)$


$$
\begin{align}
&z_p:&& \text{quantile-}p \text{ di una normale standard} \\
&z_p(\mu,\sigma):&& \text{quantile-}p \text{ di } Y
\end{align}
$$

$$
Y \sim {\cal N}(\mu,\sigma^2) \ \ → \ \ ({\rm quantile-}p\ {\rm di}\ Y)=\mu+\sigma z_p
$$

$$
\Pr(Y\le z_p(\mu,\sigma))=p
$$

$$
\Pr \bigg({\cal N}(0,1)\le \frac{z_p(\mu,\sigma)-\mu}{\sigma}\bigg)=p
$$

$$
\frac{z_p(\mu,\sigma)-\mu}{\sigma} = z_p(0,1) \ \ → \ \ z_p(\mu,\sigma) = \mu + \sigma z_p(0,1)
$$

**Sintesi**

- $y_{(j)}$ lascia a sinistra circa $j$ osservazioni su $n$, quindi dovrebbe essere vicina al quantile $j/n$ della distribuzione
- Se la distribuzione è normale, questo quantile è $\mu+\sigma z_{j/n}$, dove solo $z_{j/n}$ è una quantità nota

Se i dati sono normali, i punti di coordinate $\Big(z_{\frac{j-0,5}{n}},y_{(j)}\Big)$ dovrebbero avere un **andamento lineare**

Il grafico così ottenuto è chiamato **normal probability plot**, che rappresenta i quantili campionari verso i quantili di una distribuzione teorica







# [↑](#↓)

