# 3 - Introduzione

## Costruttore

Invocare un **costruttore all'interno di un altro** con la notazione 

```java
this(<elenco parametri>);   // prima istruzione del costruttore
super(<elenco parametri>);  // alternativa (?)
```

## Array

```java
<tipo>[] <nome> = new <tipo> [<dimensione>]
```

```java
System.arraycopy(Object src, int src_position,
    			 Object dst, int dst_position, int lenght);
```

## Enum

```java
//static final String seme[]{"Cuori","Quadri","Fiori","Picche"}
enum Seme {Cuori, Quadri, Fiori, Picche};
public static void main(String args[]) {
    Seme c = Seme.Cuori;
    Seme p = Seme.Picche;
    System.out.println(c.name() +" "+ p);				// Cuori Picche
    System.out.println(c.ordinal() +" "+ p.ordinal());  // 0 3
    System.out.println(c.compareTo(p));					// -3
    for (Seme x : Seme.values()) {						// Cuori Quadri
        System.out.print(x); }}							// Fiori Picche
```



# 7 - User input

```java
import java.util.Scanner;
Scanner scanner = new Scanner(System.in);
System.out.println("Write");
String inputString = scanner.nextLine(); // blocca esecuzione
System.out.println(inputString);
```

```java
Alert alert = new Alert(AlertType.INFORMATION);
alert.setTitle("Alert title");
alert.setHeader("Alert header");
alert.setContentText("Alert text");
alert.showAndWait(); // blocca esecuzione fino a pressione [OK]
```

``` java
TextInputDialog dialog = new TextInputDialog("Default answer");
dialog.setTitle("Dialog title");
dialog.setHeaderText("Dialog header");
dialog.setContentText("Answer lable:");
String s = dialog.showAndWait().get();
```

```java
Scanner scanner = new Scanner(System.in);
String inputString;    int z;    boolean failure = true;
do { try {
        System.out.println("Inserisci un numero");
        inputString = scanner.nextLine();
        z = Integer.parseInt(inputString);
        failure = false;
    } catch (NumberFormatException ex) {
        failure = true; }
} while (failure);
```



# 8 - Interfaces and collections

## Interfaces

```java
interface <nome> {  <constanti>
    <lista metodi (solo firme senza corpo)>}
```

```java
class <nome> implements <nome1>,..,<nome_n> { ... }
```

## Collections

- **Collection**: arbitraria collezione di elementi singoli _
  - **Set**: _ senza duplicati (secondo la equals) ma non ordinati _
    - **SortedSet**: _ su cui è definito un ordinamento (su una certa proprietà)
  - **List**: _ ordinati secondo l'inserimento e accessibili tramite indice
  - **Queue**: _ organizzati in una coda _
    - **Deque**: _ a cui si può accedere da entrambe le estremità
- **Map**: collezione di coppie chiave-valore senza duplicati _
  - **SortedMap**: _ su cui è definito un ordinamento (sulle chiavi)

### Tipizzazione parametrica

```java
// restrizione sugli elementi
List<Number> numberList = new LinkedList();
numberList.add(new Number(x));
Number y = numberList.get();   // non necessita cast
numberList.add(new Papera());  // early error detection
```



### Visita di una collection

```java
List<Number> numberList = new LinkedList();
for (Number n : numberList) {
    System.out.printl(n);   }
```

```java
Iterator<Number> i = c.iterator();
```

```java
boolean cond(Number n) { ... }
void filter(Collection<Number> x) {
    Iterator<Number> i = x.iterator();
    while (i.hasNext()) {
        if (!cond(i.next()))
            i.remove();  }}
```

## Wrappers e autoboxing

```java
Collection<Integer> coll = new ArrayList();
coll.add(1);
int x = coll.get(0);
```



# 9 - Equals

```java
class P {
    int x; int y;
    public boolean equals(Object var) {
        if (var == this) return true;
        if (var == null) return false;
        if (!(var instanceof P)) return false;
        if (var.getClass() != this.getClass()) return false;
        return x == ((P)var).x && y == ((P)var).y;  }}
```

## Hashcode

È bene usare gli **stessi campi** su cui è definito `equals`

- **Somme e prodotti** di interi su un intervallo ampliato (per evitare collisioni)

  - **Primitivi**: conversione / mappatura in intero
  - **Oggetti**: si utilizza il loro metodo `hashCode()`

- `Objects.hash()` partire da Java 7

  - ```java
    return Objects.hash(<elenco campi>);
    ```







# 10 - Confronto

## Interfaccia Comparable

L'interfaccia `Comparable` consente di

- Confrontare due oggetti secondo una **relazione d'ordine**
- Definire **ordinamento totale / naturale** fra gli oggetti che la implementano

Definisce un unico metodo `int compareTo(Object o)` che ritorna

- Un intero negativo se `this < o`
- Un intero positivo se `this > o`
- `0` se `this.equals(o)`

```java
class Element implements Comparable {
    public int compareTo(Object o) {
        if (this.equals(o)) return 0;
        if (this.x < ((Element)o).x) return -1;
        return 1;  }}
```

## Insiemi ordinati

Oggetti di classi che implementano `Comparable` possono essere

- Elementi di un `SortedSet`
- Chiavi di una `SortedMap`

Oggetti di tipo `List` o array i cui elementi implementano `Comparable` possono essere ordinati invocando

- `Collections.sort(o)`
- `Arrays.sort(o)`

## Comparazioni multiple

È possibile definire un **unico metodo** `compareTo` per ogni classe

L'interfaccia `Comparator` consente

- Di delegare il confronto a una **classe separata**
- Maggiore **flessibilità**
- **Criteri diversi** dall'ordinamento naturale

Fornisce il metodo `int compare(Object o1, Object o2)`

Il metodo sort è `Collections.sort(list, new ClassComparator())`



# 11 - Modificatori

## Final

- **Variabili**
  - **Primitive**: costanti non modificabili
  - **Riferimenti**: identificatore non modificabile (lo stato è modificabile)
- **Metodi**: impedisce l'overriding nelle sottoclassi (static binding)
- **Classi**: impedisce la creazione di sottoclassi (static binding)

## Information hiding

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

<img src="https://i.stack.imgur.com/niONO.png" alt="img" style="zoom:150%;" />

<img src="/home/zeep/Documenti/UniTN/2-Semestre/0_Note/Java (copy).assets/image-20200511231117475.png" alt="image-20200511231117475" style="zoom: 80%;" />



# 12 - JavaDoc

- Tutte le **classi**
- Tutti i **metodi** e le **variabili di istanza**
  - In particolare (almeno) quelli **pubblici** (i soli inseriti automaticamente)

- All'**esame** almeno per le classi principali e i metodi pubblici



# 14 - Eventi

![image-20200517173241889](/home/zeep/Documenti/UniTN/2-Semestre/0_Note/Java.assets/image-20200517173241889.png)

```java
EventHandler l = new Listener();
btn.addEventHandler(ActionEvent.ACTION, l);
btn.removeEventHandler(ActionEvent.ACTION, l);
```

## Interazione fra originatore e gestore

- **Listener integrato**

  ```java
  public class E extends Applications implements EventHandler {
      public void start(Stage stage) {
          // l'ascoltatore è la classe stessa
          btn.addEventHandler(ActionEvent.ACTION, this); }
      public void handle(Event t) { ... }
  ```
  
- **Listener esterno** (permette la comunicazione fra classi distinte)

  ```java
  public class EventTest extends Applications {
      public void start(Stage stage) {
          // all'ascoltatore è passato un rif alla chiamante
          Listener a = new Listener(this);
          btn.addEventHandler(ActionEvent.ACTION, a); }}
  class Listener implements EventHandler {
      EventTest et = null;
      Listener(EventTest e) { et = e; }
      public void handle(Event t) { ... } }
  ```
  
- **Listener interno**

  ```java
  public class EventTest extends Applications {
      public void start(Stage stage) {
          // all'ascoltatore è passato un rif alla chiamante
          Listener a = new Listener();
          btn.addEventHandler(ActionEvent.ACTION, a); }
      class Listener implements EventHandler {
          public void handle(Event t) { ... } }}
  ```
  
- **Listener inerno anonimo**

  ```java
  public class EventTest extends Applications {
      public void start(Stage stage) {
          // EventHandler definito e utilizzato nel bottone
          btn.setOnAction(new EventHandler() {
              public void handle(Event t) { ... } }); }}
  ```

### Listener per oggetti multipli

```java
public class Board extends TilePane {
    Palo[] palo = new Palo[3];
    public Board() {
        for (int i = 0; i < 3; i++) {
            palo[i].addEventFilter(MouseEvent.MOUSE_CLICKED,
                                   new Listener());
            getChildren().add(palo[i]); }}
    class Listener implements EventHandler {
        public void handle(Event e) {
            Palo p = (Palo) e.getSource(); { ... }
            e.consume(); }}}
```



















# 16 - Java FX - modello degli eventi

## Keyboard event

```java
Button btn = new Button("PLUS");
EventHandler<KeyEvent> keyEventHandler = new 										EventHandler<KeyEvent>() {
    public void handle(KeyEvent e) {
        if (e.getCharacter().equals("+")) {
            btn.fireEvent(new ActionEvent());
        	System.out.println("Buttom + pressed"); }}};
btn.addEventHandler(KeyEvent.KEY_TYPED, keyEventHandler);
```

**Metodi** di `KeyEvent`

- `e.getCharacter()`
  - <u>Uguaglianza</u>:  `e.getCharacter().equals("u")`
  - <u>Usare con</u>:  `KEY_TYPED`
- `e.getCode()`
  - <u>Uguaglianza</u>:  `e.getCode()	==	KeyCode.U`
  - <u>Usare con</u>:  `KEY_PRESSED`

`Node.fireEvent(new Event())` lancia un evento generato dal codice

## Generazione e propagazione

### Assegnazione del target

- **Key events**: nodo con il **focus**
- **Mouse events**: nodo in **primo piano** nella posizione del mouse

### Event dispatch chain

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

```java
SuperHandler filter = new SuperHandler() {
    public void handle(ActionEvent t) {
        super.handle(t); ... }};
SuperHandler handler = new SuperHandler() {
    public void handle(ActionEvent t) {
        super.handle(t); ... }};   
SuperHandler cutter = new SuperHandler() {
    public void handle(ActionEvent t) {
        super.handle(t); ...
        t.consume(); }};
stage.addEventHandler(KeyEvent.KEY_TYPED, keyEventHandler);
box.addEventFilter(ActionEvent.ACTION, filter);
box.addEventHandler(ActionEvent.ACTION, handler);
btn.addEventFilter(ActionEvent.ACTION, filter);
btn.addEventHandler(ActionEvent.ACTION, cutter);
```

### Key event per bottoni multipli

```java
// start()
EventHandler<KeyEvent> keyEventHandler =
    new EventHandler<KeyEvent>() {
    public void handle(KeyEvent keyEvent) {
        switch (keyEvent.getCharacter()) {
            case "u": case "U":
                b1.fireEvent(new ActionEvent());
                b1.requestFocus();
                break;
            case "d": case "D":
                b2.fireEvent(new ActionEvent());
                b2.requestFocus();
                break; }}};
stage.addEventHandler(KeyEvent.KEY_TYPED, keyEventHandler);
// handler associato allo stage: non dipende da chi ha il focus
```

