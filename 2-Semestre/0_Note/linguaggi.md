# [↓](#↑)

[TOC]



# [1.][slide2] Abstract Machines

## ~~Components~~

+ **CPU** executes machine instructions from RAM and can modify RAM
- **CU**: *Control Unit*, executes instructions
  - **ALU**: *Arithmetic Logic Unit*, executes A/L instructions
  - **registers**: small memory spaces
    * Invisible
      - **MAR**: *Address Register*, address to access the bus
      - **MDR**: *Data Register*, data to read or write
    * Visible
      - **PC**: *Program Counter*, address of the next instructions
      - **SR**: *Status Register*, result of an operation / state of machine
      - data and addresses
  
+ **RAM** stores data and programs

+ **Mass storage**

+ **I/O peripherals**

+ **BUS**: *electrical connections used to transmit machine instructions and data between different components*



## ~~Execution of a program~~

>  **Execution**: *infinite cycle of fetch / decode / execute*

1. **Fetch**: read the next instruction
    `→ ++PC → MAR →↓ RAM ↑→ MDR → inv reg →`
    a. Copy the PC into the AR
    b. Transfer data addressed in AR from RAM to DR
    c. Save the DR in an invisible register
    d. Increment the PC
2. **Decode**
3. **Execute**
   - Load data
   - Save data
   - Modify the PC (jump)



## Machines

### Physical machine

> **Physical machine**: *machine designed for execution of programs written in its own ML*

> **CPU**: *implementation in hardware of the cycle*

> **Implementation in hardware**: *algorithm that can understand and execute its ML*



### Abstract machine

> **Abstract machine**: *implementation in software of the cycle*

> **Implementation in software**: *algorithms and data structures that enable us to store and execute programs*

Each **A.M.** is associated to **only one ML** (not vice versa):

  - $\cal M_L$:  A.M. $\cal M$ that understand and execute language $\cal L$
  - $\cal L$:  ML for $\cal M_L$
  - **Program**: sequence of instructions in $\cal L$

~~**Execution** of a program in $\cal L$ by $\cal M_L$:~~

  1. ~~Execute elementary operations (ALU)~~
  2. ~~Control the sequence of execution (PC)~~
  3. ~~Transfer data from/to memory (MAR/MDR)~~
  4. ~~Memory organization~~



## Implementation of a language

> **Implementation of** $\cal L$: *realize it by a $\cal M_L$ that can execute programs written in $\cal L$ (via hardware, software or firmware)*



### In software

Software that runs on a **host machine** $\cal MO_{LO}$

#### Interpretive

> **Interpreter**: *a program in $\cal LO$ executed by $\cal MO_{LO}$, that understand and executes $\cal L$*

Translation from $\cal L$ to $\cal LO$ instruction by instruction

![image-20200611115411222](/home/zeep/Documenti/UniTN/2-Semestre/linguaggi.assets/image-20200611115411222.png)

#### Compilative

> **Compiler**: *a program that translates the entire program from $\cal L$ to $\cal LO$ before execution*

It doesn't have to be in $\cal LO$ and can be executed on a different $\cal MA$

![image-20200611115441465](/home/zeep/Documenti/UniTN/2-Semestre/linguaggi.assets/image-20200611115441465.png)

#### Hybrid

Compilation to an **intermediate language** $\cal LI$, that is then interpreted by a $\cal MO_{LO}$ program in ==$\cal LI$==

![image-20200611115503382](/home/zeep/Documenti/UniTN/2-Semestre/linguaggi.assets/image-20200611115503382.png)

#### Comparison

- Purely **interpretive**
  - Flexible and portable
  - Simple debug
- Purely **compilative**
  - More efficient
  - More complex



### In firmware

Intermediate implementation by **micro-programmable CPUs**


+ ~~$\cal M_{ML}$ is implemented as a micro-interpreter~~
+ ~~The cycle is implemented using invisible micro-instructions~~
+ ~~Data structures and algorithms are realized as micro-programs~~
+ ~~More flexible than pure hardware~~



## Formal definitions

Programs as **functions**

$$
\begin {align*}
& \cal {P^L : D → D} &&&&&&&&& \\
& \cal {P^L(i) = o} \\ 
& \cal {i,o ∈ D}
\end {align*}
$$

Interpreters and compilers are programs, whose $i$ and $o$ are other programs

$\cal PR^L$ is the set of programs $\cal P$ in $\cal L$

+ **Interpreter** for $\cal L$ in $\cal LO$

  + Implements $\cal M_L$ on $\cal MO_{LO}$
    $$
    \begin {align*}
    &\cal{ I_L^{LO} : (PR^L\ \times\ D) → D} &&&&&&& \\
    &\cal{ ∀ i ∈ D}, \ \ I_L^{LO}(P^L,i) = P^L(i)￼
    \end {align*}
    $$

+ **Compiler** from $\cal L$ to $\cal LO$ in $\cal LA$

  + Implements $\cal M_L$ on $\cal MO_{LO}$

  + Transforms $\cal{P^L ∈ PR^L}$ to $\cal{P^{LO} ∈ PR^{LO}}$
    $$
    \begin {align*}
    & \cal {C_{L,LO}^{LA} : PR^L → PR^{LO}} \\
    & \cal {∀ i ∈ D, \ \ P_C^{LO} = C_{L,LO}^{LA}(P^L) → P_C^{LO}(i) = P^L(i)}
    \end {align*}
    $$





# [2.][slide3] Names and environments

## Names

> **Identifiers**: *sequence of characters, alphanumerical tokens*

> **Name**: *identifier used to denote something else*

Defined by

  - User
  - Language (primitives, constants)

> **Denotable object**: *object that can be associated with a name*

> **Binding**: *association between name and denotable object*

Bindings are made at

  - Language design (primitives, constants)
  - Program writing (allocation)
  - Compile time (static)
  - Runtime (dynamic)



## Environments

> **Environment**: *the collection of associations between names and denotable objects that exists at runtime at a specific point in the program and or a specific point in the execution*

> **Block**: *a section of the program, identified by opening and closing signs, that can contain local declarations for that region*

  - Anonymous (inline)
  - Associated with a procedure

> **Declaration**: *a mechanism that creates an association in an environment*

  - **Overlapping**: the same name denotes different objects at different points (nested blocks)
  - **Aliasing**: different names that denote the same object


Environments in a specific block

  - **Local**
  - **Nonlocal** (inherited)
  - **Global**



## Operations

- **On associations**
    - **Naming**: creation of bindings (local declaration in a block)
    - **Referencing**: reference to an object by its name (use of a name)
    - **Disactivation**: local declaration in a block that masks a previous one
    - **Reactivation**: exit from a block that masked the association
    - **Destruction**: exit from a block with a local declaration


- **On denotable objects**
    - **Creation**
    - **Access**
    - **Modification** (if possible)
    - **Destruction**
    

**Fundamental events**

1. <u>Creation</u> of an object
2. <u>Naming</u> creation of an association for the object
3. <u>Referencing</u> to an object via association
4. <u>Disactivation</u> of an association
5. <u>Reactivation</u> of an association
6. <u>Destruction</u> of an association
7. <u>Destruction</u> of an object



### Lifetime

Lifetime of an **object** does not coincide with lifetime of an **association**

- Lifetime of an **object**: 1-7
- Lifetime of an **association**: 2-6

Particular cases

  - **Longer** (variable passed by reference)
  - **Shorter** (dangling reference)



## Scopes

> **Rules of visibility**: a local declaration in a block is visible in that block and in all nested blocks, as long as no intervening block contains a new declaration of the same name (that hides the previous one). In a procedure, this means in blocks that are executed in a diﬀerent position than their deﬁnition


A nonlocal reference in a block $B$ can be solved by

  + **Static scoping**: in the block that syntactically includes $B$
    - Principle of independence (of position and of local names)
    - Information in the program text
    - Associations at compile time
    - Easier to implement and more efficient
    
  + **Dynamic scoping**: in the block that is executed immediately before $B$
    - Information at runtime
    - Hard to read and implement, less efficient



## Determining the environment

The environment is determined by rules for

  - **Scoping** (static or dynamic)
  - **Binding** (shallow or deep)
  - **Parameter passing**
  - **Specific rules**
    - Declaration visibility in the block





# [3.][slide4] Memory allocation

Three mechanisms

+ **Static allocation**: at compile time
+ **Dynamic allocation**: at execution time
  - **Stack**: LIFO
  - **Heap**: any time



## Static

> **Static allocation**: *an object has an absolute address that is maintained throughout the execution*

- Unique static area of memory for storing an object
- Does not permit recursion



## Stack

> **Stack**: *for every runtime instance of a subprogram, there is an activation record (or frame) that contains the information about this instance*

> **Instance**: *particular call to a particular procedure* (~block)

> **Dynamic link**: *pointer to previous record on the stack*

Each block has an **activation record**

  - **Push** on entry
      - Creation of dynamic link to new record
      - AR set to pointer to new record
  - **Pop** on exit
      - Elimination of the pointer to current AR
      - Set pointer to AR on top

**Pointer** of AR points to the AR of the active block



### Activation record

- **Anonymous blocks**
    - Pointer for dynamic chain
    - Local variables
    - Intermediate results

- **Procedures**
    - Pointer for dynamic chain
    - Pointer for static chain
    - Address for return
    - Address for result
    - Parameters
    - Local variables
    - Intermediate results



### Implementation

- Sequence of calls
- Prologue
- Epilogue
- Return sequence



### Information

> **Offset**: *statically-determined distance in memory from the address of the AR to the location of the variable*

Information is **accessed**

- **In AR**: via offset (address = AR address + offset)
- **Nonlocal**: following the dynamic chain



## Heap

> **Heap**: *region of memory in which blocks can be allocated and deallocated at arbitrary moments*

Necessary when the **language** allows

- Explicit allocation at **runtime**
- Objects of **varying size**
- Objects whose lifetime is **not LIFO**



### Free list

|                  |               Blocks of fixed size               |                   Blocks of variable size                    |
| :--------------: | :----------------------------------------------: | :----------------------------------------------------------: |
|    **Start**     |            all linked in a free list             |                        a single block                        |
|  **Allocation**  | contiguous blocks are removed from the free list | find a free block of the appropriate size (free list is before and after that block) |
| **Deallocation** |          restore them to the free list           |              restore the block to the free list              |

+ **Single list**
  + <u>Start</u>: **single block**
  + <u>Allocation</u>: **first fit** or **best fit**
    + <u>Cost</u>: **linear** in the number of free block
    + If the free block is much larger it's **divided**

- **Multiple lists**
  - Better management
  - **Division** of blocks between lists
    - **Static** (fixed)
    - **Dynamic** (buddy system 2^k^, Fibonacci)



### Management

- Access and operations must be efficient
- Efficient allocation of space (avoid wasting memory)
  - **Internal fragmentation**
    Space $X$ is allocated in a block $Y$, if $Y > X$ then $Y - X$ is wasted
  - **External fragmentation**
    The total amount of free space is available but not usable





# [4.][slide4] Scoping rules

## Static scoping

### Static chain

> **Static link**: *pointer to the activation record of the block that immediately contains the text of the current block*

|                |           Dynamic link            |               **Static link**               |
| :------------: | :-------------------------------: | :-----------------------------------------: |
| **Pointer to** |     previous AR on the stack      |         AR of the containing block          |
| **Depends on** | execution sequence of the program | static nesting of declarations of procedure |

If a subprogram is at level $k$ of **nesting**, the chain has **length $k$**

![image-20200611190953717](/home/zeep/Documenti/UniTN/2-Semestre/linguaggi.assets/image-20200611190953717.png)

#### Determine the correct association

1. Determine the AR where the variable is **located**
   - If it isn't in the AR pointed by the static link ($k\ne0$)
     - Follow the static chain, from S.L. until the declaration
     - The number of operation is linear in the degree of nesting
2. Access the variable via the **offset** from this record



### Display

Reduces the costs of scanning the chain to a **constant** (two memory accesses)

The static chain is represented by an **array**

- The $i^{\rm th}$ element is a pointer to the AR of the subprogram at level $i$
- An object in the external scope at level $h$ is at level $j=i_{\text{this}}-h$ in display

**Procedure call** manages the display

1. $Ch$ calls $P$ at nesting level $j$
2. $P$ saves the value of its own ${\rm Display}[\ j\ ]$ in its own AR
3. $P$ sets the pointer to point to a copy of its new AR pointer

![image-20200611192538863](/home/zeep/Documenti/UniTN/2-Semestre/linguaggi.assets/image-20200611192538863.png)



## Dynamic scoping

The **binding** depends on

- **Flow** of control at runtime
- **Order** in which subprograms are called

**Basic rule**: the current association for a name is that determined by the last association to have been called and not yet destroyed

**Implementation**

1. Store the names in the AR
2. Search for names via the stack

![image-20200611193521248](/home/zeep/Documenti/UniTN/2-Semestre/linguaggi.assets/image-20200611193521248.png)



### $A$-list

Associations are stored in an structure managed as a **stack**

![image-20200611193607613](/home/zeep/Documenti/UniTN/2-Semestre/linguaggi.assets/image-20200611193607613.png)



### Central table of references (CRT)

Reduces the costly scanning of $A$-lists to a **constant**

- <u>Static</u>: access in **constant** time
- <u>Dynamic</u>: use **hash** functions

Each name has an **association list** (most recent first, inactive ones then)

![image-20200611194422343](/home/zeep/Documenti/UniTN/2-Semestre/linguaggi.assets/image-20200611194422343.png)



### Comparison

|                                               |     $A$-list      |                      CRT                       |
| :-------------------------------------------: | :---------------: | :--------------------------------------------: |
|             <u>Implementation</u>             |      Simple       |                  More complex                  |
|          <u>Memory usage</u> (names)          | Listed explicitly |     Stored only once, not needed if static     |
| <u>Management costs</u> (entry/exits a block) |    As a stack     | All of the lists of all the names in the block |
|              <u>Access cost</u>               |  Linear in depth  |            Constant (two accesses)             |





# [5.][slide5] Control structure

## Flow control

Structure of control of what determines what is **executed next** by the program 

- **Expressions**
  - Notations
  - Values
  - ~~Problems~~
- **Commands**
  - Assignment
  - Sequential
  - Conditional
  - Iterative
- **Recursion**
  - Tail recursion



## Expressions

> **Expression**: *syntactic entities whose evaluation either produces a value or does not terminate (undefined expression)*



### Notational systems

|                              |       Infix        |         Postfix          |          Prefix          |
| :--------------------------: | :----------------: | :----------------------: | :----------------------: |
|        <u>Syntax</u>         |       $a+b$        |        $a\ b\ +$         |        $+\ a\ b$         |
|    <u>Precedence rule</u>    | :heavy_check_mark: | :heavy_multiplication_x: | :heavy_multiplication_x: |
|  <u>Associativity rules</u>  | :heavy_check_mark: | :heavy_multiplication_x: | :heavy_multiplication_x: |
|   <u>Need parenthesis</u>    | :heavy_check_mark: | :heavy_multiplication_x: | :heavy_multiplication_x: |
| <u>Evaluation difficulty</u> | Not always simple  |    Simple using stack    |      In the middle       |



### Evaluation

The **compiler**

1. <u>Analyzes</u> where are the **operators** and what are the **variables**
2. <u>Represents</u> it internally as a **tree**
3. <u>Produces</u> **object code** that evaluates the expression

The **order of evaluation** of subexpressions is important because of

- Side effects
- Finite arithmetic
- Undefined operands
- Optimization

Two **methods** of evaluation

- **Lazy evaluation**: operands are evaluated only when needed
  - **Short circuit evaluation**: lazy evaluation of boolean expression
- **Eager evaluation**: all operands are evaluated



## Commands

> **Command**: *syntactic entities that do not necessarily have a result*

- May have **collateral effects** (modify the state)
- May yield a **result** (`=` in C)
- Typical of the **imperative** paradigm
- Not present in functional and logical



### Assignment

> **Assignment**: *command that modifies the value of a variable*

Its **evaluation** has a side effect, but doesn't produce a value (except C)

#### Variables

- <u>Imperative</u>: a container of modifiable values, that has a name
- <u>Functional</u>: denotes a value and cannot be modified
- <u>Logical</u>: modifiable under certain conditions (instantiation)
- <u>Object</u>: a reference to a value which has a name (accessible indirectly)
- <u>Java</u>: modifiable for primitive types, reference for object types



### ~~Environment and memory~~

- <u>Imperative</u>
  - **Three semantic domains**
    - Denotable values
    - Storable values
    - Expressible values (result of evaluation)
  - The **semantics** use
    - **Environment**: maps names to denotable values
    - **Memory**: maps locations to storable values
    - Permit aliasing
- <u>Functional</u>
  - Only the **environment**



### Control of flow

- **Explicit**:  `;`, `goto`, blocks
- **Conditional**:  `if`, `case`
- **Iterative**:  determinate/fixed (`for`), indeterminate (`while`)
- **Sequential**:  `C1 ; C2`
- **Compound**:  `(C1 ; C2)`
  - Used in place of a simple command
  - Value is that of the last command



## Recursion

~~Iteration and recursion let us obtain languages that are **Turing-complete** (theoretical notion of what can be computed by a machine)~~

~~Otherwise they are **finite automata**~~

> **Recursion**: *a function or procedure defined in terms of itself*

> **Principle of induction**: a propriety $P$ is true for all natural numbers $n$ iff
>
> - $P(0)$ is true
> - $\forall n \in \N, \ P(n)$ is true implies that $P(n+1)$ is true

> **Inductive definition**: if  $g:\N\times A → A$  is a total function, then there exists a unique total function  $f:\N→A$  such that
>
> - $f(0)=a$
> - $f(n+1)=g(n,f(n))$

A recursive function $F$ is similar to an **inductive definition** of $F$

The value of $F$ at $n$ is defined in terms of the values of $F$ on $m<n$

Language **requirements**

- Programs and procedures to **call themselves**
- **Dynamic** memory management

**Conversion** between recursion and iteration

- Functional, logical → recursion
- Imperative → iteration

Recursion is **less efficient**

- Optimizing compilers
- Tail recursion



### Tail recursion

> **Tail call**: *a call of $g$ in $f$ is in the tail if $f$ returns the value returned by $g$ without further computation*

> **Tail recursion**: *$f$ is tail recursive if it only contains call in the tail (recursive call is the last instruction)*

No need for **dynamic** memory management and more **efficient**

- <u>Space</u>: **constant** (a single A.R)

- <u>Time</u>: **linear** in $n$

It uses the **continuation passing** style

~~You can't understand recursion if you cannot understand recursion~~





# [6.][slide6] Control abstraction

## ~~Abstraction of control~~

- Identify **important proprieties**
- Concentrate only on **relevant questions**
- What is relevant depends on the **scope**

Without knowing the context of a **procedure** $P$, it is necessary to

- Specify $P$
- Write $P$
- Use $P$



## Parameter passing

### Terminology

- **Declaration** / **Definition**

  ```c
  int f (int n)  /* { return n + 1; } */
  ```

- **Value returned**

  ```c
  /* int f (int n) */  { return n + 1; }
  ```

- **Use**

  ```c
  x = f (y + 3);
  ```

- **Parameters**

  - Formal parameter: `n`
  - Actual parameter: `y + 3`



### Methods of parameter passing

- #### Call by value

  - At call evaluate actual (**r-value**) and assign value to formal
  - Formal is a **local variable** on the stack
  - Transmission **only from** `main` to `proc` via parameters
  - Modification to formal **don't affect** actual (no link between parameters)
  - **Expensive** call for large data as they must be copied
  - On exit formals are **removed from the stack**
  - **Simple** semantics: referential transparency, independent from caller

  

- #### Call by reference

  - Reference (address / pointer / **l-value**) to the actual parameter is passed
  - **Aliasing** between formal and actual
  - **Two way** transmission from `main` to `proc` and vice versa
  - Modification to formal **transferred** to actual
  - **Efficient** call, but indirection in body
  - On exit the **link** between parameters is **destroyed**
  - **Complicated** semantics: aliasing

  

- #### Read-only call

  - Procedures are not allowed to change value of formal
  - Statically controlled by the compiler
  - Could be at discretion of compiler (value or reference depending on size)

  

- #### Call by result

  - Similar to value
  - Information cannot be sent from `main` to `proc` via parameters
  - When procedure ends, value of formal is assigned to actual

  

- #### Call by value-result

  - Between value and result
  - When procedure ends, value of formal is assigned to actual

  

- #### Call by name

  - **Copy rule**: a call to $P$ is the same as executing the body of $P$ after substituting the actual parameters for the formal one
  - **Macro expansion**
  - A pair `<exp,env>` is passed
    - `exp` is the actual parameter non evaluated
      Passed as a pointer to the text of `exp`
    - `env` is the evaluation environment (**static scoping**)
      Passed as a pointer to the static chain of the AR of the calling block
  - `exp` is always evaluated **statically** in `env`
  - More expensive
  - Used to pass **functions as arguments** to the other procedures



## Higher order functions

Management of the **environment**

- Passing functions as **arguments**: pointer to the AR in the stack
- Returning functions as **result**: maintain the AR of the resulting function, but not on the stack



### Functions as parameters

#### Binding rules

A procedure passed as a parameter creates a **reference** between a **name** (formal `h`) and a **procedure** (actual `f`)

Determine **non-local environment** applied when `f` called by `h` is executed

- <u>Dynamic scoping</u>
  - **Deep binding**: the one at the moment of creation of link (**calling** block)
  - **Shallow binding**: the one at the moment of call (**internal** block)
- <u>Static scoping</u>: scoping rules are sufficient, always deep (**external** block)

```c
int x = 4;				// static
int z = 0;
int f (int y) {
    return x * y;		// x?
}
void g (int h(int n)) {
    int x = 7;			// dynamic shallow
    z = h(3) + x;		// h(3) + x = ? * 3 + 7
} {
    int x = 5;			// dynamic deep
    g(f);
}
```



#### Closure

> **Closure**: *a record storing a function together with an environment*

1. At **call** of `g` are passed
   - Link to the **code** of function `f`
   - Non-local **environment**
2. The procedure `f` passed as **parameter**
   1. Allocates its **activation record**
   2. Takes the **pointer to the static chain** of the closure



#### Implementation

- <u>Static scope</u>
  - Always uses **deep binding**
  - Static **scoping rules** determines non-local variable
  - ~~No real difference between deep and shallow~~
- <u>Dynamic scoping</u>
  - **Deep binding**: implementation with **closure** to freeze the scope
  - **Shallow binding**: no special implementation needed



#### Summary

- Closure to maintain pointers in the static environment of body of function
- When called, the pointer to the static chain is determined via the closure
- Pointers of the static chain points to the stack
  - AR can be jumped over to access non-local variables
  - Deallocation of AR using stack



### Functions as results

Returning a function `g` in `F`  (`gg = F()`)

- `F` returns a **closure**
- A call to `gg` is relative to the **environment** where `F` is returned
- Modify the **abstract machine** to manage “call by closure” as in `gg()`

```c
void->int F() {
    int x = 1;
    int g() {
        return x + 1;
    }
    return g;
}
void->int gg = F();
int z = gg();
```

When `F` **terminates**, its **AR is removed** from the stack and it's no longer possible to access variables in there

- Use **closure**
- Keep the **activation record**
  - Loss of **LIFO** property
- **Implementation** of this structure
  - No automatic **deallocation**
  - AR on **heap**
  - Static or dynamic **chain** connects the record
  - Call **garbage collector** when needed



## Exception handling

If there's something wrong the program jumps to the **exception handler**, one for each type of error

When the exception is raised it provides automatically **information** about the error (type, position...)



### Structured exit

**Conclude** a part of a computation

- **Exit** from a construct
- **Pass data** via a jump
- **Return control** to the most recent AR
- **Deallocate** AR and other resources no longer needed

Two **constructs**

- **Declaration** of the exception manager (location and code)
- **Commands** for raising exceptions

The **exception handler** is in a **static** block of protected code

```java
class EmptyExcp extends Throwable { int x = 0; };
// Throwable is the superclass of all the exceptions

int average(int[] V) throws EmptyExcp() {
// average is a function that could throw exception EmptyExcp
    if (length(V) == 0) throw new EmptyExcp();
    else { int s = 0; ... }
    return s;
};
...
try {
    average(W);
    // if the list is empty the function throws EmptyExcp
    ...
} catch (EmptyExcp e) { write("Empty array"); }
  // EmptyExcp is catched by the nearest catch in the
  // blocks sequence from where the exception is thrown
```



### Exception propagation

If the excp is **not** handled by the **current procedure**

- Procedure **terminate**
- Excp is raised again at the **calling point**
- Excp is **propagated** along the dynamic chain until
  - We **find** an excp handler
  - We reach the **top level** that provides a **default handler**
- Corresponding **frames** are **removed** from the stack

Each routine has a **hidden excp handler**

- **Restores** the state
- **Propagates** the excp along the stack



### Dynamic chain

```java
void f() throws X {
    throw new X();
}
void g(int sw) throws X {
    if (sw == 0) { f(); }  // no excp handler in this AR -> *
    try { f(); } catch (X e) { write("in g"); }  // if sw != 0
}
...
try { g(0); }
catch (X e) { write("in main"); }  // * <-  if sw == 0
// handler found in the upper AR (of main)
```

When the argument of `g` is the result of the execution, the handler is determined **dynamically**

<u>Implementation</u>

- At the **beginning** of a protected block
  - **Insert** the caller on the stack
- When an **exception** is raised
  - **Remove** the caller from the stack
  - **Check** if this is the right one
    - If not: raise a **new exception** and repeat
    - If yes: pass the control to the **handler**

**Inefficient** due to operations on stack

<u>Better solution</u>: **table of addresses**





# [7.][slide7] Data structures

## Data types

> **Type**: *collection of values (homogeneous and effectively described) together with a set of operators on these values*

What is a type depends on the **programming language**

Used for

- **Project level**: organize the information
- **Program level**: identify and avoid errors
- **Implementation level**: permit optimizations

Each type has

- **Values**
- **Operations**
- **Representation**



### Type system

The **type system** of a language has

- **Predefined** types
- Mechanisms to **define new types**
- **Control** mechanisms
  - Equivalence
  - Compatibility
  - Inference
- Specifies if types are **static or dynamic**

Is **type safe** if at runtime we cannot have **undetected type errors**



## Classification

- **Ordinal / discrete**
  - Booleans, integers, characters, enumerations, interval
  - Each value has a **successor** and a **predecessor** (except for extremes)
  - It is possible to
    - **Iterate** over them
    - Use as **indexes** of an array
- **Scalar**
  - **Ordinals**, reals, complex numbers
  - **Direct representation** in the implementation
  - **Not** composed of **aggregations** of values
- **Structured / non-scalar**
  - **Records** (structs)
    - Collection of **fields**, each of a (possibly different) type
    - Fields are selected by their **name**
  - **Variant records**
    - **Only one** of the the **alternative fields is active** for a specific datum
  - **Arrays**
    - Function from a (scalar) index type to another type
  - **Sets**
    - **Subsets** of the base type
  - **Pointers**
    - **Reference** to an object of another type



### Scalar types

- **Boolean**
  - <u>Val</u>		true / false
  - <u>Op</u>		and, or, not, conditionals
  - <u>Repr</u>	one byte
  - <u>Note</u>	C does not have this type
- **Characters**
  - <u>Val</u>		a single symbol
  - <u>Op</u>		equality, code / decode, (language-dependent)
  - <u>Repr</u>	one byte (ASCII) or two (UNICODE)
  - <u>Note</u>	C does not have this type
- **Integers**
  - <u>Val</u>		0, positive and negative to maxInt
  - <u>Op</u>		$+ \ -\ *$  mod div
  - <u>Repr</u>	several byte (2 or 4)
  - <u>Note</u>	long integers (8 bytes) could have portability problems
- **Reals**
  - <u>Val</u>		rational numbers in a certain interval
  - <u>Op</u>		$+ \ -\ *$  mod div …
  - <u>Repr</u>	several byte (4), floating point
  - <u>Note</u>	long reals (8 bytes) could have severe portability problems
- **Complex numbers**
  - <u>Val</u>		''
  - <u>Op</u>		''
  - <u>Repr</u>	2 reals
  - <u>Note</u>	used in Scheme and Ada
- **Fixed point**
  - <u>Val</u>		rational numbers in a certain interval
  - <u>Op</u>		$+ \ -\ *$  mod div …
  - <u>Repr</u>	several byte (2 or 4)
  - <u>Note</u>	supported by Ada
- **Void**
  - <u>Val</u>		a single value (always the same)
  - <u>Op</u>		none
  - <u>Repr</u>	
  - <u>Note</u>	used to define the type of operations that modify the state without returning a value
- **Enumeration**
  - <u>Val</u>		short integers
  - <u>Op</u>		
  - <u>Repr</u>	1 byte
  - <u>Note</u>	make the program easier to understand
- **Intervals**
  - <u>Val</u>		interval of values of an ordinal type
  - <u>Op</u>		
  - <u>Repr</u>	same of the base type
  - <u>Note</u>	controllable documentation, efficient code



### Structured types

#### Record

- Manipulate data of **different types** in a uniform manner (struct)
- Records can be **nested**
- Storable, expressible and denotable
- Equality usually not defined

**Memory layout**

- **Sequential** storage of fields
- Aligned to **word boundaries**
  - Memory wasted
- **Packed** records
  - Not aligned with word boundaries
  - More costly access



#### Variant record

- Several **exclusive alternatives** (conditional) for some fields
- Variant fields can use the **same location** of memory but **different names**



#### Array

https://stackoverflow.com/questions/56287596/in-which-memory-address-is-stored-an-element-in-a-multidimensional-matrix

Collection of **homogeneous** data

- **Function** from **index** type (discrete) to **element** type (any)

**Multidimensional** array

- **Function** from **index** type (discrete) to **array** type

**Operations**

- **Selection** of an element
- **Slicing**: selection of a contiguous part (only some languages)
  - ~~Sum and other manipulations~~

**Storage**

- Elements stored in **contiguous locations**
- **Order** (row or column) is important in systems with **catching**

**Calculating address** (by row)

- $S_3$ size of element type;  $S_2$ size of a row;  $S_1$ size of a plane
- $\alpha$ address of beginning of `A`
- `&A[i,j,k]` $= i\cdot S_1+j\cdot S_2+k\cdot S_3+\alpha$

**Form / shape**

- Number of **dimensions** or intervals of an index
  - Static form
  - Form fixed on evaluation of the declaration
  - Dynamic form
- Information about the form of the array is maintained by the **compiler**

**Dope vector**

- Maintains the **information** of an array which **form can vary at runtime**
- Contains
  - Pointer to the beginning
  - Number of dimension
  - Lower bound (upper bound if fixed)
  - Space for each dimension
- Stored in the **fixed part of AR**



#### Pointer

- <u>Values</u>	**references** (l-values) and constants (`null nil`)
- <u>Operations</u>
  - **Creation** (function that return a pointer)
  - **Dereferencing** (access the object pointed)
  - **Equality test**
  - **Referring** and **modifying** without dereferencing



## Equivalence and compatibility

Two types $T$ and $S$

- Are **equivalent** if every object of type $T$ is also of type $S$ and vice versa

  - **Equivalence by name**: types with the same name or alias

  - **Structural equivalence**: types with the same structure

    Is the **minimal equivalence relation** that satisfies

    - A type name is eq to itself
    - A type $T$ defined as $T=exp$ is eq to $exp$
    - The same type constructor leads to eq types

  Equivalence controlled by **rewriting** (conversion between eq types)

- $T$ is **compatible** with $S$ if any object of type $T$ can be used in a context where an object of type $S$ is expected

  - $T$ and $S$ are **equivalent**
  - $T$ is a **subset** of $S$
  - **Operations** of $S$ can be performed on $T$
  - **Natural correspondence**
  - $T$ can be made **corresponding** to $S$



### Type conversion

Conversion mechanisms if $T$ is **compatible** with $S$

- **Implicit / coercion**: conversion made by the abstract machine
  - Same values, same representation → **compile time**
  - Different values, same representation → **dynamic control**
  - Different representation → **code for conversion**
- **Explicit / cast**: mentioned at language level
  - Only when the **language** knows how to do the conversion
  - Always with **compatible** types



## Polymorphism

A single value has **different types**

- **<u>Overloading</u>** (ad hoc)
  - Same **symbol** has **different meanings** depending on the context (eg `+`)
  - Resolved at **compile time** after type inference
- **<u>Universal</u>**
  - **<u>Parametric</u>** (explicit or implicit)
    - A value has an **infinite** number of possible **types**, obtained by instantiation of a **general type schema**
    - Function is a **single definition** applied uniformly to all instances of a **general type**
    - **<u>Explicit</u>**
      - Function template written by the programmer
      - Automatic instantiation at link time
    - **<u>Implicit</u>**
      - Language inserts the template automatically
      - Instantiation at compile time
  - **<u>Subtype</u>** (limited explicit)
    - A value has an **infinite** number of possible types, obtained by substituting for a parameter all the **subtypes** of the given one
    - Function is a **single program** that can be applied uniformly to **all legal instances** of the general type



## Handling dangling references

> **Dangling reference**: *pointer to an object that is no longer valid*

- **Tombstones**

  - Structure that acts as an **intermediary** between a pointer and the value
  - When the pointer is **freed**, the tombstone **changes its state**

  <img src="/home/zeep/Documenti/UniTN/2-Semestre/linguaggi.assets/image-20200515133201206.png" alt="image-20200515133201206" style="zoom:80%;" />

- **Locks and keys**

  - Each pointer has an additional **hash code** (lock), which is the same of the object pointed (key)
  - When a pointer is **freed**, the key of the pointed object is set to 0
  - The algorithm check if locks and keys are **equal**

  <img src="/home/zeep/Documenti/UniTN/2-Semestre/linguaggi.assets/image-20200515133319755.png" alt="image-20200515133319755" style="zoom:80%;" />



### Garbage collection

> **Garbage collection**: *the system periodically recovers allocated memory that is no longer in use (no valid way to access it)*

- **Reference count**

  - Each pointed **object takes count** of pointers that **directly reference** to it
  - Objects with reference count **0** can be **restored**

  ![image-20200515134618702](/home/zeep/Documenti/UniTN/2-Semestre/linguaggi.assets/image-20200515134618702.png)

  - <u>Potential problem</u>: **circular structure**

  <img src="/home/zeep/Documenti/UniTN/2-Semestre/linguaggi.assets/image-20200515135427093.png" alt="image-20200515135427093" style="zoom:60%;" />

- **Mark and sweep**

  1. Mark **all** the objects in heap as **unused**
  2. Starting from a pointer not in heap, mark all object **visited** as **used**
  3. **Recover** all **unused** items

  - <u>Problems</u>: **expensive** in performance and space
  - <u>Solutions</u>
    - **Incremental GC**: checks only changes (Java)
    - Stack for **depth first visit**: add marks to the existing structure





# [8.][slide8] Data abstraction

## Abstraction and modularity

> **Abstraction**: *hiding details of the implementation of a structure*

- **Component**: unity of a program (functions, data structures, module)
- **Interface**: types and operations defined in a component, visible outside
- **Specify**: functionality of a component (expressed by properties of interface)
- **Implementation**: data structures and functions inside the component



### Data abstraction

- **Data type**: values and operations
- **Data abstraction**:
  - Representation (implementation) of data and operations
  - Inaccessible to the user, hidden by encapsulation



### Linguistic support

- **Control abstraction**: hide the implementation of procedure bodies
- **Data abstraction**: hide decisions about the representation of data structures and the implementation of operations

Languages provide linguistic support for **information hiding**



### Abstract Data Types

**Separate** the interface from the implementation

**Type checking** to guarantee the separation

- **User** has access only to the **interface**
- **Implementation** is **encapsulated** in constructs (ADT)

**Signature**: list of operations defined for an ADT

- Possibility to use the same signature for **different implementations**



### Encapsulation

**Representation-independent**

- Two correct implementation are **not distinguishable** by the user
- Implementations can be **modified** without interference with their use
- User has **no access** to the implementation



### Modules

**General constructs** for information hiding

- **Interface**: set of names and types
- **Implementation**: declarations of types and functions, hidden declarations





# [9.][slide9] Lambda calculus

https://en.wikipedia.org/wiki/Lambda_calculus

https://stackoverflow.com/questions/34140819/lambda-calculus-reduction-steps

## Function definition

<u>ML syntax of functions</u>

- `fn x => e`
- `x` :  formal parameter (input)
- `e` :  expression, usually using `x ` (output)

<u>λ-calculus</u>

- $\lambda x.e$
- $x$ :  bound variable (input)
- $e$ :  expression (output)

**Formal mathematical basis** for functional programming

Very **expressive** and **Turing-complete**: any computation can be expressed

Used for study of **computability**



### Formal definitions

#### Expressions

**Expression** of λ-calculus has

- **Name** (parameter):  $n$
- Function or application of expressions $e$ to expression
  - **Abstraction** (function):  $\lambda n.e$
  - **Application**:  $e_1\ e_2$  ~~(applies $e_1$ to $e_2$)~~

$\boldsymbol e$ is a **generic expression** that could be

- **Identifier** (variable or constant):  $x$
- **Abstraction** (definition):  $\lambda x.e$
- **Application**:  $e\ e$

**Parenthesis** could be used for readability:  $f_1f_2f_3=((f_1f_2)f_3)$



#### Variables

$e$ is an **expression**

- **Free variables**:  $F_v(e)$
- **Bound variables**:  $B_v(e)$

$x$ is an **identifier**

- $F_v(x)=\{x\}$
- $B_v(x)=\empty$

$(e_1\ e_2)$ is an **application**

- $F_v(e_1\ e_2)=F_v(e_1)\cup F_v(e_2)$
- $B_v(e_1\ e_2)=B_v(e_1)\cup B_v(e_2)$

$\lambda x.e$ is a **λ-expression**

- $F_v(\lambda x.e)=F_v(e)-\{x\}$
- $B_v(\lambda x.e)=B_v(e)\cup \{x\}$
- The abstraction operator ($\lambda$) **removes** a variable from the list of free variables and **adds** it to the bound ones



## Substitution

$e[e'/x]$:  **replace** every occurrence of $x$ by $e'$ in expression $e$

**Result** of substitution written with  $→$

- **Value**
  - If $x$ is an identifier:  $x[e'/x]=e'$
  - If $x \ne y$ is an identifier:  $y[e'/x]=y$
- **Application**
  - $(e_1e_2)[e'/x] = (e_1[e'/x]\ e_2[e'/x])$
- **Abstraction**
  - $x=y\ \and y\in F_v(e')\ \Rightarrow\ (\lambda y.e)[e'/x]=(\lambda y.e)$
  - $x\ne y\ \and y\notin F_v(e')\ \Rightarrow \ (\lambda y.e)[e'/x]=(\lambda y.e[e'/x])$



## Abstraction

Variable $x$ in expression $λx.e$ is a **bound**

Replacing $\lambda x$ by $\lambda y$ the **semantics doesn't change**

- Different expression with the **same meaning**
- The λ-calculus applies $e$ for all $x$ returning an expression $e'$ that could involve the free variables $x$; after abstraction or quantification we have an expression $e'$ that no longer has the variables $x$, which is a bound variable

A function should **not depend on the name** of the formal parameter

- $\lambda x.x=\lambda y.y$
- $\lambda x.e=\lambda y.(e[y/x])$



## Equivalence and reduction

### Alpha

> **α-equivalence**: *two expressions are α-equivalent if one can be obtained from the other by replacing part of one by an α-equivalent one*

$e_1 \equiv e_2$ if they differ only in the **names of the bound** variables

- If $y$ is not present in $e$:  $\lambda x.e \equiv \lambda y.e[x/y]$
- If $y$ is present in $e$:  change the name of the free $y$ to avoid confusion

**α-reduction**: substitution of the names of the bound variables



### Beta

> **β-equivalence**: *equivalence of function evaluation*
> $$
> (\lambda x.e)e'\ →_\beta \ e[e'/x]
> $$

<u>Terminology</u>

- **Redex** (reducible expression):  $(\lambda x.e)e'$
- **Reduct** (result of redex):  $e[e'/x]$

**β-reduction**

- Replacing the bound variables with the argument expression in the body of the abstraction:  $(\lambda x.e)e'\ →_\beta \ e[e'/x]$
- Not symmetric:  $e_1 →_β e_2$ does not imply $e_2 →_β e_1$
- It's not an equivalence relation

A notion of $\equiv_β$ can be defined as the **reflexive** and **transitive** closure of $→_β$

- ~~$e_1→_βe_2\ \Rightarrow\ e_1=_β e_2$~~
- ~~$\forall e,\ e=_βe$~~
- ~~$e_1=_β e_2\ \Rightarrow\ e_2=_β e_1$~~
- ~~$e_1=_β e_2\ \and\ e_2=_β e_3\ \Rightarrow\ e_1=_β e_3$~~

#### Confluence

> **Theorem**: if by a β-reduction, $e$ can be reduced to $e_1$ and $e$ can be reduced to $e_2$, then there exists a $e_3$ such that both $e_1$ and $e_2$ can be reduced to $e_3$ by a β-reduction

~~If $e$ can be reduce to normal form, the **order** of the reductions does **not matter**~~

~~$e_1\equiv_β e_2$ means that there is at least a sequence of β-reductions from $e_1$ to $e_2$~~



### Normal form

**Normal form**: expression with **no redex** (have no β-reductions)

**Repeated** applications of **β-reductions** to an expression could

- Terminate in a **normal form**
- Run **forever**
  - $(λx.xx)(λx.xx) →_β (xx)[(λx.xx)/x] = (λx.xx)(λx.xx)$

~~<u>Examples</u>~~

- ~~Normal form:  $λx.λy.x$~~
- ~~Not normal form:  $λx.((λy.y)x)$~~
  - ~~$(λy.y)x→_βx$~~
  - ~~$λx.((λy.y)x)→_βλx.x$~~



## Natural numbers

Natural numbers can't be represented as they are, they are **not variables**

**Coding** is based on the **Peano** axioms

- ~~$0$ is a natural number~~
- ~~If $n$ is a natural number, `succ(n)` is its successor~~

**Church**'s idea

- $0$ is coded as $λf.λx.x$
  - $f$ applied to $x$ zero times
- `succ(n)`: apply $f$ to $n$
  - Abstraction that takes a function and a variable and returns a variable

$n$ is represented by the **higher order function** that maps any function $f$ to its $n$-fold composition

- The “value” of the numeral $n$ is equivalent to the **number of times the function is applied** to its argument

$$
f^n=f \circ f \circ f\circ··· \circ f \ \ (n \text { times})
$$

Every **Church numeral** $n$ represents the application for $n$ times of a **function** $f$ that takes **two parameters** $f$ and $x$

- <u>Notation</u>:  $nfx$  means apply $f$ for $n$ times to $x$
- $f$ is first applied to parameter $x$ and then successively to its own result $fx$
- If $f$ is the successor function and $x$ is $0$, the result is the numeral $n$
- Church numeral is function itself and not the result (do anything $n$ times)

| Number | Function definition | Lambda expression |
| ------ | ------------------- | ----------------- |
| $0$    | $0fx=x$             | $λf.λx.x$         |
| $1$    | $1fx=fx$            | $λf.λx.fx$        |
| $2$    | $2fx=f(fx)$         | $λf.λx.f(fx)$     |
| $3$    | $3fx=f(f(fx))$      | $λf.λx.f(f(fx))$  |
| …      | …                   | …                 |
| $n$    | $nfx=f^nx$          | $λf.λx.nfx$       |



### Successor

> <u>Definition</u>
> $$
> {\rm succ}(n) = λn.λf.λx.f(nfx)
> $$

Applied to the λ definition of $n$, it gives the λ definition of $n+1$ (apply $f$ to $n$)
$$
\begin {align}
1={\rm succ}(0) &= (λn.λf.λx.f ((nf)x))(λf.λx.x) \\
&= (λn.λg.λy.g((ng)y))(λf.λx.x) \\
&= λg.λy.g(((λf.λx.x)g)y) \\
&= λg.λy.g((λx.x)y) \\
&= λg.λy.gy \\
&= λf.λx.fx
\end {align}
$$

$$
\begin {align}
2 = {\rm succ}(1) &= (λn.λf.λx.f((nf)x))(λf.λx.fx) \\
&= (λn.λg.λy.g((ng)y))(λf.λx.fx) \\
&= λg.λy.g(((λf.λx.fx)g)y) \\
&= λg.λy.g((λx.gx)y) \\
&= λg.λy.g(gy) \\
&= λf.λx.f(fx)
\end {align}
$$



### Addition

$n+m$  means apply $f$ for $n$ times to the result of applying $f$ for $m$ times to $x$

- Body of $m$ is $mfx$ and body of $n$ is $nfx$
- Substitute body of $m$ in place of $x$ in body of $n$ :  $nf(mfx)$

> <u>Definition</u>
> $$
> n+m=λn.λm.λf.λx.nf(mfx)
> $$

<u>Esempio</u>
$$
\begin {align}
2=n&=λf.λx.f(fx) \\
3=m&=λf.λx.f(f(fx)) \\
\\ 2+3
&=λn.λm.λf.λx.(nf)(mfx)(λf.λx.f(fx))(λf.λx.f(f(fx))) \\
&=λn.λm.λg.λy.(ng)(mgy)(λf.λx.f(fx))(λf.λx.f(f(fx))) \\
&=λg.λy.((λf.λx.f(fx))g)((λf.λx.f(f(fx)))gy) \\
&=λg.λy.(λx.g(gx))(g(g(gy))) \\
&=λg.λy.g(g(g(g(gy)))) \\
&=λf.λx.f(f(f(f(fx)))
\end {align}
$$



## ~~Extensions~~

~~It is possible to write **abbreviations** (abuse of notation)~~

- ~~Natural numbers~~
- ~~Operations ($λx.(x+2)$)~~
- ~~Conditions ($λx.{\rm if}\ x=2\ {\rm then}\ 0\ {\rm else}\ 1$)~~



## Recursion

~~In functional paradigm, recursion is the only way of **iteration**~~

In λ-calculus: **function evaluation** giving a **name** to a λ-expression

There is no notion of an **external environment** in the λ-calculus

<u>Recursion</u>

```ocaml
> val rec f = fn n => if n=0 then 0 else 1+f(n-1);
val f = fn: int -> int
(* same as  val f = fn n => n;  *)
```

$$
f=λn.\text{if }n=0 \text{ then } 0 \text{ else } 1+f(n-1)
$$

<u>Abstraction of</u> $G$

```ocaml
(* eliminate recursion *)
> val G = fn f => fn n => if n=0 then 0 else 1+f(n-1);
val G = fn: (int -> int) -> int -> int
```

$$
G=λf.λn.\text{if }n=0 \text{ then } 0 \text{ else } 1+f(n-1)
$$

This is an **equation**, not a definition

- In the form $f=G(f)$
- $G$ is a higher order function ~~(argument and result are functions)~~
- Find $h$ that satisfy  $h=_βGh$



## Combinators and fixpoints

> **Combinator**: *expression without free variables*

> **Fixpoint**: *function that applied to another function gives the same function*

**Find a fixpoint** of $G$

- Given a function $G$, find $f$ such that $f=_βGf$
- Using the **Y-combinator**

$$
Y=λf.(λx.f(xx))(λx.f(xx))
$$

$YG$ is a **fixpoint** for $G$

- $YG=G(YG)$
- $\forall\ e,\ Ye=e(Ye)$

<u>Demonstration</u>

- Definition: 		$Ye=λf.(λx.f(xx))(λx.f(xx))e$
- Application : 	$Ye=(λx.e(xx))(λx.e(xx))$
- Substitution:	$Ye=e(λx.e(xx))(λx.e(xx))=e(Ye)$
- Result: 				$Ye=e(Ye)\ →\ YG=G(YG)$
- $YG$ is a fixpoint for $G$

A **higher-order function** $F$ is a fixpoint of $g$ if

- $F(g)=g(F(g))$
- $F=λg.g(F(g))$

<u>Evaluation</u>
$$
\begin{align}
F(g)&=(λg.g(F(g)))g \\
&=g(F(g)) \\
g(F(g))&=g((λg.g(F(g)))g) \\
&=g(g(F(g))) \\
&\ ...
\end{align}
$$
The reduction **diverges**:  $F(g)=g(F(g))=g(g(F(g)))=\ ...$



## ML

Defining **non recursive** functions evaluated using **β-reduction**

```ocaml
(*  Y = λf.(λx.f(xx))(λx.f(xx))  *)
> val Y = fn f => (fn x => f(x x))(fn x => f(x x));
poly: : error: Type error in function application.
	Function: x : 'a -> 'b
	Argument: x : 'a -> 'b
	Reason:   Can’t unify 'a to 'a -> 'b
			  (Type variable to be unified occurs in type)
```



### Types

In the expression `(x x)`, `x` must be at the same time

- A **function** of type `'a -> 'b`
- An **object** of type `'a`

`'a = 'a -> 'b` is **impossible**

- **Isomorphism** of values of the first type to values of the second

The Y-combinator works in λ-calculus because it's **untyped**

**Recursive** definition of a type in ML

- ```ocaml
  datatype 'b T = F of ('b T -> 'b);
  ```

- `F` maps values of `'b T -> 'b` to values of `'b T`

Replacing the recursion in the **fixed point operator** by recursion in datatype

```ocaml
> val Y = fn f => (fn x => f(x(F x))) (fn (F x) => f(x(F x)));
val Y = fn: ('a -> 'a) -> 'a
```

```ocaml
> fn x => (x (F x));
val it = fn: ('a T -> 'a) -> 'a
> fn f => (fn x => f(x(F x)));
val it = fn: ('a -> 'b) -> ('a T -> 'a) -> 'b
```



### Application of Y

Using the **fixed point operator**

1. **Define** factorial

   ```ocaml
   val fact_closed = fn f => fn n =>
     if n = 0 then 1 else n * f (n-1);
   ```

2. Take the **fixpoint**

   ```ocaml
   val fact = Y fact_closed;
   ```

3. **Infinite** recursion

ML uses **eager evaluation**, and this expression does not converge

Other **combinators** works properly under eager evaluation



### Z-combinator

$$
Z = λf.(λx.f (λv.((xx)v))(λx.f (λv.((xx)v)))
$$

**Abstracts** the application of `(x x)` via the variable `v`, limiting the eager evl

```ocaml
> val Z = fn f =>
	(fn  x    => f (fn v => (x (F x)) v))
	(fn (F x) => f (fn v => (x (F x)) v));
val Z = fn: (('a -> 'b) -> 'a -> 'b) -> 'a -> 'b
```



### Application of Z

1. **Define** factorial

   ```ocaml
   > val fact_closed = fn f => fn n =>
   	if n = 0 then 1 else n * f (n-1);
   val fact_closed = fn: (int -> int) -> int -> int
   ```

2. Find the **fixpoint** using Z

   ```ocaml
   > val fact = Z fact_closed;
   val fact = fn: int -> int
   ```

3. Now it **works**

   ```ocaml
   > fact 5;
   val it = 120: int
   ```



## Derive the Y-combinator

- Generic **recursive function**:	 $f(n+1)=g(f(n),n)$
- **Closed form** of the function:	$f_c=λf.λn.e$
  - Without free variables
  - $e$ is a closed expression
- This is the **solution** of:				$f=f_cf$
- This can be **evaluated as**:		 $f=Yf_c$

$f_c$ is a **non recursive** version of $f$

- It takes as **argument** the function $f$, to be **invoked recursively**
- $f(n)=(f_cf)n \iff f=f_cf$

<u>Example</u>: **factorial**
$$
f_c=λf.λn.\text{if }n=0 \text{ then } 0 \text{ else } n · f (n − 1)\\
G=λf.λn.\text{if }n=0 \text{ then } 0 \text{ else } n · ff (n − 1)\\
f=f_cf\ →\ f=GG
$$

$$
G=_β λf.(λh.λn.\text{if }n=0 \text{ then } 0 \text{ else } n · h(n − 1))(ff)\\
G=_β λf.(f_c(ff ))
$$

$$
f=GG\ \and\ (λh.(hh))G →_β GG = f\ \ \Rightarrow \\
\Rightarrow\ \ f =_β (λh.(hh))(λf.f_c(ff ))
$$

- Reverse β-reduction

$$
\begin{align}
f&=_β (λg.(λh.(hh))(λf.g(ff )))f_c \\
 &=_α (λg.(λh.(hh))(λh.g(hh)))f_c
\end{align}
$$

$$
f=_βYf_c\ \ \Rightarrow\\ Y = (λg.(λ(hh))(λh.g(hh))) \\
Y = (λg.(λh.g(hh))(λh.g(hh)))
$$

 

## Confluence

<u>Proposition</u>
$$
s→_βt \ \ \Rightarrow\ \ s>t
$$

Parallel and nested **β-reduction relation $\mathbf >$**

<u>Proof</u>
$$
s=(λx.u)v\ →_β\ u[v/x]=t \ \and \\
\and \ u>u \ \and\ v>v \ \  \Rightarrow\\
\Rightarrow \ \ (λx.u)v>u[v/x]
$$

<u>Examples</u>

- $s>s$
- $s>s' \ \Rightarrow\ λx.s>λx.s'$
- $s>s' \and t>t' \ \Rightarrow\ (st)>(s't')$
- $s>s' \and t>t' \ \Rightarrow\ (λx.s)t>s'[t'/x]$


<u>Proposition</u>
$$
s>t_1\ \and\ s>t_2\ \  \Rightarrow\\\Rightarrow \ \ 
\exist\ u \ |\ t_1>u\ \and\ t_2>u
$$
<u>Proof</u>

- **Induction** on $s$ (see below)
- If $s$ is an **atom**   $\Rightarrow \ \ s=t_1=t_2=u$
- $s=λx.s'\ \  \Rightarrow \ \ t_i=λx.t_i'\ \and\ s'>t_i' \ \ \ (i = 1,2)$
  - Induction hypothesis:  $\exist\ u'\ | \ \forall\ i,\ t_i'>u'$
  - $t_i=λx.t_i'>λx.u'=u$

<u>Final case</u>

The case where $s = (s_1\ s_2)$ is a straightword case analysis on the structures of $s_1$ and $s_2$

<u>Conclusion</u>:  $→_β$ is conﬂuent



## Converse

<u>Proposition</u>
$$
s>t \ \ \Rightarrow\ \ s→_β^*t
$$

**Induction** on the derivation of $s>t$

$→_β^*$ means a **sequence** of reductions

<u>Proof</u>
$$
s=(λx.u)v>u'[v'/x] \ \and \\
\and \ u>u' \ \and\ v>v'  \ \and \\
\and \ u→^*u' \ \and\ v→^*v'
\ \  \Rightarrow\\\Rightarrow \ \ 
(λx.uv) →_β^* (λx.u')v →_β^* (λx.u')v' →_β u'[v'/x]
$$

$u→^*u' \ \and\ v→^*v'$ is the **induction hypothesis**



## Additional lemmas

$$
λx.s > t ⇒∃s'.t = λx.s' ∧ s > s'
$$

$$
s > s' ∧ t > t' ⇒ s[t/x] > s'[t'/x]
$$





# [↑](#↓)

 