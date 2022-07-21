## Intuitions

### PL - Propositional logic

> **Proposition**: *statement about what is the case in the world*



### FOL - First order logic

> <u>Definitions</u>  (**FOL constructs**)
>
> **FOL** assumes world contains
>
> - **Constants**
> - **Functions**
> - **Predicates / relations**
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





## Languages

### PL - Language

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



### FOL - Language

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
>   - Set $f_1 ,\, f_2 ,\, . . .$ of **functional symbols[^\**]**
>   - Set $P_1 ,\, P_2 ,\, . . .$ of **relational symbols[^\**]**
>
> [^\*]: Functions with **arity equal to 0**
> [^\**]: Each of which is associated with its **arity** (number of arguments)

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





## Interpretation function

### PL - Interpretation

> **Propositional interpretation**: *function that specify if a proposition is true or false*
> $$
> I :\ {\tt PROP} → \{⊤,⊥\}
> $$

- A PI is a **subset** $S$ of $\tt PROP$ such that $I$ is the **characteristic function** of $S$

  $$
  A\in S \iff I(A)=⊤
  $$



### FOL - Interpretation

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
>   $$
>   I:L→D
>   $$
>   Let $n$ the **arity** of $f_i$ and $P_i$
>
>   - $I(c_i )∈∆\,$              ~~(elements of the domain)~~
>   - $I(f_i ) : ∆^n → ∆$    ~~($n$-ary function on the domain)~~
>   - $I(P_i ) ⊆ ∆^n$           ~~($n$-ary relation on the domain)~~