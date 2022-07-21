# <u>ASD</u> - Strutture di dati (print)

|      |                            |      |
| ---- | -------------------------- | ---- |
| ASD  | Strutture di dati  (print) |      |

[TOC]



# [1.][pdf-1] Pile e code

```c++
struct Stack
    // Costruisce una pila vuota
    Stack()
    // Restituisce true se la pila è vuota
    bool isEmpty()
    // Inserisce v in cima alla pila
    bool push(Item v)
    // Estrae l'elemento in cima e lo restituisce al chiamante
    Item pop()
    // Legge l'elemento in cima alla pila
    Item top()
```

```c++
struct Queue
    // Costruisce una coda vuota
    Queue()
    // Restituisce true se la coda è vuota
    bool isEmpty()
    // Inserisce v in fondo alla coda
    bool enqueue(Item v)
    // Estrae l'elemento in testa e lo restituisce al chiamante
    Item dequeue()
    // Legge l'elemento in testa alla coda
    Item top()
```

# [2.][pdf-2] Alberi

### Terminologia

> **Profondità**: *lunghezza del cammino semplice dalla radice a un nodo*

> **Livello**: *insieme di nodi alla stessa profondità*

> **Altezza**: *profondità massima della sue foglie*

## Alberi binari

### Specifica

```c++
struct Tree:
    // Padre del nodo (nil se radice)
    Tree parent
    // Figlio sx/dx del nodo (nil se assente)
    Tree left
    Tree right
        
    // Costruisce un nuovo nodo contenente v senza figli o genitori
    Tree(Item v)
    // Legge il valore memorizzato nel nodo
    Item read()
    // Modifica il valore memorizzato nel nodo
    void write(Item v)
    // Inserisce il sottoalbero radicato in t come figlio sx/dx
    void insertLeft(Tree t)
    void insertRight(Tree t)
    // Distrugge (ricorsivamente) il figlio sx/dx di questo nodo
    void deleteLeft()
    void deleteRight()
```

### Visita DFS

```c++
void dfs(Tree t) {
    if (t != null) {
        { print(t) }     // pre-order
        dfs(t.left())
        { print(t) }     // in-order
        dfs(t.right())
        { print(t) }     // post-order
    }
}
```

### Alberi strutturalmente diversi

Il numero di alberi strutturalmente diversi aventi $n$ nodi è dato dalla funzione
$$
P(n)=
\begin{cases}
1 & n\le 1 \\
\sum_{k=0}^{n-1}P(k)·P(n-1-k) & n>1
\end{cases}
$$

## Alberi generici

### Specifica

```c++
struct Tree
    // Costruisce un nuovo nodo contenente v senza figli o genitori
    Tree(Item v)
    // Legge il valore memorizzato nel nodo
    Item read()
    // Modifica il valore memorizzato nel nodo
    void write(Item v)
    // Restituisce il padre, oppure nil se questo nodo è radice
    Tree parent()
    // Restituisce il primo figlio, oppure nil se è una foglia
    Tree leftmostChild()
    // Restituisce il prossimo fratello, oppure nil se assente
    Tree rightSibling()
    // Inserisce il sottoalbero t come primo nodo di questo nodo
    void insertChild(Tree t)
    // Inserisce il sottoalbero t come prossimo fratello
    void insertSibling(Tree t)
    // Distrugge albero radicato identificato dal primo figlio
    void deleteChild()
    // Distrugge albero radicato identificato dal prossimo fratello
    void deleteSibling()
```

### Visite

```c++
void dfs(Tree t){
    if (t != null) {
        { print(t) }    // pre-order
        Tree u = t.leftmostChild()
		while (u != null) {
			dfs(u)
			u = u.rightSibling()
        }
        { print(t) }    // post-order
    }
}
```

```c++
void bfs(Tree t){
    Queue Q = Queue()
    Q.enqueue(t)
    while (!Q.isEmpty()) {
        Tree u = Q.dequeue())
        print(u)
        u = u.leftmostChild()
        while (u != null) {
            Q.enqueue(u)
            u = u.rightSibling()
        }
    }    
}
```

# [3.][pdf-3] Alberi binari di ricerca

### Specifica

```c++
struct Tree:
    // Nodi
    Tree parent
    Tree left
    Tree right
    // Contenuto
    Item key
    Item value
```

```c++
struct Dictionary:
    Tree tree
    Dictionary() { tree = null }
    // Operazioni dizionario
    Item lookup(Item k)
    void insert(Item k, Item v)
    void remove(Item k)
    // Ordinamento
    Tree successorNode(Tree T)
    Tree predecessorNode(Tree T)
    Tree min(Tree T)
    Tree max(Tree T)
private:
    Tree lookupNode(Tree T, Item k)
    Tree insertNode(Tree T, Item k, Item v)
    Tree removeNode(Tree T, Item k)
    void link(Tree p, Tree u, Item k)
```

## Operazioni

### Ricerca

```c++
// Dictionary
Item lookup(Item k) {
    Tree T = lookupNode(tree, k)
    if (T != null)
    	return T.value()
    else
    	return null
}
```

```c++
// Ricerca iterativa
Tree lookupNode(Tree T, Item k) {
    Tree u = T
    while (u != null && u.key != k) {
        if (k < u.key)
        	u = u.left
        else
        	u = u.right
    }
    return u
}
```

```c++
// Ricerca ricorsiva
Tree lookupNode(Tree T, Item k) {
    if (T == null || T.key == k)
    	return T
    else
    	return lookupNode((k < T.key ? T.left : T.right), k)
}
```

### Minimo / Massimo

```c++
// Minimo
Tree min(Tree T) {
    if (T.left != null)
        return min(T.left)
    else
        return T
}
```

- Massimo: `min→max`, `left→right`

### Successore / Predecessore

> <u>Definizione</u>  ($\tt Tree\ successorNode(Tree\ T)$)
>
> Il **successore** di un nodo $u$ è il **più piccolo nodo maggiore** di $u$
>
> Restituisce
>
> - Il **minimo** del sottoalbero **destro** di $u$, se presente
>   - Il successore non ha figlio sinistro
> - Il **primo avo** $v$ tale per cui $u$ sta nel sottoalbero **sinistro** di $v$, altrimenti

```c++
// Successore
Tree successorNode(Tree T) {
    if (T == null)
        return T
    if (T.right != null)
        return min(T.right)
    Tree t = T
    Tree p = t.parent
    while (p != null && t == p.right) {
        t = p
        p = p.parent
    }
    return p
}
```

- Predecessore (simmetrico): `min→max`, `right→left`

### Inserimento

> <u>Procedura</u>  ($\tt Tree\ insertNode(Tree\ T,\ Item\ k,\ Item\ v)$)
>
> Inserisce un’**associazione chiave-valore** $(k, v)$ nell’albero $T$
>
> - Se $T \tt == nil$, restituisce il **primo nodo** dell’albero
> - Altrimenti, restituisce la **radice** di $T$ inalterata
>   - Se la chiave è già presente, **sostituisce il valore** associato
>   - Altrimenti, viene inserita una **nuova associazione**

```c++
// Dictionary
void insert(Item k, Item v) {
    tree = insertNode(tree, k, v)
}
```

```c++
// Inserimento
Tree insertNode(Tree T, Item k, Item v) {
    Tree p = null  // padre
    Tree u = T
    while (u != null && u.key != k) {  // cerca posizione
        p = u
        u = (k < u.key ? u.left : u.right)
    }
    if (u != nil && u.key == k) {
    	u.value = v                   // sostituisci valore
    } else {
    	Tree newT = Tree(k, v)        // crea nodo coppia (k,v)
        link(p, newT, k)
        if (p == null)
        	T = newT           // primo nodo ad essere inserito
    }
    return T                    // T non modificato o nuovo nodo
}
```

```c++
// Collegamento
void link(Tree p, Tree u, Item k) {
    if (u != null) then
    	u.parent = p      // collega padre
    if (p != null) {
    	if (k < p.key)
            p.left = u    // attacca come figlio sinistro
    	else
            p.right = u   // attacca come figlio destro
    }
}
```

### Cancellazione

```c++
// Dictionary
void remove(Item k, Item v) {
    tree = removeNode(tree, k)
}
```

```c++
// Rimozione
Tree removeNode(Tree T, Item k) {
    Tree u = lookupNode(T, k)
    if (u != null) {	
    	if (u.left == null && u.right == null) {  // caso 1
            link(u.parent, nil, k)
            delete u	
        } else if (u.left == null) {			  // caso 2
            link(u.parent, u.right, k)
            if (u.parent = null)
				T = u.right     	
        } else if (u.right == null) {	
            link(u.parent, u.left, k)
            if (u.parent = null)
				T = u.left
        } else {	     						  // caso 3
            Tree s = successorNode(u)
            link(s.parent, s.right, s.key)
            u.key = s.key
        	u.value = s.value
            delete s
        }
    }
    return T
}
```

# [4.][pdf-4] Grafi

## Introduzione

### Dimensioni

<u>Definizioni</u>

- $n\ \, :=\, |V |$    numero di nodi
- $m\, :=\, |E|$    numero di archi

<u>Relazioni</u>

- Non orientato:  $m ≤ \dfrac{n^2-n}{2} = O(n^2)$
- Orientato:         $\,m ≤\,  n^2 − n\: = O(n^2)$

<u>Complessità degli algoritmi</u>

- Espressa in termini di $n$ e di $m$

### Memorizzazione

$$
\begin{array}{l}
\bold {Matrice\ di\ adiacenza} \\[4pt]
\begin{array}{l}
m_{uv}=\begin{cases}
1 & (u,v)\in E \\
0 & (u,v)\notin E
\end{cases}
\\[2pt]
m_{uv}=\begin{cases}
w(u,v) & (u,v)\in E \\
ω & (u,v)\notin E
\end{cases}
\end{array}
&
{\rm Mem}=\begin{cases}
n^2\ \rm bit & \rm indiretto \\
n(n − 1)/2\ \rm bit & \rm diretto
\end{cases}

\\[10pt]

\bold {Lista/Vettore\ di\ adiacenza} \\[4pt]
\begin{array}{l}
G.{\rm adj} (u) = \{v\ |\ (u, v) ∈ E\}
\\[4pt]
G.{\rm adj} (u) = \{(v,w(u,v)) | (u, v) ∈ E\}
\end{array}
&
{{\rm Mem}=\begin{cases}
an+bm\ \ \,\ \rm bit & \rm indiretto \\
an+2\,bm\ \rm bit & \rm diretto
\end{cases}}
\end{array}
$$

|      |                     |   Matrici   |      | Liste / Vettori |      |      |
| ---- | ------------------- | :---------: | ---- | :-------------: | ---- | ---- |
|      | Spazio richiesto    |  $O(n^2)$   |      |   $O(n + m)$    |      |      |
|      | Verifica adiacenza  |   $O(1)$    |      |     $O(n)$      |      |      |
|      | Iterare sugli archi |  $O(n^2)$   |      |   $O(n + m)$    |      |      |
|      | Ideale per          | Grafi densi |      |  Grafi sparsi   |      |      |

### Specifica

```c++
struct Graph
	// Crea un nuovo grafo
    Graph()
    // Restituisce l'insieme di tutti i nodi
    Set V()
    // Restituisce il numero di nodi
    int size()
    // Restituisce l'insieme dei nodi adiacenti a u
    Set adj(Node u)
    // Aggiunge il nodo u al grafo
    void insertNode(Node u)
    // Aggiunge l'arco (u, v) al grafo
    void insertEdge(Node u, Node v)
    // Rimuove il nodo u dal grafo
    void deleteNode(Node u)
    // Rimuove l'arco (u, v) dal grafo
    void deleteEdge(Node u, Node v)
```

### Visite

```pseudocode
/* Algoritmo generico di attraversamento */
void graphTraversal(Graph G, Node r)
    Set S = Set()  /* insieme generico (modificabile ad hoc) */
    S.insert(r)
    { /* marca il nodo r */ }
    while S.size() > 0 do
        Node u = S.remove()  /* politica dipende dal problema */
        { /* visita il nodo u */ }
        foreach v ∈ G.adj(u) do
            { /* visita l'arco (u, v) */ }
            if not marked(v) then
                { /* marca il nodo v */ }
                S.insert(v)
```

## BFS

### Implementazione

```pseudocode
void bfs(Graph G, Node r)  /* basato su graphTraversal */
    Queue Q = Queue()
    S.enqueue(r)
    bool[] visited = new bool[G.size()]
    foreach u ∈ G.V() - {r} do
    	visited[u] = false
    visited[r] = true
    while not Q.isEmpty() do
        Node u = Q.dequeue()
        { /* visita il nodo u */ }
        foreach v ∈ G.adj(u) do
            { /* visita l'arco (u, v) */ }
            if not visited[v] then
                visited[v] = true
                Q.enqueue(v)
```

### Cammini più brevi

```pseudocode
void distance(Graph G, Node r, int[] distance)
    Queue Q = Queue()
    Q.enqueue(r)
    foreach u ∈ G.V() - {r} do
    	distance[u] = ∞
    distance[r] = 0
    while not Q.isEmpty() do
        Node u = Q.dequeue()
        foreach v ∈ G.adj(u) do
            if distance[v] == ∞ then
                distance[v] = distance[u] + 1
                Q. enqueue (v)
```

### Albero BFS

- Restituisce il **cammino più breve** fra due nodi
- **Albero di copertura** con radice $r$
- Memorizzato in un **vettore dei padri** $\tt parent$

```pseudocode
void distance([...], Node[] parent)
    [...]
    parent[r] = nil
    while not S.isEmpty() do
        Node u = S.dequeue()
        foreach v ∈ G.adj(u) do
            if distance[v] == ∞ then
                distance[v] = distance[u] + 1
                parent[v] = u   /* memorizza il padre */
                S.enqueue(v)
```

```pseudocode
void printPath(Node r, Node s, Node[] parent)
    if r == s then
    	print(s)
    else if parent[s] == nil then
    	print("error")
    else
    	printPath(r, parent[s], parent)
    	print(s)
```

### Complessità

<u>Complessità</u>:  $O(m + n)$

- Il numero di archi analizzati è
  $$
  m=\sum_{u\in V}d_{\rm out}(u)
  $$


## DFS

### Implementazione

```pseudocode
/* Ricorsiva, stack implicito */
void dfs(Graph G, Node u, boolean[] visited)
    visited[u] = true
    { /* visita il nodo u (pre-order) */ }
    foreach v ∈ G.adj(u) do
        if not visited[v] then
            { /* visita l'arco (u, v) */ }
            dfs(G, v, visited)
    { /* visita il nodo u (post-order) */ }
```

```pseudocode
/* Iterativa, stack esplicito, pre-order */
void dfs(Graph G, Node r)
    Stack S = Stack()
    S.push(r)
    boolean[] visited = new boolean[G.size()]
    foreach u ∈ G.V() do
    	visited[u] = false
    while not S.isEmpty() do
        Node u = S.pop()
        if not visited[u] then
            { /* visita il nodo u (pre-order) */ }
            visited[v] = true
            foreach v ∈ G.adj(u) do
                { /* visita l'arco (u, v) */ }
                S.push(v)
```

- <u>Complessità</u>:  $O(m + n)$

### Componenti connesse

<u>Procedura</u>

- Un grafo è connesso se, al termine della DFS, tutti i nodi sono **marcati**
- Altrimenti, la visita deve ricominciare da capo da un nodo **non marcato**
  - Viene identificata una **nuova componente** del grafo

<u>Struttura dati</u>

- Un **vettore $\rm id$**, che contiene gli identificatori delle componenti
- ${\rm id}[u]$ è l’**identificatore della cc** a cui appartiene $u$

```pseudocode
int[] cc(Graph G)
    int[] id = new int[G.size()]
    foreach u ∈ G.V() do
    	id[u] = 0
    int counter = 0
    foreach u ∈ G.V() do
        if id[u] == 0 then
            counter = counter + 1
            ccdfs(G, counter, u, id)
	return id

void ccdfs(Graph G, int counter, Node u, int[] id)
    id[u] = counter
    foreach v ∈ G.adj(u) do
        if id[v] == 0 then
        	ccdfs(G, counter, v, id)
```

### Ricerca dei cicli

```pseudocode
/* Grafo non orientato */
bool hasCycle(Graph G)
    bool[] visited = new bool[G.size()]
    foreach u ∈ G.V() do
    	visited [u] = false
    foreach u ∈ G.V() do
        if not visited[u] then
            if hasCycleRec(G, u, nil, visited ) then
            	return true
    return false

bool hasCycleRec(Graph G, Node u, Node p, bool[] visited)
    visited[u] = true
    foreach v ∈ G.adj(u) - {p} do
        if visited[v] then
        	return true
        else if hasCycleRec(G, v, u, visited) then
        	return true
    return false
```

```pseudocode
/* Grafo orientato */
bool hasCycle(Graph G, Node u, int &time, int[] dt, int[] ft)
    time = time + 1
    dt[u] = time
    foreach v ∈ G.adj(u) do
        if dt[v] == 0 then
            if hasCycle(G, v, time, dt, ft) then
                return true
            else if dt[u] > dt[v] and ft[v] == 0 then
                return true  /* arco all'indietro */
    time = time + 1
    ft[u] = time
    return false
```

## DFS - DAG

### Classificazione degli archi

> **Arco dell'albero di copertura DFS**: *arco esaminato da un nodo marcato ad un nodo non marcato*

Gli archi $(u, v)$ **non inclusi** nell’albero possono essere divisi in tre categorie

- Se $u$ è un **antenato** di $v$ in $T$
  - $(u, v)$ è detto arco **in avanti**
- Se $u$ è un **discendente** di $v$ in $T$
  - $(u, v)$ è detto arco **all’indietro**
- **Altrimenti**
  - $(u, v)$ è detto arco di **attraversamento**

### DFS schema

```pseudocode
/* Schema generale
 * time: memorizza la successione delle visite
 * dt:   discovery time
 * ft:   finish time
 */
void dfsSchema(Graph G, Node u, int &time, int[] dt, int[] ft)
    { /* visita il nodo u (pre-order) */ }
    time = time + 1
    dt[u] = time
    foreach v ∈ G.adj(u) do
        { /* visita l'arco (u, v) (qualsiasi) */ }
        if dt[v] == 0 then
            { /* visita l'arco (u, v) (albero) */ }
            dfsSchema(G, v, time, dt, ft)
        else if dt[u] > dt[v] and ft[v] == 0 then
            { /* visita l'arco (u, v) (indietro) */ }
        else if dt[u] < dt[v] and ft[v] != 0 then
            { /* visita l'arco (u, v) (avanti) */ }
        else
        	{ /* visita l'arco (u, v) (attraversamento) */ }
    { /* visita il nodo u (post-order) */ }
    time = time + 1
    ft[u] = time
```

### Teoremi

> <u>Teorema</u>  (**Condizioni DFS**)
>
> Data una visita DFS di un grafo $G = (V, E)$, per ogni coppia di nodi $u, v ∈ V $, solo una delle condizioni seguenti è vera
>
> - Gli intervalli $[{\rm dt}[u], {\rm ft}[u]]$ e $[{\rm dt}[v], {\rm ft}[v]]$ sono non-sovrapposti
>   - $u, v$ non sono discendenti l’uno dell’altro nella foresta DF
> - L’intervallo $[{\rm dt}[u], {\rm ft}[u]]$ è contenuto in $[{\rm dt}[v], {\rm ft}[v]]$
>   - $u$ è un discendente di $v$ in un albero DF​
> - L’intervallo $[{\rm dt}[v], {\rm ft}[v]]$ è contenuto in $[{\rm dt}[u], {\rm ft}[u]]$
>   - $v$ è un discendente di $u$ in un albero DF

> <u>Teorema</u>  (**Grafo orientato aciclico**)
>
> Un grafo orientato è aciclico se e solo se non presenta archi all’indietro
>
> <u>Dimostrazione</u>
>
> - **se**: se esiste un ciclo, sia $u$ il suo primo nodo visitato e $(v, u)$ un suo arco
>   - Allora il cammino che connette $u$ a $v$ verrà prima o poi visitato, e da $v$ verrà scoperto l’arco all’indietro $(v, u)$
> - **solo se**: se esiste un arco all’indietro $(u, v)$, dove $v$ è un antenato di $u$
>   -  Allora esiste un cammino da $v$ a $u$ e un arco $u,v$, ovvero un ciclo

### Ordinamento topologico

> <u>Definizione</u>  (**Ordinamento topologico**)
>
> Ordinamento lineare dei nodi di un DAG $G$, tale per cui
> $$
> (u,v)\in E\ \Rarr\ u<v
> $$

- Esistono **più ordinamenti** topologici
- Se il grafo contiene un **ciclo**, **non esiste** un ordinamento topologico

<u>Problema</u>

- Scrivere un algoritmo che
  - Prenda in input un DAG
  - Ritorni un ordinamento topologico per esso

> <u>Algoritmo</u>  (**TopSort basato su DFS**)
>
> 1. DFS in cui la visita aggiunge, post-ordine, il nodo in testa ad una lista
> 2. Restituzione della lista così ottenuta
>
> <u>Output</u>
>
> - Sequenza dei nodi, ordinati per tempo decrescente di fine
>
> <u>Funzionamento</u>
>
> - Quando un nodo è finito
>   - Tutti i suoi discendenti sono stati scoperti e aggiunti alla lista
>   - Aggiungendolo in testa alla lista, il nodo è in ordine corretto

```pseudocode
Stack topSort(Graph G)
    Stack S = Stack()
    bool[] visited = bool[G.size()]
    foreach u ∈ G.V() do
        visited[u] = false
    foreach u ∈ G.V() do
        if not visited[u] then
            dfsTS(G, u, visited, S)
    return S

void dfsTS(Graph G, Node u, boolean[] visited, Stack S)
    visited[u] = true
    foreach v ∈ G.adj(u) do
        if not visited[v] then
            dfsTS(G, v, visited, S)
    S.push(u)
```

- In un grafo ciclico gli archi di un ciclo vengono listati in ordine ininfluente

### Componenti fortemente connesse

<u>Problema</u>

- Scrivere un algoritmo che prenda in input un grafo orientato e ritorni le componenti fortemente connesse di esso

> <u>Algoritmo</u>  (**Kosaraju**)
>
> 1. Visita DFS del grafo $G$
> 2. Calcolo del grafo trasposto $G^T$
> 3. Visita DFS sul grafo $G^T$ utilizzando $\tt cc()$
>    - Esaminare i nodi in ordine inverso di tempo di fine di prima visita
> 4. Le componenti connesse (e i relativi alberi DF) rappresentano le componenti fortemente connesse di $G$

```pseudocode
/* Grafo trasposto */
Graph transpose(Graph G)
    Graph G_T = Graph()
    foreach u ∈ G.V() do
        G_T.insertNode(u)
    foreach u ∈ G.V() do
        foreach v ∈ G.adj(u) do
            G_T.insertEdge(v, u)
    return G_T
```

- <u>Costo computazionale</u>:  $O(m+n)$
  - $O(n)$ nodi aggiunti
  - $O(m)$ archi aggiunti
  - Ogni operazione costa $O(1)$

```pseudocode
/* cc versione LIFO */
void cc(Graph G, Stack S)
    int[] id = new int[G.size()]
    foreach u ∈ G.V() do
        id[u] = 0
    int counter = 0
    while not S.isEmpty() do
        u = S.pop()
        if id[u] == 0 then
            counter = counter + 1
            ccdfs(G, counter, u, id)
    return id

void ccdfs(Graph G, int counter, Node u, int[] id)
    id[u] = counter
    foreach v ∈ G.adj(u) do
        if id[v] == 0 then
            ccdfs(G, counter, v, id)
```

- Versione di $\tt cc()$ che esamina i nodi nell’ordine LIFO nello stack

```pseudocode
int[] scc(Graph G)
    Stack S = topSort(G)  /* First visit      */
    G_T = transpose(G)    /* Graph transposal */
    return cc(G_T, S)     /* Second visit     */
```

- <u>Costo computazionale</u>:  $O(m + n)$
  - Ogni fase richiede $O(m + n)$

### Grafo delle componenti

> <u>Definizione</u>  (**Grafo delle componenti**)
> $$
> C(G) = (V_c , E_c )
> $$
>
> - $V_c = \{C_1 , C_2 , . . . , C_k \}$
>   - $C_i$ è la $i$-esima SCC di $G$
> - $E_c = \{(C_i , C_j )\ |\ ∃\,(u_i , u_j ) ∈ E\ :\ u_i ∈ C_i\ ∧\ u_j ∈ C_j \}$
>
> <u>Proprietà</u>
>
> - $C$ è aciclico
> - $C(G^T) = [C(G)]^T$
> - $\rm dt$ e $\rm ft$ di $C$ corrispondono a quelli del primo nodo visitato in $C$
>   - ${\rm dt}(C) = \min\,\{{\rm dt}(u)\ |\ u ∈ C\}$
>   - ${\rm ft}\,(C) = \max\{{\rm ft}(u)\,\ |\ u ∈ C\}$



[root]: ../Algoritmi/2-Strutture
[pdf-1]: ../Algoritmi/2-Strutture/1-strutture.pdf
[pdf-2]: ../Algoritmi/2-Strutture/2-alberi.pdf
[pdf-3]: ../Algoritmi/2-Strutture/3-abr.pdf
[pdf-3X]: ../Algoritmi/2-Strutture/3X-abr.pdf
[pdf-4]: ../Algoritmi/2-Strutture/4-grafi.pdf
[pdf-4X]: ../Algoritmi/2-Strutture/4X-grafi.pdf
[pdf-5]: ../Algoritmi/2-Strutture/5-hashing.pdf
[pdf-5X]: ../Algoritmi/2-Strutture/5X-hashing.pdf
[pdf-6]: ../Algoritmi/2-Strutture/6-insiemi.pdf
[pdf-7]: ../Algoritmi/2-Strutture/7-strutture-speciali.pdf
[pdf-7X]: ../Algoritmi/2-Strutture/7X-strutture-speciali.pdf

