# Mathematical logic – Brief

|       |       |                                                              |
| ----- | :---: | -----------------------------------------------------------: |
| Logic | Brief | [🗀][root]    [🗍](http://www.datascientia.education/cl-2020/calendar.html)    [🗪](https://github.com/avillafiorita/cl-2020/issues) |

[TOC]



# [1.][root] Introduction

## [1.1.][pdf-11] Models

### Mental model

> **Mental model**: *human representation of the world*

![gnome-shell-screenshot-M7R7R0](logica.assets/gnome-shell-screenshot-M7R7R0.png)



### Logical model

> **Logical model**: *meaning of language made explicit*

![gnome-shell-screenshot-EC67R0](logica.assets/gnome-shell-screenshot-EC67R0.png)

- **Interpretation**:  $I : L → D$  (many-to-one)
- **Truth-relation / entailment / satisfiability / ⊨**: relation which associates what is true in the model with a subset of the sentence of the language
  - $S_{\sf sentence}\in T \iff \vDash S$





## [1.2.][pdf-12] Language

### Definitions

> **Symbol**: *atomic token* 

> **Alphabet**: *set of symbols*

> **Language**: *set of symbols and formation rules to compose them to build correct sentences*



### Syntax and semantics

$$
\rm language\ =\ syntax\ +\ semantics \;
$$

> **Syntax**: *the way a language is written*

- ~~Determined by a **set of rules** saying how to construct the expressions of the language from the alphabet~~

> **Semantics**: *the way a language is interpreted*

- ~~Determines the **meaning of expressions**~~

> **Expression**: *syntactic construct*

> **Meaning**: *relationship between expressions and elements of some universe of meanings*





## [1.3.][pdf-13] Logical modeling

### Formal language

$$
\rm formal\ language\ =\ formal\ syntax\ +\ formal\ semantics
$$

> <u>Definition</u>  (**Formal syntax**)
>
> - Alphabet
> - Rules for phrase construction
> - Algorithm for correctness checking

> <u>Definition</u>  (**Formal semantics**)
>
> - Interpretation function $I : L → D$
>   - ~~Relation between expressions in $L$ and elements in $D$~~
>- Domain $D$
> - Formal syntax



### Extensional semantics

> **Intended interpretation of $L$**: *the meanings which are intended to be attached to the symbols and propositions*

> **Extension of a proposition**: *totality, or class, or set of all objects $D$ to which the proposition applies*



### Logic

A logic has three **fundamental components**

- **Formal language** ($L$)
  ~~Defines what can be correctly said~~
- **Interpretation function** ($I$)
  ~~Defines how symbols are to be interpreted in intended domain and model~~
- **Entailment relation** ($\vDash$)
  ~~Defines/computes two relations in the model~~
  - **Validity / satisfiability**
  - **Logical consequence**



#### Theory and model

Given $\{L,\, I,\, ⊨\}$, a logic allows to define two **components**

> **Theory**: *set of sentences (usually infinite) in $L$ which are assumed true in the intended model, as computed via entailment starting from finite set (called itself theory, or finite presentation of theory)*

> **Model**: *set of facts (usually infinite) expressed in the language describing the mental model (the part of the world observed), in agreement with the theory and the interpretation function*



### Decidability and complexity

> **Reasoning**: *deriving consequences of what is known*

~~**Decidability** of reasoning~~

- ~~A **logic is decidable** if there is an **effective method** for determining whether a **formula is included in a theory**~~
- ~~A **decision procedure** is an algorithm that, given a decision **problem**, terminates with the **correct yes/no answer**~~
- ~~All logic in this course but first-order logic are decidable~~





## [~~1.4.~~][pdf-14] ~~Formal and informal languages/models~~







# [~~2.~~][root] ~~Set theory~~

## [~~2.1.~~][pdf-21] ~~Introduction~~

## [~~2.2.~~][pdf-22] ~~Sets~~

## [~~2.3.~~][pdf-23] ~~Relations~~

## [~~2.4.~~][pdf-24] ~~Functions~~







# [3.][root] Propositional logic

## [3.1.][pdf-31] Intuition

### Proposition

> **Proposition**: *statement about what is the case in the world*

- ~~**Atomic language element** of PL~~
- ~~Can be **true** or **false**~~
- ~~Different propositions can be **equivalent**~~





## [3.2.][pdf-32] Language

### PL language

> <u>Definitions</u>  (**Propositional alphabet**)
>
> - **Logical symbols and priority**:  $¬ \,\ \ {\tt >}\ \ ∧ \ \ {\tt >}\ \ ∨ \ \ {\tt >}\ \ → \ \ {\tt >}\ \ ≡$
> - **Non logical symbols**:  propositional variables $P$ of set $\tt PROP$
> - **Separator symbols**:  $(\ \ )$

> <u>Definitions</u>  (**Well formed formulas**)
>
> - **Atomic formula**
>   - ${\sf Every}\ P\in\tt PROP$
> - **Formula**
>   - Every atomic formula
>   - $A,B\,\ {\sf formulas}\ \Rarr\ ¬ A\,,\ A ∧ B\,,\ A ∨ B \,,\ A → B\,,\ A ≡ B\ \ \sf formulas$

> <u>Definitions</u>  (**Constants and variables**)
>
> - **Constant**: simple proposition
> - **Variable**: proposition where a variable can be substituted with a constant, a variable or in general any formula





## [3.3.][pdf-33] Satisfiability

### Interpretation of PL

> <u>Definition</u>  (**Propositional interpretation**)
>
> Function that specify if a proposition is true or false
> $$
> I :\ {\tt PROP} → \{⊤,⊥\}
> $$

- A PI is a **subset** $S$ of $\tt PROP$ such that $I$ is the **characteristic function** of $S$

  $$
  A\in S \iff I(A)=⊤
  $$



### Satisfiability of a formula

> <u>Definition</u>  (**Satisfiability**) 
>
> A formula $A$ is **satisfied by** (**true in**) an interpretation $I$ (in symbols $I\vDash A$) according to the following inductive definition
>
> - $I(P)=⊤\ \ \ \ \Rarr\ \ \ I\vDash P\,,\ \ \ P\in\tt PROP$
>   - $I\,\nvDash\,A\, \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \Rarr\ \ \ \ I\vDash ¬A$
>   - $I\vDash A\ \ \ \, \and\ \ \ \ I\vDash B\ \ \ \ \Rarr\ \ \ \ I\vDash A\and B$
>   - $I\vDash A\ \ \ \, \or\ \ \ \ I\vDash B\ \ \ \ \Rarr\ \ \ \ I\vDash A\or B$
>   - $I\vDash A\ \ \, →\ \ \ I\vDash B\ \ \ \ \Rarr\ \ \ \ I\vDash A→ B$
>   - $I\vDash A \iff I\vDash B\ \ \ \ \Rarr\ \ \ \ I\vDash A\equiv B$



### Checking satisfiability

> <u>Procedure</u>  (**Checking satisfiability**)
>
> Given a formula $A$, of primitive propositions $P_I$, and an interpretation $I$
>
> 1. **Replace** each occurrence of $P_I$ in $A$ with the truth value assigned by $I$
> 2. **Apply** the definitions for connectives

> <u>Algorithm</u>  (**Lazy evaluation**) ~~(~~[~~Go to MCDP~~](###Model checking)~~)~~
>
> - $A=p$
>
>   ```c
>   bool check(I ⊨ p)
>   	if I(p) == true
>   		return true
>   	else
>           return false
>   ```
>
> - $A=B\and C$
>
>   ```c
>   bool check(I ⊨ B ∧ C)
>       if check(I ⊨ B)
>           return check(I ⊨ C)
>       else
>           return false
>   ```
>
> - $A=B\or C$
>
>   ```c
>   bool check(I ⊨ B ∨ C)
>   	if check(I ⊨ B)
>   		return true
>       else
>           return check(I ⊨ C)
>   ```
>
> - $A=B→ C$
>
>   ```c
>   bool check(I ⊨ B → C)
>       if check(I ⊨ B)
>           return check(I ⊨ C)
>   	else
>           return true
>   ```
>
> - $A=B\equiv C$
>
>   ```c
>   bool check(I ⊨ B ≡ C )
>       if check(I ⊨ B)
>           return check(I ⊨ C)
>       else
>           return ¬(check(I ⊨ C))
>   ```





## [3.4.][pdf-34] Validity and unsatisfiability

### Formulas classification

~~(~~[~~Go to Properties~~](# Properties - Open and closed formulas)~~)~~

> <u>Definition</u>  (**Formulas classification**)
>
> A **formula** $A$ is
>
> - **Valid**             $\ \iff\ \forall I\,,\ \ \ I\vDash A$
> - **Satisfiable**     $\,\iff\ \exist I\ \ |\ \ I\vDash A$
> - **Unsatisfiable** $\iff\ \nexists I\ \ |\ \ I\vDash A$

> <u>Propositions</u>  (**Implications**)
>
> - ${\rm VAL}(A)\ \Rarr\ {\rm SAT}(A)\iff ¬{\rm UNSAT}(A)$
> - ${\rm UNSAT}(A)\iff ¬{\rm SAT}(A)\ \Rarr\ ¬{\rm VAL}(A)$
>
> $$
> \begin{array}{l}
> \begin{array}{c}
> A && ¬A \\ \hline
> \rm VAL &→& \rm UNSAT \\
> \rm SAT &→& \rm ¬VAL \\
> \rm ¬VAL &→& \rm SAT \\
> \rm UNSAT &→& \rm VAL 
> \end{array}
> &&
> {{\rm VAL}(A)\iff {\rm UNSAT}(¬A) \\
> {\rm SAT}(A)\iff {\rm ¬VAL}(¬A)}
> \end{array}
> $$

><u>Theorem</u>  (**Refutation principle - validity**)  [~~(Please tell me if it is correct)~~](mailto:davide.vecchi@studenti.unitn.it)
>$$
>⊨ A \iff \{¬ A\}\ \sf unsatisfiable
>$$
><u>Proof</u>
>
>- Suppose that  $⊨A$
>   - $\Rarr \ \ \forall I,\ I\vDash A\ \ \Rarr\ \ I ⊭ ¬A$
>   - $\Rarr \ \ \nexists I\ \ |\ \ I\vDash ¬A\ \ \Rarr\ \ \{¬A\}\ {\sf unsatisfiable}$
>- Suppose that $\{¬A\}\ {\sf unsatisfiable}$
>    - $\Rarr\ \ ⊭ ¬A\ \ \Rarr\ \ ⊨A$



### Sets of formulas

> <u>Definition</u>  (**Set of formulas**)
>
> A **set of formulas** $Γ$ is
>
> - **Valid**             $\ \iff\ \forall A\inΓ\,,\ \ \forall I\,,\ \ \ I\vDash A$
> - **Satisfiable**     $\,\iff\ \forall A\inΓ\,,\ \ \exist I\ \ |\ \ I\vDash A$
> - **Unsatisfiable** $\iff\ \forall A\inΓ\,,\ \ \nexists I\ \ |\ \ I\vDash A$

> <u>Proposition</u>  (**Finite set**)
> $$
> \forall\,Γ = \{A_1 , ..., A_n \},\ \ \ {\rm VAL}(Γ)\iff {\rm VAL}(A_1\and ··· \and A_n) \\
> \sf (resp.\, {\rm SAT}\ and\ {\rm UNSAT})
> $$





## [3.5.][pdf-35] Logical consequence and equivalence

### Definitions

> **Logical consequence**: *a formula $A$ is a LC of a set of formulas $Γ$ iff*
> $$
> Γ\vDash A\ \iff\ \forall F\in Γ,\ \ \forall I:I\vDash F\,,\ \ \ I\vDash A
> $$

> **Logical equivalence**: *two formulas $F$ and $G$ are logically equivalent iff* 
> $$
> F ≡ G\ \iff\ \forall I\,,\ \ \ I(F) = I(G)
> $$



### Properties of LC

$Γ$ and $Σ$ are two sets of formulas and $A$ and $B$ two formulas

- **Reflexivity**                   $\{ A \} ⊨ A$
- **Monotonicity**              $\,Γ ⊨A \ \Rarr\ Γ ∪ Σ ⊨ A$
- **Cut**                               $\,Γ ⊨A \and Σ ∪ \{ A \} ⊨B \ \Rarr\ Γ∪ Σ ⊨ B$
- **Compactness**              $\,Γ ⊨A\ \Rarr\ \exist\ Γ_0 ⊆ Γ\ |\ Γ_0 ⊨ A$
- **Deduction theorem**    $\,Γ,\, A ⊨B \iff Γ ⊨A → B$
- **Refutation principle**   $\,Γ ⊨A \iff Γ∪ \{¬A\}\ \sf unsatisfiable$

> <u>Theorem</u>  (**Refutation principle - LC**)
> $$
> Γ ⊨φ\ \iff\ Γ ∪\{¬φ\}\ {\sf unsatisfiable}
> $$
> <u>Proof</u>
>
> - Suppose that  $Γ ⊨φ$
>   - $\Rarr \ \ \forall I\ |\ I\vDash Γ\,,\ I\vDash φ\ \ \Rarr\ \ I ⊭ ¬φ$
>   - $\Rarr \ \ \nexists I\ \ |\ \ I\vDash Γ\and I \vDash ¬φ$
> - Suppose that  $I ⊨Γ$
>   - $Γ ∪\{¬φ\}\ {\sf unsatisfiable}\ \ \Rarr\ \ I ⊭ ¬φ\ \ \Rarr\ \ I ⊨φ$





## [3.6.][pdf-36] Axioms and theories

### Propositional theory

> **Propositional theory**: *set of formulas closed under the LC relation*
> $$
> T\ {\sf theory}\ \iff\ T ⊨A\ \Rarr\ A \in T
> $$

- A propositional theory always contains an **infinite set of formulas**
  - ~~Any theory $T$ contains at least **all the valid formulas**, which are infinite~~

> **Logical closure**: *for any set of formulas $Γ$*
> $$
> {\rm cl}(Γ)=\{A\ |\ Γ\vDash A \}
> $$

- For any set $Γ$, the closure ${\rm cl}(Γ)$ is a **theory**



### Axiomatization

> **Set of axioms**: *a set of formulas $Ω$ is a set of axioms for a theory $T$ if*
> $$
> \forall A\in T\,,\ \ Ω ⊨A
> $$

- $Γ$ is a set of axioms for ${\rm cl}(Γ)$

> **Finitely axiomatizable theory**: *a theory $T$ is finitely axiomatizable if it has a finite set of axioms*



### ~~Logic based systems~~

- ~~Used for **representing** and **reasoning** about **knowledge**~~
- ~~Composed by~~
  - ~~**Reasoning system**~~
  - ~~**Knowledge base**~~
    - ~~Consists of a finite **collection of formulas** in a logical language~~
    - ~~**Answers queries** submitted to it by means of a **reasoning system**~~

~~<img src="logica.assets/gnome-shell-screenshot-KVEQS0.png" alt="gnome-shell-screenshot-KVEQS0" style="zoom:80%;" />~~

- ~~**Tell** action~~
  - ~~Incorporates the **new knowledge** encoded in an **axiom** (formula)~~
  - ~~Allows to build a **knowledge base**~~
- ~~**Ask** action~~
  - ~~Allows to **query what is known**~~
    - ~~If a formula $φ$ is a LC of the axioms contained in the KB ($KB ⊨ φ$)~~







# [4.][root] Reasoning via truth tables

## [~~4.1.~~][pdf-41] ~~Summary~~



## [4.2. ][pdf-42]Decision problems

### Reasoning / Decision problems

Four types of **questions**

- **Model checking**            ${\rm MC}(I, φ)\ :\ I ⊨ φ$
  ~~What is the truth value of $φ$ in $I\,$?~~
- (Un)**Satisfiability**          ${\rm SAT}(φ)\ :\ ∃I\ |\ I ⊨φ$
  ~~Is there a model $I$ that satisfies $φ\,$?~~

- **Validity**                          ${\rm VAL}(φ)\ :\ \forall I,\ I⊨φ$
  ~~Is $φ$ satisfied by all the models $I\,$?~~
- **Logical consequence**   ${\rm LC}(Γ, φ)\ :\ Γ ⊨φ$
  ~~Is $φ$ satisfied by all the models $I$ that satisfy all the formulas in $Γ\,$?~~



### Model checking

> <u>Definition</u>  (**MC decision procedure**)
>
> Algorithm that checks if a **formula** $φ$ is satisfied by an **interpretation** $I$
> $$
> \begin{array}{c}
> {\rm MCDP}(φ,I) & = & ⊤ & \iff & I ⊨ φ \\
> {\rm MCDP}(φ,I) & = & ⊥ & \iff & I ⊭ φ
> \end{array}
> $$

> <u>Algorithm</u>  (**MCDP naive**)
>
> 1. **Replace** each occurrence of a variable $P$ in $φ$ with the truth value $I(P)$
> 2. Recursively apply the **reduction rules** for connectives
>

> <u>Algorithm</u>  (**MCDP lazy evaluation**)
>
> Use lazy evaluation rules to skip **superfluous evaluations**
>
> - $A=p$
>
>   ```c
>   bool MCDP(I, p)
>   	if I(p) == true
>   		return true
>   	else
>           return false
>   ```
>
> - [… see satisfiability rules](###Checking satisfiability)



### Satisfiability

> <u>Definition</u>  (**Satisfiability decision procedure**)
>
> Algorithm that takes in input a **formula** $φ$ and checks if $φ$ is (un)satisfiable
> $$
> \begin{array}{cclcl}
> {\rm SDP}(φ) & = & {\sf satisfiable} & \iff & \exist I\ \ |\ \ I ⊨φ\\
> {\rm SDP}(φ) & = & {\sf unsatisfiable} & \iff & \nexists I\ \ |\ \ I\vDash A
> \end{array}
> $$

- ~~If ${\rm SDP}(φ) = {\sf satisfiable}$, it can **return at least a model** $I$ that satisfies $φ$~~



### Validity

> <u>Definition</u>  (**Validity decision procedure**)
>
> Algorithm that checks if a **formula** is valid
>
> $\rm VDP$ can be based on $\rm SDP$ by exploiting the **refutation principle (VAL)**
> $$
> \begin{array}{cclccl}
> {\rm VDP}(φ) & = & ⊤ & \iff & {\rm SDP}(¬φ) & = & {\sf unsatisfiable}\\
> {\rm VDP}(φ) & = & ⊥ & \iff & {\rm SDP}(¬φ) & = & {\sf satisfiable}
> \end{array}
> $$

- ~~Interpretation $I$ returned by ${\rm SDP}(¬φ)$ is a **counter-model** for $φ$~~



### Logical consequence

> <u>Definition</u>  (**LC procedure**)
>
> Algorithm that checks whether a **formula** $φ$ is a LC of a **finite set of formulas** $Γ = \{γ_1,..., γ_n \}$
>
> $\rm LDCP$ can be based on $\rm SDP$ by exploiting the **refutation principle (LC)**
> $$
> \begin{array}{cclcl}
> {\rm LCDP}(Γ,φ) & = & ⊤ & \iff & {\rm SDP}(γ_1 ∧···∧ γ_n∧¬φ)\  =\  {\sf unsatisfiable}\\
> {\rm LCDP}(Γ,φ) & = & ⊥ & \iff & {\rm SDP}(γ_1 ∧···∧ γ_n∧¬φ)\  =\  {\sf satisfiable}
> \end{array}
> $$

- ~~Interpretation $I$ returned by ${\rm SDP}(γ_1 ∧···∧ γ_n∧¬φ)$ is a **model** for $Γ$ and a **counter-model** for $φ$~~





## [4.3.][pdf-43] Conjunctive normal form

### Definitions

> **Literal**: *either a variable or the negation of a variable*

> **Clause**: *disjunction of literals.*

> **Conjunctive normal form**: *conjunction of clauses*
> $$
> (I_{11}∨···∨I_{1n_1})∧···∧(I_{m1}∨···∨I_{mn_m}) \ \ \equiv \ \ \bigwedge_{i=1}^m\bigg(\bigvee_{j=1}^{n_j}I_{ij}\bigg)
> $$



### Properties

#### Properties of $∧$ and $∨$

- **Commutativity**   $φ*ψ ≡ ψ* φ$
- **Absorption**         $\,φ*φ ≡ φ$



#### Properties of clauses

- **Order** of literals does not matter
- Multiple literals can be **merged**
- Clauses as **set of literals**



#### Properties of formulas in CNF

Same as **clauses** ~~(with the right substitution of terms)~~

<u>In addition</u>

- **Existence**: every formula can be reduced into CNF
- **Equivalence**:  $⊨{\rm CNF}(φ) ≡ φ$



### ~~Reduction in CNF~~

> ~~**CNF function**: *recursive function that transforms a formula in its CNF*~~
>
> [~~See slide 9~~][pdf-43]

[~~Examples slides 10-12~~][pdf-43]





## [4.4.][pdf-44] DPLL SAT decision procedure

### Satisfiability of a set of clauses

> ~~**Partial evaluation**: *partial function that associates to some variables of the alphabet $\, \tt PROP$ a truth value and can be undefined for the other elements*~~

- ~~Allows to **construct models** for a set of clauses **incrementally**~~
- ~~To check satisfiability, we don't need to know all the truth values~~



### Partial valuation

> <u>Procedure</u>  (**DPLL**)
>
> 1. Starts with an **empty valuation** (undefined for all letters)
> 2. **Extends** it step by step to letters in $N$



### DPLL

> <u>Procedure</u>  (**Simplification of a formula** by an evaluated literal)
>
> For any CNF formula $φ$ and atom $p$, the notation $φ|_p$ stands for the formula obtained from $φ$ by
>
> 1. **Replacing** all occurrences of $p$ by $⊤$
> 2. **Simplifying** the result by removing
>    - **Clauses** containing the disjunctive term $⊤$
>    - **Literals** $¬⊤ =\,\,⊥$ in all remaining clauses
>
> ~~Similarly $φ|_{¬p}$ is the result of~~
>
> 1. ~~Replacing $p$ in $φ$ by $⊥$~~
> 2. ~~Simplifying the result, according to the process dual to above~~

> **Unit clause**: *CNF formula $φ$ that contains a single-literal clause $\,C = \{l\}$*

> <u>Procedure</u>  (**Unit propagation**)
>
> **Simplification** of $φ$
>
> ```c++
> void UnitPropagation(φ, I)  // I(φ) initially empty
> 	while φ ⊇ {l}
> 		φ = φ|l
>     	if l == p
>         	I(p) = true
>     	if l == ¬p
>         	I(p) = false
> ```

- **Outputs**
  - $\big\{\big\}\ \Rarr\ \sf satisfiable$
  - $\big\{\{\},\,···\big\}\ \Rarr\ \sf unsatisfiable$
- **UP does not terminate** when the CNF
  - Isn't in the **previous forms**
  - Does not contain **unit clauses**



### DPLL definition

> <u>Procedure</u>  (**DPLL**)
>
> **Extension of the UP** method that can solve the satisfiability
>
> ```c
> bool DPLL(φ, I)  // I(φ) initially empty
> 	UnitPropagation(φ, I)
> 	if φ ⊃ {}
> 		return false
> 	if φ = {}
> 		return true  // exit with I
>  
> 	// heuristic choice of l in order to achieve efficiency
> 	l = selectLiteralIn(C ∈ φ)
>  
> 	// l == p  → ln = ¬p
> 	// l == ¬p → ln = p
>  	return (DPLL(φ|l , I ∪ (I(l) = true)) || 
>  			DPLL(φ|ln, I ∪ (I(l) = false)))
> ```







# [5.][root] PL - reasoning as deduction

## [5.1.][pdf-51] Reasoning as deduction

### Deduction / Proof

> <u>Definition</u>  (**Deduction / Proof**)
>
> Given
>
> 1. **Premises** $\,Γ$
> 2. **Conclusion** $\,A$
>
> A deduction is a **sequence** or a **tree** of nodes, where
>
> - Each **node** of the deduction is labeled with a **formula**
> - **Links** are labeled with **motivation** (inference rules)
> - **Root** nodes are **premises**
> - **Leaf** nodes are **conclusion**
>
> $Γ \vdash A$ means that (equivalently)
>
> - There is at least a **deduction** which connects $Γ$ and $A$
> - $A$ can be **deduced**/**derived** from $Γ$

**Key properties** that have to be satisfied

- **Correctness theorem** ($⇒$)
- **Completeness theorem** ($⇐$)

$$
Γ \vdash φ \iff Γ ⊨ φ
$$





## [~~5.2.~~][pdf-52] ~~Hilbert systems (VAL - forward chain)~~





## [5.3.][pdf-53] Tableaux systems (SAT - backward)

### Tableaux calculus and method

> ~~**Tableaux calculus**: *algorithm solving the problem of satisfiability*~~

- Tableaux **rooted in** $\bf φ$ is a method to search **interpretations that satisfies** $\bf φ$
- Tableaux exaustively builds a branch for **any possible truth assignment**
  - **Interpretation** corresponding to a **branch** should **satisfy all the formulas** that appear in the branch

**Tableau method** allows to perform **automated deduction**

- <u>Given</u>:  set of premises $Γ$ and conclusion $φ$
- <u>Task</u>:    prove $Γ ⊨φ$
- <u>How</u>:    show $Γ ∪\{¬φ\}$ is not satisfiable via **refutation procedure**

> **Refutation procedure**: *add the complement of the conclusion to the premises and derive a contradiction*



### ~~Constructing proofs~~

- ~~**Data structure**: a proof/deduction is represented as a tableau~~
  - ~~Binary tree which nodes are labeled with formulas~~
- ~~**Start**: put premises and negated conclusion into root of empty tableau~~
- ~~**Expansion**: apply expansion rules to the formulas on the tree~~
  - ~~Add new formulas and split branches~~
- ~~**Closure**: close branches that are obviously contradictory~~
- ~~**Success**: a proof is successful iff we can close all branches~~



### Expansion rules

~~(~~[~~Go to FO tableaux~~](# First order tableaux)~~)~~

> <u>Definition</u>  (**Standard / Smullyan-style tableau rules**)
> $$
> \begin{array}{c}
> \begin{array}{c}
>  α\ {\sf rules} \\
>  \begin{array}{c}
>    \begin{array}{c}
>      φ∧ψ \\ \hline
>  	φ \\
>      ψ
>    \end{array} \ \
>    \begin{array}{c}
>      ¬(φ∨ψ) \\ \hline
>      ¬φ \\
>      ¬ψ
>    \end{array} \ \
>    \begin{array}{c}
>      ¬(φ→ψ) \\ \hline
>      φ \\
>      ¬ψ
>    \end{array}
>  \end{array}
> \end{array}
> \ \ & \ \
> \begin{array}{c}
>  ¬¬\ {\sf elimination} \\
>  \begin{array}{c}
>    ¬¬φ \\ \hline
>    φ \\
>    \
>  \end{array}
> \end{array}
> \end{array}
> \\
> $$
>
> $$
> \begin{array}{c}
> \begin{array}{c}
>  β\ {\sf rules} \\
>  \begin{array}{c}
>    \begin{array}{c}
>      φ∨ψ \\ \hline
>  	φ\ \vline\ ψ \\ \
>    \end{array} \ \
>    \begin{array}{c}
>      ¬(φ∧ψ) \\ \hline
>      ¬φ\ \vline\ ¬ψ \\ \
>    \end{array} \ \
>    \begin{array}{c}
>      φ→ψ \\ \hline
>      ¬φ\ \vline\ ψ \\ \
>    \end{array}
>  \end{array}
> \end{array}
> \ \ & \ \
> \begin{array}{c}
>  {\sf Branch\ closure} \\
>  \begin{array}{c}
>    φ \\
>    ¬φ \\ \hline
>    \sf X
>  \end{array}
> \end{array}
> \end{array}
> $$
>
> $$
> φ\ \lang\,≡\,,\iff\rang\ ψ\ \ \ \ :=\ \ \ \ (φ → ψ) ∧ (ψ → φ)
> $$



### Smullyan's uniform notation

Two **types of formulas** / rules

- **Conjunctive** / determininstic ($α$)
- **Disjunctive** / splitting ($β$)

$$
\begin{array}{c}
  \begin{array}{c|cc}
    α      & α_1 & α_2 \\
    \hline
    φ∧ψ    & φ   & ψ   \\
    ¬(φ∨ψ) & ¬φ  & ¬ψ  \\
    ¬(φ→ψ) & φ   & ¬ψ
  \end{array}
\ \ \ & \ \ \
  \begin{array}{c|cc}
    β      & β_1 & β_2 \\
    \hline
    φ∨ψ    & φ   & ψ   \\
    ¬(φ∧ψ) & ¬φ  & ¬ψ  \\
    φ→ψ    & ¬φ  & ψ
  \end{array}
\end{array}
$$

$α$ and $β$ rules can be **stated** as follows
$$
\begin{array}{c}
  \begin{array}{c}
    α \\ \hline α_1 \\ α_2
  \end{array}
\ \ \ & \ \ \
  \begin{array}{c}
    β \\ \hline β_1 \ \vline\ β_2 \\ \
  \end{array}
\end{array}
$$



### Definitions

> ~~**Closed branch**: *branch which contains a formula and its negation* ($\sf X$)~~

> ~~**Open branch**: *branch which isn't closed* ($\sf O$)~~

> **Closed tableaux**: *tableaux with all branches closed*

> **Derivation / LC**: *given a formula $φ$ and a finite set of formulas $\,Γ$,*
> *$\,Γ \vdash φ$ means that there exists a closed tableau for $\,Γ ∪ \{¬φ\}$*



### Test validity and satisfiability

A tableaux for $Γ$ builds an **interpretation** for $Γ$

**Construct tableaux** to test

- **Satisfiability of a set $Γ$**
  - <u>Root</u>:  **all formulas** in $Γ$
    - <u>Close off</u>         $\,→$   $Γ$ **not satisfiable**
    - <u>Not close off</u>   $→$   $Γ$ **satisfiable**
- **Validity of a formula** $φ$
  - <u>Root</u>:  $\bf ¬φ$
    - <u>Close off</u>   $→$   $φ$ logically **valid**
- $φ$ is a **logical consequence** of $Γ$
  - <u>Root</u>:  **all formulas** in $Γ$ and $\bf ¬φ$
    - <u>Close off</u>   $→$   $φ$ **LC** of $Γ$
- **Logical equivalence of two formulas**
  - If **LC** holds in **both direction**

$$
\begin{array}{c|c}
\ φ \ &  ¬φ \ & \ φ \ &  ¬φ \ & \ φ \ &  ¬φ\ \\
⟋\ ⟍ & ⟋\ ⟍ & ⟋\ ⟍ & ⟋\ ⟍ & ⟋\ ⟍ & ⟋\ ⟍ \\
\sf X\ \ \ \ \ X & \sf X\ \ \ \ \ X & \sf O\ \ \ \ \ X & \sf O\ \ \ \ \ X & \sf O\ \ \ \ \ O & \sf O\ \ \ \ \ O \\
\hline
\rm ¬SAT &\rm VAL &\rm SAT &\rm¬VAL   \\
\rm   ↓  &\rm  ↓  &\rm\and &\rm\and &\rm SAT &\rm ¬VAL    \\
\rm ¬VAL &\rm SAT &\rm¬VAL &\rm SAT
\end{array}
$$



### Build interpretations

For each **open branch** and for each **atom** $p$ in the formula, $I(p)$ is defined as
$$
I(p)=
\begin{cases}
\top & {\sf if}\ p\ {\sf belongs\ to\ the\ branch} \\
\bot & {\sf if}\ ¬p\ {\sf belongs\ to\ the\ branch}
\end{cases}
$$
If neither $p$ nor $¬ p$ belong to the branch, $I(p)$ is defined in **arbitrary way**



### Soundness and completeness

> <u>Theorem</u>  (**Soundness**)
> $$
> Γ ⊢ φ \ \ \Rarr\ \ Γ ⊨ φ
> $$

> <u>Theorem</u>  (**Completeness**)
> $$
> Γ ⊨ φ \ \ \Rarr\ \ Γ ⊢ φ
> $$



### Decidability

> <u>Theorem</u>  (**Decidability**)
>
> Tableau method is a **decision procedure** for classical PL
>
> <u>Proof</u>
>
> To **check validity** of $φ$, develop a tableau for $¬ φ$
>
> Because of **termination**, we will eventually get a tableau that is either closed (1) or that has a branch that cannot be closed (2)
>
> 1. The formula $φ$ must be valid (**soundness**)
> 2. The branch that cannot be closed shows that $¬ φ$ is satisfiable, so $φ$ cannot be valid (**completeness**)







# [7.][root] First order logic

## [7.1.][pdf-71] Intuition

### First order logic

> <u>Definitions</u>  (**FOL constructs**)
>
> **FOL** assumes world contains
>
> - **Constants**
> - **Predicates / relations**
> - **Functions**
>
> In FOL it is possible to **build**
>
> - **Atomic propositions**
>
>   - Applying **predicate to constants**
>
> $$
> \rm Predicate(Constants)
> $$
>
> - **Propositions**
>
>   - Applying **function to a constant**
>     Then **predicate to the resulting** object
>
>   $$
>   \rm Predicate(Function(Constant))
>   $$
>
>   - Applying universal (existential) **quantifiers to variables**
>     This allows to **quantify to arbitrary objects** of the universe
>
>   $$
>   {\rm [Qt]}\ x.{\rm Proposition}(x)
>   $$





## [7.2.][pdf-72] Language

### Syntax

> <u>Definition</u>  (**Alphabet**)
>
> - **Logical symbols**
>   - **Constant**  $⊥$
>   - **PL connectives**  $¬,\, ∧,\, ∨,\, →,\, ≡$
>   - **Quantifiers**  $∀,\, ∃$
>   - Infinite set of **variable symbols**  $x_1 ,\, x_2 ,\,...$
>   - **Equality symbol**  $=$  ~~(optional)~~
> - **Non logical symbols**
>   - Set $c_1 ,\, c_2 ,\, . . .$ of **constants symbols[^\*]**
>   - Set $P_1 ,\, P_2 ,\, . . .$ of **relational symbols[^\**]**
>   - Set $f_1 ,\, f_2 ,\, . . .$ of **functional symbols[^\**]**
>
> [^\*]: Functions with **arity equal to 0**
> [^\**]: Each of which is associated with its **arity** (number of arguments)


- **Non logical symbols**
  - Depends from the **domain** we want to model
  - ~~Must have an **intuitive interpretation** on such a domain~~



### Terms and formulas

> <u>Definition</u>  (**Language**)
>
> - **Terms**
>   - Every **constant** $c_i$ and every **variable** $x_i$
>   - $t_1 ,\, . . . ,\, t_n {\sf\ terms},\, f_i {\sf\ functional} \ |\ \#f_i=n \ \ \Rarr\ \ f (t_1 ,\, . . . ,\, t_n ) \sf\ term$
> - (Well formed) **Formulas**
>   - $t_1,\,t_2 {\sf\ terms}\ \ \Rarr\ \ t_1 = t_2 \sf\ formula$
>   - $t_1 , ... , t_n {\sf\ terms}\,,\ P_i {\sf\ relational}\ |\ \#P_i=n \ \ \Rarr\ \ P_i (t_1 , ... , t_n) \sf\ formula$
>   - $A,\, B {\sf\ formulas} \ \Rarr \ \lang⊥, A ∧B, A → B, A ∨B, ¬A, A ≡ B\rang\sf\ formulas$
>   - $A {\sf\ formula},\, x {\sf\ variable} \ \ \Rarr\ \ \lang ∀x.A,\,  ∃x.A\rang \sf\ formulas$



### Common mistakes

- **Use of $∧$ with $∀$**

- **Use of $→$ with $∃$​**



### Representing variations quantifiers

> <u>Definition</u>  (**At least $n$**)
> $$
> ∃x_1···∃x_n \bigg(\bigwedge_{i=1}^n φ(x_i)\ ∧\ \bigwedge_{i\ne j=1}^n x_i ≠ x_j\bigg)
> $$

> <u>Definition</u>  (**At most $n$**)
> $$
> ∀x_1···∀x_{n+1} \bigg(\bigwedge_{i=1}^{n+1} φ(x_i)\ →\ \bigvee_{i\ne j=1}^{n+1} x_i = x_j\bigg)
> $$





## [7.3.][pdf-73] Interpretation function

### Interpretation function

> <u>Definition</u>  (**Interpretation for a language $L$**)
>
> A FO interpretation for the language
> $$
> L = (c 1 ,\, c 2 ,\, . . . ,\, f 1 ,\, f 2 ,\, . . . ,\, P 1 ,\, P 2 ,\, . . . )
> $$
> is a **pair** $(∆,\, I )$ where
>
> - $∆$ is a non empty set called **interpretation domain**
>
> - $I$ is is a function, called **interpretation function**
> $$
> I:L→Δ
> $$
>   Let $n$ the **arity** of $f_i$ and $P_i$
>
>   - $I(c_i )∈∆\,$              ~~(elements of the domain)~~
>   - $I(f_i ) : ∆^n → ∆$    ~~($n$-ary function on the domain)~~
>   - $I(P_i ) ⊆ ∆^n$           ~~($n$-ary relation on the domain)~~
> 

[Example slides 4-5][pdf-73]





## [7.4.][pdf-74] Satisfiability w.r.t an assignment

### Interpretation of terms

> <u>Definition</u>  (**Assignment**)
>
> Function $a$ from set of variables to domain of interpretation $∆$
> $$
> a[x/d ]
> $$
> Denotes the **assignment that coincides** with $a$ on all the variables but $x$, which is associated to $d$

> <u>Definition</u>  (**Interpretation of terms**)
>
> The **interpretation** $I$ of a term $t$ w.r.t. the assignment $a$, in symbols $I(t)[a]$, is **recursively defined** as follows
> $$
> \begin{align}
> I(x_i )[a] &\ \ =\ \ a(x_i ) \\
> I(c_i )[a] &\ \ =\ \ I(c_i ) \\
> I \big( f (t_1 , . . . , t_n )\big)[a] &\ \ =\ \ I ( f )\big(I(t_1 )[a],\, . . . ,\, I(t_n )[a]\big)
> \end{align}
> $$

[Example slide 3][pdf-74]



### Satisfiability of formulas

> <u>Definition</u>  (**Satisfiability of a formula w.r.t. $a$**)
>
> An interpretation $I$ satisfies a formula $φ$ **w.r.t. the assignment** $a$ according to the following **rules**
> $$
> \begin{array}{l}
> I ⊨ t_1 = t_2 &[a] &\ \ \iff\ \ & I(t_1 )[a] = I(t_2 )[a]\\
> I ⊨ P (t_1 , . . . , t_n )&[a] &\ \ \iff\ \ & \lang I(t_1 )[a], . . . , I(t_n )[a]\rang ∈ I(P )\\
> I ⊨ φ ∧ ψ&[a] &\ \ \iff\ \ & I ⊨ φ[a] \and I ⊨ ψ[a]\\
> I ⊨ φ ∨ ψ&[a] &\ \ \iff\ \ & I ⊨ φ[a] \or I ⊨ ψ[a]\\
> I ⊨ φ → ψ&[a] &\ \ \iff\ \ & I ⊭ φ[a] \or I ⊨ ψ[a]\\
> I ⊨ ¬ φ&[a] &\ \ \iff\ \ & I ⊭ φ[a]\\
> I ⊨ φ ≡ ψ&[a] &\ \ \iff\ \ & I ⊨ φ[a] \iff I ⊨ ψ[a]\\
> I ⊨ ∃x.φ&[a] &\ \ \iff\ \ & \exist\, d ∈ ∆ \ |\ I ⊨ φ[a[x/d ]]\\
> I ⊨∀x.φ&[a] &\ \ \iff\ \ & \forall d ∈ ∆,\ I ⊨ φ[a[x/d ]]
> \end{array}
> $$

[Example slides 6-7][pdf-74]





## [7.5.][pdf-75] SAT, VAL, LC, LE

### Free variables and terms

> <u>Definition</u>  (**Free occurrence**)
>
> A free occurrence of a variable $x$ is an occurrence of $x$ which is **not bounded by** a (universal or existential) **quantifier**
>
> - Any occurrence of $x$ in $t_i$ is free in $P (t_1 ,\,...,\, t_n )$
> - Any f.o. of $x$ in $φ$ or in $ψ$ is also free in $φ ∧ ψ,\, ψ ∨ φ,\, ψ → φ,\, ¬φ$
> - Any f.o. of $x$ in $φ$ is free in $∀y.φ$ and $∃y.φ$ if $y$ is distinct from $x$

> **Ground formula**: *formula that doesn't contain any variable*

> **Closed formula**: *formula that doesn't contain f.o. of variables*

> **Free variable**: *variable $x$ is free in $φ$ (denote by $φ(x)$) if there is at least a free occurrence of $x$ in $φ$*

- ~~Free variables represent **individuals** which must be **instantiated** to make the formula a meaningful proposition~~

> **Free term**: *term $t$ is free for variable $x$ in formula $φ$ iff all the occurrences of $x$ in $φ$ don't occur in the scope of a quantifier of some variables in $t$*



### Satisfiability and validity

> <u>Definition</u>  (**Model, satisfiability and validity**)
>
> - An interpretation $I$ is a **model** of $φ$ under the assignment $a$ if
>
> $$
> I ⊨ φ[a]
> $$
>
> - A formula $φ$ is **satisfiable** if
>
> $$
> \exist\, I,\,\exist\, a \ \ |\ \ I ⊨ φ[a]
> $$
>
> - A formula $φ$ is **unsatisfiable** if it is not satisfiable
>
> $$
> ¬\big(\exists\, I,\,\exists\, a \ \ |\ \ I ⊨ φ[a]\big)
> $$
>
> - A formula $φ$ is **valid** if 
>
> $$
> \forall\, I,\,\forall\, a \,, \ \ I ⊨ φ[a]
> $$

><u>Definition</u>  (**Logical consequence**)
>
>A formula $φ$ is a LC of a set of formulas $Γ$, in symbols $Γ ⊨ φ$, if
>$$
>\forall\, I,\,\forall\, a \,, \ \ I ⊨ Γ[a]\ ⇒\ I ⊨ φ[a]
>$$

- ~~$I ⊨ Γ[a]$ means that $I$ satisfies all the formulas in $Γ$ under $a$~~
- ~~**Logical equivalence** defined as **bidirectional LC**~~



### Open and closed formulas

For **closed formulas**

- SAT, VAL, LC, LE **don't depend on the assignment** of variables

- We can **omit the assignment** and write $I ⊨ φ$


<u>In general</u>
$$
I ⊨ φ[a] \iff I ⊨ φ[a'] \\
{\sf when}\ [a]\ {\sf and}\ [a']\ {\sf coincide\ on\ the\ variables\ free\ in}\ φ
$$

- $[a]$ and $[a']$ can **differ** on all the other variables
- With **closed formulas** holds for **all assignments**





## [~~7.6.~~][pdf-76] ~~Exercises~~





## [7.7.][pdf-77] Finite domains

### FD with names for every element

> **Unique name assumption**: *assumption under which the language contains a name for each element of the domain*
> $$
> {\rm UNA}\ :=\ φ_{∆=\{c_1 ,...,c_n\}}\ =\ \bigg(\bigwedge^n_{i≠j=1} c_i ≠ c_j\ ∧\ ∀x \Big(\bigvee^n_{i=1} x=c_i\Big)\bigg)
> $$

- ~~The language contains the constants $c_1 ,\, . . . ,\, c_n$ , and each constant is the name of **one and only** one domain element~~
- ~~Finite domain with a **constant name** for every elements~~
- ~~Constants are also elements of the **domains**~~



### Finite predicate extension

The **assumption** that states that a **predicate $P$ is true** only for a finite set of objects for which the language contains a name, can be formalized as
$$
∀x.P (x) ≡ ( x = c_1 ∨··· ∨ x = c_n )
$$



### Grounding

Under the hypothesis of FD with the UNA, **FO formulas** can be **propositionalized** (**grounded**) as
$$
φ_{∆=\{ c_1 ,...,c_n \}} ⊨ ∀x.φ(x ) ≡ φ(c_1 ) ∧ ··· ∧ φ(c_n)
$$

$$
φ_{∆=\{ c_1 ,...,c_n \}} ⊨ \exist x .φ(x ) ≡ φ(c_1 ) \or ··· \or φ(c_n )
$$

Generalizing
$$
φ_{∆=\{ c_1 ,...,c_n \}} ⊨ ∀x_1···∀x_k.φ(x_1,...,x_k ) ≡ \bigwedge_{c_{i_1},..,c_{i_k}\in\\\in\{c_1,..,c_n\}} φ(c_{i_1},...,c_{i_k})
$$

$$
φ_{∆=\{ c_1 ,...,c_n \}} ⊨ \exist x_1···\exist x_k. φ(x_1,...,x_k ) ≡ \bigvee_{c_{i_1},..,c_{i_k}\in\\\in\{c_1,..,c_n\}} φ(c_{i_1},...,c_{i_k})
$$

Grounding allows to **reduce FOL reasoning to PL reasoning**





## [7.8.][pdf-78] Analogies with databases

### Query answering in FOL

- ~~<u>Purpose</u>: knowing the **set of objects** which share a **given property**~~
- ~~<u>General purpose</u>: knowing the set of **$n$-tuples of objects** which are in a certain **$n$-ary relation**~~
- A **property in FOL** can be expressed by a **formula** $φ(x_1 , . . . , x_n )$ with free variables $x_1 , ... , x_n$

> <u>Definition</u>  (**Query answering**)
>
> Given
>
> - **Interpretation** $I$ (a database instance) of a FOL language
> - **Formula** $φ(x_1 , . . . , x_n )$ with $n$ free variables
>
> Find all the **$n$-tuples** of elements of domain $(d_1 , . . . , d_n ) ∈( ∆^I)^n$ such that
> $$
> I ⊨φ\big[a[x_1 /d_1 ··· x_n /d_n ]\big]
> $$

**Analogy** with relational DBs

1. $φ(x_1 , . . . , x_n )$ represents one DB **relation**
2. Relational **DB** as a **set of formulas**

[Examples slides 3, 5-6][pdf-78]



### Requirements

**FOL** can be used to **formalize relational databases** iff

- **Domain** of interpretation $∆$ is **finite**
- There is the **UNA**
- $L$ contains **no functional symbols** (relational language)
- **Unknown facts** (not stated in tables) are assumed to be **false**
  - Closed World Assumption



#### ~~Correspondences~~

| ~~FOL~~                                     | ~~Relational DB~~                             |
| ------------------------------------------- | --------------------------------------------- |
| ~~Non logical symbols of $L$~~              | ~~Database schema [^n1]~~                     |
| ~~Domain $∆$ [^n2]~~                        | ~~Set of values which appears in the tables~~ |
| ~~Interpretation $I$ of a relation~~        | ~~Tuples that belong to each relation~~       |
| ~~“Certain” formulas on $L$~~               | ~~Queries over the database~~                 |
| ~~Interpretation of formulas of $L$ [^n3]~~ | ~~Answers~~                                   |

[^n1]: (tables)
[^n2]: Elements of the language and of the domain have the same name
[^n3]: (queries)







# [8.][root] FOL - reasoning as deduction

## [~~8.1.~~][pdf-81] ~~Reasoning problems (recap)~~

## [~~8.2.~~][pdf-81] ~~Hilbert systems (VAL - forward chain)~~



## [8.3.][pdf-82] Tableaux systems (SAT - backward)

### First order tableaux

> <u>Definition</u>  (**First order tableaux**)
>
> A tableau is a **rooted tree**, where each **node** carries a **FO sentence** (closed formula), and the **children** of a node $n$ are generated by applying a set of **expansion rules** to $n$ or to one of the ancestors of $n$

> <u>Definition</u>  (**Expansion rules**)
>
> The expansion rules for a **FO semantic tableaux** are
>
> - $\bf α$ and $\bf β$ **rules** ~~(~~[~~See propositional semantic tableaux~~](# Expansion rules  ~~(~~[~~Go to first order tableaux~~](# First order tableaux)~~)~~)~~
>   $$
>   \\ \begin{array}{c}
>     \begin{array}{c}
>       α\ {\sf rules} \\
>       \begin{array}{c}
>         \begin{array}{c}
>           φ∧ψ \\ \hline
>       	φ \\
>           ψ
>         \end{array} \
>         \begin{array}{c}
>           ¬(φ∨ψ) \\ \hline
>           ¬φ \\
>           ¬ψ
>         \end{array} \
>         \begin{array}{c}
>           ¬(φ→ψ) \\ \hline
>           φ \\
>           ¬ψ
>         \end{array}
>       \end{array}
>     \end{array}
>   &
>     \begin{array}{c}
>       β\ {\sf rules} \\
>       \begin{array}{c}
>         \begin{array}{c}
>           φ∨ψ \\ \hline
>       	φ\ \vline\ ψ \\ \
>         \end{array} \
>         \begin{array}{c}
>           ¬(φ∧ψ) \\ \hline
>           ¬φ\ \vline\ ¬ψ \\ \
>         \end{array} \
>         \begin{array}{c}
>           φ→ψ \\ \hline
>           ¬φ\ \vline\ ψ \\ \
>         \end{array}
>       \end{array}
>     \end{array}
>   \end{array} \\ 
>   $$
>
> - Extended with rules that deal with the **quantifiers**
>   $$
>   \ \\ \begin{array}{c}
>     \begin{array}{c}
>       γ\ {\sf rules} \\
>       \begin{array}{c}
>         \begin{array}{c}
>           \forall x.φ(x) \\ \hline
>       	φ(t)
>         \end{array} \ \
>         \begin{array}{c}
>           ¬\exist x.φ(x) \\ \hline
>           ¬φ(t)
>         \end{array}
>       \end{array}
>     \end{array}
>     \ \ & \ \
>     \begin{array}{c}
>       δ\ {\sf rules} \\
>       \begin{array}{c}
>         \begin{array}{c}
>           ¬\forall x.φ(x) \\ \hline
>       	¬φ(c)
>         \end{array} \ \
>         \begin{array}{c}
>           \exist x.φ(x) \\ \hline
>           φ(c)
>         \end{array}
>       \end{array}
>     \end{array}
>   \end{array} \\ \
>   $$
>
>   - $t$ is a **term free** for $x$ in $φ$
>   - $c$ is a **new fresh constant** not previously appearing in the tableaux

> **Fresh constant/variable**: *term that denote an unconditioned object for denoting an unknown object*



### Substitution

> **Substitution**: *$φ[x/t]$ denotes the formula we get by replacing each free occurrence of the variable $x$ in the formula $φ$ by the term $t$*

- ~~This is admitted if $t$ does **not contain any variable** $y$ such that $x$ occurs in the scope of a quantifier for $y$~~
- ~~If $φ(x )$ is a **free variable** and $t$ is a **term**, we use the notation $φ(t)$ (instead of the more precise $φ[x/t]$) to represent the **substitution** of $x$ for $t$ in $φ$~~





## [~~8.4.~~][pdf-84] ~~Examples~~

[~~Examples PDF 82 slides 13-16~~][pdf-82]

[~~Examples PDF 84~~][pdf-84]





## [8.5.][pdf-85] Termination

### Termination of a FOL tableaux

In contrast to PL, FOL tableaux construction is **not guaranteed to terminate**

If the **formula** $φ$ that labels the **root** is

- **Unsatisfiable**, then construction
  - Is **guaranteed to terminate** and tableau can be **closed**
- **Satisfiable**, then construction either
  -  Is **guaranteed to terminate** and tableau is **open**
  - Does **not terminate**

> <u>Problem</u>  (**Search dilemma**)
>
> If you have **not** yet been able to **close** the tableaux, is it either
>
> - because the formula is **satisfiable**?
> - because you have **not found the way** to construct the tableaux?
>
> You cannot know!





## [8.6.][pdf-86] Counter models

### Saturated branches

> ~~**$\bf γ$-formulas**: *formulas in the form $∀xφ$ or $¬∃xφ$*~~

> <u>Definition</u>  (**Saturated open branch**)
>
> **Open branch** where
>
> - Every **non-literal** has been **analyzed** at least once
> - Every $\bf γ$**-formula** has been **instantiated with every term** we can construct using the function symbols on the branch

- ~~**Failing proof**: tableau with an SOB can never be closed~~
- ~~We can **stop** an declare the proof a failure~~



### ~~Counter models~~

- ~~If the construction of a tableaux ends in a **saturated open branch**, the~~
  ~~tableaux can be used to **define the interpretation** which is also a model~~
  ~~$M$ for all the formulas on that branch~~
- ~~$M$ is **finite by construction**, it is a subset of other possibly infinite models~~
- ~~A **model** $M$, being an interpretation, must tell how to **interpret constants** (the elements of the domain), function symbols, and predicate symbols~~
- ~~**Domain**: set of all terms constructible using function symbols on branch~~
- ~~**Function symbols**: interpreted as themselves (or using the fake constants)~~
- ~~**Predicate symbols**: interpreted in terms of their occurrences in the branch~~







# 🗍

[root]: ../Logica
[pdf-11]: ../Logica/L1.T11.Introduction.Modeling.pdf
[pdf-12]: ../Logica/L2.T12.Introduction.Language.pdf
[pdf-13]: ../Logica/L2.T13.Introduction.LogicalModeling.pdf
[pdf-14]: ../Logica/L2.T14.Introduction.WhyLogic.pdf
[pdf-21]: ../Logica/L3.T21.SetTheory.Introduction.pdf
[pdf-22]: ../Logica/L3.T22.SetTheory.BasicNotions.pdf
[pdf-23]: ../Logica/L3.T23.SetTheory.Relations.pdf
[pdf-24]: ../Logica/L3.T24.SetTheory.Functions.pdf
[pdf-31]: ../Logica/L3.T31.PL.Intuition.pdf
[pdf-32]: ../Logica/L3.T32.PL.Language.pdf
[pdf-33]: ../Logica/L4.T33.PL.Satisfiability.pdf

[pdf-34]: ../Logica/L4.T34.PL.Validity.Unsat.pdf
[pdf-35]: ../Logica/L5.T35.PL.LogCE.pdf
[pdf-36]: ../Logica/L5.T36.PL.theories.pdf
[pdf-41]: ../Logica/L5.T41.PL.Reasoning.TruthTables.Summary.pdf
[pdf-42]: ../Logica/L6.T42.PL.Reasoning.TruthTables.DecisionProblems.pdf
[pdf-43]: ../Logica/L6.T43.PL.Reasoning.TruthTables.SATCNF.pdf
[pdf-44]: ../Logica/L6.T44.PL.Reasoning.TruthTables.SATDPLL.pdf
[pdf-51]: ../Logica/L7.T51.PL.Reasoning.Deduction.pdf
[pdf-52]: ../Logica/L7.T52.PL.Reasoning.Hilbert.calculus.pdf
[pdf-53]: ../Logica/L7.T53.PL.Reasoning.Tableau.pdf
[pdf-71]: ../Logica/L9.T71.FOL.Intuition.pdf
[pdf-72]: ../Logica/L9.T72.FOL.Language.pdf
[pdf-73]: ../Logica/L10.T73.FOL.Interpretation.function.pdf
[pdf-74]: ../Logica/L10.T74.FOL.SAT.wrt.assignment.pdf
[pdf-75]: ../Logica/L10.T75.FOL.SAT2LE.pdf
[pdf-76]: ../Logica/L10.T76.FOL.exercises.pdf
[pdf-77]: ../Logica/L10.T77.FOL.Finite.Domains.pdf
[pdf-78]: ../Logica/L10.T78.FOL.FOL.wrt.DB.pdf
[pdf-81]: ../Logica/L11.T81.FOL.Reasoning.Hilbert.calculus.pdf
[pdf-82]: ../Logica/L11.T82.FOL.Reasoning.Tableau.pdf
[pdf-83]: ../Logica/L11.T83.FOL.Reasoning.Tableau.corr.compl.pdf
[pdf-84]: ../Logica/L11.T84.FOL.Reasoning.Tableau.examples.pdf
[pdf-85]: ../Logica/L11.T85.FOL.Reasoning.Tableau.termination.pdf
[pdf-86]: ../Logica/L11.T86.FOL.Reasoning.Tableau.countermodels.pdf
