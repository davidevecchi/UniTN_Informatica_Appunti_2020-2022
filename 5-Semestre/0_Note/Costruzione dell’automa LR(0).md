### Costruzione dell'automa LR(0)

1. Il kernel dello stato $0$ è costituito da $S'→·S$

2. ==Le reduce nella tabella sono 4, quindi $\cal G$ avrà 4 produzioni==

3. Si osservi lo stato $0$

   - Presenta mosse di shift verso gli stati $3=τ(0,b)$ e $4=τ(0,a)$
     - ==Quindi conterrà due items aventi componente LR(0) in forma $B→·bα$ e $B→·aα$==
   - Presenta mosse di goto verso gli stati $1=τ(0,S)$ e $2=τ(0,A)$
     - ==Quindi conterrà due items aventi componente LR(0) in forma $B→·Sα$ e $B→·Aα$==
     - $B→·Sα$ deve essere distinto da $S'→·S$, poiché lo stato $1$ non presenta soltanto $Acc$ fra i suoi items

   $$
   \begin{align}
   B&→aα\\
   B&→bα\\
   B&→Sα\\
   B&→Aα\\
   \end{align}
   $$

   

4. Si osservino gli stati $3=τ([0-2,5-7],\ b)$ e $4=τ([0-2,5-7],\ a)$

   - <u>Osservazione 1</u>
     - Sono **target degli shift** di ogni stato, ad eccezioni di loro stessi
     - Possiedono **soltanto reduce** nelle loro entries
     - Quindi avranno kernel con items rispettivamente in forma $B→αb·$ e $B→αa·$
     - Quindi deriveranno da items nelle forme $B→α·b$ e $B→α·a$
     - ==Quindi tutte le produzioni della grammatica avranno $a$ e $b$ soltanto in ultima posizione==
   - <u>Osservazione 2</u>
     - Hanno reduce con lookahead-set $a$ e $b$
     - Per avere lookahead-set diverso da $\$$, è necessario che esista un cammino che porti ad essi passante da uno stato avente un LR(0)-item nella forma $B→CΧα$
       - $X$ deve essere un simbolo del vocabolario di $\cal G$, tale per cui $\set{a,b}⊆{\rm first}(X)$
       - In questo modo i reducing items di $3$ e $4$ comprendono i terminali $a$ e $b$

5. ==Dalle considerazioni (3) e (4) si deduce che $0$ conterrà due items aventi componente LR(0) in forma $B→·b$ e $B→·a$==
   $$
   \begin{align}
   B&→a\\
   B&→b\\
   B&→Sα\\
   B&→Aα\\
   \end{align}
   $$
   
6. 

7. Osservare lo stato $3$

   - È raggiungibile solo tramite $b$-transizioni
   - Ha una reduce con accepting item $\$$ (al contrario dello stato $4$)
   - Quindi dal punto (5) si deduce che 





