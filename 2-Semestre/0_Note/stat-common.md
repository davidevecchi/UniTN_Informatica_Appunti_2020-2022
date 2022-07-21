# Statistica

|            |
| ---------- |
| Statistica |



# Probabilità condizionata

> $$
> \Pr(A|B) = \frac{\Pr(A \cap B)}{\Pr(B)} \ \ \ \ \text{ se } \Pr(B) \neq 0
> $$

#### Teorema delle probabilità composte
$$
\Pr(A \cap B) = \Pr(A|B) \cdot \Pr(B) = \Pr(B|A) \cdot \Pr(A) \\
$$

#### Formule di Bayes

> $$
> \Pr(A|B) = \dfrac {\Pr(B|A) \cdot \Pr(A)}{\Pr(B)}
> $$

#### Teorema di Bayes

> $$
> \Pr(A_i|B) = \frac {\Pr(B|A_i) \cdot \Pr(A_i)}{\sum_{j=1}^n \Pr(B|A_j) \cdot \Pr(A_j)}
> $$



# Calcolo combinatorio

| $n = \text{numero di oggetti}\\ k = \text{numero di posti}$ |           Senza ripetizione di oggetti           |      Con ripetizione $r$ di oggetti      |
| :---------------------------------------------------------- | :----------------------------------------------: | :--------------------------------------: |
| **Permutazioni**<br>conta l'ordine<br>$n = k$               |                    $P_n = n!$                    |  $P_n^r = \dfrac {n!}{r_1!r_2!...r_k!}$  |
| **Disposizioni**<br>conta l'ordine<br>$n \ne k$             |          $D_{n,k} = \dfrac{n!}{(n-k)!}$          |            $D_{n,k}^r = n^k$             |
| **Combinazioni**<br>non conta l'ordine<br>$n \ne k$         | $C_{n,k} = \dfrac{n!}{k!(n-k)!} = {n \choose k}$ | $C_{n,k}^r = \dfrac{(n+k-1)!}{k!(n-1)!}$ |



# R

```R
F <- function(x) { y <- 1 / (1 + exp(1.4*x)) }
curve (F, -10, 10)
```

```R
F <- function(x) {
    ifelse (x<0, 0.5*exp(x/1.4), 1-0.5*exp(-x/1.4))
}
curve (F, -10, 10)
```



# Distribuzioni

## Discrete

![image-20200615124044050](/home/zeep/Documenti/UniTN/2-Semestre/0_Note/stat-common.assets/image-20200615124044050.png)

## Continue

![image-20200615124012159](/home/zeep/Documenti/UniTN/2-Semestre/0_Note/stat-common.assets/image-20200615124012159.png)

























# Metodo dei momenti

<img src="https://media.discordapp.net/attachments/699368516595351733/715117470268260372/momenti.png?width=653&amp;height=649" alt="img" style="zoom:150%;" />

![img](https://media.discordapp.net/attachments/699368516595351733/715124333881851924/naturalPenis.png)

<img src="https://media.discordapp.net/attachments/699368516595351733/715124695296507974/unknown.png" alt="img" style="zoom:150%;" />



# Intervalli di confidenza

![confidenza](/home/zeep/Documenti/UniTN/2-Semestre/0_Note/stat-common.assets/confidenza.png)







































# Test statistico

![test](/home/zeep/Documenti/UniTN/2-Semestre/0_Note/stat-common.assets/test-1592217050985.png)

![img](https://media.discordapp.net/attachments/699368516595351733/715133573463801926/unknown.png)

