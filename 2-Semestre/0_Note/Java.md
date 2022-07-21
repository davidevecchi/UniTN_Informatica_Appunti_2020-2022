# [↓](#↑)

[root]: ../Java
[pdf-1]: ../Java/1_intro.pdf
[pdf-2]: ../Java/2_pilacpp.pdf
[pdf-3]: ../Java/3_pilajava.pdf
[pdf-4]: ../Java/4_EreditarietaParte1.pdf
[pdf-5]: ../Java/5_JavaFXIntro.pdf
[pdf-6]: ../Java/6_DynamicBinding.pdf
[pdf-7]: ../Java/7_Cast-Input-Exceptions.pdf

[pdf-8]: ../Java/8_InterfaceCollections.pdf
[pdf-9]: ../Java/9_equals.pdf
[pdf-10]: ../Java/10_confronto.pdf

[pdf-11]: ../Java/11_Static.pdf
[pdf-12]: ../Java/12_Wrappers_Tombola.pdf
[pdf-13]: ../Java/13_UML.pdf
[pdf-14]: ../Java/14_Eventi_in_JavaFX.pdf
[pdf-15]: ../Java/15_Layout.pdf
[pdf-16]: ../Java/16_PropagazioneEventi.pdf
[pdf-17]: ../Java/17_Esercizi.pdf
[pdf-Checklist]: ../Java/Checklist.pdf
[pdf-Minicalculator]: ../Java/Minicalculator.pdf
[pdf-TestA]: ../Java/TestA.110918.pdf
[pdf-VeroFalso]: ../Java/VeroFalso.pdf



[TOC]

# [1.][pdf-3] Introduzione

## Modello di memoria

> **Processo**: *programma in esecuzione a cui viene riservata una parte di memoria inaccessibile ad altri processi*

La memoria è suddivisa in

1. **Text**: codice eseguibile e non modificabile
2. **Variabili globali e statiche**
3. **Heap**: memoria allocata dinamicamente dal programmatore
4. **Stack**: memoria allocata dai blocchi (variabili automatiche)

> **Principio di Parnas / information hiding / need to know**
>
> - *Il committente di una funzione deve dare all'implementatore tutte le informazioni necessarie a realizzarla e nulla più*
>- *L'implementatore deve dare all'utente tutte le informazioni necessarie ad usare la funzione e nulla più*
> - *Ciascuno deve avere tutte e solo le informazioni che servono a svolgere il compito affidato*



## Architettura di Java

![image-20200420114759510](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200420114759510.png)

![image-20200420114832518](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200420114832518.png)



## Struttura di un programma

Un programma Java è organizzato come un insieme di **classi**

Classi diverse possono essere raggruppate nella stessa **compilation unit**

Il programma principale è rappresentato dal metodo **`main`** della classe il cui nome coincide con il nome del programma

È possibile inserire un main per ciascuna classe per verificarne il corretto funzionamento, indipendente dal resto del progetto (**unit / integration test**)

Il main è l'**ultimo** a essere scritto

**Struttura**

- ==**Package**==
  - Introduce un nuovo ==ambito di visibilità== dei nomi
  - Ogni package contiene ==una o più compilation unit==
  - Rappresenta ==unità logiche== all'interno del codice (eg. logica e grafica)
  - ==Disambiguare le omonimie== (univoco in tutto il mondo, eg. url)
  - `package it.unitn.disi.lingProg.vecchi.project`
- ==**Compilation unit**==
  - Ogni compilation unit contiene ==una o più classi o interfacce delle quali una sola è pubblica==
- ==**Classi e interfacce**==
- ==**Relazioni con il file system**==
  - package $\leftrightarrow$ directory
  - compilation unit $\leftrightarrow$ file

==**Regole**==

- ==Ogni file deve contenere **una e una sola classe pubblica**==

- ==Il **nome di ogni file deve coincidere** con quello della classe pubblica==



## Information hiding

<img src="https://i.stack.imgur.com/niONO.png" alt="img" style="zoom:150%;" />



## Struttura dell'applicazione

```java
class MyApp {
    public static void main(String args[]) {
        MyApp p = new MyApp();  // crea un oggetto
        p.doSomething();  // invoca una funzionalità
    }
    public MyApp() {  // costruttore
        // inizializza l'oggetto applicazione
    }
    public void doSomething(){
        // programma vero e proprio
    }
}
```



## Hello, world!

```java
class HelloWorld {
    public HelloWorld() {
        System.out.println("Hello, world!");
    }
    public static void main(String args[]) {
    	new HelloWorld;
    }
}
```

```bash
# Compilazione
$ javac HelloWorld.java
## produce HelloWorld.class e un file *.class per ogni classe del sorgente

# Esecuzione
$ java HelloWorld
## la classe indicata deve contenere il main
```



## Classi e oggetti

> **Classe**: *struttura dati che rappresenta una qualche entità astratta (definizione di un tipo di dato), che incapsula la definizione delle azioni che possono essere eseguite su quel tipo di dato*

> **Attributi**: *stato degli oggetti istanziati a partire dalla classe*

> **Metodi**: *comportamento degli oggetti (identico per oggetti della stessa classe)*

Una classe può essere **superflua** se non possiede metodi

> **Firma**: *nome della funzione seguito dalla lista dei parametri*

> **Oggetto**: *istanza di una classe, allocata in heap e accessibile solo per riferimento*

==**ID**: attributo di ciascun oggetto che lo identifica nel codice tramite una stringa==

Ogni variabile il cui tipo sia una classe contiene un **riferimento** ad un oggetto

Ad ogni variabile di tipo riferimento può essere assegnato il riferimento **`null`**

Nuovi oggetti sono costruiti usando l'**operatore `new`**

![image-20200420123408942](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200420123408942.png)



## Costruttore

La creazione di un oggetto include l'invocazione al ==**costruttore**, un metodo== particolare che

- ==**Alloca** la memoria necessaria a contenere l'oggetto==
- ==**Inizializza** lo spazio allocato==

Un costruttore ha lo **stesso nome** della classe, non indica il tipo del risultato e non ha `return`

==Se non è definito alcun costruttore, il compilatore inserisce un **costruttore di default** (vuoto e senza parametri) che alloca lo spazio per==

- ==Attributi di **tipo primitivo** e li inizializza al valore di default==
- ==Riferimenti agli attributi di tipo definito dall'utente e li inizializza a `null`== 

==È possibile invocare un **costruttore all'interno di un altro** con la notazione (posta come prima istruzione)==

```java
this(<elenco parametri>);
```



## Garbage collector

Java attiva ==**automaticamente**== il GC quando serve memoria, ==eliminando gli oggetti per cui non vi sono più riferimenti attivi==

==Non vi è un **distruttore** né si devono né possono deallocare esplicitamente gli oggetti==

Non si incanta grazie al multithreading

- **Multithreading**: flussi multipli nello stesso processo

- **Multitasking**: esecuzione “simultanea” di più programmi dal calcolatore



## Tipi primitivi e variabili

Java ignora i limiti di memoria della macchina (word) e ==definisce le **dimensioni dei tipi costanti**==. Sarà poi la ==JVM ad organizzare gli spazi==

==Per ciascun tipo è definito un **valore di default**==

È possibile definire attributi costanti con il **modificatore `final`**

```java
final int SIZE = 5;
```



## Tipi array

==In mancanza di inizializzazione, la dichiarazione di un array **non alloca** spazio==

==L'allocazione di realizza **dinamicamente** tramite l'operatore `new`==

- ==Gli array sono **oggetti**==

```java
<tipo>[] <nome> = new <tipo> [<dimensione>]
```

La **copia** di array è possibile tramite

```java
System.arraycopy(
    Object src, int src_position,
    Object dst, int dst_position, int lenght
);
```



## Asserzioni

==**Assert** permette di verificare che una **proprietà** del programma necessaria a proseguire l'esecuzione (precondizione o asserzione) sia vera==; se non lo è l'esecuzione termina

```java
assert(marker > 0) : "Estrazione da una pila vuota!";
```

L'uso delle asserzioni deve essere ==esplicitamente abilitato==

```bash
$ java -ea Pila  # enable assertions
```



## Enum

==L'entità definita con `enum` è come una pseudo classe che può essere istanziata==

```java
//static final String seme[]{"Cuori","Quadri","Fiori","Picche"}
enum Seme {Cuori, Quadri, Fiori, Picche};
public static void main(String args[]) {
    Seme c = Seme.Cuori;
    Seme p = Seme.Picche;
    System.out.println(c.name()+" "+p.name());	// Cuori Picche
    System.out.println(c + " " + p);			// Cuori Picche
    System.out.println(c.ordinal()+" "+p.ordinal()); // 0 3
    System.out.println(c.compareTo(p));			// -3
    for (Seme x : Seme.values()) {				// Cuori
        System.out.println(x);					// Quadri
    }											// Fiori
}												// Picche
```





# [2.][pdf-4] Ereditarietà

## Gerarchia

==Tutte le classi== di un sistema OO sono ==legate da una **gerarchia di ereditarietà**==

- Definita mediante la parola chiave ==**`extends`**==

==La **sottoclasse eredita** tutti gli attributi ed i metodi della superclasse==

<u>Relazione fra le classi</u>:  [sottoclasse]   **is-a (→)**  [superclasse]

==Se `extends` non è specificato== nella definizione di ==una classe==, essa ==estende implicitamente la classe **`Object`**==, che è dunque la ==**radice** della gerarchia==

==Classi con super comune sono **alberi**; alberi senza super comune sono **foreste**==

==Classi definite con **`final`** non possono avere **sottoclassi**==

Java supporta ==solo **ereditarietà semplice**== (una classe non può ereditare da più di una superclasse) e non si possono generare foreste

==`<object1> instanceof <object2>` è un operatore che ritorna `true` se il primo oggetto a runtime è un'istanza (is-a) del secondo==, `false` altrimenti



## Estensioni

Le estensioni possono essere

- ==**Strutturali**: aggiunta di variabili d'istanza==
- ==**Comportamentali**: aggiunta e/o modifica di metodi==

> **Overriding**: *ridefinizione di metodi della superclasse (firma uguale)*

> **Overloading**: *definizione in una stessa classe di più metodi con lo stesso nome, distinti per numero e/o tipo dei parametri (firma diversa)*

> **`super`**: *pseudo variabile che si riferisce a un metodo della superclasse ridefinito nella classe estesa*
>
> ```java
> super.<metodo>(<parametri>)
> ```

==I **costruttori** non vengono ereditati==

==All'interno di un costruttore è possibile **richiamare** il costruttore della superclasse== tramite la notazione (posta come ==prima istruzione==)

```java
class MyExtended extends MyClass {
    public MyExtended(<parametri>) {
		super(<parametri>);
        // ...
    }
}
```

==Se non viene chiamato esplicitamente il costruttore della superclasse, il compilatore inserisce automaticamente il codice che ne invoca il **costruttore di default** (senza parametri), se e solo se nella superclasse non è definito alcun costruttore non void==

==È possibile impedire l'**overridding** di un metodo ponendolo **`final`**==

- ==Impone il binding **statico** e migliora l'**efficienza**==



## Assegnazione

==L'entità a sinistra deve essere **compatibile** con ciò che le viene assegnato==

- ==deve valere la is-a==

```java
Super x = new Super();
Super x = new Extended();
// Extended x = new Super();  // non ammesso
```



## Classi e metodi astratti

> **Metodo astratto**: *metodo per il quale non è specificata alcuna implementazione (dichiarato ma non definito)*

> **Classe astratta**: *classe contenente almeno un metodo astratto*

Entrambi definiti mediante la parola chiave ==**`abstract`**==

Non è possibile creare istanze di una classe astratta (è definita parzialmente)

==Bisogna definire una loro **sottoclasse** che ne implementa i metodo astratti==





# [3.][pdf-5] JavaFX

## Framework

> **Framework**: *pezzi di codice già esistente con i quali il programmatore può interagire*

> **Callback**: *metodi predefiniti invocati dal framework*

È possibile sovrascrivere le callback per **personalizzare** il funzionamento del framework

```java
public class JavaFXApplicationTEST extends Application {
    @Override
    public void start(Stage primaryStage) {
        Circle circ = new Circle(40, 40, 30);
        Group root = new Group();
        root.getChildren().addAll(circ);
        Scene scene = new Scene(root, 300, 250);
        scene.setFill(Color.AQUAMARINE);
        primaryStage.setTitle("Hello World!");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    public static void main(String[] args) {
        Application.launch(args);
    }
}
```

==Il framework JavaFX come prima cosa costruisce lo **stage** (finestra) e lo passa come parametro al metodo `start`, invocato da `launch`==

Un **gruppo** è una forma di contenitore che non viene visualizzato graficamente, ma è utile per raggruppare elementi

==Il processo associato al framework rimane attivo anche al termine dell'esecuzione di `start`==

==Parent (contenitore) **has-a** and **is-a** Node (componente) → relazione ricorsiva di finestre all'interno di altre finestre==

![image-20200421171117903](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200421171117903.png)



![image-20200421171146544](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200421171146544.png)

![image-20200421174330970](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200421174330970.png)



## Gerarchia di Node

- #### Parent

  - **Group**: contenitore di altri nodi senza una specificata area di schermo
  - **Region**: gruppo con un'area associata (ha un background)
  - **WebView**: gestisce un WebEngine e mostra il contenuto (è un browser)
  - **Control**: superclasse di widget vari
    - **FileChooser**: seleziona un file

  

- #### Shape

  - **Text**: visualizza testo, supporta a capo (wrapping) e paragrafi con `'\n'`
  - **SVGPath**: linea composta da sottoelementi
  - **Line Polyline Polygon Rectangle Arc Circle Ellipse Quad/CubicCurve**

  

- #### Canvas

  Componenti su cui è possibile disegnare (le forme non sono oggetti)

  - **GraphicContext**
  - **fillArc() fillRect() drawImage()**
  
  
  
- #### ImageView

  Mostra immagini

  - Has-a **Image**

  

- #### MediaView

  Riproduce video e audio

  - Has-a **MediaPlayer**: motore / controllore della riproduzione
    - Has-a **Media**: entità multimediale



## Layout

### Posizionamento di un Node

Non vengono sempre forniti metodi per il **posizionamento assoluto**

- `setX setY` posizionamento assoluto solo di alcune sottoclassi
- `setLayoutX setTranslateY` sono definiti in compenso

==La responsabilità di posizionare contenuto è delegata a **componente specifica**==

- ==Tipo particolare di contenitore (Parent) `Pane` e sottoclassi==



### Aggiunta / rimozione di elementi

`Group`: spazio di dimensione non precisata che contiene le componenti

Aggiunta e rimozione vengono effettuate e applicate tramite la **lista dei figli** del contenitore `<parent>.getChildren()` con i metodi

- `add(Node x) addAll(Collection<Node> c)`
- `remove(Node x) removeAll(Collection<Node> c)`



### Posizionamento automatico tramite layout

==Il **layout** contiene la **logica della disposizione**==

Semplifica il compito del programmatore definendo **contenitori** di oggetti che vengono posizionati secondo **regole prestabilite** del contenitore stesso

==**Disposizione liquida**==: il contenitore può ignorare le posizioni specificate nei componenti (`setLayoutX`)

==Solo `setTranslateX` non viene ignorato dal layout==

==Diversi **layout managers** predefiniti==

![image-20200517201334174](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200517201334174.png)

[Esempi da slide 10][pdf-15]





# [4.][pdf-6] Static and dynamic binding

## Polimorfismo

> **Polimorfismo**: *capacità di un elemento sintattico di riferirsi a elementi di diverso tipo*

> **Principio di sostituzione di Liskov**: *se $S$ è un sottotipo di $T$, allora variabili di tipo $T$ possono essere sostituite da variabili di tipo $S$ senza alterare alcuna proprietà desiderabile del programma*

- ==Una **variabile** di tipo **riferimento** $T$ può riferirsi ad un qualsiasi oggetto il cui tipo sia $T$ o un suo sottotipo==

- ==Un **parametro formale** di tipo **riferimento** $T$ può riferirsi a parametri attuali il cui tipo sia $T$ o a un suo sottotipo==



## Binding dinamico

> **Dynamic binding / Late binding / Lazy evaluation**: *il legame fra un oggetto e il suo tipo è dinamico; il tipo di un oggetto viene deciso a runtime*

==Nell'invocazione di un **metodo** `x.f()`, l'implementazione scelta per `f` dipende dal tipo dinamico di `x`==

```java
class A {
    int x;
}
class B extends A {
    int y;
}
...
    A z = new B();
	z.x = 3;  // CORRETTO
    z.y = 4;  // ERRORE di compilazione: z è di tipo statico A
	(B(z)).y = 4;  // CORRETTO: è necessario un casting per
				// specificare al compilatore che z è di tipo B
```

==L'operatore `instanceof` determina il **tipo dinamico** di un oggetto (vale is-a)==

```java
if (object instanceof Class) {}
```



## Regole

> 1. Il **compilatore** determina la firma del metodo da eseguire basandosi sempre sul **tipo statico**
> 2. Solo in caso di **overriding**, la specifica implementazione del metodo, la cui firma è stata decisa dal compilatore, viene determinata a runtime basandosi sul **tipo dinamico**
>

```java
C o = new {C|D};  // D is-a C
o.m(...);
```

==Il metodo scelto dipende dal tipo dinamico di `o`, e viene deciso sempre a **runtime**== con questa logica

1. Si cerca all'interno della classe `C` (tipo statico di `o`) il metodo con la **firma** più vicina all'invocazione
2. Si guarda al **tipo dinamico** `{C|D}` di `o`; se è un sottotipo di `C` si deve verificare se ridefinisce (override) `m`. Se sì, si usa l'implementazione di `D`, altrimenti quella di `C`



## Cast

> **Casting**: *conversione forzata fra tipi riferimento*

È possibile fare un cast da un tipo $T$ a un sottotipo $T_1$ se il **tipo dinamico** dell'oggetto convertito è un **sottotipo** di $T_1$

I cast seguono la **catena di ereditarietà**

- **Upcast**: conversione implicita consentita dal polimorfismo (is-a)
- **Downcast**: conversione esplicita

==**Downcast illecito** (runtime error)==: chiamare un metodo di una sottoclasse di tipo $T_1$ su un oggetto di tipo dinamico $T$ con downcast a $T_1$





# [5.][pdf-7] User input

### Senza grafica

```java
import java.util.Scanner;
... // scanner analizza ciò che avviene su System.in (tastiera)
Scanner scanner = new Scanner(System.in);
System.out.println("Write");
String inputString = scanner.nextLine(); // blocca esecuzione
System.out.println(inputString);
```

### Con grafica

#### Alert

```java
// Alert apre la finestra con icona definita dal tipo
Alert alert = new Alert(AlertType.INFORMATION);
alert.setTitle("Alert title");
alert.setHeader("Alert header");
alert.setContentText("Alert text");
alert.showAndWait(); // blocca esecuzione fino a pressione [OK]
```

#### Text input dialog

``` java
TextInputDialog dialog = new TextInputDialog("Default answer");
dialog.setTitle("Dialog title");
dialog.setHeaderText("Dialog header");
dialog.setContentText("Answer lable:");
String s = dialog.showAndWait().get();
// get funziona bene con i pulsanti [Cancel] e [OK],
// ma dà errore chiudendo la finestra
```



### Conversione di stringhe in numeri

L'input in entrambi i casi è di tipo **String**

```java
String s = "10";
int i = Integer.parseInt(s);
```

```java
String pi = "3.14159265";
float PI = Float.parseFloat(pi);
```

==**Errore** in caso di stringa non numerica==



## Gestione degli errori

I codici che potrebbero generare errori devono essere protetti dal costrutto **blocco try-catch**

```java
try {
    // codice che potrebbe generare errore
} catch (Exception ex) {
    // codice da eseguire in caso di errore
} finally {
    // codice da eseguire sempre all'uscita dal blocco try
    // anche in caso di errori diversi dal catch
    // utilizzato per ripulire il programma
}
```

**Catch** assomiglia ad una funzione con parametro `ex` di tipo `Exception`

- Esiste una serie di ==**classi predefinite** (con super `Exception`) che rappresentano i possibili errori==
- È possibile eseguire ==**operazioni** su `ex`== (come stacktrace)
- In caso di possibili ==**errori multipli**== si usano ==più `catch` per lo stesso `try`==

```java
Scanner scanner = new Scanner(System.in);
String inputString;
int z;
boolean failure = true;
do {
    try {
        System.out.println("Inserisci un numero");
        inputString = scanner.nextLine();
        z = Integer.parseInt(inputString);
        failure = false;
    } catch (NumberFormatException ex) {
        failure = true;
    }
} while (failure);
```





# [6.][pdf-8] Interfaces and collections

## Interfacce

> **Interfaccia**: *collezione di firme di metodi pubblici e astratti*

==Classe completamente e implicitamente **astratta**, senza attributi ad eccezione delle **costanti**==

==Rappresenta i **servizi** (comportamento) che la classe deve fornire==

<u>Sintassi</u>

```java
interface <nome> {
    <lista metodi (solo firme senza corpo)>
}
```

Talvolta sono usate interfacce ==completamente vuote (**tagging interfaces**)== come ==etichette / timbri per classi con speciali proprietà==



### Ereditarietà multipla

==Un'<u>interfaccia</u> può **ereditare da una o più** interfacce==

```java
interface <nome> extends <nome1>,..,<nome_n> { ... }
```

==Una <u>classe</u> può **implementare una o più** interfacce e deve implementarne tutti i metodi (a meno che non sia astratta)==

```java
class <nome> implements <nome1>,..,<nome_n> { ... }
```

`implements` è una **is-a** rappresentata con una linea tratteggiata

==Non si hanno **conflitti fra le implementazioni**== perché i metodi ereditati da più interfacce sono vuoti

**Polimorfismo**

Le interfacce possono essere utilizzate

- Per ==**definire il tipo** di una variabile==
- **Non** per creare **oggetti**



## Collections

> **Collection**: *oggetto che raggruppa elementi multipli in una singola entità*

==Utilizzate per==

- ==Immagazzinare, recuperare e **trattare dati**==
- ==**Trasferire** gruppi di dati da un metodo a un altro==

==Gli **elementi** possono essere **eterogenei**==

==La dimensione massima **non è prefissata**==



### Java Collection Framework

Il Java Collection Framework contiene tre tipi di elementi

- ==**Interfacce**== specificano insiemi di servizi associati a diversi tipi di Collection

- ==**Implementazioni**== di specifiche strutture dati di uso comune (==classi== che imlementano le interfacce)

- ==**Algoritmi**== che implementano operazioni comuni (codificati in ==metodi==)

  Lo stesso metodo può essere usato in implementazioni diverse

Per utilizzare il JCF

```java
import java.util.*;
```



### Vantaggi

- Riduce il lavoro del programmatore e migliora la qualità del codice
  - Strutture dati efficienti già sviluppate
- Interoperabilità fra API
  - Definizione comune delle strutture
- Facilita il riuso del codice
  - Evita la duplicazione di funzionalità e consente l'adattamento



## Core delle interfacce

- **Collection**: arbitraria collezione di elementi singoli _
  - **Set**: _ senza duplicati (secondo la equals) ma non ordinati _
    - **SortedSet**: _ su cui è definito un ordinamento (su una certa proprietà)
  - **List**: _ ordinati secondo l'inserimento e accessibili tramite indice
  - **Queue**: _ organizzati in una coda _
    - **Deque**: _ a cui si può accedere da entrambe le estremità
- **Map**: collezione di coppie chiave-valore senza duplicati _
  - **SortedMap**: _ su cui è definito un ordinamento (sulle chiavi)



### Operazioni

- #### `Collection`

  - Base

    ```java
    int size();
    boolean isEmpty();
    boolean contains(Object element);
    boolean add(Object element);
    boolean remove(Object element);
    Iterator iterator();
    ```

  - Bulk (su più elementi contemporaneamente)

    ```java
    boolean containsAll(Collection c);
    boolean addAll(Collection c);
    boolean removeAll(Collection c);
    boolean retainAll(Collection c);
    void clear();
    Object[] toArray();
    ```

    

- #### `List`

  - Base

    ```java
    Object get(int index);
    Object set(int index, Object element);
    void add(int index, Object element);
    Object remove(int index);
    int indexOf(Object o);
    int lastIndexOf(Object o);
    ```

    

- #### `Map`

  - Base (associazione chiave-valore)

    ```java
    Object put(Object key, Object value);
    Object get(Object key);
    Object remove(Object key);
    boolean containsKey(Object key);
    boolean containsValue(Object value);
    Set keySet();
    Collection values();
    ```




### Implementazioni

![image-20200507222752873](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200507222752873.png)



### Esempio

```java
package structures;

class Number {
    private int n;
    
    Number(int n) {
        this.n = n;
    }
    int getInt() {
        return n;
    }
    void setInt(int n) {
        this.n = n;
    }
}
```

```java
package structures;
import java.util.*;

public abstract class ArrayDati extends LinkedList {
	public void inserisci(int x) {
        Number n = new Number(x);
        this.add(n);
    }
    abstract public int estrai();
}
```

```java
public class Coda extends ArrayDati {
    public int estrai() {
        if (this.size() == 0) {
            System.out.println("Coda vuota");
            System.exit(1);
        }
        return ((Number)(this.remove(1))).getInt();
    }
}
```

```java
public class Pila extends ArrayDati {
    public int estrai() {
        if (this.size() == 0) {
            System.out.println("Pila vuota");
            System.exit(1);
        }
        return ((Number)(this.remove(size()))).getInt();
    }
}
```

```java
public static void main(String[] args) {
    ArrayDati s;
    s = new Coda(); // Pila()
    s.inserisci(1);
    int n = s.estrai();
}
```



### Tipizzazione parametrica

```java
// restrizione sugli elementi
List<Number> numberList = new LinkedList();
numberList.add(new Number(x));
Number y = numberList.get();   // non necessita cast
numberList.add(new Papera());  // early error detection
```

Vantaggi del costrutto `<Type>`

- ==**Restringe** la collection ai soli elementi della **classe** (sottoclassi) specificata==
- ==Le operazioni **restituisco** oggetti del **tipo di dato** specificato==



### Visita di una collection

```java
List<Number> numberList = new LinkedList();
...
for (Number n : numberList) {
    System.out.printl(n);
}
```

Cicla su **tutti gli elementi** della collection

==**Non** è possibile **modificare** la struttura mentre si visita==



### Iteratori

A ogni oggetto di tipo `Collection` è associato un oggetto di tipo **`Iterator`**

```java
Iterator<Number> i = c.iterator();
```

==È un'interfaccia che permette di **scandire** gli elementi della collection e di visitarla in modo più approfondito==

```java
public interface Iterator<T> {
    Boolean hasNext();	// true se ci sono elementi da scandire
    T next();			// ritorna l'elemento successivo
    void remove();		// elimina l'ultimo elemento ritornato
}						// da next(); invocabile una sola volta
```

```java
boolean cond(Number n) {
    ...
}
...
void filter(Collection<Number> x) {
    Iterator<Number> i = x.iterator();
    while (i.hasNext()) {
        if (!cond(i.next()))
            i.remove();
    }
}
```





# [7.][pdf-9] Equals

## Identità e uguaglianza

- ==L'operatore **` ==`** testa l'**identità**==
  - ==Uguaglianza di **r-value**==
  - Due riferimenti che puntano allo stesso oggetto

- ==Il metodo **`Object.equals(Object obj)`** testa l'**uguaglianza**==
  - ==Due riferimenti che puntano a oggetti “uguali”==
  - Implementato (di default) come `X == Y`
  - Se due oggetti sono indentici allora sono anche uguali
  - È la base per ridefinirne l'uguaglianza nei casi specifici
    - Da ridefinire sempre in **ogni classe**
    - **Overriding** per evitare problemi di binding
  - Definisce la relazione di uguaglianza dei `Set`

```java
class P {
    int x; int y;
    @override
    public boolean equals(Object var) {
        if (var == this) return true;
        if (var == null) return false;
        if (!(var instanceof P)) // vale is-a per sottoclassi
            return false;
        if (var.getClass() != this.getClass()) // non vale is-a
            return false;
        return x == ((P)var).x && y == ((P)var).y;
    }
}
```



## Proprietà

==`equals()` implementa una **relazione di equivalenza** fra elementi non nulli==

- **Riflessiva**:		`x.equals(x) == true`
- **Simmetrica**:	`x.equals(y) == y.equals(x)`
- **Transitiva**:		`x.equals(y) && y.equals(z) → x.equals(z)`
- **Consistente**:	sempre lo stesso risultato con gli stessi oggetti
- `x.equals(null) == false`
- (**Efficiente**)





# [8.][pdf-10] Hashcode

## Funzione hash

==`hashCode` rappresenta una **funzione hash**==

- ==Non iniettiva==
- ==Mappa un oggetto su un **intero**==
  - Sono possibili collisioni
- Utilizzata a runtime per gestire efficacemente strutture dati



## Hashcode

==Ogni classe che sovrascrive `equals()` deve sovrascrivere `hashCode()`==

- ==Oggetti diversi hanno hash code diversi (basati sull'indirizzo)==

Implementa la `equals` in maniera **efficace**

- La `equals` può essere onerosa in caso di oggetti complessi
- ==`hashCode` è un'**approssimazione** efficace della `equals`==
  - `c1.equals(c2) => c1.hashCode() == c2.hashCode()`
  - `c1.hashCode() != c2.hashCode() => !c1.equals(c2)`
  - ==Non valgono i viceversa==
- ==Meccanismo di **fail quick**==
  - ==Evita di chiamare la `equals` **solo** quando le hash sono diverse==
  - ==In caso di hash uguali **deve** essere chiamata la `equals`==



## Utilizzi

==**Velocizza** i processi nelle strutture==

- ==**Ricerca**: tempo costante o lineare ridotto==
- ==**Confronto**: quick fail==

==Sfrutta l'**associazione** fra hash code e oggetto attraverso **hash tables**==

- ==I nuovi elementi sono posizionati all'**indice** corrispondente all'hash code==
- ==Elementi diversi con lo stesso hash sono organizzati in una lista (**bucket**)==
- ==Per verificare se c'è un elemento lo si **cerca** nel bucket corrispondente==



## Proprietà

- ==**Consistente**: ritorna sempre lo stesso intero per lo stesso oggetto==
- ==Oggetti uguali secondo `equals` devono avere lo stesso `hashCode`==
- Non è richiesto che a `equals` diversi corrispondano `hashCode` diversi

È compito del **programmatore** garantire queste proprietà in caso di overriding

- Nel **dubbio** deve ritornare una costante per non dare errori



## Implementazione

È bene usare gli ==**stessi campi** su cui è definito `equals`==

- ==**Somme e prodotti** di interi su un intervallo ampliato (per evitare collisioni)==

  - ==**Primitivi**: conversione / mappatura in intero==
  - ==**Oggetti**: si utilizza il loro metodo `hashCode()`==

- `Objects.hash()` partire da Java 7

  - ```java
    return Objects.hash(<elenco campi>);
    ```





# [9.][pdf-10] Confronto

## Interfaccia Comparable

L'interfaccia `Comparable` consente di

- ==Confrontare due oggetti secondo una **relazione d'ordine**==
- ==Definire **ordinamento totale / naturale** fra gli oggetti che la implementano==

Definisce un ==unico metodo `int compareTo(Object o)` che ritorna==

- ==Un intero negativo se `this < o`==
- ==Un intero positivo se `this > o`==
- ==`0` se `this.equals(o)`==

```java
class Element implements Comparable {
    ...
    public int compareTo(Object o) {
        if (this.equals(o)) return 0;
        if (this.x < ((Element)o).x) return -1;
        return 1;
    }
}
```



## Proprietà

- `x.compareTo(y) && y.compareTo(z) → x.compareTo(z)`
- `sgn(x.compareTo(y)) == -sgn(y.compareTo(x))`
- `x.cmpTo(y) == 0 → sgn(x.cmpTo(z)) == sgn(y.cmpTo(z))`
- (`(x.compareTo(y) == 0) == (x.equals(y))`)



## Insiemi ordinati

==Oggetti di classi che implementano `Comparable`== possono essere

- ==Elementi di un `SortedSet`==
- ==Chiavi di una `SortedMap`==

==Oggetti di tipo `List` o array== i cui elementi implementano `Comparable` possono essere ordinati invocando

- ==`Collections.sort(o)`==
- ==`Arrays.sort(o)`==



## Comparazioni multiple

È possibile definire un ==**unico metodo** `compareTo` per ogni classe==

L'==interfaccia `Comparator`== consente

- Di delegare il ==confronto a una **classe separata**==
- ==Maggiore **flessibilità**==
- ==**Criteri diversi**== dall'ordinamento naturale

==Fornisce il metodo `int compare(Object o1, Object o2)`==

==Il metodo sort è `Collections.sort(list, new ClassComparator())`==





# [10.][pdf-11] Modificatori

## Final

==TUTTO==

- **Variabili**
  - **Primitive**: costanti non modificabili
  - **Riferimenti**: identificatore non modificabile (lo stato è modificabile)
- **Metodi**: impedisce l'overriding nelle sottoclassi (static binding)
- **Classi**: impedisce la creazione di sottoclassi (static binding)



## Information hiding

==TUTTO==

**Visibilità** di attributi e metodi con **modificatori**

- `public`
  - Visibili a tutto il mondo
  - Vengono ereditati
- `protected`
  - Visibili a stessa classe, sottoclassi (anche in packages diversi) e classi nello stesso package
  - Vengono ereditati
- “package” (nessun modificatore specificato)
  - Visibili sollo alle classi dichiarate nello stesso package
  - Raggruppa le classi che “collaborano”
- `private`
  - Visibili solo nella stessa classe
  - Non visibili nelle sottoclassi (non ereditati)

![image-20200511231117475](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200511231117475.png)



## Static

==**Modificatore** che associa variabili o metodi a una **classe** o **oggetto**==

- ==**Variabili** come singola variabile **condivisa fra le istanze** della stessa classe==
  
  - ==Stesso blocco di memoria nell'area **variabili statiche** (e globali)==
  - ==Visibili e modificabili **ovunque** nella stessa classe== 
  - Hanno i problemi delle **variabili globali** (meglio `static final`)
    - Può essere utile creare una classe `Common` con tutte le **costanti**
  
- ==**Metodi** legati a una classe possono essere invocati **senza creare un'istanza**==
  
  - ==Possono accedere a **variabili di classe** ma non di istanza==
  
    <Non static variables cannot be referenced from static context>
  
  - `Math System` sono **classi di servizio** che non vengono mai istanziate
  
  - `Math.cos()` è un **metodo di classe** (simili a funzioni di libreria)
  
  - `System.out.println()`
    
    - `System` è una classe (istanza statica di `out`)
    - `out` è una variabile statica di classe (oggetto che incapsula i canali)
    - `println` è un metodo dell'oggetto `out`

==Quando il sistema parte vengono create tutte le variabili statiche che **vivono fino al termine dell'esecuzione** del programma e non possono essere gestite==

```java
// conta il numero di istanze in memoria (referenziate)
public class S {
    static int instanceCount = 0;	// variabile di classe
    int numProg;					// variabile di istanza
    S() {
        numProg = instanceCount++;
    }
    public void finalize() {  // rimozione dalla memoria
        instanceCount--;
    }
    static void resetCount() {
        instanceCOunt = 0;
    }
}
public class A {
    // public: accessibile a classi esterne
    // static: invocato all'inizio senza essere istanziato
    // void:   non deve ritornare nulla
    public static void main(String args[]) {
        new A;
    }
    A() {
        for (int i = 0; i < 10; i++) {
            S instance = new S();
        }
        System.out.println("# of instances: "+S.instanceCount);
        System.gc();
        System.out.println("# of instances: "+S.instanceCount);
        resetCount()
        System.out.println("# of instances: "+S.instanceCount);
    }
}
// # of instances: 10
// # of instances: 0
// # of instances: 0
```



## Main

```java
public class A {
    public static void main(String args[]) {
        new A;
    }
    A() { ... }
}
```

- `public`:	accessibile a classi esterne
- `static`:	invocato nel bootstrap senza essere istanziato
-  `void`:		 non deve ritornare nulla
- `String args[]`:	parametri di ingresso





# [11.][pdf-12] Wrappers e autoboxing

## Wrappers

Dati **primitivi** non sono trattati come oggetti per ragioni di **efficienza**

Per poterli inserire in collections bisogna usare un **wrapper**

> **Wrapper**: *classe che incapsula un solo attributo di tipo primitivo*

- `Integer Float Boolean Double Char`
- Usati anche come contenitori di **metodi di servizio**



## Autoboxing e unboxing

```java
Collection<Integer> coll = new ArrayList();
```

> **Autoboxing**: *conversione automatica che il compilatore Java fa fra il dato primitivo e la corrispondente classe wrapper*

```java
// coll.add(new Integer(1));
coll.add(1);
```

> **Unboxing**: *conversione automatica che il compilatore Java fa fra la classe wrapper e il corrispondente dato primitivo*

```java
// int x = coll.get(0).intValue();
int x = coll.get(0);
```





# [12.][pdf-12] JavaDoc

## Motore di estrazione

JavaDoc offre la possibilità di ==scrivere **commenti** in modo che un **motore di estrazione automatico** generi delle pagine html== (indentificati con `/**`)

==Per ogni **classe** devono essere presenti==

- ==**Descrizione** (a mano)==
- ==**Autore** (`@author`)==

==Per ogni **metodo**== (se presenti)

- ==Lista degli **argomenti** (`@param`)==
- ==Valore di **ritorno** (`@return`)==

### Cosa commentare

- ==Tutte le **classi**==

  - Generati automaticamente alla creazione

- ==Tutti i **metodi** e le **variabili di istanza**==

  - In particolare (almeno) quelli **pubblici** (i soli inseriti automaticamente)

  - **Metodi**: digitando `/**` nella riga precedente viene generato un commento con l'elenco dei parametri

    ```java
    /**
     * Descrizione di cosa fa il metodo
     * @param k descrizione del parametro
     * @param h una riga per ciascun parametro della lista
     * @return valore di ritorno
     */
    ```

  - **Variabili**: commento senza template predefinito

- Un commento sbagliato o non aggiornato è **peggio che assente**

- ==All'**esame** almeno per le classi principali e i metodi pubblici==





# [13.][pdf-13] Unified Modeling Language

## UML

~~**Linguaggio visuale standard** (OMG) per definire, progettare, realizzare e documentare i sistemi software a oggetti~~

- ~~Fornisce una **modellazione visuale** del mondo da sviluppare~~
- ~~Riunisce molte proposte esistenti~~
- ~~Copre l'**intero processo di produzione**~~
- ~~Sponsorizzato dalle maggiori industrie~~
- ~~Riunisce aspetti di ingegneria del software, database e sistemi~~
- ~~**Indipendente dal linguaggio** di programmazione~~
- ~~Utilizzabile in **domini applicativi e progetti diversi**~~
- ~~Estendibile per modellare meglio le **diverse realtà applicative**~~



### Class diagram

==Rappresenta le **relazioni strutturali** (statiche) fra le entità==

- ==**Classi**==

  - ==Nome==
  - ==Attributi==
  - ==Metodi==

- ==**Relazioni**==

  <img src="/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200517124318790.png" alt="image-20200517124318790" style="zoom:150%;" />

![image-20200517124439711](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200517124439711.png)



### Sequence / Activity diagram (swim lanes)

==Rappresenta **dinamica** e funzionamento in relazione al **tempo**==

==Evidenzia la **sequenza temporale delle azioni / interazioni** fra gli oggetti==

Non sono mostrate le associazioni

L'**utente** (attore esterno) è rappresentato con un omino stilizzato

Usabili in due forme

- **Generici**: tutte le sequenze / esecuzioni / interazioni possibili fra classi

- **Istanza**: sequenza particolare, consistente con quella generica

  ![image-20200517125034925](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200517125034925.png)





# [14.][pdf-14] Eventi

==TUTTO==

## Terminologia

> **Evento**: *azione o accadimento, spesso originato esternamente e asincrono, riconosciuto da un software che può essere gestito dal software*

> **Software framework**
>
> - *Codice che gestisce in modo standardizzato un certo tipo di eventi e che può essere customizzato scrivendo la sola parte non standard del codice*
> - *Astrazione in cui un software che fornisce funzionalità generiche può essere selettivamente cambiato da codice addizionale scritto dall'utente, specifico per l'applicazione*

> **Callback**
>
> * *Codice che customizza il comportamento di risposta a un tipo di evento*
> * *Codice eseguibile passato come argomento ad altro codice, che esegue l'argomento al tempo dato*

> **Event handler**: *callback subroutine che gestisce gli input ricevuti*



## Architettura di un framework

Un framework **genera degli eventi** in risposta a una sua logica interna

<u>Fasi</u>

1. **Abbonamento** dell'utente, che sa rispondere alle notifiche
2. **Creazione dell'oggetto evento** al verificarsi di una condizione, contenente informazioni relative a ciò che si è verificato
3. Passaggio dell'evento a un **gestore**

Si definisce un'**interfaccia** per limitare l'utilizzo del framework ai soli oggetti che siano in grado di interagire con esso

- Garantisce **omogeneità** fra richieste e risposte

![image-20200517164945511](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200517164945511.png)



## Eventi base

Tramite gli eventi è possibile **tracciare** tutto ciò che avviene nell'**ambiente**, interno o esterno

```java
public class EventTest extends Application {
    public void start (Stage stage) {
        Button btn = new Button();
        btn.setText("Click me");  // INPUT_METHOD_TEXT_CHANGED
        Listener a = new Listener();
        btn.addEventHandler(Event.ANY, a); // iscrizione
     // btn.addEventHandler(ActionEvent.ACTION, a);
        Group root = new Group(btn);
        Scene scene = new Scene(root, 300, 250);
        stage.setScene(scene)
        stage.sizeToScene();
        stage.show();
    }
    public static void main(String[] args) {
        Application.launch(args);
    }
}
class Listener implements EventHandler {
    int counter = 0;
    public void handle(Event t) {
        System.out.println(++counter
                           + " Ricevuto un evento di tipo "
                           + t.getEventType());
    }
}
/* OUTPUT
1 Ricevuto un evento di tipo INPUT_METHOD_TEXT_CHANGED
2 Ricevuto un evento di tipo MOUSE_ENTERED
3 Ricevuto un evento di tipo MOUSE_ENTERED_TARGET
4 Ricevuto un evento di tipo MOUSE_MOVED
...
12 Ricevuto un evento di tipo MOUSE_MOVED
13 Ricevuto un evento di tipo MOUSE_PRESSED
14 Ricevuto un evento di tipo ACTION
15 Ricevuto un evento di tipo MOUSE_RELEASED
16 Ricevuto un evento di tipo MOUSE_CLICKED
17 Ricevuto un evento di tipo MOUSE_MOVED
17 Ricevuto un evento di tipo MOUSE_EXIT
*/

/* OUTPUT alternativo
1 Ricevuto un evento di tipo ACTION
*/
```



## Gerarchia di tipi Event

**Gerarchia di eventi** predefinita in JavaFX associata agli elementi della GUI

- `Event` è la superclasse generica di tutti gli eventi
- Ogni oggetto `Event` raggruppa uno o più sottoeventi definiti da costanti
- Ogni sottoclasse definisce attributi e metodi specifici per tipologia di eventi

![image-20200517173241889](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200517173241889.png)

![image-20200517173412329](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200517173412329.png)



## Listener

Ascoltatore secondo il paradigma “**publish & subscribe**”

1. Un **mediatore / gestore List** contiene le entità (iscritti)
2. Il “soggetto” (abbonato) invia una **richiesta** al “servizio” (rivista)
3. Il “servizio” **aggiunge** il “soggetto” **a List** (abbonato / mailing list)
4. Il “serivio” può **inviare una notifica** comune a tutti gli ascoltatori

<u>Vantaggi</u>

- La gestione degli iscritti è enucleata in un **gestore esterno **e più **flessibile**
- La **richiesta di iscrizione** è espressa dal diretto **interessato**
- Possibilità di aggiungersi / rimuoversi dalla lista in **qualsiasi momento**
- La **stessa entità** riceve **richieste** e **notifica** / pubblica informazioni
- **Disaccoppiamento** del processo di produzione dell'evento dalla lista di distribuzione (e dal suo accesso / recesso)

![image-20200517131525221](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200517131525221.png)

![image-20200517135520210](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200517135520210.png)

```java
public class Banco {
    ...
    List<Cartella> cartelle;
    public Banco() {
        cartelle = new LinkedList();
        ...
    }
    void addListener(Cartella c) {
        cartelle.add(c);
    }
    void removeListener(Cartella c) {
        cartelle.remove(c);
    }
    private void notifyAllListeners(int x) {
        Iterator<Cartella> iter = cartelle.iterator();
        while (iter.hasNext()) {
            iter.next().checkNumber(x);
        }
    }
    public int getNextNumber() {
        ...
        notifyAllListeners(estratto);
        return estratto;
    }
    ...
}
```



### Listener di Event

Il codice applicativo può reagire agli eventi specificando uno o più **listener**

- Deve implementare l'interfaccia `EventHandler`
- Tipicamente è un oggetto di una classe apposita, o l'applicazione stessa

**Aggiunta / rimozione** di un ascoltatore

1. Implementare l'oggetto listener che implementa `EventHandler`
2. Aggiungere / rimuovere l'ascoltatore a una sorgente specificata di eventi

Un evento scatena una **callback** per ogni ascoltatore

```java
EventHandler l = new Listener();
btn.addEventHandler(ActionEvent.ACTION, l);
btn.removeEventHandler(ActionEvent.ACTION, l);
```



## Eventi di Button

Gli eventi possono essere

- **Di basso livello**: eventi elettrici generati dall'hardware (sinistra)
- **Semantici**: permettono di filtrare e unificare eventi e ottimizzazioni (destra)

![image-20200517173835647](/home/zeep/Documenti/UniTN/2-Semestre/Java.assets/image-20200517173835647.png)



## Interazione fra originatore e gestore

Per permettere all'EventHandler di modificare variabili di **contesti diversi**

- **Listener integrato**

  ```java
  public class EventTest extends Applications
                         implements EventHandler {
      int counter = 0;
      Text text = null;
      public void start(Stage stage) {
          ...
          // l'ascoltatore è la classe stessa
          btn.addEventHandler(ActionEvent.ACTION, this);
          ...
      }
      public void handle(Event t) {
          updateText(++counter);
      }
      public void updateText(int n) {
          text.setText("Hai cliccato " + n + " volte");
      }
      { /* main */ }
  }
  ```

- **Listener esterno** (permette la comunicazione fra classi distinte)

  ```java
  public class EventTest extends Applications {
      Text text = null;
      public void start(Stage stage) {
          ...
          // all'ascoltatore è passato un rif alla chiamante
          Listener a = new Listener(this);
          btn.addEventHandler(ActionEvent.ACTION, a);
          ...
      }
      public void updateText(int n) {
          text.setText("Hai cliccato " + n + " volte");
      }
      { /* main */ }
  }
  class Listener implements EventHandler {
      EventTest et = null;
      int counter = 0;
      Listener(EventTest e) {
          et = e;
      }
      public void handle(Event t) {
          et.updateText(++counter);
      }
  }
  ```

- **Listener interno**

  ```java
  public class EventTest extends Applications {
      Text text = null;
      public void start(Stage stage) {
          ...
          // all'ascoltatore è passato un rif alla chiamante
          Listener a = new Listener();
          btn.addEventHandler(ActionEvent.ACTION, a);
          ...
      }
      public void updateText(int n) {
          text.setText("Hai cliccato " + n + " volte");
      }
      class Listener implements EventHandler {
          int counter = 0;
          public void handle(Event t) {
              updateText(++counter);
          }
      }
      { /* main */ }
  }
  ```

- **Listener inerno anonimo**

  ```java
  public class EventTest extends Applications {
      Text text = null;
      public void start(Stage stage) {
          ...
          // EventHandler definito e utilizzato nel bottone
          btn.setOnAction(new EventHandler() {
          // == btn.addEventHandler(ActionEvent.ACTION, ...
          // convenience method
              int counter = 0;
              public void handle(Event t) {
                  updateText(++counter);
              }
          });
          ...
      }
      public void updateText(int n) {
          text.setText("Hai cliccato " + n + " volte");
      }
      { /* main */ }
  }
  ```





# [15.][pdf-16] Java FX - modello degli eventi

==TUTTO==

## Keyboard event

```java
Button btn = new Button("PLUS");
EventHandler<KeyEvent> keyEventHandler = new
    				   EventHandler<KeyEvent>() {
    @Override
    public void handle(KeyEvent e) {
        if (e.getCharacter().equals("+")) {
            btn.fireEvent(new ActionEvent());
        	System.out.println("Buttom + pressed");
        }
    }
};
btn.addEventHandler(KeyEvent.KEY_TYPED, keyEventHandler);
```

**Metodi** di KeyEvent

- `e.getCharacter()`
  - **Carattere generato**, frutto della pressione di una **combinazione** di tasti
  - <u>Uguaglianza</u>:  `e.getCharacter().equals("u")`
  - <u>Usare con</u>:  `KEY_TYPED`
- `e.getCode()`
  - Codice ottenuto da un **singolo tasto**, speciali inclusi
  - <u>Uguaglianza</u>:  `e.getCode()	==	KeyCode.U`
  - <u>Usare con</u>:  `KEY_PRESSED`

`Node.fireEvent(new Event())` lancia un evento generato dal codice



## Generazione e propagazione

### Assegnazione del target

<u>Primo problema</u>
Un evento può essere generato in un'area di interesse per **più di un oggetto**

Regole per **assegnare** il target

- **Key events**: nodo con il **focus**
- **Mouse events**: nodo in **primo piano** nella posizione del mouse
  - Foglie della gerarchia di contenimento



### Event dispatch chain

<u>Secondo problema</u>
Può essere utile far gestire un evento al **contenitore**

**Regola base**
Tutti gli eventi partono dallo stage, arrivano al target e tornano allo stage

- **Event capturing**:  stage → target
  - Eventi intercettati mediante **filter**
- **Event bubbling**:  target → stage
  - Eventi intercettati mediante **handler**

**Event dispatch chain**

- Sequenza di componenti stage ↔ target
  - **Source**
    - Entità che sta **gestendo** l'evento in quel momento
    - Percorre tutta la catena
  - **Target**
    - Entità per la quale l'evento è stato **scatenato**
    - Fisso
- `t.consume()`  interrompe la propagazione dell'evento

Gli **eventi** vengono

- **Notificati** a **tutti** gli elementi della catena
- **Filtrati / gestiti** dagli elementi che hanno associato un **event handler**

<u>Utilizzi</u>

- Centralizzare la gestione di eventi omogenei al contenitore
- Debugging

```java
SuperHandler filter = new SuperHandler() {
    public void handle(ActionEvent t) {
        super.handle(t);
        ...
    }
};
SuperHandler handler = new SuperHandler() {
    public void handle(ActionEvent t) {
        super.handle(t);
        ...
    }
};   
SuperHandler cutter = new SuperHandler() {
    public void handle(ActionEvent t) {
        super.handle(t);
        ...
        t.consume();
    }
};
...
stage.addEventHandler(KeyEvent.KEY_TYPED, keyEventHandler);
box.addEventFilter(ActionEvent.ACTION, filter);
box.addEventHandler(ActionEvent.ACTION, handler);
btn.addEventFilter(ActionEvent.ACTION, filter);
btn.addEventHandler(ActionEvent.ACTION, cutter);
```



### Key event per bottoni multipli

```java
// dentro start()…
EventHandler<KeyEvent> keyEventHandler =
    new EventHandler<KeyEvent>() {
    public void handle(KeyEvent keyEvent) {
        ...
        switch (keyEvent.getCharacter()) {
            case "u": case "U":
                b1.fireEvent(new ActionEvent());
                b1.requestFocus();
                break;
            case "d": case "D":
                b2.fireEvent(new ActionEvent());
                b2.requestFocus();
                break;
        }
    }
};
stage.addEventHandler(KeyEvent.KEY_PRESSED, keyEventHandler);
// handler associato allo stage: non dipende da chi ha il focus
```





# Extra

Fasi di sviluppo del codice

1. Elementi grafici
2. Classi
3. Metodi (logica)
4. Flusso degli eventi



```java
public class Board extends TilePane {
    Palo[] palo = new Palo[3];
    public Board() {
        Listener a = new Listener();
        for (int i = 0; i < 3; i++) {
            palo[i].addEventFilter(MouseEvent.MOUSE_CLICKED,a);
            getChildren().add(palo[i]);
        }
    }
    class Listener implements EventHandler {
        @Override
        public void handle(Event e) {
            Palo p = (Palo) e.getSource();
            System.out.println("" + p.id);
            e.consume();
        }
    }
}
```



```java
static final Random R = new Random(System.currentTimeMillis());
R.nextInt(420); // 0-419
R.nextDouble(); // 0.0-1.0
```





# [↑](#↓)

